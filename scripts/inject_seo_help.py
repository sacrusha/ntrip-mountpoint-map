"""Splice a static SEO mirror of data/help_topics.json into index.html.

The map page is a JS-rendered SPA; the help drawer's contents only enter the
DOM after a click. Crawlers without a JS renderer (and Googlebot's slow JS
queue for low-priority sites) never see that copy. This script bakes a
visually-hidden but indexable mirror of every topic's `q` (question) and
`lead` (one-paragraph answer) into `index.html` between sentinel comments.

Run after editing `data/help_topics.json`. Idempotent — re-running with no
data change yields no diff.

Usage: python scripts/inject_seo_help.py
"""

import json
import pathlib
import sys
from html import escape

ROOT = pathlib.Path(__file__).resolve().parent.parent
HELP_PATH = ROOT / "data" / "help_topics.json"
INDEX_PATH = ROOT / "index.html"

START_MARKER = "<!-- SEO_HELP_START — generated from data/help_topics.json by scripts/inject_seo_help.py -->"
END_MARKER = "<!-- SEO_HELP_END -->"


def render_block(help_data: dict) -> str:
    categories = help_data["categories"]
    topics = help_data["topics"]

    by_cat: dict[str, list[tuple[str, dict]]] = {c: [] for c in categories}
    for tid, t in topics.items():
        cat = t.get("cat")
        if cat in by_cat:
            by_cat[cat].append((tid, t))

    lines = [
        START_MARKER,
        '<section class="sr-only" aria-hidden="true">',
        "<h2>Help topics</h2>",
        "<p>Common questions about finding and using free NTRIP RTK correction streams.</p>",
    ]
    for cat in categories:
        items = by_cat.get(cat, [])
        if not items:
            continue
        lines.append(f"<h3>{escape(cat)}</h3>")
        for _tid, t in items:
            q = t.get("q", "").strip()
            lead = t.get("lead", "").strip()
            if not q or not lead:
                continue
            lines.append(f"<h4>{escape(q)}</h4>")
            lines.append(f"<p>{escape(lead)}</p>")
    lines.append("</section>")
    lines.append(END_MARKER)
    return "\n".join(lines)


def splice(index_html: str, block: str) -> str:
    start = index_html.find(START_MARKER)
    end = index_html.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        raise SystemExit(
            f"Sentinels not found in {INDEX_PATH}. Expected\n  {START_MARKER}\n  {END_MARKER}"
        )
    end_full = end + len(END_MARKER)
    return index_html[:start] + block + index_html[end_full:]


def main() -> int:
    help_data = json.loads(HELP_PATH.read_text(encoding="utf-8"))
    block = render_block(help_data)
    index_html = INDEX_PATH.read_text(encoding="utf-8")
    new_html = splice(index_html, block)
    if new_html == index_html:
        print("inject_seo_help: no change")
        return 0
    INDEX_PATH.write_text(new_html, encoding="utf-8")
    print(f"inject_seo_help: updated {INDEX_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
