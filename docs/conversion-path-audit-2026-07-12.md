# GitHub-to-First-Call Conversion Path Audit

- Audit date: 2026-07-12
- Model: GLM-5.2
- Campaign: `awesome-glm-5.2-usecases`
- Result: PASS for public route and link accessibility; runtime smoke is recorded separately.

| Step | Action | Target | Verification |
|---|---|---|---|
| 1 | Open the current GLM-5.2 model page | `https://evolink.ai/glm-5-2` | HTTP 200 |
| 2 | Get an API key | `https://evolink.ai/dashboard/keys` | HTTP 200 |
| 3 | Run the current-model first call | `https://docs.evolink.ai/en/api-manual/language-series/glm-5.2/glm-5.2-api` | HTTP 200 |

The first screen and Quick Start expose this route before the first case category. No adjacent or older model is presented as the current GLM-5.2 first-run surface. No verified installable GLM-5.2 skill repository is asserted; Related Repositories explicitly routes readers to the verified API documentation.

All README CTA slots are recorded in `docs/url-utm-matrix.md` and passed the public-surface UTM audit.
