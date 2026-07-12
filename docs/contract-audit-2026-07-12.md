# Contract Audit: awesome-glm-5.2-usecases

- Audit date: 2026-07-12
- Repository: `Evolink-AI/awesome-glm-5.2-usecases`
- Pipeline / shape: `guide-prompt` / `usecase`
- Run mode: `recurring-update`
- Contract: `model-repo-pipeline/contracts/standard-guide-repo-contract.md`
- Initial verdict: **FAIL**
- Initial completion state: `local scaffold complete`

## Executive Summary

The repository already has a strong English usecase surface: 209 unique cases, complete source/author headings, explicit anchors, bold takeaways, Type/Date metadata, 11 README files, maintenance and community files, and a public GitHub front door. It does not yet pass the current contract because the portable verifier, localization semantics, public media policy, and required evidence gates are incomplete.

## Initial Audit Results

| # | Contract area | Initial status | Evidence | Priority | Required remediation |
|---|---|---|---|---|---|
| 1 | Repository identity and public state | PASS | `origin` resolves to `Evolink-AI/awesome-glm-5.2-usecases`; GitHub reports public `main` | - | Preserve remote identity lock. |
| 2 | First-screen positioning | PASS | Model name, usecase role, banner, badges and CTA are above the first section | - | Preserve during fixes. |
| 3 | URL/UTM matrix | FAIL | Banner, badge, Introduction and docs links omit placement-specific `utm_content`; docs links use inconsistent target/medium | P1 | Normalize all EvoLink-owned CTA slots across 11 READMEs. |
| 4 | Conversion path | PARTIAL | Model page, key dashboard, API request and docs exist; current-surface/skill availability wording and dedicated evidence report are absent | P1 | Make the three-step route explicit and record link verification. |
| 5 | Usecase namespace | FAIL | 209 IDs form the contiguous set 1-209, but the document is category-grouped and no machine-readable `set-contiguous` namespace config exists | P0 | Add and consume `data/usecase-update-config.json`. |
| 6 | Menu completeness | FAIL | English Menu omits case links 146-151, 167-173, 206 and 209 | P0 | Add all 15 missing case links and synchronize localized Menus. |
| 7 | English case shape | PASS | 209 headings, 209 anchors, 209 valid English Type/Date lines, no missing IDs | - | Preserve and verify after mutation. |
| 8 | Localized case parity | FAIL | All 10 localized READMEs have 209 cases, but 1,627 case titles remain byte-identical to English; localized Type values/labels cause thousands of verifier mismatches | P0 | Translate remaining titles, preserve source/author/date, and normalize machine-verifiable Type/Date metadata. |
| 9 | Structured source of truth | FAIL | No public curated JSON/Markdown inventory exists | P1 | Generate a public curated inventory from the English source and verify source equality. |
| 10 | Maintenance contract | PARTIAL | `docs/maintenance.md` exists, but it does not define the new structured source of truth, namespace config, full verifier command, or R2/render checks | P1 | Expand the maintenance guide. |
| 11 | Pull request contract | PARTIAL | PR template covers evidence and localization, but not public media/R2 checks or Related Repositories boundary | P1 | Add the missing checks. |
| 12 | Public media policy | FAIL | All 11 READMEs reference local `images/en.jpg`; no R2 inventory/upload/origin evidence exists | P0 | Upload the full public media directory to the locked R2 namespace and rewrite README references. |
| 13 | Rendered GitHub media | FAIL | No post-change rendered GitHub/camo audit exists | P0 | Run the rendered media audit after push. |
| 14 | Public surface link audit | FAIL | No all-public-surface link/anchor/UTM report exists | P0 | Audit every README/docs link, image, relative path and fragment. |
| 15 | Real EvoLink API test | BLOCKED | No current run report records approved credit budget, request ID and final success signal | P0 | Reuse valid applicable evidence, run an owner-approved smoke, or record an explicit waiver. |
| 16 | GitHub About / SEO | PASS | Public description, homepage and topics are populated and aligned with GLM-5.2 usecases | - | Retain; minor topic expansion is optional. |
| 17 | Community standards | PASS | README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, issue templates and PR template exist | - | Preserve. |
| 18 | Repository hygiene | FAIL | A local `.DS_Store` exists and model-pipeline evidence is not ignored | P1 | Remove the system file and ignore local pipeline evidence. |
| 19 | Publication evidence | BLOCKED | Modification has no run-specific commit, push, raw/rendered readback or completion-gate pass | P0 | Complete only after local audits pass and public action approval is recorded. |

## Initial Verifier Evidence

- `model_repo_orchestrator.py full-cycle`: exited non-zero and reported `local scaffold complete`.
- `verify_usecase_update.py --repo .`: exited non-zero; initial output included category-order namespace failure, missing Menu links, metadata drift and localized semantic failures.
- Independent structure scan: English and all 10 localized READMEs each contain 209 unique case headings and 209 explicit anchors.
- GitHub metadata readback: public repository, default branch `main`, bare homepage `https://evolink.ai/glm-5-2`, populated description and six relevant topics.

## Remediation Order

1. Fix machine-readable namespace, Menu completeness and repository hygiene.
2. Normalize all CTA/UTM slots and the explicit first-call path.
3. Repair localized title and metadata parity across all 10 localized READMEs.
4. Add structured curated data, maintenance rules and PR checks.
5. Move the banner to R2 and verify origin plus public GitHub rendering.
6. Run public-surface link audit, portable verification, child reviews and completion gate.
7. After explicit public-action approval, commit, push and perform public readback.

## Final Re-Audit

The initial findings above remain unchanged as audit evidence. After remediation:

| Gate | Result | Evidence |
|---|---|---|
| `github-template` W17 audit | PASS locally | `docs/template-audit-2026-07-12.md` |
| Legacy 11-README verifier | PASS | 11 README files; 209 English cases |
| Contract usecase verifier | PASS | Configured `set-contiguous` namespace; 209 English cases; 10 localized READMEs |
| Menu/anchor parity | PASS | Every README has 209 unique case links, 209 anchors and 209 headings |
| Localization semantic gate | PASS | No localized title remains identical to English; source/author/Type/Date parity passes |
| README/data equality | PASS | 209 generated JSON items equal the parsed English public-case records |
| Public surface link audit | PASS | P0=0, P1=0 across README/docs links, assets, relative files, fragments and UTM slots |
| R2 origin/media gate | PASS | Full two-file media inventory; 11 README rewrites; banner and Star History origins return HTTP 200 |
| GitHub rendered media | PASS | All 16 rendered images and canonical sources return HTTP 200; failures=0 |
| GitHub general review | PASS locally | Community profile 100%; About/SEO/front door/maintenance checks pass |
| Real API smoke | PASS | Approved 256-token-boundary retry returned HTTP 200, `finish_reason=stop`, and exact visible content `contract-smoke-ok` |
| Usecase handoff verifier | APPROVED N/A WAIVER | This run added no candidate cases and made only contract/structure/localization changes; waiver is scoped to this run |
| Commit/push/public render | PASS | Owner replied `继续`; commits `84fbd27` and `ae8091c` were pushed to `main`; remote HEAD matched local and raw/rendered readback passed |

### Current Verdict

- Repository content and local contract layers: **PASS**
- Final contract state: **PUBLISHED / PASS**
- Public verification: remote `main` matched local implementation commit; raw README, R2 origins, and all GitHub/camo-rendered media passed.
- Agent runtime note: the workspace copy of `completion-gate` currently calls an undefined `has_complete_github_utm`; the canonical installed framework copy was used instead and correctly reported the remaining external gates.
