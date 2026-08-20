import subprocess
import re
from bs4 import BeautifulSoup

# Load original index.html from git HEAD
res = subprocess.run(['git', 'show', 'HEAD:index.html'], capture_output=True, text=True)
soup = BeautifulSoup(res.stdout, 'html.parser')

# 1. Update title & meta tags
title_el = soup.find('title')
if title_el:
    title_el.string = "ICICSC 2027 — International Conference on Intelligent, Connected and Sustainable Computing"

for meta in soup.find_all('meta'):
    if meta.get('content') and 'ICNGCI' in meta['content']:
        meta['content'] = meta['content'].replace('ICNGCI 2027', 'ICICSC 2027').replace('ICNGCI', 'ICICSC').replace('19–20 February 2027', '28–29 May 2027')
    if meta.get('property') and 'og:' in meta['property']:
        if meta.get('content') and 'Next-Generation' in meta['content']:
            meta['content'] = meta['content'].replace('Next-Generation Computing & Innovations', 'Intelligent, Connected and Sustainable Computing').replace('19–20 February 2027', '28–29 May 2027')

for link in soup.find_all('link', rel='canonical'):
    if 'icngci2027' in link.get('href', ''):
        link['href'] = link['href'].replace('icngci2027', 'icicsc2027')

# 2. Update Topbar & Brand
topbar_meta = soup.find(class_='topbar__meta')
if topbar_meta:
    topbar_meta.clear()
    topbar_meta.append("28–29 May 2027")
    dot = soup.new_tag('span', **{'class': 'dot'})
    topbar_meta.append(dot)
    topbar_meta.append("Greater Noida, India")

brand_name = soup.find(class_='brand__name')
if brand_name:
    brand_name.clear()
    brand_name.append("ICICSC")
    span_sub = soup.new_tag('span')
    span_sub.string = "\xa02027"
    brand_name.append(span_sub)

brand_sub = soup.find(class_='brand__sub')
if brand_sub:
    brand_sub.string = "Intelligent, Connected & Sustainable Computing"

# 3. Update Hero
hero_acronym = soup.find(class_='hero__acronym')
if hero_acronym:
    hero_acronym.clear()
    hero_acronym.append("ICICSC")
    em = soup.new_tag('em')
    em.string = "27"
    hero_acronym.append(em)

h1 = soup.find('h1')
if h1:
    h1.string = "International Conference on Intelligent, Connected and Sustainable Computing"

hero_facts = soup.find(class_='hero__facts')
if hero_facts:
    for b in hero_facts.find_all('b'):
        if '19–20 February 2027' in b.get_text():
            b.string = "28–29 May 2027"

countdown = soup.find(class_='countdown')
if countdown:
    countdown['data-countdown'] = "2027-05-28"

# 4. Speakers Carousel (Only the 6 Keynote Speakers)
speakers_data = [
    ("Keith Sherringham", "Australia", "assets/img/flags/au.svg", "Sydney Univ. Tech", "assets/img/logos/institutions/uts.png", "Keith Sherringham", "Director", "ADT-Partners / University of Technology Sydney, Australia", "assets/img/people/keith-sherringham.jpg"),
    ("Prof. Yu-Chen Hu", "Taiwan", "assets/img/flags/tw.svg", "Tunghai University", "assets/img/logos/institutions/tunghai.png", "Prof. (Dr.) Yu-Chen Hu", "Distinguished Professor", "Tunghai University, Taiwan", "assets/img/people/yu-chen-hu.jpeg"),
    ("Prof. Rajesh Ranjan", "USA", "assets/img/flags/us.svg", "Carnegie Mellon", "assets/img/logos/institutions/cmu.png", "Prof. (Dr.) Rajesh Ranjan", "AI Product Manager & Professor", "Carnegie Mellon University, USA / Newcastle University, UK", "assets/img/people/Rajesh-Ranjan.webp"),
    ("Dr. Arkadeep Mitra", "USA", "assets/img/flags/us.svg", "Intel Hillsboro", "assets/img/logos/institutions/intel.svg", "Dr. Arkadeep Mitra", "Process Engineer", "Intel Corporation, Hillsboro, USA", "assets/img/people/arkadeep-mitra.jpg"),
    ("Vijayent Kohli", "USA", "assets/img/flags/us.svg", "Ford Motor Co.", "assets/img/logos/institutions/ford.svg", "Vijayent Kohli", "Principal Cybersecurity Engineer", "Ford Motor Company, USA", "assets/img/people/vijayent-kohli.jpeg"),
    ("Joyjit Roy", "USA", "assets/img/flags/us.svg", "Independent Researcher", "assets/img/logos/institutions/researcher.svg", "Joyjit Roy", "Independent Researcher", "Independent Researcher, USA", "assets/img/people/joyjit-roy.jpg")
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
    
    if flag:
        badge_flag = soup.new_tag('span', **{'class': 'story-card__badge story-card__badge--flag', 'title': country})
        flag_img = soup.new_tag('img', **{'alt': country, 'class': 'flag-icon-img', 'height': '20', 'loading': 'eager', 'src': flag, 'width': '28'})
        badge_flag.append(flag_img)
        frame.append(badge_flag)
        
    if inst_logo:
        badge_logo = soup.new_tag('span', **{'class': 'story-card__badge story-card__badge--logo-left', 'title': inst})
        logo_img = soup.new_tag('img', **{'alt': inst, 'class': 'inst-logo-img', 'src': inst_logo})
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

speakers_ticker = soup.find(class_='story-ticker--speakers')
if speakers_ticker:
    speakers_ticker.clear()
    for item in speakers_data:
        speakers_ticker.append(make_story_card_soup(item, 'speakers.html', is_dup=False))
    for item in speakers_data:
        speakers_ticker.append(make_story_card_soup(item, 'speakers.html', is_dup=True))

# 5. IAC Carousel (Only the 29 members in IAC)
iac_data = [
    ("Dr. Ivanna Dronyuk", "Poland", "assets/img/flags/pl.svg", "Jan Dlugosz Univ.", "assets/img/logos/institutions/jan-dlugosz.png", "Dr. Ivanna Dronyuk", "Associate Professor", "Jan Dlugosz University in Czestochowa, Poland", "assets/img/people/ivanna-dronyuk.jpg"),
    ("Dr. Pinar Demircioglu", "Turkiye", "assets/img/flags/tr.svg", "Adnan Menderes Univ.", "assets/img/logos/institutions/adnan-menderes.png", "Dr. Pinar Demircioglu", "Head of Department", "Aydin Adnan Menderes University, Turkiye", "assets/img/people/pinar-demircioglu.jpg"),
    ("Dr. Nur Azaliah", "Malaysia", "assets/img/flags/my.svg", "UTM Malaysia", "assets/img/logos/institutions/utm.png", "Dr. Nur Azaliah Abu Bakar", "Associate Professor", "Universiti Teknologi Malaysia, Malaysia", "assets/img/people/nur-azaliah-abu-bakar.jpg"),
    ("Prof. Jafar A. Alzubi", "Jordan", "assets/img/flags/jo.svg", "Al-Balqa Applied Univ.", "assets/img/logos/institutions/bau.png", "Prof. Jafar A. Alzubi", "Vice Dean - Scientific Research & Professor", "Al-Balqa Applied University, Jordan", "assets/img/people/jafar-a-alzubi.jpg"),
    ("Dr. Mohamed Hammad", "Saudi Arabia", "assets/img/flags/sa.svg", "Prince Sultan Univ.", "assets/img/logos/institutions/psu.png", "Dr. Mohamed Hammad", "Senior Researcher", "Prince Sultan University, Saudi Arabia", "assets/img/people/mohamed-hammad.jpeg"),
    ("Dr. Gautam Srivastava", "Canada", "assets/img/flags/ca.svg", "Brandon University", "assets/img/logos/institutions/brandon.png", "Dr. Gautam Srivastava", "Professor", "Brandon University, Canada", "assets/img/people/gautam-srivastava.webp"),
    ("Dr. Cun Ji", "China", "assets/img/flags/cn.svg", "Shandong Normal Univ.", "assets/img/logos/institutions/snu.png", "Dr. Cun Ji", "Associate Professor", "Shandong Normal University, China", "assets/img/people/cun-ji.jpg"),
    ("Dr. Shanmuga Dhanabalan", "Australia", "assets/img/flags/au.svg", "La Trobe Univ.", "assets/img/logos/institutions/latrobe.png", "Dr. Shanmuga Sundar Dhanabalan", "Deputy Director & Group Leader", "La Trobe University, Melbourne, Australia", "assets/img/people/shanmuga-dhanabalan.jpg"),
    ("Dr. M. Ajmal Azad", "United Kingdom", "assets/img/flags/gb.svg", "Birmingham City Univ.", "assets/img/logos/institutions/bcu.png", "Dr. M. Ajmal Azad", "Associate Professor", "Birmingham City University, UK", "assets/img/people/muhannmad-ajmal-azad.jpg"),
    ("Dr. Naresh Kshetri", "USA", "assets/img/flags/us.svg", "RIT USA", "assets/img/logos/institutions/rit.svg", "Dr. Naresh Kshetri", "Lecturer", "Rochester Institute of Technology, USA", "assets/img/people/naresh-kshetri.jpg"),
    ("Prof. Noor Z. Jhanjhi", "Malaysia", "assets/img/flags/my.svg", "Sunway University", "assets/img/logos/institutions/sunway.png", "Prof. (Dr.) Noor Zaman Jhanjhi", "Distinguished Professor", "Sunway University, Malaysia", "assets/img/people/noor-zaman-jhanjhi.jpg"),
    ("Dr. Ganesh Kumar", "Malaysia", "assets/img/flags/my.svg", "UTP Malaysia", "assets/img/logos/institutions/utp.png", "Dr. Ganesh Kumar", "Lecturer & Coordinator", "Universiti Teknologi PETRONAS, Malaysia", "assets/img/people/Ganesh-Kumar.webp"),
    ("Dr. Alaa A. Jaber", "Iraq", "assets/img/flags/iq.svg", "Univ. of Technology", "assets/img/logos/institutions/uot.png", "Dr. Alaa Abdulhady Jaber", "Professor", "University of Technology, Iraq", "assets/img/people/alaa-abdulhady-jaber.jpg"),
    ("Oloruntoyin Taiwo", "Nigeria", "assets/img/flags/ng.svg", "Fed. Poly. Ayede", "assets/img/logos/institutions/ayede.png", "Oloruntoyin Sefiu Taiwo", "Lecturer", "Federal Polytechnic Ayede, Nigeria", "assets/img/people/oloruntoyin-sefiu-taiwo.jpg"),
    ("Prof. Joel Rodrigues", "Brazil", "assets/img/flags/br.svg", "Ajman Univ. / UFPI", "assets/img/logos/institutions/ajman.png", "Prof. Joel J. P. C. Rodrigues", "Professor", "Ajman University, UAE / UFPI, Brazil", "assets/img/people/joel-rodrigues.jpg"),
    ("Prof. Ali Kashif Bashir", "United Kingdom", "assets/img/flags/gb.svg", "Manchester Met Univ.", "assets/img/logos/institutions/mmu.png", "Prof. Ali Kashif Bashir", "Professor", "Manchester Metropolitan University, UK", "assets/img/people/ali-kashif-bashir.jpg"),
    ("Meriem Mandar", "Morocco", "assets/img/flags/ma.svg", "Hassan II Univ.", "assets/img/logos/institutions/hassan.png", "Meriem Mandar", "Researcher", "HASSAN II University, Casablanca, Morocco", "assets/img/people/meriem-mandar.jpg"),
    ("Dr. Surbhi Khan", "United Kingdom", "assets/img/flags/gb.svg", "Univ. of Salford", "assets/img/logos/institutions/salford.png", "Dr. Surbhi Khan", "Senior Lecturer", "University of Salford, UK", "assets/img/people/surbhi-khan.jpg"),
    ("Dr. Hari Mohan Rai", "Kazakhstan", "assets/img/flags/kz.svg", "Astana SCAI", "assets/img/logos/institutions/astana.png", "Dr. Hari Mohan Rai", "Assistant Professor", "School of Computing & AI, Astana, Kazakhstan", "assets/img/people/Hari-Rai.webp"),
    ("Dr. Avijit Chaudhuri", "India", "assets/img/flags/in.svg", "Brainware Univ.", "assets/img/logos/institutions/brainware.png", "Dr. Avijit Kumar Chaudhuri", "Professor & Head", "Brainware University, India", "assets/img/people/avijit-kumar-chaudhuri.jpg"),
    ("Prof. Mehmet R. Bozkurt", "Turkiye", "assets/img/flags/tr.svg", "Sakarya University", "assets/img/logos/institutions/sakarya.png", "Prof. (Dr.) Mehmet Recep Bozkurt", "Professor", "Sakarya University, Turkiye", "assets/img/people/mehmet-recep-bozurt.jpeg"),
    ("Dr. Sannasi Chakravarthy", "India", "assets/img/flags/in.svg", "Bannari Amman Inst.", "assets/img/logos/institutions/bits.png", "Dr. Sannasi Chakravarthy S R", "Associate Professor", "Bannari Amman Institute of Technology, India", "assets/img/people/sannasi-chakravarthy-s-r.jpg"),
    ("Dr. M. Edan AlKhazraje", "Iraq", "assets/img/flags/iq.svg", "Middle Technical Univ.", "assets/img/logos/institutions/mtu.png", "Dr. Mohammed Edan AlKhazraje", "Head of Department", "Middle Technical University, Iraq", "assets/img/people/mohammed-edan-alkhazraje.jpg"),
    ("Dr. Nishant Doshi", "India", "assets/img/flags/in.svg", "PDEU Gandhinagar", "assets/img/logos/institutions/pdeu.png", "Dr. Nishant Doshi", "Associate Professor", "Pandit Deendayal Energy University, India", "assets/img/people/nishant-doshi.jpg"),
    ("Prof. Fateh Mebarek-Oudina", "Algeria", "assets/img/flags/dz.svg", "Skikda University", "assets/img/logos/institutions/skikda.png", "Prof. (Dr.) Fateh Mebarek-Oudina", "Full Professor", "Skikda University, Algeria", "assets/img/people/fateh-mebarek-oudina.jpg"),
    ("Prof. Yaroslav Sergeyev", "Italy", "assets/img/flags/it.svg", "Univ. of Calabria", "assets/img/logos/institutions/calabria.png", "Prof. (Dr.) Yaroslav D. Sergeyev", "Distinguished Professor", "University of Calabria, Italy", "assets/img/people/yaroslav-d-sergeyev.jpg"),
    ("Dr. Ayodeji Salau", "Nigeria", "assets/img/flags/ng.svg", "Afe Babalola Univ.", "assets/img/logos/institutions/abuad.png", "Dr. Ayodeji Olalekan Salau", "Associate Professor", "Afe Babalola University, Nigeria", "assets/img/people/ayodeji-olalekan-salau.jpg"),
    ("Prof. Muhammad Imran", "Australia", "assets/img/flags/au.svg", "Federation Univ.", "assets/img/logos/institutions/federation.png", "Prof. (Dr.) Muhammad Imran", "Associate Professor", "Federation University Australia, Australia", "assets/img/people/muhammad-imran.jpg"),
    ("Dr. Biren Prasad", "USA", "assets/img/flags/us.svg", "AAKS Solutions", "assets/img/logos/institutions/aaks.svg", "Dr. Biren (Brian) Prasad", "Editor-in-Chief & Director", "AAKS, USA", "assets/img/people/biren-brian-prasad.jpg")
]

intl_ticker = soup.find(class_='story-ticker--intl')
if intl_ticker:
    intl_ticker.clear()
    for item in iac_data:
        intl_ticker.append(make_story_card_soup(item, 'committee.html', is_dup=False))
    for item in iac_data:
        intl_ticker.append(make_story_card_soup(item, 'committee.html', is_dup=True))

# 6. NAC Carousel (Only the 5 members in NAC)
nac_data = [
    ("Prof. Amit Prakash Singh", "GGSIPU New Delhi", "assets/img/flags/in.svg", "GGSIPU Delhi", "assets/img/logos/institutions/ggsipu.png", "Prof. Amit Prakash Singh", "Professor", "Guru Gobind Singh Indraprastha University, New Delhi", "assets/img/people/amit-prakash-singh.jpg"),
    ("Prof. (Dr.) Nanhay Singh", "NSUT New Delhi", "assets/img/flags/in.svg", "NSUT New Delhi", "assets/img/logos/institutions/nsut.png", "Prof. (Dr.) Nanhay Singh", "Professor & Ex-Head", "Netaji Subhas University of Technology, New Delhi", "assets/img/people/nanhay-singh.jpg"),
    ("Dr. Sherin Zafar", "Jamia Hamdard", "assets/img/flags/in.svg", "Jamia Hamdard", "assets/img/logos/institutions/jamia.png", "Dr. Sherin Zafar", "Assistant Professor", "Jamia Hamdard, New Delhi", "assets/img/people/sherin-zafar.jpg"),
    ("Dr. SK Hafizul Islam", "IIIT Kalyani", "assets/img/flags/in.svg", "IIIT Kalyani", "assets/img/logos/institutions/iiit-kalyani.png", "Dr. SK Hafizul Islam", "Assistant Professor", "Indian Institute of Information Technology Kalyani", "assets/img/people/sk-hafizul-islam.jpg"),
    ("Dr. Samiya Khan", "Univ. of Southampton", "assets/img/flags/in.svg", "Univ. of Southampton", "assets/img/logos/institutions/southampton.png", "Dr. Samiya Khan", "Assistant Professor", "University of Southampton Delhi Campus", "assets/img/people/samiya-khan.jpg?v=2")
]

nat_ticker = soup.find(class_='story-ticker--nat')
if nat_ticker:
    nat_ticker.clear()
    for item in nac_data:
        nat_ticker.append(make_story_card_soup(item, 'committee.html', is_dup=False))
    for item in nac_data:
        nat_ticker.append(make_story_card_soup(item, 'committee.html', is_dup=True))

# 7. Update About Section text
about_sec = soup.find(id='about')
if about_sec:
    for p in about_sec.find_all('p'):
        p_text = p.get_text()
        if 'International Conference on Next-Generation Computing' in p_text:
            p.clear()
            p.append("The ")
            st1 = soup.new_tag('strong')
            st1.string = "International Conference on Intelligent, Connected and Sustainable Computing (ICICSC 2027)"
            p.append(st1)
            p.append(" is a premier two-day international forum hosted by the Sharda School of Computing Science and Engineering, Sharda University, Greater Noida, on ")
            st2 = soup.new_tag('strong')
            st2.string = "28–29 May 2027"
            p.append(st2)
            p.append(" in a hybrid format.")
        elif 'ICNGCI 2027 unites' in p_text:
            p.clear()
            p.append("As computing continues to transform global industries and society, the future is emerging from the powerful convergence of ")
            st = soup.new_tag('strong')
            st.string = "Artificial Intelligence, Data Science, Cybersecurity, Blockchain, IoT, Robotics, and Sustainable Systems"
            p.append(st)
            p.append(". ICICSC 2027 unites leading researchers, academicians, scientists, industry professionals, and innovators from across the globe to present cutting-edge breakthroughs and debate emerging directions.")

# 8. Update Dates in date list
dates_ul = soup.find(class_='dates')
if dates_ul:
    for li in dates_ul.find_all('li'):
        if 'conference' in li.get('data-title', '').lower():
            li['data-date'] = "2027-05-28"
            li['data-end'] = "2027-05-29"
            li['data-title'] = "ICICSC 2027 conference"
            when_span = li.find(class_='dates__when')
            if when_span:
                when_span.string = "28–29 May 2027"

# 9. Update Footer branding & links
footer_brand_name = soup.find(class_='footer__brand')
if footer_brand_name:
    name_el = footer_brand_name.find(class_='brand__name')
    if name_el:
        name_el.string = "ICICSC 2027"
    p_el = footer_brand_name.find('p')
    if p_el and 'International Conference' in p_el.get_text():
        p_el.string = "International Conference on Intelligent, Connected and Sustainable Computing · 28–29 May 2027."
    for a in footer_brand_name.find_all('a'):
        if a.get('aria-label') and 'ICNGCI' in a['aria-label']:
            a['aria-label'] = a['aria-label'].replace('ICNGCI', 'ICICSC')

footer = soup.find('footer')
if footer:
    for a in footer.find_all('a'):
        if a.get('href') and 'ICNGCI' in a['href']:
            a['href'] = a['href'].replace('ICNGCI', 'ICICSC')

footer_bottom = soup.find(class_='footer__bottom')
if footer_bottom:
    for p in footer_bottom.find_all('p'):
        if 'Organised by Sharda University' in p.get_text():
            p.clear()
            p.append("© ")
            sp = soup.new_tag('span', **{'data-year': ''})
            sp.string = "2027"
            p.append(sp)
            p.append(" ICICSC. Organised by Sharda University.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("index.html cleanly updated.")
