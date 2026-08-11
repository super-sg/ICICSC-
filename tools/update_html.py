import re
import os

with open('committee.html', 'r', encoding='utf-8') as f:
    html = f.read()

def generate_slug(name):
    # Remove titles
    name = re.sub(r'\b(Dr\.|Prof\.|Mr\.|Ms\.|Er\.|Dr|Prof|PhD|Ph\.D)\b', '', name, flags=re.IGNORECASE)
    name = name.replace('(Dr.)', '').replace('(', '').replace(')', '').replace(',', '')
    slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    return slug

# Updated regex to match the actual HTML structure
pattern = re.compile(r'(<div class="person__avatar"[^>]*>.*?</div>)(\s*<div class="person__body">\s*(?:<p class="person__role">.*?</p>\s*)?<p class="person__name(?:[^>]*)">)([^<]+)(</p>)', re.DOTALL)

def repl(match):
    avatar_html = match.group(1)
    info_html = match.group(2)
    name_html = match.group(3).strip()
    end_html = match.group(4)
    
    slug = generate_slug(name_html)
    
    # Check if a matching image exists
    img_name = None
    for ext in ['.jpg', '.png', '.jpeg', '.webp']:
        if os.path.exists(f'assets/img/people/{slug}{ext}'):
            img_name = f'{slug}{ext}'
            break
            
    # Some hardcoded fallbacks because of naming mismatch
    fallbacks = {
        'satish-chand': 'satish-chand.jpg',
        'nanhay-singh': 'nanhay-singh.jpg',
        'oppili-prasad-l': 'oppili-prasad.jpg',
        'r-k-saket': 'r-k-saket.jpg',
        'sushama-nagpal': 'sushama-nagpal.jpg',
        'd-p-vidyarthi': 'd-p-vidyarthi.jpg',
        'kalpana-chaudhary': 'kalpana-chaudhary.jpg',
        'naveen-yalla': 'naveen-yalla.jpg',
        'n-s-rajput': 'n-s-rajput.jpg',
        'r-mahanty': 'r-mahanty.jpg',
        'smrity-dwivedi': 'smrity-dwivedi.jpg',
        'bhuvanesh-unhelkar': 'bhuvanesh-unhelkar.jpg',
        'narayan-debnath': 'narayan-debnath.jpg',
        'amit-prakash-singh': 'amit-prakash-singh.jpg',
        'r-k-shyamasundar': 'r-k-shyamasundar.jpg',
        'mohd-anas-wajid': 'mohd-anas-wajid.jpg',
        'tariq-saeed-mian': 'tariq-saeed-mian.jpg',
        'muhamad-fazil-ahmad': 'muhamad-fazil-ahmad.jpg',
        'nur-azaliah-abu-bakar': 'nur-azaliah-abu-bakar.jpg',
        'samiya-khan': 'samiya-khan.jpg',
        'yu-chen-hu': 'yu-chen-hu.jpg',
        'jawwad-sami-ur-rahman': 'jawwad-sami-ur-rahman.jpg',
        'inam-ullah': 'inam-ullah.jpg'
    }
    
    if not img_name and slug in fallbacks:
        if os.path.exists(f"assets/img/people/{fallbacks[slug]}"):
            img_name = fallbacks[slug]
            
    if img_name:
        print(f"Replaced {name_html} ({slug}) -> {img_name}")
        return f'<img src="assets/img/people/{img_name}" alt="{name_html}" class="person__photo">{info_html}{name_html}{end_html}'
    else:
        print(f"MISSING: {name_html} ({slug})")
        return match.group(0)

new_html = pattern.sub(repl, html)

with open('committee.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done updating HTML.")
