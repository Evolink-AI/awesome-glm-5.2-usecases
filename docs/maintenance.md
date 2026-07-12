# Maintenance Guide

## Source Policy

This public repository does not store raw X/Twitter exports, private spreadsheets, local data paths, or internal curation artifacts. It does store a generated public inventory for portable verification:

- `data/glm-5.2-usecase-curated.json` — machine-readable public case inventory
- `data/glm-5.2-usecase-curated.md` — human-readable inventory
- `data/usecase-update-config.json` — namespace, numbering, Menu, localization, and structured-data verifier policy

`README.md` is the editorial source of truth. Regenerate both curated inventory files after every English case change:

```bash
python3 scripts/build_curated_data.py
```

Public traceability is maintained through each case heading:

```md
### Case X: [Title](source-link) (by [@author](author-link))
```

The source link points to the public post or public source, and the author link points to the creator profile.

## Case Selection Rules

Include only high-signal GLM-5.2 cases with concrete evidence:

- benchmark, leaderboard, or evaluation results
- coding-agent workflows with task detail
- hands-on demo or shipped output
- provider, framework, or tool integration
- pricing, free access, quota, or local deployment details
- limitation, caveat, safety, latency, or benchmark-methodology concern

Exclude:

- pure hype or reaction-only posts
- prediction-only posts
- duplicate quote posts without new evidence
- unsupported claims without source context
- invented prompts or inferred results

## Update Checklist

1. Confirm the source is public and directly related to GLM-5.2.
2. Choose the best category based on the actual evidence.
3. Add a stable `<a id="case-x"></a>` anchor.
4. Use the `### Case X` heading format exactly.
5. Write a bold, reusable usage takeaway.
6. Keep notes grounded in the source.
7. Add `Type: ... | Date: YYYY-MM-DD`.
8. Rebuild the Menu and all localized README files with the same case order, source links, author links, Type, and Date.
9. Translate every localized case title and takeaway; preserve model IDs, URLs, anchors, commands, and code blocks.
10. Regenerate the curated JSON/Markdown inventory.
11. Re-run the usecase verifier, public-link audit, R2 origin check, and rendered GitHub media audit.

## Case Format

Every published case uses this shape:

```md
<a id="case-X"></a>
### Case X: [Title](source-link) (by [@author](author-link))

**A source-grounded reader-action takeaway.**

Source-content notes.

Type: Demo | Date: YYYY-MM-DD
```

Public case IDs must remain a unique contiguous set. Category-grouped document order is allowed because `data/usecase-update-config.json` declares `numbering_order: set-contiguous`.

## Validation Commands

```bash
python3 scripts/build_curated_data.py
python3 .skills/repo-update/scripts/verify_prompt_repo_update.py --repo .
python3 /path/to/usecase-update-loop/scripts/verify_usecase_update.py --repo .
python3 scripts/audit_public_links.py --repo . --out docs/public-surface-link-audit.md
git diff --check
find . \( -name .DS_Store -o -name __pycache__ -o -name '*.pyc' \) -print
```

The portable usecase verifier must consume the tracked namespace config and curated JSON. It must not depend on ignored `.codex/` artifacts.

## Quick API Access

The repository includes an Evolink-only Quick API Access section in every README. The example uses the GLM-5.2 OpenAI-compatible Chat Completions endpoint documented by Evolink:

- API docs: `https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api`
- Endpoint: `https://direct.evolink.ai/v1/chat/completions`
- Model: `glm-5.2`

Do not replace this section with Z.ai examples or non-Evolink provider snippets.

## Suggested GitHub About

Description:

> Curated GLM-5.2 use cases for coding agents, benchmarks, integrations, pricing, local deployment, and real-world limits.

Website:

> https://evolink.ai/glm-5-2

Topics:

`glm-5-2`, `glm`, `z-ai`, `open-weight-models`, `coding-agents`, `ai-benchmarks`, `llm-use-cases`, `agentic-coding`, `evolink`, `multilingual-readme`

## Media And R2 Policy

- Public README/docs media must render from the locked `github-repo-media` R2 namespace.
- Keep local source assets only when they are useful for maintenance; public Markdown must use the R2 URL.
- Record the full media inventory, upload result, R2 origin status, and post-push GitHub/camo render result.
- Videos must use an R2-hosted poster frame linked to a playable R2 video URL; do not embed raw video as the primary visible media.

## Related Repository Boundary

This usecase repository may link to verified GLM-5.2 API, Skill, prompt, guide, or other usecase surfaces. It does not scaffold, audit, release, or completion-gate adjacent Skill/API repositories; those are owned by the corresponding release agent.
