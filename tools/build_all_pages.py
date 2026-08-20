import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

print("Starting build_all_pages.py in:", ROOT)

# -------------------------------------------------------------
# Base Replacements across all files
# -------------------------------------------------------------
COMMON_REPLACEMENTS = [
    ("International Conference on Next-Generation Computing and Innovations", "International Conference on Intelligent, Connected and Sustainable Computing"),
    ("International Conference on Next-Generation Computing & Innovations", "International Conference on Intelligent, Connected and Sustainable Computing"),
    ("International Conference on Next-Generation Computing and Intelligence", "International Conference on Intelligent, Connected and Sustainable Computing"),
    ("International Conference on Next-Generation Computing & Intelligence", "International Conference on Intelligent, Connected and Sustainable Computing"),
    ("Next-Generation Computing &amp; Innovations", "Intelligent, Connected &amp; Sustainable Computing"),
    ("Next-Generation Computing &amp; Intelligence", "Intelligent, Connected &amp; Sustainable Computing"),
    ("Next-Generation Computing and Innovations", "Intelligent, Connected and Sustainable Computing"),
    ("Next-Generation Computing & Innovations", "Intelligent, Connected and Sustainable Computing"),
    ("Next-Generation Computing & Intelligence", "Intelligent, Connected and Sustainable Computing"),
    ("ICNGCI 2027", "ICICSC 2027"),
    ("ICNGCI-2027", "ICICSC-2027"),
    ("ICNGCI", "ICICSC"),
    ("icngci2027", "icicsc2027"),
    ("icngci", "icicsc"),
    ("19–20 February 2027", "28–29 May 2027"),
    ("19-20 February 2027", "28–29 May 2027"),
    ("19–20 Feb 2027", "28–29 May 2027"),
    ("19-20 Feb 2027", "28–29 May 2027"),
    ("February 19–20, 2027", "May 28–29, 2027"),
    ("February 19-20, 2027", "May 28–29, 2027"),
]

def apply_global_text_transforms(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in COMMON_REPLACEMENTS:
        content = content.replace(old, new)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Applied base global transforms to {file_path}")

all_html = [f for f in os.listdir(ROOT) if f.endswith(".html")]
for html_file in all_html:
    apply_global_text_transforms(html_file)

print("Base replacements finished.")
