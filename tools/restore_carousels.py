import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# 1. Keynote speakers (6 members)
speakers_cards = [
    ("Keith Sherringham", "Australia", "assets/img/flags/au.svg", "Sydney Univ. Tech", "assets/img/logos/institutions/uts.png", "Keith Sherringham", "Strategy Consultant & Director", "ADT-Partners / University of Technology Sydney, Australia", "assets/img/people/keith-sherringham.jpg"),
    ("Prof. (Dr.) Yu-Chen Hu", "Taiwan", "assets/img/flags/tw.svg", "Tunghai University", "assets/img/logos/institutions/tunghai.png", "Prof. (Dr.) Yu-Chen Hu", "Distinguished Professor", "Tunghai University, Taiwan", "assets/img/people/yu-chen-hu.jpeg"),
    ("Prof. (Dr.) Rajesh Ranjan", "USA", "assets/img/flags/us.svg", "Carnegie Mellon", "assets/img/logos/institutions/cmu.png", "Prof. (Dr.) Rajesh Ranjan", "AI Product Manager & Professor", "Carnegie Mellon University, USA / Newcastle University, UK", "assets/img/people/Rajesh-Ranjan.webp"),
    ("Dr. Arkadeep Mitra", "USA", "assets/img/flags/us.svg", "Intel Hillsboro", "assets/img/logos/institutions/intel.svg", "Dr. Arkadeep Mitra", "Process Engineer", "Intel Corporation, Hillsboro, USA", "assets/img/people/arkadeep-mitra.jpg"),
    ("Vijayent Kohli", "USA", "assets/img/flags/us.svg", "Ford Motor Co.", "assets/img/logos/institutions/ford.svg", "Vijayent Kohli", "Principal Cybersecurity Engineer", "Ford Motor Company, USA", "assets/img/people/vijayent-kohli.jpeg"),
    ("Joyjit Roy", "USA", "assets/img/flags/us.svg", "Independent Researcher", "assets/img/logos/institutions/researcher.svg", "Joyjit Roy", "Independent Researcher", "Independent Researcher, USA", "assets/img/people/joyjit-roy.jpg")
]

# 2. IAC members (29 members)
iac_cards = [
    # Requested 14
    ("Dr. Ivanna Dronyuk", "Poland", "assets/img/flags/pl.svg", "Jan Dlugosz Univ.", "assets/img/logos/institutions/jan-dlugosz.png", "Dr. Ivanna Dronyuk", "Associate Professor", "Jan Dlugosz University in Czestochowa, Poland", "assets/img/people/ivanna-dronyuk.jpg"),
    ("Dr. Pinar Demircioglu", "Turkiye", "assets/img/flags/tr.svg", "Adnan Menderes Univ.", "assets/img/logos/institutions/adnan-menderes.png", "Dr. Pinar Demircioglu", "Head of Department", "Aydin Adnan Menderes University, Turkiye", "assets/img/people/pinar-demircioglu.jpg"),
    ("Dr. Nur Azaliah Abu Bakar", "Malaysia", "assets/img/flags/my.svg", "UTM Malaysia", "assets/img/logos/institutions/utm.png", "Dr. Nur Azaliah Abu Bakar", "Associate Professor", "Universiti Teknologi Malaysia, Malaysia", "assets/img/people/nur-azaliah-abu-bakar.jpg"),
    ("Prof. Jafar A. Alzubi", "Jordan", "assets/img/flags/jo.svg", "Al-Balqa Applied Univ.", "assets/img/logos/institutions/bau.png", "Prof. Jafar A. Alzubi", "Vice Dean - Scientific Research & Professor", "Al-Balqa Applied University, Jordan", "assets/img/people/jafar-a-alzubi.jpg"),
    ("Dr. Mohamed Hammad", "Saudi Arabia", "assets/img/flags/sa.svg", "Prince Sultan Univ.", "assets/img/logos/institutions/psu.png", "Dr. Mohamed Hammad", "Senior Researcher", "Prince Sultan University, Saudi Arabia", "assets/img/people/mohamed-hammad.jpeg"),
    ("Dr. Gautam Srivastava", "Canada", "assets/img/flags/ca.svg", "Brandon University", "assets/img/logos/institutions/brandon.png", "Dr. Gautam Srivastava", "Professor", "Brandon University, Canada", "assets/img/people/gautam-srivastava.webp"),
    ("Dr. Cun Ji", "China", "assets/img/flags/cn.svg", "Shandong Normal Univ.", "assets/img/logos/institutions/snu.png", "Dr. Cun Ji", "Associate Professor", "Shandong Normal University, China", "assets/img/people/cun-ji.jpg"),
    ("Dr. Shanmuga Sundar Dhanabalan", "Australia", "assets/img/flags/au.svg", "La Trobe Univ.", "assets/img/logos/institutions/latrobe.png", "Dr. Shanmuga Sundar Dhanabalan", "Deputy Director & Group Leader", "La Trobe University, Melbourne, Australia", "assets/img/people/shanmuga-dhanabalan.jpg"),
    ("Dr. M. Ajmal Azad", "United Kingdom", "assets/img/flags/gb.svg", "Birmingham City Univ.", "assets/img/logos/institutions/bcu.png", "Dr. M. Ajmal Azad", "Associate Professor", "Birmingham City University, UK", "assets/img/people/muhannmad-ajmal-azad.jpg"),
    ("Dr. Naresh Kshetri", "USA", "assets/img/flags/us.svg", "RIT USA", "assets/img/logos/institutions/rit.svg", "Dr. Naresh Kshetri", "Lecturer", "Rochester Institute of Technology, USA", "assets/img/people/naresh-kshetri.jpg"),
    ("Prof. (Dr.) Noor Zaman Jhanjhi", "Malaysia", "assets/img/flags/my.svg", "Sunway University", "assets/img/logos/institutions/sunway.png", "Prof. (Dr.) Noor Zaman Jhanjhi", "Distinguished Professor", "Sunway University, Malaysia", "assets/img/people/noor-zaman-jhanjhi.jpg"),
    ("Dr. Ganesh Kumar", "Malaysia", "assets/img/flags/my.svg", "UTP Malaysia", "assets/img/logos/institutions/utp.png", "Dr. Ganesh Kumar", "Lecturer & Coordinator", "Universiti Teknologi PETRONAS, Malaysia", "assets/img/people/Ganesh-Kumar.webp"),
    ("Dr. Alaa Abdulhady Jaber", "Iraq", "assets/img/flags/iq.svg", "Univ. of Technology", "assets/img/logos/institutions/uot.png", "Dr. Alaa Abdulhady Jaber", "Professor", "University of Technology, Iraq", "assets/img/people/alaa-abdulhady-jaber.jpg"),
    ("Oloruntoyin Sefiu Taiwo", "Nigeria", "assets/img/flags/ng.svg", "Fed. Poly. Ayede", "assets/img/logos/institutions/ayede.png", "Oloruntoyin Sefiu Taiwo", "Lecturer", "Federal Polytechnic Ayede, Nigeria", "assets/img/people/oloruntoyin-sefiu-taiwo.jpg"),
    # Document scholars
    ("Prof. Joel J. P. C. Rodrigues", "Brazil", "assets/img/flags/br.svg", "Ajman Univ. / UFPI", "assets/img/logos/institutions/ajman.png", "Prof. Joel J. P. C. Rodrigues", "Professor", "Ajman University, UAE / UFPI, Brazil", "assets/img/people/joel-rodrigues.jpg"),
    ("Prof. Ali Kashif Bashir", "United Kingdom", "assets/img/flags/gb.svg", "Manchester Met Univ.", "assets/img/logos/institutions/mmu.png", "Prof. Ali Kashif Bashir", "Professor", "Manchester Metropolitan University, UK", "assets/img/people/ali-kashif-bashir.jpg"),
    ("Meriem Mandar", "Morocco", "assets/img/flags/ma.svg", "Hassan II Univ.", "assets/img/logos/institutions/hassan.png", "Meriem Mandar", "Researcher", "HASSAN II University, Casablanca, Morocco", "assets/img/people/meriem-mandar.jpg"),
    ("Dr. Surbhi Khan", "United Kingdom", "assets/img/flags/gb.svg", "Univ. of Salford", "assets/img/logos/institutions/salford.png", "Dr. Surbhi Khan", "Senior Lecturer", "University of Salford, UK", "assets/img/people/surbhi-khan.jpg"),
    ("Dr. Hari Mohan Rai", "Kazakhstan", "assets/img/flags/kz.svg", "Astana SCAI", "assets/img/logos/institutions/astana.png", "Dr. Hari Mohan Rai", "Assistant Professor", "School of Computing & AI, Astana, Kazakhstan", "assets/img/people/Hari-Rai.webp"),
    ("Dr. Avijit Kumar Chaudhuri", "India", "assets/img/flags/in.svg", "Brainware Univ.", "assets/img/logos/institutions/brainware.png", "Dr. Avijit Kumar Chaudhuri", "Professor & Head", "Brainware University, India", "assets/img/people/avijit-kumar-chaudhuri.jpg"),
    ("Prof. (Dr.) Mehmet Recep Bozkurt", "Turkiye", "assets/img/flags/tr.svg", "Sakarya University", "assets/img/logos/institutions/sakarya.png", "Prof. (Dr.) Mehmet Recep Bozkurt", "Professor", "Sakarya University, Turkiye", "assets/img/people/mehmet-recep-bozurt.jpeg"),
    ("Dr. Sannasi Chakravarthy S R", "India", "assets/img/flags/in.svg", "Bannari Amman Inst.", "assets/img/logos/institutions/bits.png", "Dr. Sannasi Chakravarthy S R", "Associate Professor", "Bannari Amman Institute of Technology, India", "assets/img/people/sannasi-chakravarthy-s-r.jpg"),
    ("Dr. Mohammed Edan AlKhazraje", "Iraq", "assets/img/flags/iq.svg", "Middle Technical Univ.", "assets/img/logos/institutions/mtu.png", "Dr. Mohammed Edan AlKhazraje", "Head of Department", "Middle Technical University, Iraq", "assets/img/people/mohammed-edan-alkhazraje.jpg"),
    ("Dr. Nishant Doshi", "India", "assets/img/flags/in.svg", "PDEU Gandhinagar", "assets/img/logos/institutions/pdeu.png", "Dr. Nishant Doshi", "Associate Professor", "Pandit Deendayal Energy University, India", "assets/img/people/nishant-doshi.jpg"),
    ("Prof. (Dr.) Fateh Mebarek-Oudina", "Algeria", "assets/img/flags/dz.svg", "Skikda University", "assets/img/logos/institutions/skikda.png", "Prof. (Dr.) Fateh Mebarek-Oudina", "Full Professor", "Skikda University, Algeria", "assets/img/people/fateh-mebarek-oudina.jpg"),
    ("Prof. (Dr.) Yaroslav D. Sergeyev", "Italy", "assets/img/flags/it.svg", "Univ. of Calabria", "assets/img/logos/institutions/calabria.png", "Prof. (Dr.) Yaroslav D. Sergeyev", "Distinguished Professor", "University of Calabria, Italy", "assets/img/people/yaroslav-d-sergeyev.jpg"),
    ("Dr. Ayodeji Olalekan Salau", "Nigeria", "assets/img/flags/ng.svg", "Afe Babalola Univ.", "assets/img/logos/institutions/abuad.png", "Dr. Ayodeji Olalekan Salau", "Associate Professor", "Afe Babalola University, Nigeria", "assets/img/people/ayodeji-olalekan-salau.jpg"),
    ("Prof. (Dr.) Muhammad Imran", "Australia", "assets/img/flags/au.svg", "Federation Univ.", "assets/img/logos/institutions/federation.png", "Prof. (Dr.) Muhammad Imran", "Associate Professor", "Federation University Australia, Australia", "assets/img/people/muhammad-imran.jpg"),
    ("Dr. Biren (Brian) Prasad", "USA", "assets/img/flags/us.svg", "AAKS Solutions", "assets/img/logos/institutions/aaks.svg", "Dr. Biren (Brian) Prasad", "Editor-in-Chief & Director", "AAKS, USA", "assets/img/people/biren-brian-prasad.jpg")
]

# 3. NAC members (5 members)
nac_cards = [
    ("Prof. Amit Prakash Singh", "GGSIPU New Delhi", "assets/img/flags/in.svg", "GGSIPU Delhi", "assets/img/logos/institutions/ggsipu.png", "Prof. Amit Prakash Singh", "Professor", "Guru Gobind Singh Indraprastha University, New Delhi", "assets/img/people/amit-prakash-singh.jpg"),
    ("Prof. (Dr.) Nanhay Singh", "NSUT New Delhi", "assets/img/flags/in.svg", "NSUT New Delhi", "assets/img/logos/institutions/nsut.png", "Prof. (Dr.) Nanhay Singh", "Professor & Ex-Head", "Netaji Subhas University of Technology, New Delhi", "assets/img/people/nanhay-singh.jpg"),
    ("Dr. Sherin Zafar", "Jamia Hamdard", "assets/img/flags/in.svg", "Jamia Hamdard", "assets/img/logos/institutions/jamia.png", "Dr. Sherin Zafar", "Assistant Professor", "Jamia Hamdard, New Delhi", "assets/img/people/sherin-zafar.jpg"),
    ("Dr. SK Hafizul Islam", "IIIT Kalyani", "assets/img/flags/in.svg", "IIIT Kalyani", "assets/img/logos/institutions/iiit-kalyani.png", "Dr. SK Hafizul Islam", "Assistant Professor", "Indian Institute of Information Technology Kalyani", "assets/img/people/sk-hafizul-islam.jpg"),
    ("Dr. Samiya Khan", "Univ. of Southampton", "assets/img/flags/in.svg", "Univ. of Southampton", "assets/img/logos/institutions/southampton.png", "Dr. Samiya Khan", "Assistant Professor", "University of Southampton Delhi Campus", "assets/img/people/samiya-khan.jpg?v=2")
]

def make_card(key, country, flag, inst, inst_logo, display_name, desig, affil, img_src, href, is_dup=False):
    attr = ' aria-hidden="true" tabindex="-1"' if is_dup else ''
    flag_badge = f'<span class="story-card__badge story-card__badge--flag" title="{country}"><img alt="{country}" class="flag-icon-img" height="20" loading="eager" src="{flag}" width="28"/></span>' if os.path.exists(flag) else ''
    logo_badge = f'<span class="story-card__badge story-card__badge--logo-left" title="{inst}"><img alt="{inst}" class="inst-logo-img" src="{inst_logo}"/></span>' if os.path.exists(inst_logo) else ''
    
    return f"""<a class="story-card" href="{href}"{attr}>
<div class="story-card__photo-frame">
<img alt="{display_name}" class="story-card__photo" loading="lazy" src="{img_src}"/>
{flag_badge}
{logo_badge}</div>
<div class="story-card__info">
<h3 class="story-card__name">{display_name}</h3><p class="story-card__desig">{desig}</p>
<p class="story-card__affil">{affil}</p>
<p class="story-card__country">{country}</p></div>
</a>"""

def build_showcase(title, items, href, ticker_class, section_class, label_count_name):
    set1 = [make_card(*item, href=href, is_dup=False) for item in items]
    set2 = [make_card(*item, href=href, is_dup=True) for item in items]
    
    return f"""<section aria-label="{title} Showcase" class="committee-showcase {section_class}">
<div class="wrap">
<div class="carousel-mini-head">
<span class="carousel-mini-head__label">{title}</span>
<div aria-hidden="true" class="carousel-mini-head__line"></div>
</div>
<div class="story-ticker-wrap">
<div class="story-ticker {ticker_class}">
<!-- Set 1 ({len(set1)} {label_count_name}) -->
""" + "\n".join(set1) + f"""
<!-- Set 2 (Duplicate for Infinite Marquee) -->
""" + "\n".join(set2) + """
</div>
</div>
</div>
</section>"""

speakers_sec = build_showcase("Distinguished Keynote Speakers", speakers_cards, "speakers.html", "story-ticker--speakers", "committee-showcase--speakers", "Speakers")
iac_sec = build_showcase("International Advisory Committee", iac_cards, "committee.html", "story-ticker--intl", "", "Members")
nac_sec = build_showcase("National Advisory Committee", nac_cards, "committee.html", "story-ticker--nat", "committee-showcase--national", "Members")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace all 3 showcases cleanly
content = re.sub(
    r'<section aria-label="Keynote Speakers Showcase"[^>]*>.*?</section>',
    speakers_sec,
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<section aria-label="International Advisory Committee Showcase"[^>]*>.*?</section>',
    iac_sec,
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<section aria-label="National Advisory Committee Showcase"[^>]*>.*?</section>',
    nac_sec,
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("index.html carousels successfully rewritten with titles, wrap containers, and exact members.")
