#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

MODEL_MARKERS = [
    'glm-5.2', 'glm 5.2', 'glm5.2', 'glm 5', 'z.ai', 'zai', 'z-code', 'zcode'
]

EVIDENCE_MARKERS = [
    'prompt:', 'full prompt:', 'one prompt', 'single prompt', 'tek prompt',
    'github', 'repository', 'open source', 'source code',
    'demo', 'built', 'building', 'created', 'shipped', 'tested', 'scored',
    'benchmark', 'swe-bench', 'deepswe', 'frontierswe', 'terminal-bench', 'kernelbench',
    'bridgebench', 'swelancer', 'code arena', 'design arena', 'eval', 'evaluation',
    'comparison', 'cost', 'pricing', 'tokens',
    'api', 'opencode', 'zcode', 'z-code', 'cursor', 'replit', 'agent', 'workflow', 'tutorial',
    'course', 'guide', 'breakdown', 'article', 'simulator', 'game',
    'app', 'website', 'integration', 'changelog'
]

HARD_NOISE_MARKERS = [
    'giveaway', 'airdrop', 'promo code', 'follow me', 'subscribe',
    'dm me', 'waitlist only', 'hiring', 'job opening',
    '$tao', 'smart money', 'buying the infrastructure', 'no data center',
    'national security', 'anthropic ceo:', 'cointelegraph',
    'invisible guardrails', 'secretly degrading', 'researchers called',
    'bookmark it', 'this guy', 'wow!!', 'worth of website',
    'agencies sell', 'smart money', 'buying the infrastructure',
    'biden', 'kamala', 'joe rogan', 'behind closed doors',
    '已入驻', '不妨一试', '#tronecoster'
]

SOFT_NOISE_MARKERS = [
    'now:', 'walks back', 'walking back', 'wired reports', 'apologizes',
    'secret sabotage', 'hidden safeguards', 'covertly degraded',
    '10 things about', 'most people don', 'nobody', 'save this',
    'wow!!', 'this guy', 'bookmark it', 'wildest things', 'hype',
    'dropped yesterday', 'just launched', 'worth trying'
]

HARD_NOISE_AUTHORS = {
    'cointelegraph', 'coinbureau', 'wallstengine', 'crypto77qi', 'bitgetwallet'
}


def first_hit(text: str, markers):
    lower = (text or '').lower()
    for marker in markers:
        if marker.lower() in lower:
            return marker
    return ''


def hits(text: str, markers):
    lower = (text or '').lower()
    return [marker for marker in markers if marker.lower() in lower]


def main():
    parser = argparse.ArgumentParser(description='Prefilter usecase candidates using deterministic rules only')
    parser.add_argument('--in-json', required=True)
    parser.add_argument('--out-json', required=True)
    args = parser.parse_args()

    src = Path(args.in_json)
    dst = Path(args.out_json)
    data = json.loads(src.read_text(encoding='utf-8'))
    records = data['records'] if isinstance(data, dict) and 'records' in data else data

    out = []
    for item in records:
        text = item.get('full_text', '') or ''
        model_hit = first_hit(text, MODEL_MARKERS)
        evidence_hits = hits(text, EVIDENCE_MARKERS)
        has_media = bool(item.get('media_urls'))
        has_body = bool(text.strip())
        hard_noise_hits = hits(text, HARD_NOISE_MARKERS)
        soft_noise_hits = hits(text, SOFT_NOISE_MARKERS)
        author_handle = (item.get('author_handle') or '').lower().lstrip('@')
        hard_noise_author = author_handle in HARD_NOISE_AUTHORS
        like_count = int(item.get('like_count') or 0)

        evidence_score = len(set(evidence_hits))
        if has_media and evidence_score:
            evidence_score += 1

        should_review = (
            has_body
            and like_count >= 11
            and bool(model_hit)
            and evidence_score >= 2
            and not hard_noise_hits
            and not hard_noise_author
            and (not soft_noise_hits or evidence_score >= 2)
        )
        out.append({
            **item,
            'model_marker_hit': model_hit,
            'evidence_marker_hits': evidence_hits,
            'evidence_score': evidence_score,
            'has_media': has_media,
            'has_body': has_body,
            'hard_noise_hits': hard_noise_hits,
            'soft_noise_hits': soft_noise_hits,
            'hard_noise_author': hard_noise_author,
            'should_send_to_llm_review': should_review,
        })

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps({'records': out}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({
        'total': len(out),
        'for_llm_review': sum(1 for x in out if x['should_send_to_llm_review']),
        'model_hits': sum(1 for x in out if x['model_marker_hit']),
        'evidence_hits': sum(1 for x in out if x['evidence_marker_hits']),
        'hard_noise_hits': sum(1 for x in out if x['hard_noise_hits']),
        'hard_noise_authors': sum(1 for x in out if x['hard_noise_author']),
        'soft_noise_hits': sum(1 for x in out if x['soft_noise_hits'])
    }, ensure_ascii=False))


if __name__ == '__main__':
    main()
