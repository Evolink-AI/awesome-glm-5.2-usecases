# Prompt Curation Workflow

## Goal

Turn recent X/Twitter posts into a clean approval queue for the GLM-5.2 usecase repository, without touching README or curated dataset files before approval.

## Steps

### 1. Collect

Use `twitterapi-toolkit` to search recent posts within the requested time window.

Every search must enforce **like count > 10**:
- include `min_faves:11` or an equivalent advanced-search filter
- run a local result check and drop any record with `like_count < 11`

Collect at least:
- tweet_url
- tweet_id
- author_handle
- created_at
- full_text
- like_count
- reply_count / retweet_count / view_count when available
- media summary
- raw result payload or a recoverable reference

### 2. Deduplicate

Deduplicate in this order:
1. links already present in `README.md` and `README_*.md`
2. links already present in `glm-5.2-usecase-curated.json` / `.md`, when those files exist
3. duplicate or near-duplicate candidate posts from the same collection round

Rules:
- tweet URL is the primary key
- prefer original posts over reposts, quotes, or copied reposts
- if the same author posts several variants, keep the most complete one

### 3. Initial Screening

Drop items that are clearly not worth review:
- like_count is 10 or lower
- pure promotion with no usecase evidence
- not actually about GLM-5.2 / GLM-5.2 / `glm-5.2`
- no concrete workflow, prompt, demo, integration, benchmark, pricing note, limitation, or reproducible evidence
- too low information density to support a case
- pure news retellings about policy, backlash, hidden safeguards, or company statements unless they include concrete user-facing implications or source-backed operational detail
- crypto / investment / token promotion that only uses GLM-5.2 as a hook
- marketing CTA posts such as "bookmark this", "this guy made $X", or hype summaries unless they include a concrete prompt, demo, repo, benchmark, API workflow, or tutorial breakdown

The deterministic prefilter should require:
- a model-name hit
- at least one concrete evidence marker
- no hard news/marketing/crypto noise
- if soft noise is present, at least two concrete evidence signals

### 4. Manual Review

For each remaining item, identify:
- approved title
- proposed bold takeaway
- source text that should become the case body
- keep / drop / unsure
- target README section
- case type: Tutorial / Demo / Evaluation / Integration
- publication date as `YYYY-MM-DD`
- evidence note and caveats

Do not invent missing prompt text, benchmark numbers, dates, or creator attribution.

### 5. Approval Package

Prepare a user-facing review list.

Do not collapse nuance. The user should be able to approve or reject each candidate quickly.

### 6. Handoff

Once approved, pass the final approved set to `prompt-repo-update`.

Handoff rules:
- keep curation-stage artifacts in `/Users/evolink/.openclaw/workspace-github-ops/tmp/awesome-glm-5.2/...`
- do not move temp files into git history
- provide `prompt-repo-update` with a clean input package derived from the approved set
- if approval is incomplete or ambiguous, stop here instead of letting `prompt-repo-update` guess

## Recommended Artifact Paths

- `/Users/evolink/.openclaw/workspace-github-ops/tmp/awesome-glm-5.2/candidate_tweets.json`
- `/Users/evolink/.openclaw/workspace-github-ops/tmp/awesome-glm-5.2/prefiltered_candidates.json`
- `/Users/evolink/.openclaw/workspace-github-ops/tmp/awesome-glm-5.2/review_queue.json`
- `/Users/evolink/.openclaw/workspace-github-ops/tmp/awesome-glm-5.2/review_summary.md`

These are curation-only working files. Keep them outside the repo and do not commit or push them.
