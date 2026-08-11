#!/usr/bin/env bash
#
# Regenerates assets/downloads/ICNGCI-2026-Conference-Information.docx from the
# site's HTML pages, so the Word document and the website cannot drift apart.
#
#   ./tools/make-docx.sh
#
# Creates a throwaway virtualenv in tools/.venv the first time (python-docx is
# the only dependency, and it is kept out of your system Python).

set -euo pipefail
cd "$(dirname "$0")/.."

VENV="tools/.venv"

if [ ! -d "$VENV" ]; then
  echo "Creating $VENV and installing python-docx…"
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install --quiet --upgrade pip
  "$VENV/bin/pip" install --quiet python-docx
fi

"$VENV/bin/python" tools/make_docx.py
