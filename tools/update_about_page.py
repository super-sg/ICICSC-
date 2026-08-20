import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

path = "about.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Pagehead lede
content = re.sub(
    r'<p>A two-day international forum on next-generation computing.*?</p>',
    '<p>A premier two-day international forum on intelligent, connected and sustainable computing, hosted by Sharda University, Greater Noida, on 28–29 May 2027.</p>',
    content
)

# Overview section
overview_html = """      <span class="eyebrow">Overview</span>
      <h2>About the Conference</h2>
      <p class="lede">The International Conference on Intelligent, Connected and Sustainable Computing (ICICSC 2027) brings together researchers, academicians, and industry practitioners to explore the technologies shaping the next era of computing. As artificial intelligence, connected systems, and sustainable digital infrastructure increasingly converge, the conference provides a focused platform to examine how these advances are transforming industries, governance, and everyday life.</p>
      <p>Spanning seven core tracks — Artificial Intelligence &amp; Machine Learning, Internet of Things &amp; Cyber-Physical Systems, Robotics &amp; Intelligent Automation, Data Analytics &amp; Big Data, Blockchain &amp; Distributed Ledger Technologies, Cybersecurity &amp; Privacy, and Computer Vision, Cloud &amp; Distributed Systems — ICICSC offers a comprehensive view of both foundational research and emerging applications in computer science and engineering. The conference welcomes original, unpublished research that pushes the boundaries of intelligent systems, secure and connected infrastructure, and sustainable computing practices.</p>
      <p>To maintain the highest scholarly standards, all submissions undergo a rigorous double-blind peer review process, with an acceptance rate maintained under 7%. The organizing committee has also built in deliberate diversity safeguards — capping contributions from any single institute or author, and ensuring strong international representation — so the final proceedings reflect a genuinely global cross-section of research rather than a concentration from any one region or institution.</p>
      <p>ICICSC is hosted at Sharda University, Greater Noida, India — a globally connected campus with 43% female students, 1,300+ distinguished faculty, 300+ international academic collaborations, 200+ patents awarded, an 1,800+ bed super-speciality teaching hospital, and a 30,000+ alumni network spanning the world. The conference is supported by an international Advisory Committee spanning 10+ countries and a National Advisory Committee drawing heavily from India's premier IITs, ensuring both global perspective and deep technical rigor in the review process.</p>
      <p>Accepted papers will be published as part of a peer-reviewed proceedings volume, offering authors visibility through established academic indexing channels and connecting their work to a wider international research community.</p>"""

content = re.sub(
    r'<span class="eyebrow">Overview</span>\s*<h2>About ICICSC 2027</h2>.*?</div>\s*<aside>',
    overview_html + '\n    </div>\n    <aside>',
    content,
    flags=re.DOTALL
)

# Sharda at a glance table
glance_html = """        <h3>Sharda University at a glance</h3>
        <ul class="kv">
          <li><span class="kv__k">Location</span><span class="kv__v">Knowledge Park III, Greater Noida, NCR-Delhi</span></li>
          <li><span class="kv__k">Approval</span><span class="kv__v">University Grants Commission (UGC)</span></li>
          <li><span class="kv__k">Accreditation</span><span class="kv__v">NAAC A+ grade</span></li>
          <li><span class="kv__k">Ranking</span><span class="kv__v">87th, University category, NIRF 2023</span></li>
          <li><span class="kv__k">Campus</span><span class="kv__v">63 acres, 43% female students</span></li>
          <li><span class="kv__k">Faculty</span><span class="kv__v">1,300+ distinguished faculty</span></li>
          <li><span class="kv__k">Collaborations</span><span class="kv__v">300+ international partnerships</span></li>
          <li><span class="kv__k">Innovation</span><span class="kv__v">200+ patents awarded</span></li>
          <li><span class="kv__k">On campus</span><span class="kv__v">Sharda Hospital, 1,800+ beds</span></li>
          <li><span class="kv__k">Alumni</span><span class="kv__v">30,000+ alumni worldwide</span></li>
          <li><span class="kv__k">Organising school</span><span class="kv__v">Sharda School of Computing Science &amp; Engineering</span></li>
        </ul>"""

content = re.sub(
    r'<h3>Sharda University at a glance</h3>\s*<ul class="kv">.*?</ul>',
    glance_html,
    content,
    flags=re.DOTALL
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("about.html updated successfully with full docx text and stats.")
