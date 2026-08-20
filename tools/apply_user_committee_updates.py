import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# -------------------------------------------------------------
# 1. committee.html updates
# -------------------------------------------------------------

# International Advisory Committee
iac_cards = [
    # The 14 requested:
    ("Poland", "Dr. Ivanna Dronyuk", "Associate Professor", "Department of Mathematics and Informatics", "Jan Dlugosz University in Czestochowa, Poland", "assets/img/people/ivanna-dronyuk.jpg", "https://scholar.google.com/citations?user=AQaGSBIAAAAJ&hl=en"),
    ("Turkiye", "Dr. Pinar Demircioglu", "Head of Department", "Department of Mechanical Engineering", "Aydin Adnan Menderes University, Turkiye", "assets/img/people/pinar-demircioglu.jpg", "https://scholar.google.com/citations?user=G70xB2JfpAAC&hl=en"),
    ("Malaysia", "Dr. Nur Azaliah Abu Bakar", "Associate Professor", "Faculty of Artificial Intelligence", "Universiti Teknologi Malaysia, Malaysia", "assets/img/people/nur-azaliah-abu-bakar.jpg", "https://scholar.google.com/citations?user=kvcfTNgAAAAJ&hl=en&authuser=1"),
    ("Jordan", "Prof. Jafar A. Alzubi", "Vice Dean - Scientific Research & Professor", "Faculty of Engineering", "Al-Balqa Applied University, Jordan", "assets/img/people/jafar-a-alzubi.jpg", "https://scholar.google.com/citations?user=9c3pVfUAAAAJ&hl=en"),
    ("Saudi Arabia", "Dr. Mohamed Hammad", "Senior Researcher", "College of Computer and Information Sciences", "Prince Sultan University, Saudi Arabia", "assets/img/people/mohamed-hammad.jpeg", "https://scholar.google.com/citations?hl=en&user=UrXcpl8AAAAJ"),
    ("Canada", "Dr. Gautam Srivastava", "Professor", "Department of Mathematics & Computer Science", "Brandon University, Canada", "assets/img/people/gautam-srivastava.webp", "https://www.brandonu.ca/"),
    ("China", "Dr. Cun Ji", "Associate Professor", "School of Computer Science and Artificial Intelligence", "Shandong Normal University, China", "assets/img/people/cun-ji.jpg", "https://scholar.google.com.hk/citations?user=dBZqUX0AAAAJ"),
    ("Australia", "Dr. Shanmuga Sundar Dhanabalan", "Deputy Director (Research) & Group Leader", "School of Computing, Engineering and Mathematical Sciences", "La Trobe University, Melbourne, Australia", "assets/img/people/shanmuga-dhanabalan.jpg", "https://scholar.google.com/citations?user=t2k_6_AAAAAJ&hl=en"),
    ("United Kingdom", "Dr. M. Ajmal Azad", "Associate Professor", "Department of Computer Science and Digital Technology", "Birmingham City University, UK", "assets/img/people/muhannmad-ajmal-azad.jpg", "https://scholar.google.com/citations?user=pK6mxEAAAAAJ&hl=en"),
    ("USA", "Dr. Naresh Kshetri", "Lecturer", "Department of Computing and Information Sciences", "Rochester Institute of Technology, USA", "assets/img/people/naresh-kshetri.jpg", "https://scholar.google.com/citations?user=rG0k1O8AAAAJ&hl=en"),
    ("Malaysia", "Prof. (Dr.) Noor Zaman Jhanjhi", "Distinguished Professor", "School of Computer Science", "Sunway University, Malaysia", "assets/img/people/noor-zaman-jhanjhi.jpg", "https://scholar.google.com/citations?user=h3n8J14AAAAJ&hl=en"),
    ("Malaysia", "Dr. Ganesh Kumar", "Lecturer and Post-graduate Coordinator", "Department of Computing", "Universiti Teknologi PETRONAS, Malaysia", "assets/img/people/Ganesh-Kumar.webp", "https://scholar.google.com/citations?user=dXWS62MAAAAJ&hl=en"),
    ("Iraq", "Dr. Alaa Abdulhady Jaber", "Professor", "Mechanical Engineering Department", "University of Technology, Iraq", "assets/img/people/alaa-abdulhady-jaber.jpg", "https://scholar.google.com/citations?user=9_20vK4AAAAJ&hl=en"),
    ("Nigeria", "Oloruntoyin Sefiu Taiwo", "Lecturer", "Department of Electrical and Electronic Engineering", "Federal Polytechnic Ayede, Nigeria", "assets/img/people/oloruntoyin-sefiu-taiwo.jpg", "https://scholar.google.com/citations?user=7Vn389AAAAAJ&hl=en"),
    # Plus word doc scholars:
    ("Brazil / UAE", "Prof. Joel J. P. C. Rodrigues", "Professor", "Artificial Intelligence Research Center (AIRC)", "Ajman University, UAE / Federal University of Piauí (UFPI), Brazil", "assets/img/people/joel-rodrigues.jpg", "https://scholar.google.com/citations?user=97WutEsAAAAJ&hl=en"),
    ("United Kingdom", "Prof. Ali Kashif Bashir", "Professor of Networks and Cybersecurity", "Department of Computing and Mathematics", "Manchester Metropolitan University, UK", "assets/img/people/ali-kashif-bashir.jpg", "https://scholar.google.com/citations?user=znmrVSoAAAAJ&hl=en"),
    ("Morocco", "Meriem Mandar", "Researcher", "Department of Mathematics and Computer Science, Superior Normal School", "HASSAN II University, Casablanca, Morocco", "assets/img/people/meriem-mandar.jpg", "https://orcid.org/0000-0002-6734-0830"),
    ("United Kingdom", "Dr. Surbhi Khan", "Senior Lecturer (Associate Professor)", "School of Science, Engineering and Environment", "University of Salford, UK", "assets/img/people/surbhi-khan.jpg", "https://www.salford.ac.uk/our-staff/surbhi-khan"),
    ("Kazakhstan", "Dr. Hari Mohan Rai", "Assistant Professor", "School of Computing and Artificial Intelligence (SCAI)", "Astana, Kazakhstan", "assets/img/people/Hari-Rai.webp", "https://scholar.google.com/citations?user=GBkDDr0AAAAJ&hl=en"),
    ("India", "Dr. Avijit Kumar Chaudhuri", "Professor & Head of Department", "Department of Computer Science and Engineering", "Brainware University, India", "assets/img/people/avijit-kumar-chaudhuri.jpg", "https://scholar.google.com/citations?user=GBkDDr0AAAAJ&hl=en"),
    ("Turkiye", "Prof. (Dr.) Mehmet Recep Bozkurt", "Professor", "Department of Electrical and Electronics Engineering", "Sakarya University, Turkiye", "assets/img/people/mehmet-recep-bozurt.jpeg", "https://scholar.google.com/citations?user=TCrqBsAAAAAJ&hl=en"),
    ("India", "Dr. Sannasi Chakravarthy S R", "Associate Professor", "Department of Electronics and Communication Engineering", "Bannari Amman Institute of Technology, India", "assets/img/people/sannasi-chakravarthy-s-r.jpg", "https://scholar.google.com/citations?user=NN-PHcIAAAAJ&hl=en"),
    ("Iraq", "Dr. Mohammed Edan AlKhazraje", "Head of Department", "Department of Electronic Technologies", "Middle Technical University, Iraq", "assets/img/people/mohammed-edan-alkhazraje.jpg", "https://scholar.google.com/citations?user=4fEs7-UAAAAJ&hl=ar"),
    ("India", "Dr. Nishant Doshi", "Associate Professor", "Department of Computer Science and Engineering", "Pandit Deendayal Energy University (PDEU), Gandhinagar, India", "assets/img/people/nishant-doshi.jpg", "https://scholar.google.com/citations?user=9KXgKl8AAAAJ&hl=en"),
    ("Algeria", "Prof. (Dr.) Fateh Mebarek-Oudina", "Full Professor", "Department of Physics, Faculty of Sciences", "Skikda University, Algeria", "assets/img/people/fateh-mebarek-oudina.jpg", "https://scholar.google.com/citations?user=UbsZtmQAAAAJ&hl=en&oi=sra"),
    ("Italy", "Prof. (Dr.) Yaroslav D. Sergeyev", "Distinguished Professor & Head of Numerical Calculus Lab", "Department of Computer Science, Modeling, Electronics and Systems Engineering", "University of Calabria, Italy", "assets/img/people/yaroslav-d-sergeyev.jpg", "https://scholar.google.com/citations?user=CJQN7wkAAAAJ&hl=en"),
    ("Nigeria", "Dr. Ayodeji Olalekan Salau", "Associate Professor", "Department of Electrical/Electronics and Computer Engineering", "Afe Babalola University, Nigeria", "assets/img/people/ayodeji-olalekan-salau.jpg", "https://scholar.google.com/citations?user=ayodeji-salau"),
    ("Australia", "Prof. (Dr.) Muhammad Imran", "Associate Professor", "School of Engineering, Information Technology and Physical Sciences", "Federation University Australia, Australia", "assets/img/people/muhammad-imran.jpg", "https://scholar.google.com/citations?user=muhammad-imran"),
    ("USA", "Dr. Biren (Brian) Prasad", "Editor-in-Chief & Executive Director", "AI and Knowledge Engineering", "The Association for the Advancement of Knowledge Solutions (AAKS), USA", "assets/img/people/biren-brian-prasad.jpg", "https://scholar.google.com/citations?user=biren-prasad")
]

iac_grid_items = []
for country, name, desig, dept, affil, img, link in iac_cards:
    item = f"""                <div class="person">
                  <img alt="{name}" class="person__photo" loading="lazy" src="{img}" />
                  <div class="person__body">
                    <p class="person__role">{country}</p>
                    <p class="person__name">{name}</p>
                    <p class="person__desig">{desig}</p>
                    <p class="person__dept">{dept}</p>
                    <p class="person__affil">{affil}</p>
                    <a class="person__link" href="{link}" rel="noopener" target="_blank">Profile ↗</a>
                  </div>
                </div>"""
    iac_grid_items.append(item)

iac_section_html = """            <div data-people-group="" id="advisory">
              <h3 style="margin-top:2.5rem">International Advisory Committee</h3>
              <div class="grid grid--3">
""" + "\n".join(iac_grid_items) + """
              </div>
            </div>"""

# National Advisory Committee (Amit, Nanhay, Sherin, SK Hafizul, Samiya)
nac_cards = [
    ("GGSIPU New Delhi", "Prof. Amit Prakash Singh", "Professor", "University School of Information, Communication and Technology", "Guru Gobind Singh Indraprastha University, New Delhi", "assets/img/people/amit-prakash-singh.jpg", "http://www.ipu.ac.in/usict/AmitPrakashSingh.php"),
    ("NSUT New Delhi", "Prof. (Dr.) Nanhay Singh", "Professor & Ex-Head", "Department of Computer Science and Engineering", "Netaji Subhas University of Technology, New Delhi", "assets/img/people/nanhay-singh.jpg", "http://www.nsit.ac.in/faculty/nanhay-singh/"),
    ("Jamia Hamdard", "Dr. Sherin Zafar", "Assistant Professor", "Department of Computer Science and Engineering", "Jamia Hamdard, New Delhi", "assets/img/people/sherin-zafar.jpg", "http://jamiahamdard.edu/faculty/sherin-zafar/"),
    ("IIIT Kalyani", "Dr. SK Hafizul Islam", "Assistant Professor", "Department of Computer Science and Engineering", "Indian Institute of Information Technology Kalyani", "assets/img/people/sk-hafizul-islam.jpg", "http://iiitkalyani.ac.in/faculty/hafizul/"),
    ("Univ. of Southampton", "Dr. Samiya Khan", "Assistant Professor", "School of Electronics and Computer Science", "University of Southampton Delhi Campus", "assets/img/people/samiya-khan.jpg?v=2", "https://scholar.google.com/citations?user=samiya-khan")
]

nac_grid_items = []
for inst, name, desig, dept, affil, img, link in nac_cards:
    item = f"""                <div class="person">
                  <img alt="{name}" class="person__photo" loading="lazy" src="{img}" />
                  <div class="person__body">
                    <p class="person__role">{inst}</p>
                    <p class="person__name">{name}</p>
                    <p class="person__desig">{desig}</p>
                    <p class="person__dept">{dept}</p>
                    <p class="person__affil">{affil}</p>
                    <a class="person__link" href="{link}" rel="noopener" target="_blank">Profile ↗</a>
                  </div>
                </div>"""
    nac_grid_items.append(item)

nac_section_html = """            <div data-people-group="">
              <h3 style="margin-top:2.5rem">National Advisory Committee</h3>
              <div class="grid grid--3">
""" + "\n".join(nac_grid_items) + """
              </div>
            </div>"""

# Technical Program Committee (Ilham laabab, ekta maini, anuja, kingsy, henry, qasem)
tpc_cards = [
    ("Morocco", "Dr. Ilham Laabab", "PhD Researcher", "Department of Computer Science, Faculty of Sciences", "Sidi Mohamed Ben Abdellah University, Fez, Morocco", "assets/img/people/ilham-laabab.jpg", "https://scholar.google.com/citations?user=ilham-laabab"),
    ("India", "Dr. Ekta Maini", "Associate Professor", "Amity School of Engineering and Technology", "Amity University Hyderabad, India", "assets/img/people/ekta-maini.jpg", "https://scholar.google.com/citations?user=ekta-maini"),
    ("India", "Prof. Anuja Arora", "Professor", "Department of Computer Science and Engineering", "Jaypee Institute of Information Technology, Noida, India", "assets/img/people/anuja-arora.jpg", "https://scholar.google.com/citations?hl=en&user=Uz_ML8cAAAAJ"),
    ("India", "Dr. Kingsy Grace R", "Professor", "Department of Artificial Intelligence and Data Science", "Sri Ramakrishna Engineering College, Coimbatore, India", "assets/img/people/kingsy-grace-r.jpg", "https://scholar.google.com/citations?user=kingsy-grace"),
    ("Nigeria", "Dr. Henry Chima Ukwuoma", "Research Scientist", "Directorate of Research", "National Institute for Policy and Strategic Studies (NIPSS), Nigeria", "assets/img/people/henry-chima-ukwuoma.jpeg", "https://scholar.google.com/citations?user=henry-chima"),
    ("Jordan", "Dr. Qasem Abu Al-Haija", "Head of Department & Associate Professor", "Department of Cyber Security", "Jordan University of Science and Technology, Jordan", "assets/img/people/qasem-abu-alhaija.jpeg", "https://scholar.google.com/citations?user=qasem-abu-alhaija")
]

tpc_grid_items = []
for country, name, desig, dept, affil, img, link in tpc_cards:
    item = f"""                <div class="person">
                  <img alt="{name}" class="person__photo" loading="lazy" src="{img}" />
                  <div class="person__body">
                    <p class="person__role">{country}</p>
                    <p class="person__name">{name}</p>
                    <p class="person__desig">{desig}</p>
                    <p class="person__dept">{dept}</p>
                    <p class="person__affil">{affil}</p>
                    <a class="person__link" href="{link}" rel="noopener" target="_blank">Profile ↗</a>
                  </div>
                </div>"""
    tpc_grid_items.append(item)

tpc_section_html = """            <div data-people-group="">
              <h3 style="margin-top:2.5rem">Technical Programme Committee (TPC)</h3>
              <div class="grid grid--3">
""" + "\n".join(tpc_grid_items) + """
              </div>
            </div>"""

with open("committee.html", "r", encoding="utf-8") as f:
    comm_content = f.read()

# Replace IAC
comm_content = re.sub(
    r'<div data-people-group="" id="advisory">\s*<h3 style="margin-top:2\.5rem">International Advisory Committee</h3>.*?</div>\s*</div>\s*(?=<div data-people-group="">\s*<h3 style="margin-top:2\.5rem">National Advisory Committee</h3>)',
    iac_section_html + '\n            ',
    comm_content,
    flags=re.DOTALL
)

# Replace NAC
comm_content = re.sub(
    r'<div data-people-group="">\s*<h3 style="margin-top:2\.5rem">National Advisory Committee</h3>.*?</div>\s*</div>\s*(?=<div data-people-group="">\s*<h3 style="margin-top:2\.5rem">(?:Publication Chair|Technical Program|Technical Programme|Local Organizing|Organizing))',
    nac_section_html + '\n            ',
    comm_content,
    flags=re.DOTALL
)

# Replace TPC (Technical Program Chairs + Technical Program Committee members)
comm_content = re.sub(
    r'<div data-people-group="">\s*<h3 style="margin-top:2\.5rem">Technical Program Chairs</h3>.*?</div>\s*</div>\s*(?=<div data-people-group="">\s*<h3 style="margin-top:2\.5rem">Local Organizing)',
    tpc_section_html + '\n            ',
    comm_content,
    flags=re.DOTALL
)

with open("committee.html", "w", encoding="utf-8") as f:
    f.write(comm_content)
print("committee.html successfully updated with all exact sections.")
