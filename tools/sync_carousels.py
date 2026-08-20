import os
import re
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# 1. Keynote speakers (6 members)
speakers_cards = [
    ("Australia", "Keith Sherringham", "Strategy Consultant & Director", "ADT-Partners / University of Technology Sydney, Australia", "assets/img/people/keith-sherringham.jpg"),
    ("Taiwan", "Prof. (Dr.) Yu-Chen Hu", "Distinguished Professor", "Tunghai University, Taiwan", "assets/img/people/yu-chen-hu.jpeg"),
    ("USA", "Prof. (Dr.) Rajesh Ranjan", "AI Product Manager & Professor", "Carnegie Mellon University, USA / Newcastle University, UK", "assets/img/people/Rajesh-Ranjan.webp"),
    ("USA", "Dr. Arkadeep Mitra", "Process Engineer", "Intel Corporation, Hillsboro, USA", "assets/img/people/arkadeep-mitra.jpg"),
    ("USA", "Vijayent Kohli", "Principal Cybersecurity Engineer", "Ford Motor Company, USA", "assets/img/people/vijayent-kohli.jpeg"),
    ("USA", "Joyjit Roy", "Independent Researcher", "Independent Researcher, USA", "assets/img/people/joyjit-roy.jpg")
]

# 2. International Advisory Committee (all 29 members from committee.html)
iac_cards = [
    ("Poland", "Dr. Ivanna Dronyuk", "Associate Professor", "Jan Dlugosz University in Czestochowa, Poland", "assets/img/people/ivanna-dronyuk.jpg"),
    ("Turkiye", "Dr. Pinar Demircioglu", "Head of Department", "Aydin Adnan Menderes University, Turkiye", "assets/img/people/pinar-demircioglu.jpg"),
    ("Malaysia", "Dr. Nur Azaliah Abu Bakar", "Associate Professor", "Universiti Teknologi Malaysia, Malaysia", "assets/img/people/nur-azaliah-abu-bakar.jpg"),
    ("Jordan", "Prof. Jafar A. Alzubi", "Vice Dean - Scientific Research & Professor", "Al-Balqa Applied University, Jordan", "assets/img/people/jafar-a-alzubi.jpg"),
    ("Saudi Arabia", "Dr. Mohamed Hammad", "Senior Researcher", "Prince Sultan University, Saudi Arabia", "assets/img/people/mohamed-hammad.jpeg"),
    ("Canada", "Dr. Gautam Srivastava", "Professor", "Brandon University, Canada", "assets/img/people/gautam-srivastava.webp"),
    ("China", "Dr. Cun Ji", "Associate Professor", "Shandong Normal University, China", "assets/img/people/cun-ji.jpg"),
    ("Australia", "Dr. Shanmuga Sundar Dhanabalan", "Deputy Director (Research) & Group Leader", "La Trobe University, Melbourne, Australia", "assets/img/people/shanmuga-dhanabalan.jpg"),
    ("United Kingdom", "Dr. M. Ajmal Azad", "Associate Professor", "Birmingham City University, UK", "assets/img/people/muhannmad-ajmal-azad.jpg"),
    ("USA", "Dr. Naresh Kshetri", "Lecturer", "Rochester Institute of Technology, USA", "assets/img/people/naresh-kshetri.jpg"),
    ("Malaysia", "Prof. (Dr.) Noor Zaman Jhanjhi", "Distinguished Professor", "Sunway University, Malaysia", "assets/img/people/noor-zaman-jhanjhi.jpg"),
    ("Malaysia", "Dr. Ganesh Kumar", "Lecturer & Post-graduate Coordinator", "Universiti Teknologi PETRONAS, Malaysia", "assets/img/people/Ganesh-Kumar.webp"),
    ("Iraq", "Dr. Alaa Abdulhady Jaber", "Professor", "University of Technology, Iraq", "assets/img/people/alaa-abdulhady-jaber.jpg"),
    ("Nigeria", "Oloruntoyin Sefiu Taiwo", "Lecturer", "Federal Polytechnic Ayede, Nigeria", "assets/img/people/oloruntoyin-sefiu-taiwo.jpg"),
    ("Brazil / UAE", "Prof. Joel J. P. C. Rodrigues", "Professor", "Ajman University, UAE / UFPI, Brazil", "assets/img/people/joel-rodrigues.jpg"),
    ("United Kingdom", "Prof. Ali Kashif Bashir", "Professor of Networks and Cybersecurity", "Manchester Metropolitan University, UK", "assets/img/people/ali-kashif-bashir.jpg"),
    ("Morocco", "Meriem Mandar", "Researcher", "HASSAN II University, Casablanca, Morocco", "assets/img/people/meriem-mandar.jpg"),
    ("United Kingdom", "Dr. Surbhi Khan", "Senior Lecturer (Associate Professor)", "University of Salford, UK", "assets/img/people/surbhi-khan.jpg"),
    ("Kazakhstan", "Dr. Hari Mohan Rai", "Assistant Professor", "School of Computing & AI, Astana, Kazakhstan", "assets/img/people/Hari-Rai.webp"),
    ("India", "Dr. Avijit Kumar Chaudhuri", "Professor & Head of Department", "Brainware University, India", "assets/img/people/avijit-kumar-chaudhuri.jpg"),
    ("Turkiye", "Prof. (Dr.) Mehmet Recep Bozkurt", "Professor", "Sakarya University, Turkiye", "assets/img/people/mehmet-recep-bozurt.jpeg"),
    ("India", "Dr. Sannasi Chakravarthy S R", "Associate Professor", "Bannari Amman Institute of Technology, India", "assets/img/people/sannasi-chakravarthy-s-r.jpg"),
    ("Iraq", "Dr. Mohammed Edan AlKhazraje", "Head of Department", "Middle Technical University, Iraq", "assets/img/people/mohammed-edan-alkhazraje.jpg"),
    ("India", "Dr. Nishant Doshi", "Associate Professor", "Pandit Deendayal Energy University, India", "assets/img/people/nishant-doshi.jpg"),
    ("Algeria", "Prof. (Dr.) Fateh Mebarek-Oudina", "Full Professor", "Skikda University, Algeria", "assets/img/people/fateh-mebarek-oudina.jpg"),
    ("Italy", "Prof. (Dr.) Yaroslav D. Sergeyev", "Distinguished Professor", "University of Calabria, Italy", "assets/img/people/yaroslav-d-sergeyev.jpg"),
    ("Nigeria", "Dr. Ayodeji Olalekan Salau", "Associate Professor", "Afe Babalola University, Nigeria", "assets/img/people/ayodeji-olalekan-salau.jpg"),
    ("Australia", "Prof. (Dr.) Muhammad Imran", "Associate Professor", "Federation University Australia, Australia", "assets/img/people/muhammad-imran.jpg"),
    ("USA", "Dr. Biren (Brian) Prasad", "Editor-in-Chief & Executive Director", "AAKS, USA", "assets/img/people/biren-brian-prasad.jpg")
]

# 3. National Advisory Committee (5 members)
nac_cards = [
    ("GGSIPU New Delhi", "Prof. Amit Prakash Singh", "Professor", "Guru Gobind Singh Indraprastha University, New Delhi", "assets/img/people/amit-prakash-singh.jpg"),
    ("NSUT New Delhi", "Prof. (Dr.) Nanhay Singh", "Professor & Ex-Head", "Netaji Subhas University of Technology, New Delhi", "assets/img/people/nanhay-singh.jpg"),
    ("Jamia Hamdard", "Dr. Sherin Zafar", "Assistant Professor", "Jamia Hamdard, New Delhi", "assets/img/people/sherin-zafar.jpg"),
    ("IIIT Kalyani", "Dr. SK Hafizul Islam", "Assistant Professor", "Indian Institute of Information Technology Kalyani", "assets/img/people/sk-hafizul-islam.jpg"),
    ("Univ. of Southampton", "Dr. Samiya Khan", "Assistant Professor", "University of Southampton Delhi Campus", "assets/img/people/samiya-khan.jpg?v=2")
]

def make_ticker_html(items, href, ticker_class):
    # create set 1 and duplicate as set 2 (with aria-hidden="true" tabindex="-1")
    set1 = []
    for country, name, desig, affil, img in items:
        card = f"""<a class="story-card" href="{href}">
<div class="story-card__photo-frame">
<img alt="{name}" class="story-card__photo" loading="lazy" src="{img}"/>
</div>
<div class="story-card__info">
<h3 class="story-card__name">{name}</h3><p class="story-card__desig">{desig}</p>
<p class="story-card__affil">{affil}</p>
</div>
</a>"""
        set1.append(card)

    set2 = []
    for country, name, desig, affil, img in items:
        card = f"""<a aria-hidden="true" class="story-card" tabindex="-1" href="{href}">
<div class="story-card__photo-frame">
<img alt="{name}" class="story-card__photo" loading="lazy" src="{img}"/>
</div>
<div class="story-card__info">
<h3 class="story-card__name">{name}</h3><p class="story-card__desig">{desig}</p>
<p class="story-card__affil">{affil}</p>
</div>
</a>"""
        set2.append(card)

    all_cards = "\n".join(set1) + "\n<!-- Set 2 -->\n" + "\n".join(set2)
    return f"""<div class="story-ticker-wrap">
<div class="story-ticker {ticker_class}">
{all_cards}
</div>
</div>"""

speakers_ticker_html = make_ticker_html(speakers_cards, "speakers.html", "story-ticker--speakers")
intl_ticker_html = make_ticker_html(iac_cards, "committee.html", "story-ticker--intl")
nat_ticker_html = make_ticker_html(nac_cards, "committee.html", "story-ticker--nat")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace speakers ticker
content = re.sub(
    r'<section aria-label="Keynote Speakers Showcase"[^>]*>.*?<div class="story-ticker-wrap">.*?</div>\s*</div>\s*</div>\s*</section>',
    f'<section aria-label="Keynote Speakers Showcase" class="committee-showcase committee-showcase--speakers">\n<div class="story-ticker-container">\n{speakers_ticker_html}\n</div>\n</section>',
    content,
    flags=re.DOTALL
)

# Replace international advisory ticker
content = re.sub(
    r'<section aria-label="International Advisory Committee Showcase"[^>]*>.*?<div class="story-ticker-wrap">.*?</div>\s*</div>\s*</div>\s*</section>',
    f'<section aria-label="International Advisory Committee Showcase" class="committee-showcase">\n<div class="story-ticker-container">\n{intl_ticker_html}\n</div>\n</section>',
    content,
    flags=re.DOTALL
)

# Replace national advisory ticker
content = re.sub(
    r'<section aria-label="National Advisory Committee Showcase"[^>]*>.*?<div class="story-ticker-wrap">.*?</div>\s*</div>\s*</div>\s*</section>',
    f'<section aria-label="National Advisory Committee Showcase" class="committee-showcase committee-showcase--national">\n<div class="story-ticker-container">\n{nat_ticker_html}\n</div>\n</section>',
    content,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Carousels in index.html synchronized with exact committee and speaker rosters.")
