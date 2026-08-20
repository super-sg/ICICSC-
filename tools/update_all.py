import os
import re

ROOT = "/Users/supersg/Documents/Random Projects/Conference SIte (IEEE)"
os.chdir(ROOT)

print("Starting full site modernization to ICICSC-2027...")

# Common brand replacements
COMMON_REPLACEMENTS = [
    (r"International Conference on Next-Generation Computing and Innovations", "International Conference on Intelligent, Connected and Sustainable Computing"),
    (r"International Conference on Next-Generation Computing & Innovations", "International Conference on Intelligent, Connected and Sustainable Computing"),
    (r"Next-Generation Computing &amp; Innovations", "Intelligent, Connected &amp; Sustainable Computing"),
    (r"Next-Generation Computing and Innovations", "Intelligent, Connected and Sustainable Computing"),
    (r"Next-Generation Computing & Innovations", "Intelligent, Connected and Sustainable Computing"),
    (r"Next-Generation Computing &amp; Intelligence", "Intelligent, Connected &amp; Sustainable Computing"),
    (r"ICNGCI\s*2027", "ICICSC 2027"),
    (r"ICNGCI-2027", "ICICSC-2027"),
    (r"ICNGCI", "ICICSC"),
    (r"icngci2027", "icicsc2027"),
    (r"icngci", "icicsc"),
    (r"19[–-]20 February 2027", "28–29 May 2027"),
    (r"19[–-]20 Feb 2027", "28–29 May 2027"),
    (r"February 19[–-]20, 2027", "May 28–29, 2027"),
]

def apply_common_replacements(content):
    for pat, rep in COMMON_REPLACEMENTS:
        content = re.sub(pat, rep, content)
    return content

print("Common replacer ready.")
