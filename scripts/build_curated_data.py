#!/usr/bin/env python3
"""Build the public GLM-5.2 usecase inventory from the English README."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
JSON_OUT = ROOT / "data" / "glm-5.2-usecase-curated.json"
MD_OUT = ROOT / "data" / "glm-5.2-usecase-curated.md"
CASE_RE = re.compile(
    r'^<a id="case-(?P<number>\d+)"></a>\n'
    r'^### Case (?P=number): \[(?P<title>[^\]]+)\]\((?P<source>[^)]+)\) '
    r'\(by \[(?P<author>[^\]]+)\]\((?P<author_url>[^)]+)\)\)$',
    re.MULTILINE,
)
META_RE = re.compile(
    r"^Type: (?P<type>Demo|Tutorial|Evaluation|Integration|Benchmark|Limit) \| "
    r"Date: (?P<date>\d{4}-\d{2}-\d{2})$",
    re.MULTILINE,
)
TAKEAWAY_RE = re.compile(r"^\*\*(?P<takeaway>[^*\n].+?)\*\*$", re.MULTILINE)
PROMPT_RE = re.compile(r"\n\*\*Prompt:\*\*\n\n```\n(?P<prompt>.*?)\n```\n", re.DOTALL)


def category_at(text: str, offset: int) -> str:
    headings = list(re.finditer(r"^## (?P<title>.+)$", text[:offset], re.MULTILINE))
    if not headings:
        raise ValueError(f"No category heading before offset {offset}")
    title = headings[-1].group("title")
    return re.sub(r"^[^\w]+\s*", "", title).strip()


def build_items(text: str):
    matches = list(CASE_RE.finditer(text))
    items = []
    for index, match in enumerate(matches):
        if index + 1 < len(matches):
            end = matches[index + 1].start()
        else:
            related = text.find("## Related Repositories", match.end())
            acknowledge = text.find("## 🙏 Acknowledge", match.end())
            candidates = [position for position in (related, acknowledge) if position >= 0]
            end = min(candidates) if candidates else len(text)
        block = text[match.end():end]
        takeaway = TAKEAWAY_RE.search(block)
        meta = META_RE.search(block)
        if not takeaway or not meta:
            raise ValueError(f"Case {match.group('number')} lacks takeaway or metadata")
        notes_start = takeaway.end()
        notes_end = meta.start()
        body_notes = block[notes_start:notes_end].strip()
        prompt = PROMPT_RE.search("\n" + body_notes + "\n")
        prompt_text = prompt.group("prompt").strip() if prompt else ""
        if prompt:
            body_notes = PROMPT_RE.sub("\n", "\n" + body_notes + "\n").strip()
        category = category_at(text, match.start())
        source_url = match.group("source")
        items.append({
            "case_number": int(match.group("number")),
            "dedup_key": source_url.replace("https://", "").replace("http://", "").rstrip("/"),
            "source_url": source_url,
            "author_url": match.group("author_url"),
            "author_handle": match.group("author"),
            "title": match.group("title"),
            "takeaway": takeaway.group("takeaway"),
            "body_notes": body_notes,
            "type": meta.group("type"),
            "date": meta.group("date"),
            "category": category,
            "decision_reason": f"Published as a source-backed, high-signal {meta.group('type').lower()} case.",
            "primary_topic": category,
            "quality_tier": "high",
            "evidence_type": meta.group("type"),
            "prompt_public": bool(prompt_text),
            "prompt_text": prompt_text,
        })
    numbers = sorted(item["case_number"] for item in items)
    expected = list(range(1, max(numbers) + 1)) if numbers else []
    if numbers != expected:
        raise ValueError("Case numbers are not a contiguous set")
    sources = [item["source_url"] for item in items]
    if len(sources) != len(set(sources)):
        raise ValueError("Duplicate source URLs detected")
    return sorted(items, key=lambda item: item["case_number"])


def main():
    text = README.read_text(encoding="utf-8")
    items = build_items(text)
    category_counts = Counter(item["category"] for item in items)
    type_counts = Counter(item["type"] for item in items)
    payload = {
        "model": "GLM-5.2",
        "repository": "Evolink-AI/awesome-glm-5.2-usecases",
        "source_of_truth": "README.md",
        "public_subset_policy": "All published source-backed cases in README.md",
        "total_kept": len(items),
        "category_counts": dict(sorted(category_counts.items())),
        "type_counts": dict(sorted(type_counts.items())),
        "items": items,
    }
    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# GLM-5.2 Curated Usecase Inventory",
        "",
        "This file is generated from `README.md` by `scripts/build_curated_data.py`.",
        "",
        f"- Published cases: {len(items)}",
        "- Numbering: contiguous set from 1 through the current maximum",
        "- Policy: every item is source-backed and included in the public README",
        "",
        "| Case | Title | Category | Type | Date | Source | Author |",
        "|---:|---|---|---|---|---|---|",
    ]
    for item in items:
        title = item["title"].replace("|", "\\|")
        category = item["category"].replace("|", "\\|")
        lines.append(
            f"| {item['case_number']} | {title} | {category} | {item['type']} | {item['date']} | "
            f"[Open source]({item['source_url']}) | [{item['author_handle']}]({item['author_url']}) |"
        )
    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"PASS: wrote {len(items)} cases to {JSON_OUT.relative_to(ROOT)} and {MD_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
