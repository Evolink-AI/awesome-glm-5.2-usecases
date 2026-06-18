# GitHub Repo Action List

Repo: awesome-glm-5.2-usecases
Review date: 2026-06-18
Review mode: Review + Fix

## P0

- [x] Action: Verify all case anchors, headings, Menu links, and Type/Date lines.
  - Why: Broken anchors or inconsistent case metadata would make the usecase repo hard to navigate and maintain.
  - Owner: Codex
  - Expected result: 59/59 cases have stable anchors, correct headings, and valid Type/Date lines.

- [x] Action: Remove raw source exports and internal curation datasets from the final repo.
  - Why: User explicitly required the public repo not to retain raw data source or curated source dataset files.
  - Owner: Codex
  - Expected result: No raw JSON, no source insights copy, no internal curation dataset, no local source paths.

## P1

- [x] Action: Add explicit stable anchors before localized category headings.
  - Why: Translated headings produce different GitHub auto-slugs; explicit anchors keep Menu links stable across languages.
  - Owner: Codex
  - Expected result: Each README has 6 stable category anchors used by the Menu.

- [x] Action: Add Evolink GLM-5.2 Quick API Access to every README.
  - Why: The user provided the official Evolink GLM-5.2 API page, so the repository can now include the correct Evolink-only API entry.
  - Owner: Codex
  - Expected result: Every README contains the same endpoint, model id, and docs link, with localized surrounding text.

## P2

- [x] Action: Add GitHub About recommendation to `docs/maintenance.md`.
  - Why: Local files cannot set the remote About sidebar, but maintainers need a copy-ready description and topics list.
  - Owner: Codex
  - Expected result: Maintainer can paste About description, website, and topics after repo creation.

## Notes

- Blockers: None.
- Optional future enhancement: copy polish for case-level prose in each localized README, without changing anchors, links, or case order.
- Out of scope: Raw source dataset storage; Z.ai Quick Start; non-Evolink API examples.
- Follow-up check: After pushing to GitHub, verify the sidebar About fields and image rendering in GitHub UI.
- Link copy issues: No P0 issues. Top usage CTA uses `Try it on Evolink`; case/source links are exempt from action-verb rewriting.
