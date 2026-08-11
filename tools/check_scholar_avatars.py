import urllib.request
import re

scholars = {
    "Rania Lampou": "ozvmG2kAAAAJ",
    "Faisal Nabi": "lHqJA88AAAAJ",
    "Ismail Adaramola": "KxJsRggAAAAJ",
    "Chittaranjan Mandal": "n-mJ-dEAAAAJ",
    "Bhim Singh": "1QQOMOAAAAAJ",
    "Chakradhar Reddy": "ZSxBtpIAAAAJ",
    "Anurag Jain": "03-jVLwAAAAJ",
    "Avinash Kumar": "LB_8ueoAAAAJ",
    "HENRY CHIMA": "qd6Y29cAAAAJ",
    "Mehmet Recep Bozkurt": "F21VO-kAAAAJ",
    "Shriya Misra": "gTBK48oAAAAJ",
    "Arab Naz": "CT_f8AoAAAAJ",
    "Qasem Abu Al-Haija": "b6bvLQwAAAAJ",
    "Kevin M. Rivera": "3t3db_cAAAAJ",
    "Ilham Laabab": "GaWofL4AAAAJ",
}

headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

results = []

for name, user_id in scholars.items():
    url = f"https://scholar.google.com/citations?user={user_id}&hl=en"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            if "avatar_scholar" in html:
                results.append(f"{name}: DEFAULT AVATAR")
            elif 'id="gsc_prf_pup-img"' in html:
                results.append(f"{name}: HAS CUSTOM PHOTO")
            else:
                results.append(f"{name}: NO PHOTO DIV FOUND (Maybe blocked/404)")
    except Exception as e:
        results.append(f"{name}: ERROR ({e})")

for res in results:
    print(res)
