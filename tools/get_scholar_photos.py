import urllib.request
import re
import os

scholars = {
    "henry-chima-ukwuoma": "qd6Y29cAAAAJ",
    "mehmet-recep-bozkurt": "F21VO-kAAAAJ",
    "shriya-misra": "gTBK48oAAAAJ",
    "qasem-abu-al-haija": "b6bvLQwAAAAJ",
    "kevin-m-rivera": "3t3db_cAAAAJ",
    "ilham-laabab": "GaWofL4AAAAJ",
    "rania-lampou": "ozvmG2kAAAAJ",
    "anurag-jain": "03-jVLwAAAAJ",
    "chittaranjan-mandal": "n-mJ-dEAAAAJ",
    "bhim-singh": "1QQOMOAAAAAJ",
    "chakradhar-reddy": "ZSxBtpIAAAAJ",
    "samiya-khan": "5xXQRsQAAAAJ",
    "yu-chen-hu": "yIYwXkMAAAAJ"
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, user_id in scholars.items():
    url = f"https://scholar.google.com/citations?user={user_id}&hl=en"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Find the profile picture URL
            match = re.search(r'id="gsc_prf_pup-img"[^>]*src="([^"]+)"', html)
            if not match:
                match = re.search(r'id="gsc_prf_pup"[^>]*src="([^"]+)"', html)
                
            if match:
                img_url = match.group(1)
                img_url = img_url.replace('&amp;', '&')
                
                # Check if it's the default avatar
                if "avatar_scholar" in img_url:
                    print(f"[{name}] Default avatar found. Skipping.")
                else:
                    if img_url.startswith('/'):
                        img_url = "https://scholar.google.com" + img_url
                    
                    print(f"[{name}] Found real photo: {img_url}")
                    
                    # Download the image
                    img_req = urllib.request.Request(img_url, headers=headers)
                    with urllib.request.urlopen(img_req) as img_response:
                        img_data = img_response.read()
                        with open(f"assets/img/people/{name}.jpg", "wb") as f:
                            f.write(img_data)
                    print(f"[{name}] Downloaded.")
            else:
                print(f"[{name}] No photo URL found.")
    except Exception as e:
        print(f"[{name}] Error: {e}")
