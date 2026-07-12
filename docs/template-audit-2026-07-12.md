# Usecase Template Audit: awesome-glm-5.2-usecases

- Audit date: 2026-07-12
- Workflow: `github-template` W17 audit-usecase
- English cases: 209
- Localized README files: 10
- Local structural verdict: **PASS**
- Publication verdict: **PENDING public render and publication evidence**

## Compliance

| # | Rule | Result | Evidence |
|---|---|---|---|
| 1 | Centered top cover | PASS | `<div align="center">` begins all 11 READMEs and closes before Introduction. |
| 2 | R2 banner policy | PASS locally | Shared R2 policy and full inventory/upload/origin evidence are in `docs/media-audit-2026-07-12.md`; post-push render remains a publication gate. |
| 3 | Badge order | PASS | License → EvoLink/Docs → language badges. |
| 4 | Canonical 11-language badge block | PASS | The badge block is byte-identical across all 11 READMEs. |
| 5 | English source naming | PASS | `README.md` exists and `README_en.md` does not. |
| 6 | Overview after Introduction | PASS | 209-case scope, field promise, coverage, and evidence-first note are present. |
| 7 | Quick Start after Overview | PASS | Current GLM-5.2 API route, key dashboard, endpoint, model ID, and unavailable-skill boundary are explicit. |
| 8 | Table Menu | PASS | Section table and six per-category case tables exist in every README. |
| 9 | Stable case anchors | PASS | 209 anchors equal 209 headings in every README. |
| 10 | Case heading format | PASS | Titles link sources; one canonical author link is preserved; no quality/type badge appears in headings. |
| 11 | Bold reader-action takeaway | PASS | Usecase verifier checks every case. |
| 12 | Source-content notes | PASS | Published cases contain source-grounded prose; no default excerpt labels or invented prompt filler detected. |
| 13 | Type/Date metadata | PASS | 209 canonical Type/Date lines in every README; type/date parity passes. |
| 14 | Maintenance and data files | PASS | Maintenance guide, PR template, namespace config, curated JSON/Markdown, and builders exist. |
| 15 | README/data equality | PASS | Generated 209-item JSON matches all parsed English public-case fields; source set verifier passes. |
| 16 | R2 media/video policy | PASS for current image-only scope | One JPEG banner is R2-hosted; there are no public videos or GIFs. |
| 17 | Related Repositories | PASS | Localized section and stable anchor exist in all READMEs; API/Skill release boundary is explicit. |
| 18 | Acknowledge | PASS | Explicit creator coverage and attribution-correction wording are present; no vague creator rollup is used. |
| 19 | Star History at end | PASS | Star History is the final public block after Acknowledge. |

## Verification

- Legacy repo verifier: PASS, 11 READMEs and 209 English cases.
- Contract usecase verifier: PASS, configured namespace and 10 localized READMEs.
- Public-surface link audit: PASS, P0=0 and P1=0.
- Structured-data full equality: PASS, 209 items.
- `git diff --check`: PASS.

The template layer is locally compliant. The broader contract cannot report `published` until the change is committed/pushed, rendered GitHub media is re-audited, and the API smoke evidence gate is resolved.
