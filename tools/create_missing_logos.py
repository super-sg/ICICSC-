import os

logos = {
    'ajman.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><circle cx="50" cy="50" r="45" fill="#0b2341"/><text x="50" y="58" fill="#fff" font-size="26" font-family="sans-serif" font-weight="bold" text-anchor="middle">AU</text></svg>''',
    'mmu.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><rect width="100" height="100" rx="15" fill="#001838"/><text x="50" y="60" fill="#fff" font-size="28" font-family="sans-serif" font-weight="bold" text-anchor="middle">MMU</text></svg>''',
    'hassan.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><circle cx="50" cy="50" r="45" fill="#800000"/><text x="50" y="58" fill="#fff" font-size="26" font-family="sans-serif" font-weight="bold" text-anchor="middle">UH2</text></svg>''',
    'salford.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><rect width="100" height="100" rx="15" fill="#ba0c2f"/><text x="50" y="60" fill="#fff" font-size="26" font-family="sans-serif" font-weight="bold" text-anchor="middle">UoS</text></svg>''',
    'astana.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><circle cx="50" cy="50" r="45" fill="#003366"/><text x="50" y="58" fill="#fec50c" font-size="24" font-family="sans-serif" font-weight="bold" text-anchor="middle">NU</text></svg>''',
    'brainware.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><circle cx="50" cy="50" r="45" fill="#ec1c24"/><text x="50" y="58" fill="#fff" font-size="28" font-family="sans-serif" font-weight="bold" text-anchor="middle">BW</text></svg>''',
    'sakarya.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><circle cx="50" cy="50" r="45" fill="#002d62"/><text x="50" y="58" fill="#fff" font-size="28" font-family="sans-serif" font-weight="bold" text-anchor="middle">SAU</text></svg>''',
    'bits.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><rect width="100" height="100" rx="15" fill="#004d40"/><text x="50" y="60" fill="#fff" font-size="28" font-family="sans-serif" font-weight="bold" text-anchor="middle">BIT</text></svg>''',
    'pdeu.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><circle cx="50" cy="50" r="45" fill="#d32f2f"/><text x="50" y="58" fill="#fff" font-size="24" font-family="sans-serif" font-weight="bold" text-anchor="middle">PDEU</text></svg>''',
    'skikda.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><circle cx="50" cy="50" r="45" fill="#1565c0"/><text x="50" y="58" fill="#fff" font-size="24" font-family="sans-serif" font-weight="bold" text-anchor="middle">U20A</text></svg>''',
    'calabria.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><circle cx="50" cy="50" r="45" fill="#303f9f"/><text x="50" y="58" fill="#fff" font-size="24" font-family="sans-serif" font-weight="bold" text-anchor="middle">UNICAL</text></svg>''',
    'abuad.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="32" height="32"><rect width="100" height="100" rx="15" fill="#1b5e20"/><text x="50" y="60" fill="#fff" font-size="24" font-family="sans-serif" font-weight="bold" text-anchor="middle">ABUAD</text></svg>'''
}

os.makedirs('assets/img/logos/institutions', exist_ok=True)
for fname, content in logos.items():
    fpath = os.path.join('assets/img/logos/institutions', fname)
    if not os.path.exists(fpath):
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {fpath}")
