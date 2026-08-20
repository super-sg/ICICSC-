import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Countdown timer target
content = re.sub(
    r'data-countdown="2027-02-19"',
    'data-countdown="2027-05-28"',
    content
)

# 2. National Advisory Marquee in index.html (Update to only the 13 members from Image 4)
nat_marquee_cards = """<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. Annavarapu Rao" class="story-card__photo" loading="lazy" src="assets/img/people/annavarapu-rao.png"/>
<span class="story-card__badge story-card__badge--logo" title="IIT Dhanbad"><img alt="IIT Dhanbad" class="inst-logo-img" src="assets/img/logos/institutions/iit-dhanbad.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. Annavarapu Rao</h3><p class="story-card__desig">Associate Professor</p>
<p class="story-card__affil">IIT (ISM) Dhanbad</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. Satyam Agarwal" class="story-card__photo" loading="lazy" src="assets/img/people/satyam-agarwal.jpg"/>
<span class="story-card__badge story-card__badge--logo" title="IIT Ropar"><img alt="IIT Ropar" class="inst-logo-img" src="assets/img/logos/institutions/iit-ropar.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. Satyam Agarwal</h3><p class="story-card__desig">Associate Professor</p>
<p class="story-card__affil">IIT Ropar</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Prof. Amit Prakash Singh" class="story-card__photo" loading="lazy" src="assets/img/people/amit-prakash-singh.jpg"/>
<span class="story-card__badge story-card__badge--logo" title="GGSIPU Delhi"><img alt="GGSIPU Delhi" class="inst-logo-img" src="assets/img/logos/institutions/ggsipu.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Prof. Amit P. Singh</h3><p class="story-card__desig">Professor</p>
<p class="story-card__affil">GGSIPU New Delhi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Prof. Sushama Nagpal" class="story-card__photo" loading="lazy" src="assets/img/people/sushama-nagpal.jpg"/>
<span class="story-card__badge story-card__badge--logo" title="NSUT New Delhi"><img alt="NSUT New Delhi" class="inst-logo-img" src="assets/img/logos/institutions/nsut.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Prof. Sushama Nagpal</h3><p class="story-card__desig">Professor</p>
<p class="story-card__affil">NSUT New Delhi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. Samiya Khan" class="story-card__photo" loading="lazy" src="assets/img/people/samiya-khan.jpg?v=2"/>
<span class="story-card__badge story-card__badge--logo" title="Univ of Southampton"><img alt="Univ of Southampton" class="inst-logo-img" src="assets/img/logos/institutions/southampton.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. Samiya Khan</h3><p class="story-card__desig">Assistant Professor</p>
<p class="story-card__affil">University of Southampton Delhi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. R. K. Srivastava" class="story-card__photo" loading="lazy" src="assets/img/people/r-k-srivastava.jpeg"/>
<span class="story-card__badge story-card__badge--logo" title="IIT BHU"><img alt="IIT BHU" class="inst-logo-img" src="assets/img/logos/institutions/iit-bhu.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. R. K. Srivastava</h3><p class="story-card__desig">Professor (HAG)</p>
<p class="story-card__affil">IIT (BHU) Varanasi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. D. P. Vidyarthi" class="story-card__photo" loading="lazy" src="assets/img/people/d-p-vidyarthi.jpg"/>
<span class="story-card__badge story-card__badge--logo" title="JNU New Delhi"><img alt="JNU New Delhi" class="inst-logo-img" src="assets/img/logos/institutions/jnu.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. D. P. Vidyarthi</h3><p class="story-card__desig">Professor</p>
<p class="story-card__affil">JNU New Delhi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Prof. Anurag Jain" class="story-card__photo" loading="lazy" src="assets/img/people/anurag-jain.jpeg"/>
<span class="story-card__badge story-card__badge--logo" title="GGSIPU Delhi"><img alt="GGSIPU Delhi" class="inst-logo-img" src="assets/img/logos/institutions/ggsipu.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Prof. Anurag Jain</h3><p class="story-card__desig">Professor</p>
<p class="story-card__affil">GGSIPU New Delhi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. Sherin Zafar" class="story-card__photo" loading="lazy" src="assets/img/people/sherin-zafar.jpg"/>
<span class="story-card__badge story-card__badge--logo" title="Jamia Hamdard"><img alt="Jamia Hamdard" class="inst-logo-img" src="assets/img/logos/institutions/jamia.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. Sherin Zafar</h3><p class="story-card__desig">Assistant Professor</p>
<p class="story-card__affil">Jamia Hamdard New Delhi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. Chakradhar Reddy" class="story-card__photo" loading="lazy" src="assets/img/people/chanradhar-reddy-chandupatla.jpeg"/>
<span class="story-card__badge story-card__badge--logo" title="IIT Ropar"><img alt="IIT Ropar" class="inst-logo-img" src="assets/img/logos/institutions/iit-ropar.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. Chakradhar Reddy</h3><p class="story-card__desig">Professor &amp; Head</p>
<p class="story-card__affil">IIT Ropar</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. Satish Chand" class="story-card__photo" loading="lazy" src="assets/img/people/satish-chand.jpg"/>
<span class="story-card__badge story-card__badge--logo" title="JNU New Delhi"><img alt="JNU New Delhi" class="inst-logo-img" src="assets/img/logos/institutions/jnu.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. Satish Chand</h3><p class="story-card__desig">Professor</p>
<p class="story-card__affil">JNU New Delhi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Prof. Nanhay Singh" class="story-card__photo" loading="lazy" src="assets/img/people/nanhay-singh.jpg"/>
<span class="story-card__badge story-card__badge--logo" title="NSUT New Delhi"><img alt="NSUT New Delhi" class="inst-logo-img" src="assets/img/logos/institutions/nsut.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Prof. Nanhay Singh</h3><p class="story-card__desig">Professor &amp; Ex-Head</p>
<p class="story-card__affil">NSUT New Delhi</p>
</div>
</a>
<a class="story-card" href="committee.html">
<div class="story-card__photo-frame">
<img alt="Dr. SK Hafizul Islam" class="story-card__photo" loading="lazy" src="assets/img/people/sk-hafizul-islam.jpg"/>
<span class="story-card__badge story-card__badge--logo" title="IIIT Kalyani"><img alt="IIIT Kalyani" class="inst-logo-img" src="assets/img/logos/institutions/iiit-kalyani.png"/></span>
</div>
<div class="story-card__info">
<h3 class="story-card__name">Dr. SK Hafizul Islam</h3><p class="story-card__desig">Assistant Professor</p>
<p class="story-card__affil">IIIT Kalyani</p>
</div>
</a>"""

content = re.sub(
    r'<div class="story-ticker story-ticker--nat">.*?</div>\s*</div>\s*</div>\s*</section>',
    '<div class="story-ticker story-ticker--nat">\n' + nat_marquee_cards + '\n</div>\n</div>\n</div>\n</section>',
    content,
    flags=re.DOTALL
)

# 3. About section in index.html
about_sec_html = """<section class="section" id="about">
<div class="wrap about-content">
<span class="eyebrow">About the conference</span>
<h2 style="max-width: none;">Shaping the Next Paradigm of Intelligent, Connected, and Sustainable Computing</h2>
<p style="max-width: none;">The <strong>International Conference on Intelligent, Connected and Sustainable Computing (ICICSC 2027)</strong> brings together researchers, academicians, and industry practitioners to explore the technologies shaping the next era of computing. As artificial intelligence, connected systems, and sustainable digital infrastructure increasingly converge, the conference provides a focused platform to examine how these advances are transforming industries, governance, and everyday life.</p>
<p style="max-width: none;">Spanning seven core tracks — Artificial Intelligence &amp; Machine Learning, Internet of Things &amp; Cyber-Physical Systems, Robotics &amp; Intelligent Automation, Data Analytics &amp; Big Data, Blockchain &amp; Distributed Ledger Technologies, Cybersecurity &amp; Privacy, and Computer Vision, Cloud &amp; Distributed Systems — ICICSC offers a comprehensive view of both foundational research and emerging applications. All submissions undergo a rigorous double-blind peer review process, with an acceptance rate maintained under 7% and deliberate institutional diversity safeguards.</p>
<p style="max-width: none;">Hosted at Sharda University, Greater Noida, India (43% female students, 1,300+ distinguished faculty, 300+ international academic collaborations, 200+ patents awarded, and an 1,800+ bed super-speciality teaching hospital), the conference proceedings will be published as part of a peer-reviewed proceedings volume.</p>
<div class="btn-row" style="margin-top: 1.75rem;">
<a class="btn btn--accent" href="about.html">Explore Conference Scope</a>
<a class="btn btn--ghost" href="call-for-papers.html">Call for Papers &amp; Tracks</a>
</div>
</div>
</section>"""

content = re.sub(
    r'<section class="section" id="about">.*?</section>',
    about_sec_html,
    content,
    flags=re.DOTALL
)

# 4. Tracks preview cards in index.html
tracks_cards_html = """<section class="section section--gray">
<div class="wrap">
<div class="section-head">
<div>
<span class="eyebrow">Call for papers</span>
<h2>Seven technical tracks</h2>
</div>
<a class="arrow-link" href="tracks.html">All tracks and 70 topics</a>
</div>
<div class="grid grid--3">
<article class="card trackcard" style="--tc:var(--t1)">
<div class="card__body">
<p class="trackcard__num">Track 1</p>
<h3>Artificial Intelligence &amp; Machine Learning</h3>
<ul>
<li>Deep learning &amp; neural optimization</li>
<li>Generative AI and large language models</li>
<li>Explainable, trustworthy &amp; responsible AI</li>
<li>Multi-agent and agentic AI systems</li>
</ul>
<div class="sdg-tags" style="margin-top: 1rem; margin-bottom: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Innovation</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 4 – Quality Education</span></div>
<a class="arrow-link" href="tracks.html#track-1">10 topics</a>
</div>
</article>
<article class="card trackcard" style="--tc:var(--t2)">
<div class="card__body">
<p class="trackcard__num">Track 2</p>
<h3>Internet of Things &amp; Cyber-Physical Systems</h3>
<ul>
<li>IoT architectures, protocols &amp; standards</li>
<li>Industrial IoT (IIoT) &amp; smart manufacturing</li>
<li>Smart cities &amp; urban infrastructure</li>
<li>Digital twins for cyber-physical systems</li>
</ul>
<div class="sdg-tags" style="margin-top: 1rem; margin-bottom: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Infrastructure</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 11 – Smart Cities</span></div>
<a class="arrow-link" href="tracks.html#track-2">10 topics</a>
</div>
</article>
<article class="card trackcard" style="--tc:var(--t3)">
<div class="card__body">
<p class="trackcard__num">Track 3</p>
<h3>Robotics &amp; Intelligent Automation</h3>
<ul>
<li>Autonomous mobile robots &amp; navigation</li>
<li>Human-robot collaboration &amp; SLAM</li>
<li>Swarm robotics &amp; soft bio-inspired robots</li>
<li>UAV systems &amp; autonomous drones</li>
</ul>
<div class="sdg-tags" style="margin-top: 1rem; margin-bottom: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Industry</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 8 – Economic Growth</span></div>
<a class="arrow-link" href="tracks.html#track-3">10 topics</a>
</div>
</article>
<article class="card trackcard" style="--tc:var(--t4)">
<div class="card__body">
<p class="trackcard__num">Track 4</p>
<h3>Data Analytics &amp; Big Data</h3>
<ul>
<li>Scalable big data &amp; lakehouse architectures</li>
<li>Predictive &amp; prescriptive analytics</li>
<li>Real-time stream data processing</li>
<li>Analytics for sustainability &amp; ESG reporting</li>
</ul>
<div class="sdg-tags" style="margin-top: 1rem; margin-bottom: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Innovation</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 12 – ESG Reporting</span></div>
<a class="arrow-link" href="tracks.html#track-4">10 topics</a>
</div>
</article>
<article class="card trackcard" style="--tc:var(--t5)">
<div class="card__body">
<p class="trackcard__num">Track 5</p>
<h3>Blockchain &amp; Distributed Ledgers</h3>
<ul>
<li>Consensus protocols &amp; smart contracts</li>
<li>Decentralized finance (DeFi) &amp; DApps</li>
<li>Blockchain for supply chain traceability</li>
<li>Scalability &amp; layer-2 solutions</li>
</ul>
<div class="sdg-tags" style="margin-top: 1rem; margin-bottom: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 16 – Peace &amp; Institutions</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Innovation</span></div>
<a class="arrow-link" href="tracks.html#track-5">10 topics</a>
</div>
</article>
<article class="card trackcard" style="--tc:var(--t6)">
<div class="card__body">
<p class="trackcard__num">Track 6</p>
<h3>Cybersecurity &amp; Privacy</h3>
<ul>
<li>Network security &amp; zero trust architecture</li>
<li>Post-quantum cryptography</li>
<li>Digital forensics &amp; incident response</li>
<li>AI-driven threat &amp; ransomware mitigation</li>
</ul>
<div class="sdg-tags" style="margin-top: 1rem; margin-bottom: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 16 – Digital Trust</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Resilient Systems</span></div>
<a class="arrow-link" href="tracks.html#track-6">10 topics</a>
</div>
</article>
<article class="card trackcard" style="--tc:var(--t7); grid-column: 1 / -1; max-width: 600px; margin: 0 auto;">
<div class="card__body">
<p class="trackcard__num">Track 7</p>
<h3>Computer Vision, Cloud &amp; Distributed Systems</h3>
<ul>
<li>Medical image diagnostics &amp; segmentation</li>
<li>Multi-modal vision-language models</li>
<li>Serverless, microservices &amp; container orchestration</li>
<li>Edge-cloud continuum &amp; green cloud computing</li>
</ul>
<div class="sdg-tags" style="margin-top: 1rem; margin-bottom: 1rem; display: flex; gap: 0.5rem; flex-wrap: wrap;"><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 9 – Cloud Systems</span><span class="chip" style="font-size: 0.75rem; padding: 0.25rem 0.5rem; background: var(--surface-2); border: 1px solid var(--border);">SDG 3 – Healthcare Vision</span></div>
<a class="arrow-link" href="tracks.html#track-7">10 topics</a>
</div>
</article>
</div>
</div>
</section>"""

content = re.sub(
    r'<section class="section section--gray">\s*<div class="wrap">\s*<div class="section-head">\s*<div>\s*<span class="eyebrow">Call for papers</span>\s*<h2>(?:Six|Seven) technical tracks</h2>.*?</div>\s*</div>\s*</section>',
    tracks_cards_html,
    content,
    flags=re.DOTALL
)

# 5. Dates preview in index.html
dates_sec_html = """<section class="section section--ink" id="dates">
<div class="wrap split">
<div>
<div class="section-head">
<div>
<span class="eyebrow eyebrow--light">Author timeline</span>
<h2>Important dates</h2>
</div>
<a class="arrow-link" href="dates.html">Full timeline</a>
</div>
<ul class="dates" data-dates="">
<li data-date="2026-11-15" data-title="Submission portal opens">
<span class="dates__label">Submission portal opens</span>
<span class="dates__meta"><span class="dates__when">15 November 2026</span></span>
</li>
<li data-date="2027-01-31" data-title="Full paper submission deadline">
<span class="dates__label">Full paper submission deadline</span>
<span class="dates__meta"><span class="dates__when">31 January 2027</span></span>
</li>
<li data-date="2027-03-15" data-title="Notification of acceptance (first round revision)">
<span class="dates__label">Notification of acceptance</span>
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
<li data-date="2027-05-28" data-end="2027-05-29" data-title="ICICSC 2027 conference">
<span class="dates__label">Conference dates</span>
<span class="dates__meta"><span class="dates__when">28–29 May 2027</span></span>
</li>
</ul>
<p class="small" style="margin-top:1rem;color:#9a9a9a">Deadlines close at 23:59 Anywhere on Earth (AoE). Use <strong>+ Calendar</strong> to add any deadline to your own calendar.</p>
</div>"""

content = re.sub(
    r'<section class="section section--ink" id="dates">\s*<div class="wrap split">\s*<div>\s*<div class="section-head">.*?<aside>',
    dates_sec_html + '\n<aside>',
    content,
    flags=re.DOTALL
)

# 6. Registration preview fees table in index.html
fees_sec_html = """<section class="section">
<div class="wrap">
<div>
<span class="eyebrow">Registration</span>
<h2 style="max-width:none">Registration fees</h2>
<p style="max-width:none">One registration covers one accepted paper. At least one author must register and present — on-site or online — for the paper to enter the proceedings.</p>
<div class="table-scroll" style="width:100%">
<table class="data" style="width:100%">
<caption class="visually-hidden">Registration fees</caption>
<thead>
<tr>
<th rowspan="2" scope="col">Category</th>
<th colspan="2" scope="colgroup">India — INR</th>
<th colspan="2" scope="colgroup">Foreign — USD</th>
</tr>
<tr>
<th scope="col">Early bird<br/><span class="small">until 25 Apr 2027</span></th>
<th scope="col">Standard<br/><span class="small">until 15 May 2027</span></th>
<th scope="col">Early bird<br/><span class="small">until 25 Apr 2027</span></th>
<th scope="col">Standard<br/><span class="small">until 15 May 2027</span></th>
</tr>
</thead>
<tbody>
<tr><td><strong>Attendee / listener</strong><br/><span class="small muted">No paper presentation</span></td><td class="num">₹3,125</td><td class="num">₹3,125</td><td class="num">US$65</td><td class="num">US$65</td></tr>
<tr><td><strong>Research scholar / student</strong><br/><span class="small muted">Valid institutional ID required</span></td><td class="num">₹7,500</td><td class="num">₹8,125</td><td class="num">US$100</td><td class="num">US$125</td></tr>
<tr><td><strong>Academician / faculty</strong></td><td class="num">₹8,750</td><td class="num">₹9,375</td><td class="num">US$125</td><td class="num">US$155</td></tr>
<tr><td><strong>Industry / corporate</strong></td><td class="num">₹9,375</td><td class="num">₹10,000</td><td class="num">US$125</td><td class="num">US$155</td></tr>
</tbody>
<tfoot>
<tr><td colspan="5">Taxes as applicable where levied. For complete payment instructions, see the registration page.</td></tr>
</tfoot>
</table>
</div>
<div class="btn-row" style="margin-top:1.5rem">
<a class="btn" href="registration.html">Registration details &amp; payment</a>
<a class="btn btn--ghost" href="registration.html#calculator">Estimate my fee</a>
</div>
</div>
</div>
</section>"""

content = re.sub(
    r'<section class="section">\s*<div class="wrap">\s*<div>\s*<span class="eyebrow">Registration</span>\s*<h2 style="max-width:none">Registration fees</h2>.*?</div>\s*</div>\s*</section>',
    fees_sec_html,
    content,
    flags=re.DOTALL
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated successfully with all hero, marquee, about, 7 tracks, dates, and fee changes.")
