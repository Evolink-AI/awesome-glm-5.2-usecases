# GitHub Repo Action List

Repo: `Evolink-AI/awesome-glm-5.2-usecases`
Review date: 2026-07-12
Review mode: Review + Fix

## P0

- [x] Make the usecase namespace and every Menu case link machine-verifiable.
  - Why: the current portable verifier exits non-zero.
  - Owner: repository maintainer
  - Expected result: 209 unique IDs pass the configured category-grouped policy and every case is reachable from Menu.
- [x] Repair semantic localization parity across all ten localized READMEs.
  - Why: untranslated titles and structural metadata drift block the 11-language contract.
  - Owner: repository maintainer
  - Expected result: source/author/type/date parity passes and no non-exempt title remains unchanged from English.
- [ ] Verify the migrated R2 banner on GitHub/camo after push.
  - Why: local README media and missing rendered evidence violate the current publication contract.
  - Owner: repository maintainer
  - Expected result: R2 origin and rendered GitHub media audits have no P0/P1 failures.
- [x] Run a complete public-surface link audit.
  - Why: spot checks do not cover all 11 READMEs, docs, images, relative files and anchors.
  - Owner: repository maintainer
  - Expected result: all internal targets resolve and external/UTM failures are zero or explicitly waived.

## P1

- [x] Normalize placement-specific UTM parameters and action-oriented link copy.
  - Why: current links omit `utm_content` and use inconsistent docs destinations.
  - Owner: repository maintainer
  - Expected result: every EvoLink-owned CTA matches the recorded URL/UTM matrix.
- [x] Add a public structured usecase inventory and namespace config.
  - Why: the current README-only source of truth is not sufficiently portable for contract verification.
  - Owner: repository maintainer
  - Expected result: README and curated JSON source sets match exactly.
- [x] Expand maintenance and PR guidance for data equality, R2 media, localization and Related Repositories boundaries.
  - Why: contributors need executable checks, not implicit conventions.
  - Owner: repository maintainer
  - Expected result: future updates can reproduce the same gates.
- [x] Remove repository hygiene debris and ignore local model-pipeline evidence.
  - Why: system files and untracked local evidence obscure real changes.
  - Owner: repository maintainer
  - Expected result: clean, portable working tree after formal outputs are staged.

## P2

- [ ] Consider adding `glm`, `open-weight-models`, `coding-agents` and `ai-benchmarks` topics.
  - Why: these terms align with the README's actual discovery intent.
  - Owner: repository maintainer
  - Expected result: broader accurate GitHub discovery without keyword stuffing.

## Notes

- Blockers: real API credit budget/waiver and explicit approval for commit/push remain separate owner gates.
- Out of scope: repository rename/archive/delete, npm/skill release and announcements.
- Follow-up check: rerun template audit, usecase verifier, localization gate, link audit and general GitHub review after fixes.
- Link copy issues: replace labels that depend on surrounding text with self-contained actions such as `Get your API key` and `Read GLM-5.2 API docs`.
