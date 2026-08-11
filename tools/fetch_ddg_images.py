import os
import requests
from duckduckgo_search import DDGS
from urllib.parse import urlparse

people = [
    "Rania Lampou",
    "Faisal Nabi",
    "Ismail Adaramola Abdul Azeez",
    "Chittaranjan Mandal",
    "Bhim Singh IIT Delhi",
    "Chakradhar Reddy Chandupatla",
    "R. K. Srivastava IIT BHU",
    "Anurag Jain GGSIPU",
    "Avinash Kumar Sharda University",
    "K. Meena Sharda University",
    "Henry Chima Ukwuoma",
    "Mehmet Recep Bozkurt",
    "Shriya Misra",
    "Arab Naz",
    "Qasem Abu Al-Haija",
    "Kevin M. Rivera",
    "Ilham Laabab",
    "Amit Sharma Sharda University",
    "K. Lakshmi Sharda University"
]

def generate_slug(name):
    # Remove titles
    import re
    name_clean = re.sub(r'\b(Dr\.|Prof\.|Mr\.|Ms\.|Er\.|Dr|Prof|PhD|Ph\.D)\b', '', name, flags=re.IGNORECASE)
    name_clean = name_clean.replace('(Dr.)', '').replace('(', '').replace(')', '').replace(',', '')
    # specifically for ones with institutional hints
    name_clean = name_clean.replace('IIT Delhi', '').replace('IIT BHU', '').replace('GGSIPU', '').replace('Sharda University', '')
    slug = re.sub(r'[^a-z0-9]+', '-', name_clean.lower()).strip('-')
    return slug

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

with DDGS() as ddgs:
    for name in people:
        slug = generate_slug(name)
        print(f"Searching for {name} ({slug})...")
        try:
            results = ddgs.images(
                keywords=f"{name} profile photo OR face",
                region="wt-wt",
                safesearch="off",
                size=None,
                type_image=None,
                layout=None,
                license_image=None,
                max_results=3,
            )
            
            if not results:
                print(f"  No images found for {name}")
                continue
                
            for res in results:
                img_url = res['image']
                print(f"  Trying {img_url}")
                try:
                    response = requests.get(img_url, headers=headers, timeout=10)
                    if response.status_code == 200:
                        content_type = response.headers.get('content-type', '')
                        ext = '.jpg'
                        if 'png' in content_type: ext = '.png'
                        elif 'webp' in content_type: ext = '.webp'
                        elif 'jpeg' in content_type: ext = '.jpg'
                        elif urlparse(img_url).path.endswith('.png'): ext = '.png'
                        elif urlparse(img_url).path.endswith('.webp'): ext = '.webp'
                        
                        filepath = f"assets/img/people/{slug}{ext}"
                        with open(filepath, 'wb') as f:
                            f.write(response.content)
                        print(f"  Successfully downloaded to {filepath}")
                        break
                except Exception as e:
                    print(f"  Failed to download {img_url}: {e}")
        except Exception as e:
            print(f"  Search failed for {name}: {e}")
