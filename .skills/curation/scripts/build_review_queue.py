#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding='utf-8'))


def normalize_ingested(data):
    if isinstance(data, dict) and 'records' in data:
        return data['records']
    if isinstance(data, list):
        return data
    return []


SOURCE_LINK_RE = re.compile(r'https?://(?:x\.com|twitter\.com)/[^)\s"\']+')


def collect_existing_urls(repo: Path):
    urls = set()
    for path in [repo / 'README.md', *sorted(repo.glob('README_*.md'))]:
        if path.exists():
            urls.update(SOURCE_LINK_RE.findall(path.read_text(encoding='utf-8')))
    for path in [repo / 'glm-5.2-usecase-curated.json', repo / 'glm-5.2-usecase-curated.md']:
        if path.exists():
            urls.update(SOURCE_LINK_RE.findall(path.read_text(encoding='utf-8')))
    return {url.rstrip('.,') for url in urls}


def main():
    parser = argparse.ArgumentParser(description='Build a review queue for usecase repo candidate tweets')
    parser.add_argument('--candidates', required=True, help='Path to candidate tweets JSON')
    parser.add_argument('--repo', help='Path to target repo. Used to deduplicate against README and curated dataset links.')
    parser.add_argument('--ingested', help='Optional legacy ingested_tweets.json path')
    parser.add_argument('--out-json', required=True, help='Path to write review queue JSON')
    parser.add_argument('--out-md', required=True, help='Path to write markdown review summary')
    args = parser.parse_args()

    candidates_path = Path(args.candidates)
    out_json = Path(args.out_json)
    out_md = Path(args.out_md)

    candidates = load_json(candidates_path, [])
    if isinstance(candidates, dict) and 'records' in candidates:
        candidates = candidates['records']
    ingested = normalize_ingested(load_json(Path(args.ingested), [])) if args.ingested else []
    ingested_urls = {item.get('tweet_url') for item in ingested if item.get('tweet_url')}
    existing_urls = collect_existing_urls(Path(args.repo)) if args.repo else set()

    deduped = []
    seen = set()
    for item in candidates:
        if item.get('should_send_to_llm_review') is False:
            continue
        tweet_url = item.get('tweet_url') or item.get('url')
        if not tweet_url or tweet_url in seen or tweet_url in ingested_urls or tweet_url in existing_urls:
            continue
        seen.add(tweet_url)
        deduped.append({
            'tweet_url': tweet_url,
            'tweet_id': item.get('tweet_id') or item.get('id'),
            'author_handle': item.get('author_handle') or item.get('author') or '',
            'created_at': item.get('created_at') or '',
            'full_text': item.get('full_text') or item.get('text') or '',
            'like_count': item.get('like_count') or 0,
            'reply_count': item.get('reply_count') or 0,
            'retweet_count': item.get('retweet_count') or 0,
            'view_count': item.get('view_count') or 0,
            'media_urls': item.get('media_urls') or [],
            'suggested_title': item.get('suggested_title') or '',
            'takeaway': item.get('takeaway') or '',
            'case_body': item.get('case_body') or item.get('full_text') or item.get('text') or '',
            'suggested_action': item.get('suggested_action') or 'unsure',
            'suggested_category': item.get('suggested_category') or '',
            'suggested_type': item.get('suggested_type') or '',
            'publication_date': item.get('publication_date') or '',
            'evidence_note': item.get('evidence_note') or '',
        })

    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps({'records': deduped}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = ['# Review Summary', '']
    if not deduped:
        lines += ['- No new candidates after deduplication.', '']
    for idx, item in enumerate(deduped, start=1):
        lines += [
            f'## Candidate {idx}',
            '',
            f"- Link: {item['tweet_url']}",
            f"- Author: {item['author_handle'] or '-'}",
            f"- Likes: {item['like_count']}",
            f"- Suggested title: {item['suggested_title'] or '-'}",
            f"- Suggested action: {item['suggested_action']}",
            f"- Suggested category: {item['suggested_category'] or '-'}",
            f"- Suggested type: {item['suggested_type'] or '-'}",
            f"- Publication date: {item['publication_date'] or item['created_at'] or '-'}",
            f"- Evidence note: {item['evidence_note'] or '-'}",
            '- Proposed takeaway:',
            item['takeaway'] or '-',
            '- Source text / case body seed:',
            '```text',
            item['case_body'] or '',
            '```',
            ''
        ]
    lines += [
        '## Auto Review',
        '',
        'Classify each candidate as `high_confidence_update`, `unsure`, or `drop`.',
        'Selected high-confidence items may proceed directly to repo update, capped at 10 per run.',
        ''
    ]
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text('\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    main()
