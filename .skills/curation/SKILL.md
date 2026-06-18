---
name: prompt-curation
description: Collect, deduplicate, and semantically review recent high-signal X/Twitter usecase candidates for the current GLM-5.2 repository before README updates. Use when gathering recent GLM-5.2 candidates, filtering to posts with more than 10 likes, classifying candidates as high-confidence update / unsure / drop, or preparing an auto-update package.
---

# Prompt Curation

Use this skill when the job is to **find and review GLM-5.2 usecase candidates first**.

This repository is a curated usecase repository, not an image prompt gallery. The curation output should identify public posts that can become real cases: workflows, prompts, demos, integrations, benchmarks, pricing notes, limitations, tutorials, or reproducible evidence.

## Current Repo Model

- English source: `README.md`
- Localized READMEs: `README_es.md`, `README_pt.md`, `README_ja.md`, `README_ko.md`, `README_de.md`, `README_fr.md`, `README_tr.md`, `README_zh-TW.md`, `README_zh-CN.md`, `README_ru.md`
- Curated dataset, when present: repo-specific curated JSON/Markdown files
- Maintenance reference: `docs/maintenance.md`
- There is no `cases/` directory and no `data/ingested_tweets.json` source of truth in the current repo.

## Search Rule

Only collect posts with **like count greater than 10**.

Operationally:
- add an advanced X/Twitter search filter equivalent to `min_faves:11`
- also enforce the same threshold after API results are returned
- do not include candidates with `like_count < 11`, even if they look relevant

Use `scripts/collect_candidates.py` by default. It appends `min_faves:11` unless the query already contains an explicit like/favorite filter, and it drops returned posts below the threshold.

## Primary Tool Choice

For recent X/Twitter collection, use `twitterapi-toolkit` as the default search entry.

Read `docs/maintenance.md` before reviewing candidates so the public README shape stays aligned with this repo.

## Read These References When Needed

- `references/workflow.md` — end-to-end intake workflow
- `references/review-output-format.md` — exact review and auto-update package structure

## Bundled Scripts

- `scripts/collect_candidates.py` — collects recent X/Twitter candidates with `twitterapi-toolkit`, advanced like filtering, and normalized engagement fields
- `scripts/prefilter_prompt_candidates.py` — deterministic prefilter for usecase signal, not final judgment
- `scripts/build_review_queue.py` — deduplicates against existing README/dataset links and writes reviewer JSON + markdown

## Hard Rules

- The semantic review is the approval gate for high-confidence items.
- Do not ask for human approval before updating `high_confidence_update` items.
- Select at most 10 `high_confidence_update` items per run.
- Keep curation working artifacts in `.codex/usecase-update-loop/`, not in git history.
- Tweet URL is the primary dedup key.
- Prefer the original author post over reposts, quotes, or copies.
- Do not invent prompts, benchmark numbers, workflow details, dates, or creator attribution.
- Keep exact prompt/code/command text only when it is publicly present in the source.
- A case must have enough evidence to support a concrete usage takeaway.
- The output of this skill is an auto-reviewed handoff package for `prompt-repo-update`, not a repo modification.

## Inputs To Gather

- target repo path
- target model aliases, default: `GLM-5.2`, `GLM 5.2`, `glm-5.2`, `Z.ai`
- time window, default 24h
- optional search keywords / aliases
- optional author whitelist or blacklist

## Expected Outputs

Produce curation-stage artifacts under the repo-local ignored run folder:
- `.codex/usecase-update-loop/runs/<run_id>/candidate_tweets.json`
- `.codex/usecase-update-loop/runs/<run_id>/prefiltered_candidates.json`
- `.codex/usecase-update-loop/runs/<run_id>/review_queue.json`
- `.codex/usecase-update-loop/runs/<run_id>/review_summary.md`
- `.codex/usecase-update-loop/runs/<run_id>/semantic_review.json`
- `.codex/usecase-update-loop/runs/<run_id>/auto_update_package.json`

The approval summary must include, for each candidate:
- tweet_url
- author_handle
- like_count
- curated title
- proposed bold takeaway
- source text / case body seed
- target category matching the README Menu
- type: Tutorial / Demo / Evaluation / Integration
- publication date
- evidence note
- decision: `high_confidence_update` / `unsure` / `drop`

## Semantic Review Stage

Codex decides:
- `decision` — `high_confidence_update` / `unsure` / `drop`
- `curated_title`
- `curated_takeaway` — the bold first paragraph under the case heading
- `curated_body` — readable source-content notes; no generic `Tweet excerpt` label
- `target_category` — one of the existing README sections unless a new section is explicitly needed
- `case_type` — Tutorial / Demo / Evaluation / Integration
- `publication_date` — normalized as `YYYY-MM-DD`

## Title Rules

`curated_title` is produced during semantic review.

Rules:
- 3-8 English words when possible
- describe the usecase subject, not the instruction verb
- do not start with "Generate", "Create", "Use", or similar weak verbs unless that is the natural source title
- keep technical terms in English: Claude Code, API, Cursor, SWE-Bench, APEX-SWE, etc.
- if source language is non-English, use an English title for the English README and translate later in localized files

## Stop Point

This skill stops at: **auto-update package ready**.

Hand selected high-confidence candidates to `prompt-repo-update` with a fixed selected candidate set. The update phase must not reopen keep/drop decisions unless the selected data is incomplete or contradicted by the source.
