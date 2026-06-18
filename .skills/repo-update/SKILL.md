---
name: prompt-repo-update
description: Apply auto-reviewed GLM-5.2 usecase candidates into the current repository by updating English and localized README files, optional curated dataset files, menu counts, validation checks, and git commit/push. Use after candidates are classified as high-confidence updates or explicitly provided by the user.
---

# Prompt Repo Update

Use this skill only after curation has produced fixed selected candidates.

This repository is a GLM-5.2 usecase repository. It does **not** use the older image-prompt repo layout with `cases/`, per-case image folders, `valid_mapping.json`, or `data/ingested_tweets.json`.

## Current Repo Model

- English source README: `README.md`
- Localized READMEs: `README_es.md`, `README_pt.md`, `README_ja.md`, `README_ko.md`, `README_de.md`, `README_fr.md`, `README_tr.md`, `README_zh-TW.md`, `README_zh-CN.md`, `README_ru.md`
- Curated dataset, when present: repo-specific curated JSON/Markdown files
- Maintenance rules: `docs/maintenance.md`
- Banner assets live directly under `images/`.

## Update Responsibilities

1. verify selected handoff data is complete
2. append or edit English cases in `README.md`
3. update the Menu case ranges and Overview total
4. update localized README files with matching case number, anchor, source link, creator link, type, and date
5. update curated dataset files if they exist
6. update Acknowledge creator credits when needed
7. run validation checks
8. commit and push only formal repo outputs

## Read These References When Needed

- `references/workflow.md` — ordered execution flow
- `references/handoff-contract.md` — selected input requirements
- `docs/maintenance.md` — repo-specific public README format

## Bundled Scripts

- `scripts/verify_prompt_repo_update.py` — verifies current README integrity across English and localized files

Legacy scripts in this skill directory are not part of the current repo flow unless explicitly repurposed.

## Hard Rules

- Do not use this skill until candidates have fixed title, takeaway, body, category, type, date, source URL, and author URL.
- Selected candidates may come from curation `high_confidence_update` output or exact user-provided items.
- Update at most 10 candidates per run.
- English `README.md` is the source README.
- Keep the same case number, anchor, source link, creator link, type, and date across every localized README.
- Preserve this repo's custom usecase format from `docs/maintenance.md`.
- Do not add old template labels such as `How to use it:` or `Tweet excerpt`.
- Do not add per-case quality badges.
- Code blocks are used only for actual code, prompts, commands, or structured examples.
- Do not invent prompt text, workflow steps, benchmark results, pricing, dates, or attribution.
- Only use posts that passed curation's **like > 10** rule.
- Never commit temporary curation artifacts from `.codex/usecase-update-loop/`.
- Never commit if case counts, anchors, source links, or localized case inventories are inconsistent.

## Case Format

Each case in `README.md` follows this shape:

```md
<a id="case-N"></a>
### Case N: [Title](SOURCE_URL) (by [@author](AUTHOR_URL))

**Bold usage takeaway.**

Readable source-backed case body. Keep concrete prompts, commands, code, benchmark notes, pricing, caveats, and links when present.

Type: Tutorial | Date: YYYY-MM-DD
```

Use the existing category sections from the Menu unless the user explicitly approves a new category.

## Required Input From Prior Phase

At minimum:
- repo path
- selected candidate set
- final keep list
- source URL and author URL
- curated title
- curated takeaway
- curated body
- target category
- type: Tutorial / Demo / Evaluation / Integration
- publication date as `YYYY-MM-DD`
- confirmation that like_count > 10

## Verification Contract

Run these checks before committing:

```bash
for f in README*.md; do printf '%s ' "$f"; rg -c '^### Case [0-9]+' "$f"; done
for f in README*.md; do printf '%s ' "$f"; rg -c '<a id="case-[0-9]+"></a>' "$f"; done
rg -n 'images/logo\.svg|How to use it:|Tweet excerpt|19 more creators|more creators' README*.md CONTRIBUTING.md
rg -n '<img src="images/' README*.md
python3 .skills/repo-update/scripts/verify_prompt_repo_update.py --repo .
```

The verifier must pass for all README files before commit.

## Expected Completion State

A successful run should end with:
- English README updated and verified
- localized READMEs aligned with English case inventory
- optional curated dataset files updated if present
- Overview total and Menu ranges correct
- Acknowledge creator credits current
- validation checks passing
- commit hash reported

Commit and push only repository outputs such as README files, curated dataset files, docs, and intentional assets. Do not commit curation temp files.
