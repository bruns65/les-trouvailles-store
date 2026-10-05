import urllib.request
import re
import json

asins = {
    'tech-screenbar': 'B08C4VKYFG',
    'tech-stand': 'B07D74DT3B',
    'tech-charger': 'B09PQV586X',
    'deco-clock': 'B079MCK2W9',
    'cuisine-scale': 'B01MY0E0J3'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8'
}

for name, asin in asins.items():
    url = f'https://www.amazon.fr/dp/{asin}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as res:
            html = res.read().decode('utf-8', errors='ignore')
            
            # Pattern 1: landingImage data-a-dynamic-image
            m = re.search(r'id=[\'"]landingImage[\'"][^>]*data-a-dynamic-image=[\'"]([^\'"]+)[\'"]', html)
            if m:
                raw_json = m.group(1).replace('&quot;', '"')
                imgs = json.loads(raw_json)
                main_img = list(imgs.keys())[0]
                print(f'{name} ({asin}) -> LandingImage: {main_img}')
                continue
            
            # Pattern 2: colorImages large
            m2 = re.search(r'\"large\":\"(https://m\.media-amazon\.com/images/I/[A-Za-z0-9\-_%+]+\.jpg)\"', html)
            if m2:
                print(f'{name} ({asin}) -> ColorImage: {m2.group(1)}')
                continue

            print(f'{name} ({asin}) -> Not found')
    except Exception as e:
        print(f'{name} ({asin}) -> Error: {e}')
