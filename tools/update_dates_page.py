import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

path = "dates.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Update meta
content = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Full author timeline for ICICSC 2027: submission opens 15 November 2026, paper deadline 31 January 2027, notification 15 March 2027, camera-ready 05 May 2027, conference 28–29 May 2027. Add any deadline to your calendar.">',
    content
)
content = re.sub(
    r'<meta property="og:description" content=".*?">',
    '<meta property="og:description" content="Full author timeline for ICICSC 2027: submission opens 15 November 2026, paper deadline 31 January 2027, notification 15 March 2027, camera-ready 05 May 2027, conference 28–29 May 2027. Add any deadline to your calendar.">',
    content
)

dates_list_html = """<ul class="dates" data-dates>
        <li data-date="2026-11-15" data-title="Submission portal opens">
          <span class="dates__label">Submission portal opens</span>
          <span class="dates__meta"><span class="dates__when">15 November 2026</span></span>
        </li>
        <li data-date="2027-01-31" data-title="Full paper submission deadline">
          <span class="dates__label">Full paper submission deadline</span>
          <span class="dates__meta"><span class="dates__when">31 January 2027</span></span>
        </li>
        <li data-date="2027-03-15" data-title="Notification of acceptance (first round revision)">
          <span class="dates__label">Notification of acceptance (first round revision)</span>
          <span class="dates__meta"><span class="dates__when">15 March 2027</span></span>
        </li>
        <li data-date="2027-03-31" data-title="Revised paper submission deadline">
          <span class="dates__label">Revised paper submission deadline</span>
          <span class="dates__meta"><span class="dates__when">31 March 2027</span></span>
        </li>
        <li data-date="2027-04-15" data-title="Final acceptance notification">
          <span class="dates__label">Final acceptance notification</span>
          <span class="dates__meta"><span class="dates__when">15 April 2027</span></span>
        </li>
        <li data-date="2027-04-25" data-title="Early-bird registration deadline">
          <span class="dates__label">Early-bird registration deadline</span>
          <span class="dates__meta"><span class="dates__when">25 April 2027</span></span>
        </li>
        <li data-date="2027-05-05" data-title="Camera-ready paper and copyright form due">
          <span class="dates__label">Camera-ready paper &amp; copyright due</span>
          <span class="dates__meta"><span class="dates__when">05 May 2027</span></span>
        </li>
        <li data-date="2027-05-15" data-title="Registration closes">
          <span class="dates__label">Registration closes</span>
          <span class="dates__meta"><span class="dates__when">15 May 2027</span></span>
        </li>
        <li data-date="2027-05-28" data-date-end="2027-05-29" data-title="Conference dates">
          <span class="dates__label">Conference dates</span>
          <span class="dates__meta"><span class="dates__when">28–29 May 2027</span></span>
        </li>
      </ul>"""

content = re.sub(r'<ul class="dates" data-dates>.*?</ul>', dates_list_html, content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("dates.html successfully updated.")
