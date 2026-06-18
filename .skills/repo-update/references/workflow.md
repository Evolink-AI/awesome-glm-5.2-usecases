# Prompt Repo Update Workflow

## Preconditions

Before starting, verify that the approved candidate set is fixed.

Required decisions per candidate:
- keep confirmed
- source URL and author URL confirmed
- `approved_title`
- `approved_takeaway`
- `approved_body`
- category confirmed
- type confirmed: Tutorial / Demo / Evaluation / Integration
- publication date confirmed as `YYYY-MM-DD`
- like count is greater than 10

If any item lacks source-backed body text, attribution, date, category, type, or the like threshold, stop and return to curation.

## Core Operating Model

- `README.md` is the English source README.
- Localized READMEs must keep the same case number, anchor, source link, author link, type, and date as English.
- `docs/maintenance.md` defines the public case format.
- There is no `cases/` directory, no per-case media download requirement, and no `data/ingested_tweets.json` update in this repo.

## Steps

### 1. Inspect Current State

Read:
- `docs/maintenance.md`
- `README.md`
- all `README_*.md`
- curated dataset files if present

Record current:
- total English case count
- next case number
- Menu category ranges
- localized case counts
- Acknowledge section creator list

### 2. Update English README

Append each approved case to the correct existing category section.

Use the repo's exact case shape:
- `<a id="case-N"></a>`
- `### Case N: [Title](SOURCE_URL) (by [@author](AUTHOR_URL))`
- bold usage takeaway
- readable source-backed body
- `Type: ... | Date: YYYY-MM-DD`

Then update:
- Overview selected case count
- Menu case ranges
- any section table row that summarizes the new case
- Acknowledge section if a new creator is introduced

Do not add old template labels such as `How to use it:` or `Tweet excerpt`.

### 3. Update Localized READMEs

For each localized README:
- add matching anchors and case numbers
- keep source URL, author URL, type, and date consistent with English
- localize title, takeaway, body, and Menu/table wording according to the file's existing language style
- keep technical terms such as GLM-5.2, OpenCode, API, Cursor, SWE-Bench, and model names in English when appropriate

Do not leave placeholder translation text.

### 4. Update Curated Dataset Files If Present

If `glm-5.2-usecase-curated.json` or `.md` exists, update it to match the public case inventory.

If those files are absent, do not invent a new dataset format unless the user explicitly asks.

### 5. Run Validation

Run the repo checks from `docs/maintenance.md` and the bundled verifier:

```bash
for f in README*.md; do printf '%s ' "$f"; rg -c '^### Case [0-9]+' "$f"; done
for f in README*.md; do printf '%s ' "$f"; rg -c '<a id="case-[0-9]+"></a>' "$f"; done
rg -n 'images/logo\.svg|How to use it:|Tweet excerpt|19 more creators|more creators' README*.md CONTRIBUTING.md
rg -n '<img src="images/' README*.md
python3 .skills/repo-update/scripts/verify_prompt_repo_update.py --repo .
```

Fix any inconsistency before commit.

### 6. Commit And Push

Review `git diff --stat`, then commit and push only formal repository outputs:
- README files
- curated dataset files, if they exist and were intentionally updated
- maintenance docs or intentional assets

Do not commit temporary curation artifacts.

Report the commit hash back to the user.
