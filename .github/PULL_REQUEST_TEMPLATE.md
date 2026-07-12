# Pull Request Checklist

## Case Evidence

- [ ] Every new case has a public source link.
- [ ] Every new case has a creator profile link.
- [ ] Claims are grounded in the source and do not invent prompts, scores, or results.
- [ ] Case type is one of: Demo, Tutorial, Evaluation, Integration, Benchmark, Limit.
- [ ] Date uses `YYYY-MM-DD`.

## README Structure

- [ ] Each new case has a stable `<a id="case-x"></a>` anchor.
- [ ] Case heading uses `### Case X: [Title](source-link) (by [@author](author-link))`.
- [ ] Menu links point to `#case-x`.
- [ ] English and localized README files keep the same case order and source links.
- [ ] Localized titles and takeaways are translated; source/author URLs, Type, Date, anchors, commands, model IDs, and code blocks preserve the English contract.
- [ ] `data/glm-5.2-usecase-curated.json` and `.md` were regenerated and match the public README cases.
- [ ] No raw source exports, internal curation artifacts, or local source paths are committed.

## Media And Links

- [ ] New public README/docs media is R2-hosted and covered by the media inventory/upload report.
- [ ] Images pass R2 origin and rendered GitHub/camo checks.
- [ ] Videos use an R2 poster image linked to a playable R2 video URL.
- [ ] Public links, relative files, anchors, and EvoLink UTM slots pass `scripts/audit_public_links.py`.
- [ ] Related Repositories only links adjacent surfaces; this PR does not release or completion-gate Skill/API repositories.

## Maintenance

- [ ] `docs/maintenance.md` still reflects current repository policy.
- [ ] Acknowledge section includes high-signal creators without vague rollups.
- [ ] `python3 scripts/build_curated_data.py` and the usecase verifier pass.
