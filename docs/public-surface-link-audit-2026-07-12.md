# Public Surface Link Audit

- Timestamp: 2026-07-12T10:11:56.617239+00:00
- Repository: `/Users/evolink/Desktop/github-repo/awesome-glm-5.2-usecases`
- Scope: root `README*.md` and `docs/**/*.md`; generated output report excluded from its own scan
- Extraction: Markdown links/images, HTML href/src, raw HTTP(S) URLs, relative files, and fragment anchors
- Public files scanned: 21
- Unique external URLs: 403
- External passed: 29
- External manual verification required: 374
- External failed: 0
- Raw URL occurrences: 6289
- Relative file failures: 0
- Fragment anchor failures: 0
- UTM failures: 0
- Redirects: 0
- Severity: P0=0, P1=0, P2=374
- Result: **PASS**

## Manual Verification Boundary

X/Twitter source and author URLs are reported as manual checks because the service does not provide reliable automated bot responses. The audit still validates that these are canonical `x.com`/`twitter.com` HTTPS targets and covers every occurrence. This boundary is not used for EvoLink conversion links, R2 media, badges, GitHub, or Star History assets.

## Verification Summary

- Confirmed automated external checks: 29
- Canonical X/Twitter manual-boundary URLs: 374
- Linked target occurrences covered: 8802
- Final acceptance: PASS; publication requires P0=0 and P1=0.
