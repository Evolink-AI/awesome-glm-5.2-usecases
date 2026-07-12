#!/usr/bin/env python3
"""Build an honest, deterministic Star History snapshot for the README.

The live star-history image endpoint can time out for new repositories. This
script produces a stable SVG from GitHub metadata without inventing a trend.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="GitHub owner/repository")
    parser.add_argument("--stars", required=True, type=int)
    parser.add_argument("--created-at", required=True, help="YYYY-MM-DD")
    parser.add_argument("--snapshot-date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--out", default="images/star-history.svg")
    args = parser.parse_args()

    if args.stars < 0:
        parser.error("--stars must be non-negative")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420" viewBox="0 0 900 420" role="img" aria-labelledby="title desc">
  <title id="title">Star History for {args.repo}</title>
  <desc id="desc">GitHub snapshot on {args.snapshot_date}: {args.stars} stars. Repository created {args.created_at}. No trend is inferred.</desc>
  <rect width="900" height="420" rx="18" fill="#0d1117"/>
  <text x="52" y="62" fill="#f0f6fc" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="27" font-weight="700">Star History</text>
  <text x="52" y="94" fill="#8b949e" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="16">{args.repo}</text>
  <line x1="72" y1="310" x2="842" y2="310" stroke="#30363d" stroke-width="2"/>
  <line x1="72" y1="130" x2="72" y2="310" stroke="#30363d" stroke-width="2"/>
  <line x1="72" y1="265" x2="842" y2="265" stroke="#21262d"/>
  <line x1="72" y1="220" x2="842" y2="220" stroke="#21262d"/>
  <line x1="72" y1="175" x2="842" y2="175" stroke="#21262d"/>
  <circle cx="72" cy="310" r="6" fill="#58a6ff"/>
  <circle cx="842" cy="310" r="6" fill="#58a6ff"/>
  <path d="M72 310 L842 310" fill="none" stroke="#58a6ff" stroke-width="3"/>
  <text x="457" y="216" text-anchor="middle" fill="#f0f6fc" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="54" font-weight="700">{args.stars}</text>
  <text x="457" y="247" text-anchor="middle" fill="#8b949e" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="17">stars at snapshot</text>
  <text x="72" y="342" fill="#8b949e" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="14">Created {args.created_at}</text>
  <text x="842" y="342" text-anchor="end" fill="#8b949e" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="14">Snapshot {args.snapshot_date}</text>
  <text x="450" y="388" text-anchor="middle" fill="#6e7681" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="13">Static GitHub metadata snapshot; no historical trend is inferred.</text>
</svg>
'''
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
