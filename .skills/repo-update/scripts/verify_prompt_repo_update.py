#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path
from typing import List, Tuple

CASE_HEADING_RE = re.compile(r'^### Case\s+(\d+):', re.MULTILINE)
CASE_ANCHOR_RE = re.compile(r'<a id="case-(\d+)"></a>')
CASE_COMMENT_RE = re.compile(r'^<!--\s*Case\s+\d+:', re.MULTILINE)
IMG_RE = re.compile(r'<img\s+[^>]*src="([^"]+)"', re.IGNORECASE)
ENGLISH_ADDED_RE = re.compile(r'-\s*\*\*[^*]+\*\*:\s*Added\b')
MENU_CASE_LINK_RE = re.compile(r'^-\s*\[Case\s+\d+:.*?\]\(#.*\)', re.MULTILINE)
MENU_RANGE_RE = re.compile(r'\|\s*\[[^\]]+\]\(#[^)]+\)\s*\|\s*Case\s+\d+(?:-\d+)?\s*\|')
FINAL_SECTION_RE = re.compile(r'^(##\s+Star History|##\s+Acknowledge(?:ments)?|##\s+Acknowledg?e?)\b', re.MULTILINE)
FORBIDDEN_RE = re.compile(r'How to use it:|Tweet excerpt|19 more creators|more creators')
ENGLISH_CASE_TYPE_RE = re.compile(r'^Type:\s*[^|\n]+\s*\|\s*Date:\s*\d{4}-\d{2}-\d{2}\s*$', re.MULTILINE)
LOCALIZED_CASE_META_RE = re.compile(r'^[^#\n]*[:：]\s*[^|\n]+\|\s*[^#\n]*[:：]\s*\d{4}-\d{2}-\d{2}\s*$', re.MULTILINE)


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def count_case_headings(text: str) -> int:
    return len(CASE_HEADING_RE.findall(text))


def case_numbers(text: str) -> List[int]:
    return [int(n) for n in CASE_HEADING_RE.findall(text)]


def anchor_numbers(text: str) -> List[int]:
    return [int(n) for n in CASE_ANCHOR_RE.findall(text)]


def count_case_comments(text: str) -> int:
    return len(CASE_COMMENT_RE.findall(text))


def count_menu_case_links(text: str) -> int:
    bullet_count = len(MENU_CASE_LINK_RE.findall(text))
    range_count = len(MENU_RANGE_RE.findall(text))
    return bullet_count or range_count


def expected_sequence(count: int) -> List[int]:
    return list(range(1, count + 1))


def find_final_section_start(text: str) -> int:
    match = FINAL_SECTION_RE.search(text)
    return match.start() if match else -1


def has_case_after_final_sections(text: str) -> bool:
    idx = find_final_section_start(text)
    if idx == -1:
        return False
    tail = text[idx:]
    return bool(CASE_HEADING_RE.search(tail) or CASE_COMMENT_RE.search(tail))


def find_missing_images(text: str, readme_path: Path) -> List[str]:
    missing = []
    repo_root = readme_path.parent
    for src in IMG_RE.findall(text):
        if src.startswith('http://') or src.startswith('https://'):
            continue
        normalized = src[2:] if src.startswith('./') else src
        img_path = (repo_root / normalized).resolve()
        if not img_path.exists():
            missing.append(src)
    return missing


def is_non_english_readme(path: Path) -> bool:
    return path.name != 'README.md' and path.name.startswith('README_') and path.suffix == '.md'


def verify_file(path: Path, english_case_count: int = None) -> Tuple[List[str], dict]:
    text = read_text(path)
    errors: List[str] = []
    case_count = count_case_headings(text)
    cases = case_numbers(text)
    anchors = anchor_numbers(text)
    comment_count = count_case_comments(text)
    menu_count = count_menu_case_links(text)
    missing_images = find_missing_images(text, path)

    if comment_count not in (0, case_count):
        errors.append(f'{path.name}: case heading count {case_count} != case comment count {comment_count}')
    if len(anchors) != case_count:
        errors.append(f'{path.name}: case anchor count {len(anchors)} != case count {case_count}')
    if sorted(cases) != expected_sequence(case_count):
        errors.append(f'{path.name}: case headings are not a contiguous 1..{case_count} sequence')
    if sorted(anchors) != expected_sequence(case_count):
        errors.append(f'{path.name}: case anchors are not a contiguous 1..{case_count} sequence')
    if cases != anchors:
        errors.append(f'{path.name}: case heading numbers do not match anchor numbers in order')
    if missing_images:
        errors.append(f'{path.name}: missing image references: {missing_images[:10]}')
    if has_case_after_final_sections(text):
        errors.append(f'{path.name}: found case blocks after final sections')
    if english_case_count is not None and case_count != english_case_count:
        errors.append(f'{path.name}: case count {case_count} != English case count {english_case_count}')
    if is_non_english_readme(path) and ENGLISH_ADDED_RE.search(text):
        errors.append(f'{path.name}: contains English `Added ...` News bullet in non-English README')
    if FORBIDDEN_RE.search(text):
        errors.append(f'{path.name}: contains forbidden old-template text')
    if path.name == 'README.md':
        type_lines = ENGLISH_CASE_TYPE_RE.findall(text)
        if len(type_lines) != case_count:
            errors.append(f'{path.name}: Type/Date line count {len(type_lines)} != case count {case_count}')
    else:
        meta_lines = LOCALIZED_CASE_META_RE.findall(text)
        if len(meta_lines) != case_count:
            errors.append(f'{path.name}: localized type/date metadata line count {len(meta_lines)} != case count {case_count}')

    stats = {
        'file': path.name,
        'case_count': case_count,
        'anchor_count': len(anchors),
        'comment_count': comment_count,
        'menu_count': menu_count,
        'missing_images': len(missing_images),
    }
    return errors, stats


def collect_readmes(repo: Path) -> List[Path]:
    files = [repo / 'README.md']
    files.extend(sorted(repo.glob('README_*.md')))
    return [p for p in files if p.exists()]


def main():
    parser = argparse.ArgumentParser(description='Verify English and localized usecase repo README integrity')
    parser.add_argument('--repo', required=True, help='Path to target usecase repo')
    parser.add_argument('--json', action='store_true', help='Print JSON summary')
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    english = repo / 'README.md'
    if not english.exists():
        raise SystemExit(f'Missing English README: {english}')

    english_errors, english_stats = verify_file(english)
    english_case_count = english_stats['case_count']

    all_errors = list(english_errors)
    all_stats = [english_stats]

    for path in collect_readmes(repo):
        if path == english:
            continue
        errs, stats = verify_file(path, english_case_count=english_case_count)
        all_errors.extend(errs)
        all_stats.append(stats)

    result = {
        'repo': str(repo),
        'ok': not all_errors,
        'english_case_count': english_case_count,
        'checked_files': [s['file'] for s in all_stats],
        'stats': all_stats,
        'errors': all_errors,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if all_errors:
            print('FAIL')
            for err in all_errors:
                print(f'- {err}')
        else:
            print('PASS')
            print(f'Checked {len(all_stats)} README files, English case count = {english_case_count}')

    raise SystemExit(0 if not all_errors else 1)


if __name__ == '__main__':
    main()
