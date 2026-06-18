#!/usr/bin/env python3
import argparse
import json
import os
import shlex
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path
from email.utils import parsedate_to_datetime

def resolve_toolkit_dir():
    codex_home = Path(os.environ.get('CODEX_HOME', '/Users/evolink/.codex'))
    candidates = [
        codex_home / 'skills' / 'twitterapi-toolkit',
        Path('/Users/evolink/.codex/skills/twitterapi-toolkit'),
    ]
    for candidate in candidates:
        if (candidate / 'scripts' / 'search-posts.sh').exists():
            return candidate
    return candidates[0]


TOOLKIT_DIR = resolve_toolkit_dir()
TOOLKIT_ENV = TOOLKIT_DIR / '.env'


def parse_created_at(raw: str):
    if not raw:
        return None
    try:
        return parsedate_to_datetime(raw).astimezone(timezone.utc)
    except Exception:
        return None


def run_search(query: str, query_type: str = 'Latest', max_pages: int = 1):
    env = dict(os.environ)
    env['ENV_FILE'] = str(TOOLKIT_ENV)
    env.setdefault('LC_CTYPE', 'UTF-8')
    env.setdefault('LANG', 'en_US.UTF-8')
    cmd = (
        f'cd {shlex.quote(str(TOOLKIT_DIR))} && '
        f'bash scripts/search-posts.sh {shlex.quote(query)} {shlex.quote(query_type)} {int(max_pages)}'
    )
    out = subprocess.check_output(cmd, shell=True, text=True, env=env)
    data = json.loads(out)
    tweets = data.get('tweets') or data.get('data') or []
    return tweets


def parse_int(value, default=0):
    try:
        if value is None:
            return default
        return int(value)
    except (TypeError, ValueError):
        return default


def first_present(payload, keys, default=0):
    for key in keys:
        if key in payload:
            return payload.get(key)
    return default


def ensure_min_faves_query(query: str, min_likes: int) -> str:
    if 'min_faves:' in query or 'min_favorites:' in query or 'min_likes:' in query:
        return query
    return f'({query}) min_faves:{min_likes}'


def normalize_tweet(tweet):
    media = tweet.get('extendedEntities', {}).get('media', [])
    media_urls = []
    for item in media:
        url = item.get('media_url_https') or item.get('media_url')
        if not url and item.get('type') == 'video':
            url = item.get('media_url_https') or item.get('display_url')
        if url:
            media_urls.append(url)
    author = tweet.get('author', {}) or {}
    return {
        'tweet_url': tweet.get('url') or tweet.get('twitterUrl') or '',
        'tweet_id': tweet.get('id') or '',
        'author_handle': author.get('userName') or '',
        'created_at': tweet.get('createdAt') or '',
        'full_text': tweet.get('text') or '',
        'like_count': parse_int(first_present(tweet, ['likeCount', 'like_count', 'favorite_count', 'favouritesCount'])),
        'reply_count': parse_int(first_present(tweet, ['replyCount', 'reply_count'])),
        'retweet_count': parse_int(first_present(tweet, ['retweetCount', 'retweet_count'])),
        'view_count': parse_int(first_present(tweet, ['viewCount', 'view_count', 'views'])),
        'media_urls': media_urls,
        'raw_payload': tweet,
    }


def main():
    parser = argparse.ArgumentParser(description='Collect recent candidate tweets for usecase repo curation')
    parser.add_argument('--queries', nargs='+', required=True, help='Search queries to run')
    parser.add_argument('--hours', type=int, default=24, help='Lookback window in hours')
    parser.add_argument('--max-pages', type=int, default=5, help='Max pages to fetch per query')
    parser.add_argument('--min-likes', type=int, default=11, help='Minimum likes required. Use 11 for like count > 10.')
    parser.add_argument('--out', required=True, help='Path to write collected candidate JSON')
    args = parser.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    seen = set()
    records = []

    searched_queries = []
    for query in args.queries:
        search_query = ensure_min_faves_query(query, args.min_likes)
        searched_queries.append(search_query)
        tweets = run_search(search_query, max_pages=args.max_pages)
        if not tweets:
            continue
        for tweet in tweets:
            row = normalize_tweet(tweet)
            url = row['tweet_url']
            if not url or url in seen:
                continue
            if row['like_count'] < args.min_likes:
                continue
            created = parse_created_at(row['created_at'])
            if created and created < cutoff:
                continue
            seen.add(url)
            records.append(row)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({
        'count': len(records),
        'out': str(out),
        'queries': searched_queries,
        'min_likes': args.min_likes
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
