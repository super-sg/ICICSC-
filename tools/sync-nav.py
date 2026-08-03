#!/usr/bin/env python3
"""
sync-nav.py — keep the header and footer identical across every page.

The site is plain static HTML with no build step, so the navigation bar and the
footer are written out in full in each .html file. That is deliberate: the pages
work with JavaScript disabled and search engines index them perfectly.

The cost is that adding a menu item means editing every file. This script pays
that cost for you:

    1. Edit the header and/or footer in  index.html  only.
    2. Run:  python3 tools/sync-nav.py
    3. Every other page is updated to match.

Run it from anywhere; it locates the project by its own path.

    python3 tools/sync-nav.py            # apply changes
    python3 tools/sync-nav.py --check    # report drift, change nothing (exit 1 if any)
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = "index.html"

# (name, regex capturing the whole block)
BLOCKS = [
    ("header", re.compile(r'<a class="skip-link".*?</header>', re.S)),
    ("footer", re.compile(r'<footer class="footer">.*?</footer>', re.S)),
]


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def main():
    check_only = "--check" in sys.argv

    src = read(SOURCE)
    canonical = {}
    for name, pattern in BLOCKS:
        m = pattern.search(src)
        if not m:
            sys.exit("error: could not find the %s block in %s" % (name, SOURCE))
        canonical[name] = m.group(0)

    pages = sorted(f for f in os.listdir(ROOT)
                   if f.endswith(".html") and f != SOURCE)

    drifted = []
    for page in pages:
        original = read(page)
        updated = original
        changed = []

        for name, pattern in BLOCKS:
            m = pattern.search(updated)
            if not m:
                print("  ! %-24s no %s block found — skipped" % (page, name))
                continue
            if m.group(0) != canonical[name]:
                updated = updated[:m.start()] + canonical[name] + updated[m.end():]
                changed.append(name)

        if not changed:
            print("  = %-24s up to date" % page)
            continue

        drifted.append(page)
        if check_only:
            print("  ! %-24s differs: %s" % (page, ", ".join(changed)))
        else:
            with open(os.path.join(ROOT, page), "w", encoding="utf-8") as fh:
                fh.write(updated)
            print("  + %-24s updated: %s" % (page, ", ".join(changed)))

    print()
    if check_only and drifted:
        print("%d page(s) out of sync with %s." % (len(drifted), SOURCE))
        return 1
    if drifted:
        print("Synced %d page(s) from %s." % (len(drifted), SOURCE))
    else:
        print("All %d page(s) already match %s." % (len(pages), SOURCE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
