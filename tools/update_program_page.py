import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

path = "program.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Pagehead description
content = re.sub(
    r'<p>A provisional day-by-day schedule for.*?</p>',
    '<p>A provisional day-by-day schedule for 27–29 May 2027, and what presenters need to prepare.</p>',
    content
)

# Note
content = re.sub(
    r'published on <strong>05 February 2027</strong>',
    'published on <strong>15 May 2027</strong>',
    content
)

# Grid cards
cards_html = """    <div class="grid grid--3" style="margin-bottom:3rem">
      <div class="numcard"><span class="numcard__n">27</span><h3>May — Tutorials</h3><p>Hands-on pre-conference workshops and tutorials, included with delegate registration.</p></div>
      <div class="numcard"><span class="numcard__n">28</span><h3>May — Day one</h3><p>Inauguration, keynotes, industry sessions, parallel technical track presentations across all 7 tracks, and the conference dinner.</p></div>
      <div class="numcard"><span class="numcard__n">29</span><h3>May — Day two</h3><p>Keynotes, plenary panel discussions, parallel track sessions, poster presentations, best paper awards, and the valedictory.</p></div>
    </div>"""

content = re.sub(r'<div class="grid grid--3" style="margin-bottom:3rem">.*?</div>', cards_html, content, flags=re.DOTALL)

# Tab buttons
tabs_html = """      <div class="tabs" role="tablist" aria-label="Programme by day">
        <button type="button" role="tab" id="tab-day0" aria-controls="day0" aria-selected="false">Thu 27 May · Tutorials</button>
        <button type="button" role="tab" id="tab-day1" aria-controls="day1" aria-selected="true">Fri 28 May · Day 1</button>
        <button type="button" role="tab" id="tab-day2" aria-controls="day2" aria-selected="false">Sat 29 May · Day 2</button>
      </div>"""

content = re.sub(r'<div class="tabs" role="tablist" aria-label="Programme by day">.*?</div>', tabs_html, content, flags=re.DOTALL)

# Tab Day 0
content = re.sub(
    r'<h3>Thursday 18 February 2027 &mdash; pre-conference tutorials</h3>|<h3>Thursday 18 February 2027 — pre-conference tutorials</h3>',
    '<h3>Thursday 27 May 2027 — pre-conference tutorials</h3>',
    content
)

# Tab Day 1
content = re.sub(
    r'<h3>Friday 19 February 2027 &mdash; conference day one</h3>|<h3>Friday 19 February 2027 — conference day one</h3>',
    '<h3>Friday 28 May 2027 — conference day one</h3>',
    content
)

# Tab Day 2
content = re.sub(
    r'<h3>Saturday 20 February 2027 &mdash; conference day two</h3>|<h3>Saturday 20 February 2027 — conference day two</h3>',
    '<h3>Saturday 29 May 2027 — conference day two</h3>',
    content
)

# Replace 6 tracks mention in session rows if any
content = content.replace("Tracks 1, 2, 3", "Tracks 1, 2, 3, 4")
content = content.replace("Tracks 4, 5, 6", "Tracks 5, 6, 7")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("program.html updated successfully.")
