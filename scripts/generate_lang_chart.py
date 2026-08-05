#!/usr/bin/env python3
"""
Regenerates assets/lang-chart.svg from real, byte-weighted GitHub language
data (not repo-count, which overweights small scaffold/coursework repos).

Run by .github/workflows/update-lang-chart.yml on a schedule and on push.
Needs a GITHUB_TOKEN with `public_repo` read access (the default Actions
token is enough) so it isn't limited to the 60 req/hr unauthenticated quota.
"""

import os
import sys
import urllib.request
import json

USERNAME = "HardikBhaskar2010"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"

# Palette pulled straight from the header/footer assets — keep in sync.
COLORS = {
    "TypeScript": "#3178C6",
    "Python": "#3776AB",
    "C": "#A78BFA",
    "C++": "#7C3AED",
    "JavaScript": "#F1C40F",
    "HTML": "#E34F26",
    "CSS": "#06B6D4",
    "Rust": "#DE7A22",
    "Shell": "#89E051",
}
DEFAULT_COLOR = "#6B7280"


def api_get(path):
    req = urllib.request.Request(f"{API}{path}")
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def fetch_all_repos():
    repos, page = [], 1
    while True:
        batch = api_get(f"/users/{USERNAME}/repos?per_page=100&page={page}&type=owner")
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return [r for r in repos if not r.get("fork")]


def fetch_languages(repo_name):
    try:
        return api_get(f"/repos/{USERNAME}/{repo_name}/languages")
    except Exception as e:
        print(f"  ! skipped {repo_name}: {e}", file=sys.stderr)
        return {}


def aggregate():
    totals = {}
    repos = fetch_all_repos()
    print(f"Scanning {len(repos)} non-fork repos...")
    for repo in repos:
        langs = fetch_languages(repo["name"])
        for lang, byte_count in langs.items():
            totals[lang] = totals.get(lang, 0) + byte_count
    return totals


def render_svg(totals, top_n=6):
    grand_total = sum(totals.values()) or 1
    ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:top_n]

    width, row_h, bar_max, left_pad = 640, 34, 380, 190
    height = 40 + row_h * len(ranked) + 20

    rows = []
    for i, (lang, byte_count) in enumerate(ranked):
        pct = byte_count / grand_total * 100
        bar_w = max(4, bar_max * (pct / 100))
        y = 40 + i * row_h
        color = COLORS.get(lang, DEFAULT_COLOR)
        delay = i * 0.12
        rows.append(f'''
    <text x="0" y="{y + 15}" font-family="'JetBrains Mono',monospace" font-size="13" fill="#E5E7EB">{lang}</text>
    <rect x="{left_pad}" y="{y}" width="{bar_max}" height="16" rx="4" fill="#1a1a2e"/>
    <rect x="{left_pad}" y="{y}" width="0" height="16" rx="4" fill="{color}">
      <animate attributeName="width" from="0" to="{bar_w:.1f}" dur="0.8s" begin="{delay:.2f}s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
    </rect>
    <text x="{left_pad + bar_max + 12}" y="{y + 13}" font-family="'JetBrains Mono',monospace" font-size="12" fill="#A78BFA">{pct:.1f}%</text>''')

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{width}" height="{height}" rx="12" fill="#0B1020"/>
  <text x="0" y="24" font-family="'JetBrains Mono',monospace" font-size="14" fill="#6B7280" letter-spacing="1">LANGUAGES · BY BYTES, NOT REPO COUNT</text>
  <g transform="translate(16,0)">{''.join(rows)}
  </g>
</svg>'''
    return svg


def main():
    totals = aggregate()
    if not totals:
        print("No language data collected — leaving existing chart untouched.")
        return
    svg = render_svg(totals)
    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "lang-chart.svg")
    with open(out_path, "w") as f:
        f.write(svg)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
