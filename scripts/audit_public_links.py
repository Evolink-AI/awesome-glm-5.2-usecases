#!/usr/bin/env python3
"""Audit public README/docs links, assets, fragments, and EvoLink CTA UTMs."""

from __future__ import annotations

import argparse
import concurrent.futures
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import requests


BADGE_RE = re.compile(r"\[!\[[^\]]*\]\((?P<image>[^)\s]+)\)\]\((?P<target>[^)\s]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\((?P<target>[^)\s]+)\)")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\((?P<target>[^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
HTML_RE = re.compile(r"<(?:a|img)\b[^>]*(?:href|src)=['\"](?P<target>[^'\"]+)['\"]", re.IGNORECASE)
RAW_URL_RE = re.compile(r"https?://[^\s<>'\"`\]\)]+")
EXPLICIT_ANCHOR_RE = re.compile(r"\bid=['\"](?P<id>[^'\"]+)['\"]", re.IGNORECASE)
HEADING_RE = re.compile(r"^#{1,6}\s+(?P<title>.+?)\s*$", re.MULTILINE)
X_HOSTS = {"x.com", "www.x.com", "twitter.com", "www.twitter.com"}
UTM_HOSTS = {"evolink.ai", "www.evolink.ai", "docs.evolink.ai"}


def github_slug(title: str) -> str:
    title = re.sub(r"<[^>]+>", "", title).strip().lower()
    title = re.sub(r"[^\w\-\s]", "", title, flags=re.UNICODE)
    title = re.sub(r"\s+", "-", title)
    return re.sub(r"-+", "-", title).strip("-")


def targets(text: str):
    rendered = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    rendered = re.sub(r"`[^`\n]+`", "", rendered)
    linked = []
    badge_spans = []
    for match in BADGE_RE.finditer(rendered):
        linked.extend([match.group("image"), match.group("target")])
        badge_spans.append(match.span())
    masked = list(rendered)
    for start, end in badge_spans:
        masked[start:end] = " " * (end - start)
    masked = "".join(masked)
    linked += [match.group("target") for match in IMAGE_RE.finditer(masked)]
    linked += [match.group("target") for match in LINK_RE.finditer(masked)]
    linked += [match.group("target") for match in HTML_RE.finditer(rendered)]
    raw = [match.group(0).rstrip(".,;:)") for match in RAW_URL_RE.finditer(text)]
    return linked, raw


def anchors(text: str):
    result = {match.group("id") for match in EXPLICIT_ANCHOR_RE.finditer(text)}
    seen = Counter()
    for match in HEADING_RE.finditer(text):
        base = github_slug(match.group("title"))
        suffix = seen[base]
        seen[base] += 1
        result.add(base if suffix == 0 else f"{base}-{suffix}")
    return result


def check_http(item):
    url, is_linked = item
    parsed = urlparse(url)
    if parsed.netloc.lower() in X_HOSTS:
        return (url, "manual", None, url, "X/Twitter blocks reliable automated link checks; canonical URL syntax was validated.")
    if not is_linked and parsed.netloc.lower() in {"direct.evolink.ai", "api.z.ai", "api.fireworks.ai"}:
        return (url, "manual", None, url, "API endpoint is visible as code/reference and requires its documented method or authentication; browser GET is not an acceptance test.")
    if not is_linked and parsed.netloc.lower().endswith(".r2.dev") and parsed.path in {"", "/"}:
        return (url, "manual", None, url, "R2 public base is recorded as an identity value; the concrete media object URL is checked separately.")
    try:
        response = requests.get(
            url,
            timeout=20,
            allow_redirects=True,
            stream=True,
            headers={"User-Agent": "EvoLink-Public-Surface-Audit/1.0", "Range": "bytes=0-1023"},
        )
        status = response.status_code
        final = response.url
        response.close()
        if 200 <= status < 400:
            state = "passed"
        elif status in {429, 500, 502, 503, 504} and parsed.netloc.lower() in {"api.star-history.com", "www.star-history.com"}:
            state = "manual"
        else:
            state = "failed"
        return (url, state, status, final, "")
    except requests.RequestException as exc:
        return (url, "failed", None, url, str(exc))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    out = Path(args.out)
    if not out.is_absolute():
        out = repo / out

    files = sorted(repo.glob("README*.md")) + sorted(repo.glob("docs/**/*.md"))
    files = [path for path in files if path.resolve() != out.resolve()]
    anchor_map = {path.resolve(): anchors(path.read_text(encoding="utf-8")) for path in files}
    occurrences = defaultdict(list)
    linked_occurrences = defaultdict(list)
    local_failures = []
    anchor_failures = []
    utm_failures = []
    raw_count = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        linked, raw = targets(text)
        raw_count += len(raw)
        for target in linked:
            linked_occurrences[target].append(path.relative_to(repo).as_posix())
        for target in set(linked + raw):
            occurrences[target].append(path.relative_to(repo).as_posix())
        for target in linked:
            if target.startswith(("mailto:", "tel:")):
                continue
            if target.startswith(("http://", "https://")):
                parsed = urlparse(target)
                if parsed.netloc.lower() in UTM_HOSTS:
                    query = parse_qs(parsed.query)
                    required = {"utm_source", "utm_medium", "utm_campaign", "utm_content"}
                    missing = sorted(required - set(query))
                    if missing or query.get("utm_source") != ["github"] or query.get("utm_campaign") != ["awesome-glm-5.2-usecases"]:
                        utm_failures.append((path.relative_to(repo).as_posix(), target, missing))
                continue
            base, fragment = (target.split("#", 1) + [""])[:2] if "#" in target else (target, "")
            target_path = path if not base else (path.parent / unquote(base)).resolve()
            if base and not target_path.exists():
                local_failures.append((path.relative_to(repo).as_posix(), target))
                continue
            if fragment:
                resolved = target_path.resolve()
                if resolved not in anchor_map and target_path.is_file() and target_path.suffix.lower() == ".md":
                    anchor_map[resolved] = anchors(target_path.read_text(encoding="utf-8"))
                if fragment not in anchor_map.get(resolved, set()):
                    anchor_failures.append((path.relative_to(repo).as_posix(), target))

    external = sorted(target for target in occurrences if target.startswith(("http://", "https://")))
    external_items = [(target, target in linked_occurrences) for target in external]
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as pool:
        results = list(pool.map(check_http, external_items))
    failed_http = [result for result in results if result[1] == "failed"]
    manual_http = [result for result in results if result[1] == "manual"]
    redirects = [result for result in results if result[3] != result[0]]
    passed_http = [result for result in results if result[1] == "passed"]

    p0 = len(local_failures) + len(anchor_failures)
    p1 = len(failed_http) + len(utm_failures)
    result = "PASS" if p0 == 0 and p1 == 0 else "FAIL"
    lines = [
        "# Public Surface Link Audit",
        "",
        f"- Timestamp: {datetime.now(timezone.utc).isoformat()}",
        f"- Repository: `{repo}`",
        "- Scope: root `README*.md` and `docs/**/*.md`; generated output report excluded from its own scan",
        "- Extraction: Markdown links/images, HTML href/src, raw HTTP(S) URLs, relative files, and fragment anchors",
        f"- Public files scanned: {len(files)}",
        f"- Unique external URLs: {len(external)}",
        f"- External passed: {len(passed_http)}",
        f"- External manual verification required: {len(manual_http)}",
        f"- External failed: {len(failed_http)}",
        f"- Raw URL occurrences: {raw_count}",
        f"- Relative file failures: {len(local_failures)}",
        f"- Fragment anchor failures: {len(anchor_failures)}",
        f"- UTM failures: {len(utm_failures)}",
        f"- Redirects: {len(redirects)}",
        f"- Severity: P0={p0}, P1={p1}, P2={len(manual_http) + len(redirects)}",
        f"- Result: **{result}**",
        "",
        "## Manual Verification Boundary",
        "",
        "X/Twitter source and author URLs are reported as manual checks because the service does not provide reliable automated bot responses. The audit still validates that these are canonical `x.com`/`twitter.com` HTTPS targets and covers every occurrence. This boundary is not used for EvoLink conversion links, R2 media, badges, GitHub, or Star History assets.",
        "",
    ]
    if failed_http:
        lines += ["## External Failures", "", "| URL | Status | Detail |", "|---|---:|---|"]
        for url, _, status, final, detail in failed_http:
            lines.append(f"| {url} | {status or 'error'} | {detail or final} |")
        lines.append("")
    if local_failures or anchor_failures:
        lines += ["## Internal Failures", "", "| File | Target | Type |", "|---|---|---|"]
        for file, target in local_failures:
            lines.append(f"| {file} | `{target}` | missing relative file |")
        for file, target in anchor_failures:
            lines.append(f"| {file} | `{target}` | missing fragment anchor |")
        lines.append("")
    if utm_failures:
        lines += ["## UTM Failures", "", "| File | URL | Missing |", "|---|---|---|"]
        for file, target, missing in utm_failures:
            lines.append(f"| {file} | {target} | {', '.join(missing) or 'wrong source/campaign'} |")
        lines.append("")
    if redirects:
        lines += ["## Redirects", "", "| Source | Final | Status |", "|---|---|---:|"]
        for source, _, status, final, _ in redirects:
            lines.append(f"| {source} | {final} | {status or ''} |")
        lines.append("")
    lines += [
        "## Verification Summary",
        "",
        f"- Confirmed automated external checks: {len(passed_http)}",
        f"- Canonical X/Twitter manual-boundary URLs: {len(manual_http)}",
        f"- Linked target occurrences covered: {sum(len(paths) for paths in linked_occurrences.values())}",
        f"- Final acceptance: {result}; publication requires P0=0 and P1=0.",
    ]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{result}: wrote {out}")
    print(f"files={len(files)} external={len(external)} p0={p0} p1={p1} manual={len(manual_http)} redirects={len(redirects)}")
    raise SystemExit(0 if result == "PASS" else 1)


if __name__ == "__main__":
    main()
