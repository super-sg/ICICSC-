import os
import glob

html_files = glob.glob('*.html')

submission_content = """      <h2 style="margin-top:3.5rem" id="submission">Author&rsquo;s Guidelines</h2>
      <p>At least one author of an accepted paper must register and present his / her paper in conference. Authors are invited to submit original papers of 8&ndash;10 pages in A4 size using the Springer template, with one accepted paper covered under standard registration.</p>

      <div class="deadline" style="margin:3.5rem 0">
        <div>
          <span class="deadline__label">Before you write a word</span>
          <span class="deadline__date" style="font-size:clamp(1.5rem,3.5vw,2.25rem)">Comprehensive manuscript guidelines</span>
          <span class="deadline__note">Preparation, formatting, structure, abstract &amp; keywords, and reference style &mdash; the complete Springer requirements.</span>
        </div>
        <div class="btn-row" style="margin-top:0">
          <a class="btn btn--accent" href="https://www.springernature.com/gp/authors/publish-a-book/manuscript-guidelines?srsltid=AfmBOopoOnC5v9W2FLb0SwuLBLb7d9DJH1IpWW69y2yvjuXXZISVYNAm" target="_blank" rel="noopener">Springer manuscript guidelines</a>
          <a class="btn btn--light" href="assets/downloads/Springer-Instructions-for-Authors.pdf" target="_blank" rel="noopener">Download PDF</a>
        </div>
      </div>

      <h3 style="margin-top:3rem">Manuscript Preparation</h3>
      <ul class="checklist">
        <li>The manuscript should be prepared in springer format using MS WORD and/or LaTeX template.</li>
        <li>The figures/graphs/plots in the manuscript MUST be of good resolution (600 dpi or more), tables MUST NOT be in pictorial format. Text in figures should not be too small, and preferably of equal size as text of the article.</li>
        <li>Figures, text, or the tables MUST be visible within boundary of the text area of the page and MUST NOT go beyond it.</li>
        <li>Do NOT use any Social/Academic titles (e.g. Mr., Ms., Dr., Prof. etc) preceding the author names. Do NOT mention the position of a person (e.g., research scholar, student, assistant professor, professor etc.) in the affiliation.</li>
        <li>Mention full address, affiliation, and email of ALL authors, specify a corresponding author with the corresponding e-mail ID. [Once an article is accepted, the publisher will send the proofreading of article to this e-mail].</li>
        <li>Articles must be written in spell checked and grammatically correct English.</li>
        <li>All references, figures, and tables should be numbered in sequence starting from 1 and MUST be duly cited / referred within the text.</li>
      </ul>

      <h3 style="margin-top:3rem">Policy on Plagiarism</h3>
      <ul class="checklist">
        <li>Authors are requested to kindly refrain from plagiarism in any form. Authors should submit their original and unpublished research work not under consideration for publication elsewhere.</li>
        <li>Papers found to be plagiarized during any stage of review shall be rejected.</li>
        <li>As per copyright transfer agreement, Authors are deemed to be individually and collectively responsible for the content of manuscripts published by them.</li>
        <li>Hence, it is the responsibility of each author to strive for the highest ethical standards with respect to plagiarism.</li>
      </ul>
"""

for f in html_files:
    if f == 'submission.html':
        continue
    
    with open(f, 'r') as file:
        content = file.read()
    
    # 1. Change "For Authors" to "Call for Papers" in the mainnav
    content = content.replace(
        'For Authors <span class="caret"',
        'Call for Papers <span class="caret"'
    )
    content = content.replace(
        '<span class="eyebrow">For authors</span>',
        '<span class="eyebrow">Call for papers</span>'
    )
    content = content.replace(
        '<h4>For authors</h4>',
        '<h4>Call for papers</h4>'
    )
    
    # 2. Remove the "Paper Submission" link from the submenu
    content = content.replace(
        '            <li><a href="submission.html">Paper Submission</a></li>\n',
        ''
    )
    
    # 3. Remove the "Paper submission" link from the footer
    content = content.replace(
        '        <li><a href="submission.html">Paper submission</a></li>\n',
        ''
    )
    
    # 4. Redirect other links
    content = content.replace('href="submission.html"', 'href="call-for-papers.html#submission"')
    
    # 5. Inject the content specifically into call-for-papers.html
    if f == 'call-for-papers.html':
        # Let's find the place to insert it. We'll insert it right after the table in "Submission categories"
        insert_marker = '      </div>\n    </div>\n\n    <aside>'
        if insert_marker in content:
            content = content.replace(insert_marker, submission_content + '    </div>\n\n    <aside>')
    
    with open(f, 'w') as file:
        file.write(content)

print("Files processed successfully.")
