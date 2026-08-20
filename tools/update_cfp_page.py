import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

path = "call-for-papers.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Pagehead description
content = re.sub(
    r'<p>Original, unpublished research is invited across.*?</p>',
    '<p>Original, unpublished research is invited across seven technical tracks. Full papers of 8–10 pages are due 31 January 2027.</p>',
    content
)

# Deadline block
deadline_block = """    <div class="deadline" style="margin-bottom:0">
      <div>
        <span class="deadline__label">Full paper submission deadline</span>
        <span class="deadline__date">31 January 2027</span>
        <span class="deadline__note">23:59 Anywhere on Earth &middot; 8&ndash;10 pages, A4, Springer template</span>
        <span class="deadline__left" data-deadline="2027-01-31"></span>
      </div>
      <div class="btn-row" style="margin-top:0">
        <a class="btn btn--accent" href="https://cmt3.research.microsoft.com/ICICSC2027/Submission/Index" target="_blank" rel="noopener noreferrer">Submit via CMT ↗</a>
        <a class="btn btn--light" href="call-for-papers.html#submission">Author guidelines</a>
      </div>
    </div>"""

content = re.sub(r'<div class="deadline" style="margin-bottom:0">.*?</div>\s*</div>\s*(?=<div class="cmt-ack")', deadline_block + '\n', content, flags=re.DOTALL)

# Invitation text
invitation_text = """      <h2>Invitation to authors</h2>
      <p>ICICSC 2027 invites original, unpublished research that advances the theory, engineering or application of intelligent, connected, and sustainable computing.</p>
      <p>ICICSC 2027 is held at Sharda University, Greater Noida, on 28–29 May 2027, serving researchers, developers, educators and practitioners across AI, data science, cybersecurity, blockchain, IoT, robotics, and cloud systems.</p>
      <p>Submissions are invited across all seven tracks and their seventy topic areas: theoretical contributions, systems and engineering papers, rigorous empirical studies, reproducible benchmarks, substantial surveys and deployment experience reports. Work connecting computing to healthcare, sustainability, smart cities, mobility, manufacturing, education or public policy is particularly encouraged.</p>"""

content = re.sub(r'<h2>Invitation to authors</h2>.*?</div>\s*<aside>', invitation_text + '\n    </div>\n    <aside>', content, flags=re.DOTALL)

# 7 Tracks grid
tracks_grid_cfp = """    <div class="section-head">
      <div>
        <span class="eyebrow">Scope</span>
        <h2>Tracks at a glance</h2>
      </div>
      <a class="arrow-link" href="tracks.html">All 70 topics</a>
    </div>
    <div class="grid grid--3">
      <article class="card trackcard" style="--tc:var(--t1)"><div class="card__body"><p class="trackcard__num">Track 1</p><h3>Artificial Intelligence &amp; Machine Learning</h3><p>Deep Learning, Generative AI &amp; LLMs, Reinforcement Learning, NLP, Explainable AI, Federated Learning, and Multi-Agent Systems.</p><div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Innovation</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 4 – Education</span></div><a class="arrow-link" href="tracks.html#track-1">View topics</a></div></article>
      <article class="card trackcard" style="--tc:var(--t2)"><div class="card__body"><p class="trackcard__num">Track 2</p><h3>Internet of Things &amp; Cyber-Physical Systems</h3><p>IoT Protocols, Industrial IoT (IIoT), Smart Cities, Wearables, Digital Twins, Precision Agriculture, and Smart Healthcare Monitoring.</p><div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Infrastructure</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 11 – Smart Cities</span></div><a class="arrow-link" href="tracks.html#track-2">View topics</a></div></article>
      <article class="card trackcard" style="--tc:var(--t3)"><div class="card__body"><p class="trackcard__num">Track 3</p><h3>Robotics &amp; Intelligent Automation</h3><p>Autonomous Mobile Robots, Human-Robot Interaction, Swarm Robotics, SLAM, RPA, Industry 5.0, Surgical Robotics, and UAV Systems.</p><div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Industry</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 8 – Economic Growth</span></div><a class="arrow-link" href="tracks.html#track-3">View topics</a></div></article>
      <article class="card trackcard" style="--tc:var(--t4)"><div class="card__body"><p class="trackcard__num">Track 4</p><h3>Data Analytics &amp; Big Data</h3><p>Big Data Frameworks, Predictive Analytics, Real-Time Stream Processing, Graph Analytics, Time-Series Forecasting, and ESG Analytics.</p><div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Innovation</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 12 – Responsible Production</span></div><a class="arrow-link" href="tracks.html#track-4">View topics</a></div></article>
      <article class="card trackcard" style="--tc:var(--t5)"><div class="card__body"><p class="trackcard__num">Track 5</p><h3>Blockchain &amp; Distributed Ledger Technologies</h3><p>Consensus Mechanisms, Smart Contracts, DeFi, Supply Chain Traceability, Cross-Chain Bridges, Layer-2 Scalability, and Green Blockchain.</p><div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 16 – Peace &amp; Institutions</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Innovation</span></div><a class="arrow-link" href="tracks.html#track-5">View topics</a></div></article>
      <article class="card trackcard" style="--tc:var(--t6)"><div class="card__body"><p class="trackcard__num">Track 6</p><h3>Cybersecurity &amp; Privacy</h3><p>Network Security, Threat Intelligence, Post-Quantum Cryptography, Zero Trust, Forensics, Privacy-Preserving Computing, and AI Cyber Defense.</p><div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 16 – Digital Trust</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Security</span></div><a class="arrow-link" href="tracks.html#track-6">View topics</a></div></article>
      <article class="card trackcard" style="--tc:var(--t7); grid-column: 1 / -1; max-width: 600px; margin: 0 auto;"><div class="card__body"><p class="trackcard__num">Track 7</p><h3>Computer Vision, Cloud &amp; Distributed Systems</h3><p>Medical Image Diagnostics, Multimodal Vision-Language Models, Serverless FaaS, Microservices, Edge-Cloud Continuum, and Green Cloud Computing.</p><div class="sdg-tags" style="margin-top: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Cloud Systems</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 3 – Healthcare Vision</span></div><a class="arrow-link" href="tracks.html#track-7">View topics</a></div></article>
    </div>"""

content = re.sub(
    r'<div class="section-head">\s*<div>\s*<span class="eyebrow">Scope</span>\s*<h2>Tracks at a glance</h2>.*?</div>\s*</div>\s*</section>',
    tracks_grid_cfp + '\n  </div>\n</section>',
    content,
    flags=re.DOTALL
)

# Aside key facts
content = re.sub(r'<li><span class="kv__k">Deadline</span><span class="kv__v">.*?</span></li>', '<li><span class="kv__k">Deadline</span><span class="kv__v">31 January 2027</span></li>', content)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("call-for-papers.html updated successfully.")
