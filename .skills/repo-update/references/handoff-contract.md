# Handoff Contract

`prompt-repo-update` assumes `prompt-curation` has already finished.
This skill consumes the approved curation output and does not redo keep/drop judgment.

## Required Handoff Payload

For each approved candidate, the updater should already know:
- tweet_url
- author_handle
- author profile URL
- like_count, confirmed greater than 10
- approved title
- approved bold takeaway
- approved case body
- target README category
- type: Tutorial / Demo / Evaluation / Integration
- publication date as `YYYY-MM-DD`
- whether the item passed the keep/drop decision

At batch level, the updater should also already know:
- repo path
- final approved candidate set
- final keep list for this update batch
- where curation-stage artifacts live in workspace temp

## What Should Not Still Be Undecided

These must already be settled before repo update begins:
- whether to keep or drop the item
- whether the item passed the like > 10 search threshold
- title quality
- exact body content boundaries
- category placement
- type
- publication date
- creator attribution

## If Any Of These Are Unclear

Stop and return to curation rather than guessing.

Do not start repo update work while keep/drop, evidence, attribution, date, type, or category placement are still being decided.
