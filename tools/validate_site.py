import glob
import re
from html.parser import HTMLParser

class Validator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []

for fpath in sorted(glob.glob("*.html")):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Parse HTML
    parser = Validator()
    try:
        parser.feed(content)
    except Exception as e:
        print(f"HTML Parse Error in {fpath}: {e}")
    
    # 2. Check for ICNGCI
    if "ICNGCI" in content:
        print(f"WARNING: ICNGCI found in {fpath}")
    
    # 3. Check for old dates
    if "19–20 February 2027" in content or "19-20 February 2027" in content:
        print(f"WARNING: Old conference dates found in {fpath}")

print("Validation completed.")
