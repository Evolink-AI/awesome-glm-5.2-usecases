# Review Output Format

Use this structure when presenting GLM-5.2 usecase candidates for approval.

## Per Candidate

- Link
- Author
- Likes
- Suggested title
- Proposed takeaway
- Source text / case body seed
- Suggested action: keep / drop / unsure
- Suggested category
- Suggested type: Tutorial / Demo / Evaluation / Integration
- Publication date
- Evidence note

## Example

- Link: <tweet_url>
- Author: @handle
- Likes: 42
- Suggested title: Cursor Multi-Stage Workflow
- Proposed takeaway: Use GLM-5.2 as the plan-review and critique step inside a multi-model Cursor workflow.
- Source text / case body seed:
  ```text
  source-backed notes or excerpt seed
  ```
- Suggested action: keep
- Suggested category: Coding and Code Generation
- Suggested type: Evaluation
- Publication date: 2026-06-09
- Evidence note: Includes concrete workflow phases and model routing details.

## Final Approval Prompt

After listing all candidates, ask for explicit confirmation of which items to keep.

Good pattern:
- Keep: #1 #2 #4
- Drop: #3
- Unsure: #5

Do not proceed to repo writes until the approval is clear.
