# Maintenance Guide

## Source Policy

This public repository does not store raw X/Twitter exports, private spreadsheets, local data paths, or internal curation datasets.

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
8. Rebuild the Menu and all localized README files with the same case order and source links.
9. Re-run the review checklist.

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

> https://evolink.ai/glm-5.2?utm_source=github&utm_medium=readme&utm_campaign=awesome-glm-5.2-usecases

Topics:

`glm-5-2`, `glm`, `z-ai`, `open-weight-models`, `coding-agents`, `ai-benchmarks`, `llm-use-cases`, `agentic-coding`, `evolink`, `multilingual-readme`
