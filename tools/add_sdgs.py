import os
import re

sdgs = {
    1: ["SDG 9 – Industry, Innovation & Infrastructure", "SDG 4 – Quality Education"],
    2: ["SDG 9 – Industry, Innovation & Infrastructure", "SDG 8 – Decent Work & Economic Growth"],
    3: ["SDG 16 – Peace, Justice & Strong Institutions", "SDG 9 – Industry, Innovation & Infrastructure"],
    4: ["SDG 9 – Industry, Innovation & Infrastructure", "SDG 11 – Sustainable Cities"],
    5: ["SDG 9 – Industry, Innovation & Infrastructure", "SDG 11 – Sustainable Cities"],
    6: ["SDG 11 – Sustainable Cities & Communities", "SDG 3 – Good Health & Well-being"]
}

def generate_sdg_html_tracks(track_num):
    s1, s2 = sdgs[track_num]
    # Creating a small div to hold SDG tags
    return f'\n        <div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;">\n          <span class="chip" style="font-size: 0.75rem; background: var(--surface-2); border: 1px solid var(--border);">{s1}</span>\n          <span class="chip" style="font-size: 0.75rem; background: var(--surface-2); border: 1px solid var(--border);">{s2}</span>\n        </div>'

def generate_sdg_html_cards(track_num):
    s1, s2 = sdgs[track_num]
    return f'<div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">{s1}</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">{s2}</span></div>'


# Update tracks.html
with open('tracks.html', 'r', encoding='utf-8') as f:
    content = f.read()

for i in range(1, 7):
    # In tracks.html:
    # <div class="track__head">
    #   <p class="track__num">Track 1</p>
    #   <h3>...</h3>
    #   <p>...</p>
    # </div>
    pattern = re.compile(rf'(<div class="track__head">.*?<p class="track__num">Track {i}</p>.*?<h3>.*?</h3>.*?<p>.*?</p>)(?=\s*</div>)', re.DOTALL)
    content = pattern.sub(lambda m: m.group(1) + generate_sdg_html_tracks(i), content)

with open('tracks.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update call-for-papers.html
with open('call-for-papers.html', 'r', encoding='utf-8') as f:
    content = f.read()

for i in range(1, 7):
    # In call-for-papers.html:
    # <article class="card trackcard"...><div class="card__body"><p class="trackcard__num">Track 1</p><h3>...</h3><p>...</p>
    pattern = re.compile(rf'(<article class="card trackcard"[^>]*>.*?<p class="trackcard__num">Track {i}</p>.*?<h3>.*?</h3>.*?<p>.*?</p>)(?=<a class="arrow-link")', re.DOTALL | re.IGNORECASE)
    content = pattern.sub(lambda m: m.group(1) + generate_sdg_html_cards(i), content)
    
with open('call-for-papers.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for i in range(1, 7):
    # In index.html:
    # <p class="trackcard__num">Track 1</p>
    # <h3>...</h3>
    # <p>...</p>
    # <a class="arrow-link"...>
    pattern = re.compile(rf'(<p class="trackcard__num">Track {i}</p>\s*<h3>.*?</h3>\s*<p>.*?</p>\s*)(?=<a class="arrow-link")', re.DOTALL)
    content = pattern.sub(lambda m: m.group(1) + generate_sdg_html_cards(i) + '\n          ', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates completed.")
