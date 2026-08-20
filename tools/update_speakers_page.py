import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

path = "speakers.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the grid in speakers.html
speakers_grid = """<div class="grid grid--4">
<article class="person person--feature" style="border-top-color:var(--t5)">
<img alt="Dr. Marica Amadeo" class="person__photo" height="228" loading="lazy" src="assets/img/people/marica-amadeo.jpg" width="228"/>
<div class="person__body">
<p class="person__role">Italy</p>
<p class="person__name">Dr. Marica Amadeo</p><p class="person__desig">Tenure-Track Assistant Professor</p><p class="person__dept">Department of Engineering (Telecommunications)</p>
<p class="person__affil">University of Reggio Calabria, Italy</p>
<a class="person__link" href="https://scholar.google.com/citations?user=52c4cz0AAAAJ&amp;hl" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t3)">
<img alt="Keith Sherringham" class="person__photo" height="224" loading="lazy" src="assets/img/people/keith-sherringham.jpg" width="224"/>
<div class="person__body">
<p class="person__role">Australia</p>
<p class="person__name">Keith Sherringham</p><p class="person__desig">Strategy Consultant &amp; Director</p><p class="person__dept">School of Computer Science / Strategy Consulting</p>
<p class="person__affil">QDT Partners / University of Technology Sydney, Australia</p>
<a class="person__link" href="https://scholar.google.com/citations?user=9LaCX9MAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t2)">
<img alt="Dr. Ayodeji Olalekan Salau" class="person__photo" height="224" loading="lazy" src="assets/img/people/ayodeji-olalekan-salau.jpg" width="224"/>
<div class="person__body">
<p class="person__role">Nigeria</p>
<p class="person__name">Dr. Ayodeji Olalekan Salau</p><p class="person__desig">Associate Professor &amp; Researcher</p><p class="person__dept">Department of Electrical/Electronics and Computer Engineering</p>
<p class="person__affil">Afe Babalola University, Nigeria</p>
<a class="person__link" href="https://scholar.google.com/citations?user=a0L2b5wAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t1)">
<img alt="Prof. (Dr.) Muhammad Imran" class="person__photo" height="224" loading="lazy" src="assets/img/people/muhammad-imran.jpg" width="224"/>
<div class="person__body">
<p class="person__role">Australia</p>
<p class="person__name">Prof. (Dr.) Muhammad Imran</p><p class="person__desig">Professor</p><p class="person__dept">School of Engineering, Information Technology and Physical Sciences</p>
<p class="person__affil">Federation University Australia, Australia</p>
<a class="person__link" href="https://scholar.google.com/citations?user=7iP_6gMAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t6)">
<img alt="Vijayant Kohli" class="person__photo" height="224" loading="lazy" src="assets/img/people/vijayent-kohli.jpeg" width="224"/>
<div class="person__body">
<p class="person__role">USA</p>
<p class="person__name">Vijayant Kohli</p><p class="person__desig">Principal Cybersecurity Engineer</p><p class="person__dept">Enterprise Cloud &amp; Security Architecture</p>
<p class="person__affil">USA</p>
<a class="person__link" href="https://scholar.google.com/citations?user=sY7V8gIAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t4)">
<img alt="Joyjit Roy" class="person__photo" height="224" loading="lazy" src="assets/img/people/joyjit-roy.jpg" width="224"/>
<div class="person__body">
<p class="person__role">USA</p>
<p class="person__name">Joyjit Roy</p><p class="person__desig">Independent Researcher</p><p class="person__dept">Computational Intelligence &amp; Autonomous Systems</p>
<p class="person__affil">USA</p>
<a class="person__link" href="https://scholar.google.com/citations?user=dFk5xYwAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t4)">
<img alt="Prof. (Dr.) Yu-Chen Hu" class="person__photo" loading="lazy" src="assets/img/people/yu-chen-hu.jpeg"/>
<div class="person__body">
<p class="person__role">Taiwan</p>
<p class="person__name">Prof. (Dr.) Yu-Chen Hu</p><p class="person__desig">Distinguished Professor</p><p class="person__dept">Department of Computer Science</p>
<p class="person__affil">Tunghai University, Taiwan</p>
<a class="person__link" href="https://scholar.google.com.tw/citations?hl=en&amp;user=yIYwXkMAAAAJ" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t1)">
<img alt="Dr. Biren (Brian) Prasad" class="person__photo" height="224" loading="lazy" src="assets/img/people/biren-brian-prasad.jpg" width="224"/>
<div class="person__body">
<p class="person__role">USA</p>
<p class="person__name">Dr. Biren (Brian) Prasad</p><p class="person__desig">Editor-in-Chief &amp; Executive Director</p><p class="person__dept">AI and Knowledge Engineering Solutions (KAS)</p>
<p class="person__affil">California, USA</p>
<a class="person__link" href="https://scholar.google.com/citations?user=51e7iR4AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t3)">
<img alt="Prof. (Dr.) R.M. Chandima Ratnayake" class="person__photo" height="212" loading="lazy" src="assets/img/people/r-m-chandima-ratnayake.jpg" width="212"/>
<div class="person__body">
<p class="person__role">Norway</p>
<p class="person__name">Prof. (Dr.) R.M. Chandima Ratnayake</p><p class="person__desig">Professor</p><p class="person__dept">Department of Mechanical and Structural Engineering and Materials Science</p>
<p class="person__affil">University of Stavanger, Norway</p>
<a class="person__link" href="https://scholar.google.com/citations?user=1B31T84AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t2)">
<img alt="Prof. (Dr.) Rajesh Ranjan" class="person__photo" height="224" loading="lazy" src="assets/img/people/rajesh-ranjan.jpg" width="224"/>
<div class="person__body">
<p class="person__role">USA</p>
<p class="person__name">Prof. (Dr.) Rajesh Ranjan</p><p class="person__desig">AI Product Manager &amp; Professor</p><p class="person__dept">Enterprise AI and Cloud Infrastructure</p>
<p class="person__affil">USA</p>
<a class="person__link" href="https://scholar.google.com/citations?user=tY9q7rUAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t7)">
<img alt="Dr. Giuseppe Ciaburro" class="person__photo" height="224" loading="lazy" src="assets/img/people/giuseppe-ciaburro.jpg" width="224"/>
<div class="person__body">
<p class="person__role">Italy</p>
<p class="person__name">Dr. Giuseppe Ciaburro</p><p class="person__desig">Associate Professor</p><p class="person__dept">Department of Architecture and Industrial Design</p>
<p class="person__affil">Università degli Studi della Campania Luigi Vanvitelli, Italy</p>
<a class="person__link" href="https://scholar.google.com/citations?user=Y7yHj30AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>

<article class="person person--feature" style="border-top-color:var(--t4)">
<img alt="Dr. Arkadeep Mitra" class="person__photo" height="224" loading="lazy" src="assets/img/people/arkadeep-mitra.jpg" width="224"/>
<div class="person__body">
<p class="person__role">USA</p>
<p class="person__name">Dr. Arkadeep Mitra</p><p class="person__desig">Process Engineer</p><p class="person__dept">Logic Technology Development</p>
<p class="person__affil">Intel Corporation, Hillsboro, Oregon, USA</p>
<a class="person__link" href="https://scholar.google.com/citations?user=M_m02C4AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
</div>
</article>
</div>"""

content = re.sub(r'<div class="grid grid--4">.*?</div>\s*</div>\s*</section>', speakers_grid + '\n</div>\n</section>', content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("speakers.html updated successfully with all 12 plenary/keynote speakers.")
