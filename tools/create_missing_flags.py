import os

flags = {
    'in.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="28" height="20">
  <path fill="#f93" d="M0 0h640v160H0z"/>
  <path fill="#fff" d="M0 160h640v160H0z"/>
  <path fill="#128807" d="M0 320h640v160H0z"/>
  <circle cx="320" cy="240" r="50" fill="none" stroke="#008" stroke-width="6"/>
  <circle cx="320" cy="240" r="10" fill="#008"/>
</svg>''',
    'br.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="28" height="20">
  <path fill="#009c3b" d="M0 0h640v480H0z"/>
  <path fill="#ffdf00" d="M320 50L580 240 320 430 60 240z"/>
  <circle cx="320" cy="240" r="110" fill="#002776"/>
  <path fill="#fff" d="M210 240a110 110 0 0 0 215-20 110 110 0 0 1-215 20z"/>
</svg>''',
    'ma.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="28" height="20">
  <path fill="#c1272d" d="M0 0h640v480H0z"/>
  <polygon fill="none" stroke="#006233" stroke-width="12" points="320,140 355,250 262,182 378,182 285,250"/>
</svg>''',
    'kz.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="28" height="20">
  <path fill="#00afca" d="M0 0h640v480H0z"/>
  <circle cx="320" cy="220" r="45" fill="#fec50c"/>
  <path fill="#fec50c" d="M270 280c25-10 75-10 100 0-20 20-80 20-100 0z"/>
</svg>''',
    'dz.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="28" height="20">
  <path fill="#006633" d="M0 0h320v480H0z"/>
  <path fill="#fff" d="M320 0h320v480H320z"/>
  <circle cx="320" cy="240" r="90" fill="#d21034"/>
  <circle cx="345" cy="240" r="72" fill="#fff"/>
  <polygon fill="#d21034" points="345,210 354,235 379,235 359,250 367,274 345,260 323,274 331,250 311,235 336,235"/>
</svg>'''
}

os.makedirs('assets/img/flags', exist_ok=True)
for fname, content in flags.items():
    fpath = os.path.join('assets/img/flags', fname)
    if not os.path.exists(fpath):
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {fpath}")
