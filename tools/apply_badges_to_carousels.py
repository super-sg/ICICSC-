import os
import subprocess
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def resolve_file(base_path):
    # check if .png, .svg, .webp exists
    if os.path.exists(base_path):
        return base_path
    base, _ = os.path.splitext(base_path)
    for ext in ['.svg', '.png', '.jpg', '.jpeg', '.webp']:
        cand = base + ext
        if os.path.exists(cand):
            return cand
    return None

# 1. Keynote speakers (6 members)
speakers_data = [
    ("Keith Sherringham", "Australia", "assets/img/flags/au.svg", "Sydney Univ. Tech", "assets/img/logos/institutions/uts.png", "Keith Sherringham", "Director", "ADT-Partners / University of Technology Sydney, Australia", "assets/img/people/keith-sherringham.jpg"),
    ("Prof. Yu-Chen Hu", "Taiwan", "assets/img/flags/tw.svg", "Tunghai University", "assets/img/logos/institutions/tunghai.png", "Prof. (Dr.) Yu-Chen Hu", "Distinguished Professor", "Tunghai University, Taiwan", "assets/img/people/yu-chen-hu.jpeg"),
    ("Prof. Rajesh Ranjan", "USA", "assets/img/flags/us.svg", "Carnegie Mellon", "assets/img/logos/institutions/cmu.png", "Prof. (Dr.) Rajesh Ranjan", "AI Product Manager & Professor", "Carnegie Mellon University, USA / Newcastle University, UK", "assets/img/people/Rajesh-Ranjan.webp"),
    ("Dr. Arkadeep Mitra", "USA", "assets/img/flags/us.svg", "Intel Hillsboro", "assets/img/logos/institutions/intel.svg", "Dr. Arkadeep Mitra", "Process Engineer", "Intel Corporation, Hillsboro, USA", "assets/img/people/arkadeep-mitra.jpg"),
    ("Vijayent Kohli", "USA", "assets/img/flags/us.svg", "Ford Motor Co.", "assets/img/logos/institutions/ford.svg", "Vijayent Kohli", "Principal Cybersecurity Engineer", "Ford Motor Company, USA", "assets/img/people/vijayent-kohli.jpeg"),
    ("Joyjit Roy", "USA", "assets/img/flags/us.svg", "Independent Researcher", "assets/img/logos/institutions/researcher.svg", "Joyjit Roy", "Independent Researcher", "Independent Researcher, USA", "assets/img/people/joyjit-roy.jpg")
]

# 2. IAC members (29 members)
iac_data = [
    ("Dr. Ivanna Dronyuk", "Poland", "assets/img/flags/pl.svg", "Jan Dlugosz Univ.", "assets/img/logos/institutions/jan-dlugosz.png", "Dr. Ivanna Dronyuk", "Associate Professor", "Jan Dlugosz University in Czestochowa, Poland", "assets/img/people/ivanna-dronyuk.jpg"),
    ("Dr. Pinar Demircioglu", "Turkiye", "assets/img/flags/tr.svg", "Adnan Menderes Univ.", "assets/img/logos/institutions/adnan-menderes.png", "Dr. Pinar Demircioglu", "Head of Department", "Aydin Adnan Menderes University, Turkiye", "assets/img/people/pinar-demircioglu.jpg"),
    ("Dr. Nur Azaliah", "Malaysia", "assets/img/flags/my.svg", "UTM Malaysia", "assets/img/logos/institutions/utm.png", "Dr. Nur Azaliah Abu Bakar", "Associate Professor", "Universiti Teknologi Malaysia, Malaysia", "assets/img/people/nur-azaliah-abu-bakar.jpg"),
    ("Prof. Jafar A. Alzubi", "Jordan", "assets/img/flags/jo.svg", "Al-Balqa Applied Univ.", "assets/img/logos/institutions/albalqa.svg", "Prof. Jafar A. Alzubi", "Vice Dean - Scientific Research & Professor", "Al-Balqa Applied University, Jordan", "assets/img/people/jafar-a-alzubi.jpg"),
    ("Dr. Mohamed Hammad", "Saudi Arabia", "assets/img/flags/sa.svg", "Prince Sultan Univ.", "assets/img/logos/institutions/prince-sultan.png", "Dr. Mohamed Hammad", "Senior Researcher", "Prince Sultan University, Saudi Arabia", "assets/img/people/mohamed-hammad.jpeg"),
    ("Dr. Gautam Srivastava", "Canada", "assets/img/flags/ca.svg", "Brandon University", "assets/img/logos/institutions/brandon.png", "Dr. Gautam Srivastava", "Professor", "Brandon University, Canada", "assets/img/people/gautam-srivastava.webp"),
    ("Dr. Cun Ji", "China", "assets/img/flags/cn.svg", "Shandong Normal Univ.", "assets/img/logos/institutions/shandong.png", "Dr. Cun Ji", "Associate Professor", "Shandong Normal University, China", "assets/img/people/cun-ji.jpg"),
    ("Dr. Shanmuga Dhanabalan", "Australia", "assets/img/flags/au.svg", "La Trobe Univ.", "assets/img/logos/institutions/latrobe.png", "Dr. Shanmuga Sundar Dhanabalan", "Deputy Director & Group Leader", "La Trobe University, Melbourne, Australia", "assets/img/people/shanmuga-dhanabalan.jpg"),
    ("Dr. M. Ajmal Azad", "United Kingdom", "assets/img/flags/gb.svg", "Birmingham City Univ.", "assets/img/logos/institutions/birmingham-city.png", "Dr. M. Ajmal Azad", "Associate Professor", "Birmingham City University, UK", "assets/img/people/muhannmad-ajmal-azad.jpg"),
    ("Dr. Naresh Kshetri", "USA", "assets/img/flags/us.svg", "RIT USA", "assets/img/logos/institutions/rit.png", "Dr. Naresh Kshetri", "Lecturer", "Rochester Institute of Technology, USA", "assets/img/people/naresh-kshetri.jpg"),
    ("Prof. Noor Z. Jhanjhi", "Malaysia", "assets/img/flags/my.svg", "Sunway University", "assets/img/logos/institutions/sunway.png", "Prof. (Dr.) Noor Zaman Jhanjhi", "Distinguished Professor", "Sunway University, Malaysia", "assets/img/people/noor-zaman-jhanjhi.jpg"),
    ("Dr. Ganesh Kumar", "Malaysia", "assets/img/flags/my.svg", "UTP Malaysia", "assets/img/logos/institutions/utp.png", "Dr. Ganesh Kumar", "Lecturer & Coordinator", "Universiti Teknologi PETRONAS, Malaysia", "assets/img/people/Ganesh-Kumar.webp"),
    ("Dr. Alaa A. Jaber", "Iraq", "assets/img/flags/iq.svg", "Univ. of Technology", "assets/img/logos/institutions/uot-iraq.png", "Dr. Alaa Abdulhady Jaber", "Professor", "University of Technology, Iraq", "assets/img/people/alaa-abdulhady-jaber.jpg"),
    ("Oloruntoyin Taiwo", "Nigeria", "assets/img/flags/ng.svg", "Fed. Poly. Ayede", "assets/img/logos/institutions/fed-poly.svg", "Oloruntoyin Sefiu Taiwo", "Lecturer", "Federal Polytechnic Ayede, Nigeria", "assets/img/people/oloruntoyin-sefiu-taiwo.jpg"),
    ("Prof. Joel Rodrigues", "Brazil", "assets/img/flags/br.svg", "Ajman Univ. / UFPI", "assets/img/logos/institutions/ajman.svg", "Prof. Joel J. P. C. Rodrigues", "Professor", "Ajman University, UAE / UFPI, Brazil", "assets/img/people/joel-rodrigues.jpg"),
    ("Prof. Ali Kashif Bashir", "United Kingdom", "assets/img/flags/gb.svg", "Manchester Met Univ.", "assets/img/logos/institutions/mmu.svg", "Prof. Ali Kashif Bashir", "Professor", "Manchester Metropolitan University, UK", "assets/img/people/ali-kashif-bashir.jpg"),
    ("Meriem Mandar", "Morocco", "assets/img/flags/ma.svg", "Hassan II Univ.", "assets/img/logos/institutions/hassan.svg", "Meriem Mandar", "Researcher", "HASSAN II University, Casablanca, Morocco", "assets/img/people/meriem-mandar.jpg"),
    ("Dr. Surbhi Khan", "United Kingdom", "assets/img/flags/gb.svg", "Univ. of Salford", "assets/img/logos/institutions/salford.svg", "Dr. Surbhi Khan", "Senior Lecturer", "University of Salford, UK", "assets/img/people/surbhi-khan.jpg"),
    ("Dr. Hari Mohan Rai", "Kazakhstan", "assets/img/flags/kz.svg", "Astana SCAI", "assets/img/logos/institutions/astana.svg", "Dr. Hari Mohan Rai", "Assistant Professor", "School of Computing & AI, Astana, Kazakhstan", "assets/img/people/Hari-Rai.webp"),
    ("Dr. Avijit Chaudhuri", "India", "assets/img/flags/in.svg", "Brainware Univ.", "assets/img/logos/institutions/brainware.svg", "Dr. Avijit Kumar Chaudhuri", "Professor & Head", "Brainware University, India", "assets/img/people/avijit-kumar-chaudhuri.jpg"),
    ("Prof. Mehmet R. Bozkurt", "Turkiye", "assets/img/flags/tr.svg", "Sakarya University", "assets/img/logos/institutions/sakarya.svg", "Prof. (Dr.) Mehmet Recep Bozkurt", "Professor", "Sakarya University, Turkiye", "assets/img/people/mehmet-recep-bozurt.jpeg"),
    ("Dr. Sannasi Chakravarthy", "India", "assets/img/flags/in.svg", "Bannari Amman Inst.", "assets/img/logos/institutions/bits.svg", "Dr. Sannasi Chakravarthy S R", "Associate Professor", "Bannari Amman Institute of Technology, India", "assets/img/people/sannasi-chakravarthy-s-r.jpg"),
    ("Dr. M. Edan AlKhazraje", "Iraq", "assets/img/flags/iq.svg", "Middle Technical Univ.", "assets/img/logos/institutions/middle-tech.svg", "Dr. Mohammed Edan AlKhazraje", "Head of Department", "Middle Technical University, Iraq", "assets/img/people/mohammed-edan-alkhazraje.jpg"),
    ("Dr. Nishant Doshi", "India", "assets/img/flags/in.svg", "PDEU Gandhinagar", "assets/img/logos/institutions/pdeu.svg", "Dr. Nishant Doshi", "Associate Professor", "Pandit Deendayal Energy University, India", "assets/img/people/nishant-doshi.jpg"),
    ("Prof. Fateh Mebarek-Oudina", "Algeria", "assets/img/flags/dz.svg", "Skikda University", "assets/img/logos/institutions/skikda.svg", "Prof. (Dr.) Fateh Mebarek-Oudina", "Full Professor", "Skikda University, Algeria", "assets/img/people/fateh-mebarek-oudina.jpg"),
    ("Prof. Yaroslav Sergeyev", "Italy", "assets/img/flags/it.svg", "Univ. of Calabria", "assets/img/logos/institutions/calabria.svg", "Prof. (Dr.) Yaroslav D. Sergeyev", "Distinguished Professor", "University of Calabria, Italy", "assets/img/people/yaroslav-d-sergeyev.jpg"),
    ("Dr. Ayodeji Salau", "Nigeria", "assets/img/flags/ng.svg", "Afe Babalola Univ.", "assets/img/logos/institutions/abuad.svg", "Dr. Ayodeji Olalekan Salau", "Associate Professor", "Afe Babalola University, Nigeria", "assets/img/people/ayodeji-olalekan-salau.jpg"),
    ("Prof. Muhammad Imran", "Australia", "assets/img/flags/au.svg", "Federation Univ.", "assets/img/logos/institutions/federation.png", "Prof. (Dr.) Muhammad Imran", "Associate Professor", "Federation University Australia, Australia", "assets/img/people/muhammad-imran.jpg"),
    ("Dr. Biren Prasad", "USA", "assets/img/flags/us.svg", "AAKS Solutions", "assets/img/logos/institutions/aaks.svg", "Dr. Biren (Brian) Prasad", "Editor-in-Chief & Director", "AAKS, USA", "assets/img/people/biren-brian-prasad.jpg")
]

# 3. NAC members (5 members)
nac_data = [
    ("Prof. Amit Prakash Singh", "GGSIPU New Delhi", "assets/img/flags/in.svg", "GGSIPU Delhi", "assets/img/logos/institutions/ggsipu.png", "Prof. Amit Prakash Singh", "Professor", "Guru Gobind Singh Indraprastha University, New Delhi", "assets/img/people/amit-prakash-singh.jpg"),
    ("Prof. (Dr.) Nanhay Singh", "NSUT New Delhi", "assets/img/flags/in.svg", "NSUT New Delhi", "assets/img/logos/institutions/nsut.png", "Prof. (Dr.) Nanhay Singh", "Professor & Ex-Head", "Netaji Subhas University of Technology, New Delhi", "assets/img/people/nanhay-singh.jpg"),
    ("Dr. Sherin Zafar", "Jamia Hamdard", "assets/img/flags/in.svg", "Jamia Hamdard", "assets/img/logos/institutions/jamia.png", "Dr. Sherin Zafar", "Assistant Professor", "Jamia Hamdard, New Delhi", "assets/img/people/sherin-zafar.jpg"),
    ("Dr. SK Hafizul Islam", "IIIT Kalyani", "assets/img/flags/in.svg", "IIIT Kalyani", "assets/img/logos/institutions/iiit-kalyani.png", "Dr. SK Hafizul Islam", "Assistant Professor", "Indian Institute of Information Technology Kalyani", "assets/img/people/sk-hafizul-islam.jpg"),
    ("Dr. Samiya Khan", "Univ. of Southampton", "assets/img/flags/in.svg", "Univ. of Southampton", "assets/img/logos/institutions/southampton.png", "Dr. Samiya Khan", "Assistant Professor", "University of Southampton Delhi Campus", "assets/img/people/samiya-khan.jpg?v=2")
]

def make_story_card_soup(data, href, is_dup=False):
    key, country, flag, inst, inst_logo, display_name, desig, affil, img_src = data
    a = soup.new_tag('a', **{'class': 'story-card', 'href': href})
    if is_dup:
        a['aria-hidden'] = 'true'
        a['tabindex'] = '-1'
    
    frame = soup.new_tag('div', **{'class': 'story-card__photo-frame'})
    img = soup.new_tag('img', **{'alt': display_name, 'class': 'story-card__photo', 'loading': 'lazy', 'src': img_src})
    frame.append(img)
    
    actual_flag = resolve_file(flag)
    if actual_flag:
        badge_flag = soup.new_tag('span', **{'class': 'story-card__badge story-card__badge--flag', 'title': country})
        flag_img = soup.new_tag('img', **{'alt': country, 'class': 'flag-icon-img', 'height': '20', 'loading': 'eager', 'src': actual_flag, 'width': '28'})
        badge_flag.append(flag_img)
        frame.append(badge_flag)
        
    actual_logo = resolve_file(inst_logo)
    if actual_logo:
        badge_logo = soup.new_tag('span', **{'class': 'story-card__badge story-card__badge--logo-left', 'title': inst})
        logo_img = soup.new_tag('img', **{'alt': inst, 'class': 'inst-logo-img', 'src': actual_logo})
        badge_logo.append(logo_img)
        frame.append(badge_logo)
        
    a.append(frame)
    
    info = soup.new_tag('div', **{'class': 'story-card__info'})
    h3 = soup.new_tag('h3', **{'class': 'story-card__name'})
    h3.string = display_name
    info.append(h3)
    
    p_desig = soup.new_tag('p', **{'class': 'story-card__desig'})
    p_desig.string = desig
    info.append(p_desig)
    
    p_affil = soup.new_tag('p', **{'class': 'story-card__affil'})
    p_affil.string = affil
    info.append(p_affil)
    
    p_country = soup.new_tag('p', **{'class': 'story-card__country'})
    p_country.string = country
    info.append(p_country)
    
    a.append(info)
    return a

# Update speakers ticker
speakers_ticker = soup.find(class_='story-ticker--speakers')
if speakers_ticker:
    speakers_ticker.clear()
    for item in speakers_data:
        speakers_ticker.append(make_story_card_soup(item, 'speakers.html', is_dup=False))
    for item in speakers_data:
        speakers_ticker.append(make_story_card_soup(item, 'speakers.html', is_dup=True))

# Update IAC ticker
intl_ticker = soup.find(class_='story-ticker--intl')
if intl_ticker:
    intl_ticker.clear()
    for item in iac_data:
        intl_ticker.append(make_story_card_soup(item, 'committee.html', is_dup=False))
    for item in iac_data:
        intl_ticker.append(make_story_card_soup(item, 'committee.html', is_dup=True))

# Update NAC ticker
nat_ticker = soup.find(class_='story-ticker--nat')
if nat_ticker:
    nat_ticker.clear()
    for item in nac_data:
        nat_ticker.append(make_story_card_soup(item, 'committee.html', is_dup=False))
    for item in nac_data:
        nat_ticker.append(make_story_card_soup(item, 'committee.html', is_dup=True))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Badges (flags and institution logos) added to all cards across all three carousels.")
