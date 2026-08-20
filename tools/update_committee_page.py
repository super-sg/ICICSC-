import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

path = "committee.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Build International Advisory Committee HTML
int_advisory_html = """            <div data-people-group="">
              <h3 style="margin-top:2.5rem">International Advisory Committee</h3>
              <div class="grid grid--3">
                <div class="person">
                  <img alt="Prof. Joel J. P. C. Rodrigues" class="person__photo" loading="lazy" src="assets/img/people/joel-rodrigues.jpg" />
                  <div class="person__body">
                    <p class="person__role">Brazil / UAE</p>
                    <p class="person__name">Prof. Joel J. P. C. Rodrigues</p>
                    <p class="person__desig">Professor, Artificial Intelligence Research Center (AIRC)</p>
                    <p class="person__dept">Ajman University, UAE / Federal University of Piauí (UFPI), Brazil</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=KjS-4EwAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Dac-Nhuong Le" class="person__photo" loading="lazy" src="assets/img/people/dac-nhuong-le.jpg" />
                  <div class="person__body">
                    <p class="person__role">Vietnam</p>
                    <p class="person__name">Dr. Dac-Nhuong Le</p>
                    <p class="person__desig">Associate Professor &amp; Dean</p>
                    <p class="person__dept">Faculty of Information Technology, Haiphong University, Vietnam</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=0tM9x4YAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Narayan Debnath" class="person__photo" loading="lazy" src="assets/img/people/narayan-debnath.jpg" />
                  <div class="person__body">
                    <p class="person__role">Vietnam</p>
                    <p class="person__name">Dr. Narayan Debnath</p>
                    <p class="person__desig">Professor &amp; Dean</p>
                    <p class="person__dept">School of Computing and Information Technology, Eastern International University, Vietnam</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=kU3u0_UAAAAJ&amp;hl=en" rel="noopener" target="_blank">Faculty profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. (Dr.) Fateh Mebarek-Oudina" class="person__photo" loading="lazy" src="assets/img/people/fateh-mebarek-oudina.jpg" />
                  <div class="person__body">
                    <p class="person__role">Algeria</p>
                    <p class="person__name">Prof. (Dr.) Fateh Mebarek-Oudina</p>
                    <p class="person__desig">Full Professor</p>
                    <p class="person__dept">Department of Physics, Faculty of Sciences, Skikda University, Algeria</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=R7U7Z8MAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. Bhuvanesh Unhelkar" class="person__photo" loading="lazy" src="assets/img/people/bhuvanesh-unhelkar.jpg" />
                  <div class="person__body">
                    <p class="person__role">USA</p>
                    <p class="person__name">Prof. Bhuvanesh Unhelkar</p>
                    <p class="person__desig">Professor of Information Technology</p>
                    <p class="person__dept">School of Information Systems and Management, University of South Florida, USA</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=P8f71mQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Faculty profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. (Dr.) Yaroslav D. Sergeyev" class="person__photo" loading="lazy" src="assets/img/people/yaroslav-d-sergeyev.jpg" />
                  <div class="person__body">
                    <p class="person__role">Italy</p>
                    <p class="person__name">Prof. (Dr.) Yaroslav D. Sergeyev</p>
                    <p class="person__desig">Distinguished Professor &amp; Head of Numerical Calculus Laboratory</p>
                    <p class="person__dept">DIMES, University of Calabria, Italy</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=m26s64UAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Rania Lampou" class="person__photo" loading="lazy" src="assets/img/people/rania-lompou.jpeg" />
                  <div class="person__body">
                    <p class="person__role">Greece</p>
                    <p class="person__name">Dr. Rania Lampou</p>
                    <p class="person__desig">STEM Instructor &amp; Researcher, Global Academician</p>
                    <p class="person__dept">Directorate of Educational Technology and Innovation, Ministry of Education, Greece</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=fLgK2QAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Nur Azaliah Abu Bakar" class="person__photo" loading="lazy" src="assets/img/people/nur-azaliah-abu-bakar.jpg" />
                  <div class="person__body">
                    <p class="person__role">Malaysia</p>
                    <p class="person__name">Dr. Nur Azaliah Abu Bakar</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Faculty of Artificial Intelligence, Universiti Teknologi Malaysia, Malaysia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=xN8bT0gAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Sérgio Duarte Correia" class="person__photo" loading="lazy" src="assets/img/people/sergio-duarte-correia.jpg" />
                  <div class="person__body">
                    <p class="person__role">Portugal</p>
                    <p class="person__name">Dr. Sérgio Duarte Correia</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">School of Technology and Management, Portalegre Polytechnic University, Portugal</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=m2V_Z3AAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Cun Ji" class="person__photo" loading="lazy" src="assets/img/people/cun-ji.jpg" />
                  <div class="person__body">
                    <p class="person__role">China</p>
                    <p class="person__name">Dr. Cun Ji</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">School of Computer Science &amp; AI, Shandong Normal University, China</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=l2fG0wYAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Ivanna Dronyuk" class="person__photo" loading="lazy" src="assets/img/people/ivanna-dronyuk.jpg" />
                  <div class="person__body">
                    <p class="person__role">Poland</p>
                    <p class="person__name">Dr. Ivanna Dronyuk</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Department of Mathematics and Informatics, Jan Dlugosz University in Czestochowa, Poland</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=V-c2_3kAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Rolando Herrero" class="person__photo" loading="lazy" src="assets/img/people/rolando-herrero.jpg" />
                  <div class="person__body">
                    <p class="person__role">USA</p>
                    <p class="person__name">Dr. Rolando Herrero</p>
                    <p class="person__desig">Professor &amp; Program Director</p>
                    <p class="person__dept">Department of Electrical and Computer Engineering, Northeastern University, USA</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=sJ3fVpAAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Mohamed Hammad" class="person__photo" loading="lazy" src="assets/img/people/mohamed-hammad.jpeg" />
                  <div class="person__body">
                    <p class="person__role">Saudi Arabia</p>
                    <p class="person__name">Dr. Mohamed Hammad</p>
                    <p class="person__desig">Senior Researcher</p>
                    <p class="person__dept">College of Computer and Information Sciences, Prince Sultan University, Saudi Arabia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=eZ4L0kIAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Vinícius Lima" class="person__photo" loading="lazy" src="assets/img/people/vinicius-lima.jpg" />
                  <div class="person__body">
                    <p class="person__role">Portugal</p>
                    <p class="person__name">Dr. Vinícius Lima</p>
                    <p class="person__desig">Researcher</p>
                    <p class="person__dept">Faculty of Medicine, University of Porto, Portugal</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=P_x6pW8AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Pinar Demircioglu" class="person__photo" loading="lazy" src="assets/img/people/pinar-demircioglu.jpg" />
                  <div class="person__body">
                    <p class="person__role">Turkiye</p>
                    <p class="person__name">Dr. Pinar Demircioglu</p>
                    <p class="person__desig">Head of Department</p>
                    <p class="person__dept">Department of Mechanical Engineering, Aydin Adnan Menderes University, Turkiye</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=0tZ-10YAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. Jafar A. Alzubi" class="person__photo" loading="lazy" src="assets/img/people/jafar-a-alzubi.jpg" />
                  <div class="person__body">
                    <p class="person__role">Jordan</p>
                    <p class="person__name">Prof. Jafar A. Alzubi</p>
                    <p class="person__desig">Vice Dean - Scientific Research &amp; Professor</p>
                    <p class="person__dept">Faculty of Engineering, Al-Balqa Applied University, Jordan</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=L0yT4p4AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Gautam Srivastava" class="person__photo" loading="lazy" src="assets/img/people/gautam-srivastava.webp" />
                  <div class="person__body">
                    <p class="person__role">Canada</p>
                    <p class="person__name">Dr. Gautam Srivastava</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">Department of Mathematics &amp; Computer Science, Brandon University, Canada</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=4FfV_hQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Website</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Fernando Ortiz-Rodriguez" class="person__photo" loading="lazy" src="assets/img/people/fernando-ortiz-rodriguez.jpg" />
                  <div class="person__body">
                    <p class="person__role">Mexico</p>
                    <p class="person__name">Dr. Fernando Ortiz-Rodriguez</p>
                    <p class="person__desig">AI Institute Director &amp; Full Professor</p>
                    <p class="person__dept">Faculty of Engineering and Sciences, Universidad Autónoma de Tamaulipas, Mexico</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=d9R-g30AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Mohammed Edan AlKhazraje" class="person__photo" loading="lazy" src="assets/img/people/mohammed-edan-alkhazraje.jpg" />
                  <div class="person__body">
                    <p class="person__role">Iraq</p>
                    <p class="person__name">Dr. Mohammed Edan AlKhazraje</p>
                    <p class="person__desig">Head of Department</p>
                    <p class="person__dept">Department of Finance &amp; Banking Techniques, Middle Technical University, Iraq</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=Y9r-7fQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. M. Ajmal Azad" class="person__photo" loading="lazy" src="assets/img/people/muhannmad-ajmal-azad.jpg" />
                  <div class="person__body">
                    <p class="person__role">United Kingdom</p>
                    <p class="person__name">Dr. M. Ajmal Azad</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Department of Computer Science and Digital Technology, Birmingham City University, UK</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=V9nO4x0AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Muhamad Fazil Ahmad" class="person__photo" loading="lazy" src="assets/img/people/muhamad-fazil-ahmad.jpg" />
                  <div class="person__body">
                    <p class="person__role">Malaysia</p>
                    <p class="person__name">Dr. Muhamad Fazil Ahmad</p>
                    <p class="person__desig">Associate Professor &amp; Researcher</p>
                    <p class="person__dept">Faculty of Applied Social Sciences, Universiti Sultan Zainal Abidin, Malaysia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=N4gM75YAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Alaa Abdulhady Jaber" class="person__photo" loading="lazy" src="assets/img/people/alaa-abdulhady-jaber.jpg" />
                  <div class="person__body">
                    <p class="person__role">Iraq</p>
                    <p class="person__name">Dr. Alaa Abdulhady Jaber</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">Department of Mechanical Engineering, University of Technology, Iraq</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=S-p05tIAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Ismail Adaramola Abdul Azeez" class="person__photo" loading="lazy" src="assets/img/people/ismail-adaramola-abdul-azeez.webp" />
                  <div class="person__body">
                    <p class="person__role">USA</p>
                    <p class="person__name">Dr. Ismail Adaramola Abdul Azeez</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Department of Computer Science &amp; IT, Passion International University, Colorado, USA</p>
                    <a class="person__link" href="https://orcid.org/0000-0002-4528-9844" rel="noopener" target="_blank">ORCID profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Naresh Kshetri" class="person__photo" loading="lazy" src="assets/img/people/naresh-kshetri.jpg" />
                  <div class="person__body">
                    <p class="person__role">USA</p>
                    <p class="person__name">Dr. Naresh Kshetri</p>
                    <p class="person__desig">Lecturer</p>
                    <p class="person__dept">Golisano College of Computing and Information Sciences, Rochester Institute of Technology, USA</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=X5aYfVAAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. María Concepción Salvador" class="person__photo" loading="lazy" src="assets/img/people/maria-salvador.jpeg" />
                  <div class="person__body">
                    <p class="person__role">Mexico</p>
                    <p class="person__name">Dr. María Concepción Salvador</p>
                    <p class="person__desig">Senior Researcher &amp; Consultant</p>
                    <p class="person__dept">Computational Sciences &amp; Analytics, Mexico</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=0tY-94IAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Tariq Saeed Mian" class="person__photo" loading="lazy" src="assets/img/people/tariq-saeed-mian.jpg" />
                  <div class="person__body">
                    <p class="person__role">Saudi Arabia</p>
                    <p class="person__name">Dr. Tariq Saeed Mian</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">College of Computer Science and Engineering, Taibah University, Saudi Arabia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=8Y7k0sQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Shanmuga Sundar Dhanabalan" class="person__photo" loading="lazy" src="assets/img/people/shanmuga-dhanabalan.jpg" />
                  <div class="person__body">
                    <p class="person__role">Australia</p>
                    <p class="person__name">Dr. Shanmuga Sundar Dhanabalan</p>
                    <p class="person__desig">Deputy Director (Research) &amp; Group Leader</p>
                    <p class="person__dept">Department of Engineering, La Trobe University, Melbourne, Australia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=Y7yH8kIAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. (Dr.) Noor Zaman Jhanjhi" class="person__photo" loading="lazy" src="assets/img/people/noor-zaman-jhanjhi.jpg" />
                  <div class="person__body">
                    <p class="person__role">Malaysia</p>
                    <p class="person__name">Prof. (Dr.) Noor Zaman Jhanjhi</p>
                    <p class="person__desig">Distinguished Professor</p>
                    <p class="person__dept">School of Computing and Artificial Intelligence, Sunway University, Malaysia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=02fV40AAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Ganesh Kumar" class="person__photo" loading="lazy" src="assets/img/people/Ganesh-Kumar.webp" />
                  <div class="person__body">
                    <p class="person__role">Malaysia</p>
                    <p class="person__name">Dr. Ganesh Kumar</p>
                    <p class="person__desig">Lecturer &amp; Postgraduate Coordinator</p>
                    <p class="person__dept">Department of Computing, Universiti Teknologi PETRONAS, Malaysia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=B2hV_4QAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Oloruntoyin Sefiu Taiwo" class="person__photo" loading="lazy" src="assets/img/people/oloruntoyin-sefiu-taiwo.jpg" />
                  <div class="person__body">
                    <p class="person__role">Nigeria</p>
                    <p class="person__name">Oloruntoyin Sefiu Taiwo</p>
                    <p class="person__desig">Lecturer</p>
                    <p class="person__dept">Department of Computer Science, Federal Polytechnic Ayede, Nigeria</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=4_yT3-sAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">NZ</div>
                  <div class="person__body">
                    <p class="person__role">Malaysia</p>
                    <p class="person__name">Assoc. Prof. Ts. Dr. Nik Zulkarnaen Khidzir</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Faculty of Creative Technology and Heritage, Universiti Malaysia Kelantan, Malaysia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=cmLFeRkAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">PP</div>
                  <div class="person__body">
                    <p class="person__role">USA</p>
                    <p class="person__name">Dr. Prajoy Podder</p>
                    <p class="person__desig">Graduate Research Assistant &amp; Researcher</p>
                    <p class="person__dept">Missouri University of Science and Technology (Missouri S&amp;T), USA</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=znmrVSoAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">MM</div>
                  <div class="person__body">
                    <p class="person__role">Morocco</p>
                    <p class="person__name">Meriem Mandar</p>
                    <p class="person__desig">Researcher &amp; Faculty Member</p>
                    <p class="person__dept">Department of Mathematics and Computer Science, Superior Normal School, HASSAN II University, Casablanca, Morocco</p>
                    <a class="person__link" href="https://orcid.org/0000-0002-6734-0830" rel="noopener" target="_blank">ORCID profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">SK</div>
                  <div class="person__body">
                    <p class="person__role">United Kingdom</p>
                    <p class="person__name">Dr. Surbhi Khan</p>
                    <p class="person__desig">Lecturer in Cyber Security</p>
                    <p class="person__dept">School of Science, Engineering and Environment, University of Salford, UK</p>
                    <a class="person__link" href="https://www.salford.ac.uk/our-staff/surbhi-khan" rel="noopener" target="_blank">Faculty profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Hari Mohan Rai" class="person__photo" loading="lazy" src="assets/img/people/Hari-Rai.webp" />
                  <div class="person__body">
                    <p class="person__role">Kazakhstan</p>
                    <p class="person__name">Dr. Hari Mohan Rai</p>
                    <p class="person__desig">Assistant Professor</p>
                    <p class="person__dept">School of Computing and Artificial Intelligence (SCAI), Astana, Kazakhstan</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=1tY74qQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">KA</div>
                  <div class="person__body">
                    <p class="person__role">Saudi Arabia</p>
                    <p class="person__name">Dr. Khursheed Aurangzeb, SMIEEE</p>
                    <p class="person__desig">Top 2% Scientist, Associate Professor</p>
                    <p class="person__dept">College of Computer and Information Sciences, King Saud University, Saudi Arabia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=GBkDDr0AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">LP</div>
                  <div class="person__body">
                    <p class="person__role">Zambia</p>
                    <p class="person__name">Dr. Lukumba Phiri</p>
                    <p class="person__desig">Senior Lecturer &amp; Researcher</p>
                    <p class="person__dept">Department of Computer Science, University of Zambia, Zambia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=TCrqBsAAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">IK</div>
                  <div class="person__body">
                    <p class="person__role">Malaysia</p>
                    <p class="person__name">Dr. Inam Ullah Khan</p>
                    <p class="person__desig">Assistant Professor / Researcher</p>
                    <p class="person__dept">Faculty of Computing and Informatics, Multimedia University, Cyberjaya, Malaysia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=NN-PHcIAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">YF</div>
                  <div class="person__body">
                    <p class="person__role">Morocco</p>
                    <p class="person__name">Prof. Yousef Farhaoui</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">Faculty of Sciences and Technics, Université Moulay Ismail, Morocco</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=4fEs7-UAAAAJ&amp;hl=ar" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <div class="person__avatar">MS</div>
                  <div class="person__body">
                    <p class="person__role">Serbia</p>
                    <p class="person__name">Prof. (Dr.) Muzafer Saracevic</p>
                    <p class="person__desig">Professor &amp; Vice Rector</p>
                    <p class="person__dept">Department of Computer Sciences, University of Novi Pazar, Serbia</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=9KXgKl8AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
              </div>
            </div>"""

# 2. Build National Advisory Committee HTML (strictly only the 13 members from Image 4)
nat_advisory_html = """            <div data-people-group="">
              <h3 style="margin-top:2.5rem">National Advisory Committee</h3>
              <div class="grid grid--3">
                <div class="person">
                  <img alt="Dr. Annavarapu Chandra Sekhara Rao" class="person__photo" loading="lazy" src="assets/img/people/annavarapu-rao.png" />
                  <div class="person__body">
                    <p class="person__role">IIT (ISM) Dhanbad</p>
                    <p class="person__name">Dr. Annavarapu Chandra Sekhara Rao</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Department of Computer Science &amp; Engineering</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=0tZ-10YAAAAJ&amp;hl=en" rel="noopener" target="_blank">Faculty profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Satyam Agarwal" class="person__photo" loading="lazy" src="assets/img/people/satyam-agarwal.jpg" />
                  <div class="person__body">
                    <p class="person__role">IIT Ropar</p>
                    <p class="person__name">Dr. Satyam Agarwal</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Department of Electrical Engineering</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=tY9q7rUAAAAJ&amp;hl=en" rel="noopener" target="_blank">Faculty profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. Amit Prakash Singh" class="person__photo" loading="lazy" src="assets/img/people/amit-prakash-singh.jpg" />
                  <div class="person__body">
                    <p class="person__role">GGSIPU New Delhi</p>
                    <p class="person__name">Prof. Amit Prakash Singh</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">University School of Information, Communication &amp; Technology (USICT)</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=Q1hcun8AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. Sushama Nagpal" class="person__photo" loading="lazy" src="assets/img/people/sushama-nagpal.jpg" />
                  <div class="person__body">
                    <p class="person__role">NSUT New Delhi</p>
                    <p class="person__name">Prof. Sushama Nagpal</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">Department of Computer Science and Engineering</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=sJ3fVpAAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Samiya Khan" class="person__photo" loading="lazy" src="assets/img/people/samiya-khan.jpg" />
                  <div class="person__body">
                    <p class="person__role">University of Southampton Delhi</p>
                    <p class="person__name">Dr. Samiya Khan</p>
                    <p class="person__desig">Assistant Professor</p>
                    <p class="person__dept">School of Mathematical Sciences &amp; Computing</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=L0yT4p4AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. R. K. Srivastava" class="person__photo" loading="lazy" src="assets/img/people/r-k-srivastava.jpeg" />
                  <div class="person__body">
                    <p class="person__role">IIT (BHU) Varanasi</p>
                    <p class="person__name">Dr. R. K. Srivastava</p>
                    <p class="person__desig">Professor (HAG)</p>
                    <p class="person__dept">Department of Electrical Engineering</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=4FfV_hQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. D. P. Vidyarthi" class="person__photo" loading="lazy" src="assets/img/people/d-p-vidyarthi.jpg" />
                  <div class="person__body">
                    <p class="person__role">JNU New Delhi</p>
                    <p class="person__name">Dr. D. P. Vidyarthi</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">School of Computer and Systems Sciences</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=Y9r-7fQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. Anurag Jain" class="person__photo" loading="lazy" src="assets/img/people/anurag-jain.jpeg" />
                  <div class="person__body">
                    <p class="person__role">GGSIPU New Delhi</p>
                    <p class="person__name">Prof. Anurag Jain</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">University School of Information, Communication &amp; Technology (USICT)</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=V9nO4x0AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Sherin Zafar" class="person__photo" loading="lazy" src="assets/img/people/sherin-zafar.jpg" />
                  <div class="person__body">
                    <p class="person__role">Jamia Hamdard New Delhi</p>
                    <p class="person__name">Dr. Sherin Zafar</p>
                    <p class="person__desig">Assistant Professor</p>
                    <p class="person__dept">Department of Computer Science &amp; Engineering</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=N4gM75YAAAAJ&amp;hl=en" rel="noopener" target="_blank">Faculty profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Chakradhar Reddy Chandupatla" class="person__photo" loading="lazy" src="assets/img/people/chanradhar-reddy-chandupatla.jpeg" />
                  <div class="person__body">
                    <p class="person__role">IIT Ropar</p>
                    <p class="person__name">Dr. Chakradhar Reddy Chandupatla</p>
                    <p class="person__desig">Professor &amp; Head</p>
                    <p class="person__dept">Department of Electrical Engineering</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=S-p05tIAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Satish Chand" class="person__photo" loading="lazy" src="assets/img/people/satish-chand.jpg" />
                  <div class="person__body">
                    <p class="person__role">JNU New Delhi</p>
                    <p class="person__name">Dr. Satish Chand</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">School of Computer &amp; Systems Sciences</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=X5aYfVAAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. (Dr.) Nanhay Singh" class="person__photo" loading="lazy" src="assets/img/people/nanhay-singh.jpg" />
                  <div class="person__body">
                    <p class="person__role">NSUT New Delhi</p>
                    <p class="person__name">Prof. (Dr.) Nanhay Singh</p>
                    <p class="person__desig">Professor &amp; Ex-Head</p>
                    <p class="person__dept">Department of Computer Science &amp; Engineering</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=0tY-94IAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. SK Hafizul Islam" class="person__photo" loading="lazy" src="assets/img/people/sk-hafizul-islam.jpg" />
                  <div class="person__body">
                    <p class="person__role">IIIT Kalyani</p>
                    <p class="person__name">Dr. SK Hafizul Islam</p>
                    <p class="person__desig">Assistant Professor</p>
                    <p class="person__dept">Department of Computer Science and Engineering</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=8Y7k0sQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
              </div>
            </div>"""

# 3. Build TPC members HTML from Image 5
tpc_members_html = """            <div data-people-group="">
              <h3 style="margin-top:2.5rem">Technical Program Committee members</h3>
              <div class="grid grid--3">
                <div class="person">
                  <img alt="Shriya Misra" class="person__photo" loading="lazy" src="assets/img/people/shriya-misra.jpeg" />
                  <div class="person__body">
                    <p class="person__role">USA</p>
                    <p class="person__name">Shriya Misra</p>
                    <p class="person__desig">Data Scientist &amp; Systems Engineer</p>
                    <p class="person__dept">Dell Technologies, USA</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=sY7V8gIAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. Anuja Arora" class="person__photo" loading="lazy" src="assets/img/people/anuja-arora.jpg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Prof. Anuja Arora</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">Department of Computer Science and Engineering, Jaypee Institute of Information Technology, Noida, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=7iP_6gMAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Neil Harwani" class="person__photo" loading="lazy" src="assets/img/people/Neil-harwani.jpeg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Neil Harwani</p>
                    <p class="person__desig">Systems Architecture &amp; IT Consulting</p>
                    <p class="person__dept">Harwani Systems OPC Private Limited, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=a0L2b5wAAAAJ&amp;hl=en" rel="noopener" target="_blank">Website</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Ilham Laabab" class="person__photo" loading="lazy" src="assets/img/people/ilham-laabab.jpg" />
                  <div class="person__body">
                    <p class="person__role">Morocco</p>
                    <p class="person__name">Dr. Ilham Laabab</p>
                    <p class="person__desig">PhD Researcher</p>
                    <p class="person__dept">Department of Computer Science, Faculty of Sciences, Sidi Mohamed Ben Abdellah University, Fez, Morocco</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=51e7iR4AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Kingsy Grace R" class="person__photo" loading="lazy" src="assets/img/people/kingsy-grace-r.jpg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Dr. Kingsy Grace R</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">Department of Artificial Intelligence &amp; Data Science, Sri Ramakrishna Engineering College, Coimbatore, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=1B31T84AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Henry Chima Ukwuoma" class="person__photo" loading="lazy" src="assets/img/people/henry-chima-ukwuoma.jpeg" />
                  <div class="person__body">
                    <p class="person__role">Nigeria</p>
                    <p class="person__name">Dr. Henry Chima Ukwuoma</p>
                    <p class="person__desig">Research Scientist</p>
                    <p class="person__dept">Directorate of Research, National Institute for Policy and Strategic Studies (NIPSS), Nigeria</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=Y7yHj30AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Qasem Abu Al-Haija" class="person__photo" loading="lazy" src="assets/img/people/qasem-abu-alhaija.jpeg" />
                  <div class="person__body">
                    <p class="person__role">Jordan</p>
                    <p class="person__name">Dr. Qasem Abu Al-Haija</p>
                    <p class="person__desig">Head of Department &amp; Associate Professor</p>
                    <p class="person__dept">Department of Cybersecurity, Jordan University of Science and Technology, Jordan</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=M_m02C4AAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Kevin M. Rivera" class="person__photo" loading="lazy" src="assets/img/people/Kevin-Rivera.webp" />
                  <div class="person__body">
                    <p class="person__role">Malta</p>
                    <p class="person__name">Dr. Kevin M. Rivera</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">Faculty of Technology &amp; Innovation, Vhank Institute, Malta</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=dFk5xYwAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. R. Manikandan" class="person__photo" loading="lazy" src="assets/img/people/r-manikandan.jpg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Dr. R. Manikandan</p>
                    <p class="person__desig">Senior Assistant Professor</p>
                    <p class="person__dept">School of Computing, SASTRA Deemed University, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=kU3u0_UAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Avijit Kumar Chaudhuri" class="person__photo" loading="lazy" src="assets/img/people/avijit-kumar-chaudhuri.jpg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Dr. Avijit Kumar Chaudhuri</p>
                    <p class="person__desig">Professor &amp; Head of Department</p>
                    <p class="person__dept">Department of Computer Science &amp; Engineering, Brainware University, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=R7U7Z8MAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Ekta Maini" class="person__photo" loading="lazy" src="assets/img/people/ekta-maini.jpg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Dr. Ekta Maini</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Amity School of Engineering &amp; Technology, Amity University Hyderabad, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=P8f71mQAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Manvi Breja" class="person__photo" loading="lazy" src="assets/img/people/manvi-breja.jpg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Dr. Manvi Breja</p>
                    <p class="person__desig">Assistant Professor (Selection Grade)</p>
                    <p class="person__dept">Department of Computer Science and Engineering, The NorthCap University, Gurugram, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=m26s64UAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Prof. (Dr.) Mehmet Recep Bozkurt" class="person__photo" loading="lazy" src="assets/img/people/mehmet-recep-bozurt.jpeg" />
                  <div class="person__body">
                    <p class="person__role">Turkiye</p>
                    <p class="person__name">Prof. (Dr.) Mehmet Recep Bozkurt</p>
                    <p class="person__desig">Professor</p>
                    <p class="person__dept">Department of Electrical and Electronics Engineering, Sakarya University, Turkiye</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=fLgK2QAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Sannasi Chakravarthy S R" class="person__photo" loading="lazy" src="assets/img/people/sannasi-chakravarthy-s-r.jpg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Dr. Sannasi Chakravarthy S R</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Department of Electronics and Communication Engineering, Bannari Amman Institute of Technology, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=xN8bT0gAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
                <div class="person">
                  <img alt="Dr. Nishant Doshi" class="person__photo" loading="lazy" src="assets/img/people/nishant-doshi.jpg" />
                  <div class="person__body">
                    <p class="person__role">India</p>
                    <p class="person__name">Dr. Nishant Doshi</p>
                    <p class="person__desig">Associate Professor</p>
                    <p class="person__dept">Department of Computer Science and Engineering, Pandit Deendayal Energy University (PDEU), Gandhinagar, India</p>
                    <a class="person__link" href="https://scholar.google.com/citations?user=m2V_Z3AAAAAJ&amp;hl=en" rel="noopener" target="_blank">Scholar profile</a>
                  </div>
                </div>
              </div>
            </div>"""

# Replace International Advisory
content = re.sub(
    r'<div data-people-group="">\s*<h3 style="margin-top:2.5rem">International Advisory Committee</h3>.*?</div>\s*</div>\s*</div>\s*(?=<div data-people-group="">\s*<h3 style="margin-top:2.5rem">National Advisory Committee</h3>)',
    int_advisory_html + '\n',
    content,
    flags=re.DOTALL
)

# Replace National Advisory
content = re.sub(
    r'<div data-people-group="">\s*<h3 style="margin-top:2.5rem">National Advisory Committee</h3>.*?</div>\s*</div>\s*</div>\s*(?=</div>\s*</div>\s*<div class="tab-panel" id="tab-tpc")',
    nat_advisory_html + '\n',
    content,
    flags=re.DOTALL
)

# Replace TPC members
content = re.sub(
    r'<div data-people-group="">\s*<h3 style="margin-top:2.5rem">Technical Program Committee members</h3>.*?</div>\s*</div>\s*</div>\s*(?=</div>\s*</div>\s*<div class="tab-panel" id="tab-organizing")',
    tpc_members_html + '\n',
    content,
    flags=re.DOTALL
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("committee.html successfully updated with exact National Advisory, expanded International Advisory, and TPC members.")
