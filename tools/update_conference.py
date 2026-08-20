import re
import os

print("Starting conference updates...")

# 1. Update basic replacements across all HTML files
replacements = [
    ("International Conference on Next-Generation Computing and Innovations", "International Conference on Intelligent, Connected and Sustainable Computing"),
    ("International Conference on Next-Generation Computing & Innovations", "International Conference on Intelligent, Connected and Sustainable Computing"),
    ("Next-Generation Computing &amp; Innovations", "Intelligent, Connected &amp; Sustainable Computing"),
    ("Next-Generation Computing and Innovations", "Intelligent, Connected and Sustainable Computing"),
    ("Next-Generation Computing & Innovations", "Intelligent, Connected and Sustainable Computing"),
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

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print("Found HTML files:", html_files)

