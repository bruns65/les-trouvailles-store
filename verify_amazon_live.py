import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8'
}

def verify_asin(asin):
    url = f'https://www.amazon.fr/dp/{asin}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<span id=["\']productTitle["\'][^>]*>\s*([^<]+)\s*</span>', html)
            title = title_m.group(1).strip() if title_m else 'NO TITLE'
            
            img_m = re.search(r'id=["\']landingImage["\'][^>]*data-a-dynamic-image=["\']([^"\']+)["\']', html)
            img = None
            if img_m:
                try:
                    imgs = json.loads(img_m.group(1).replace('&quot;', '"'))
                    img = list(imgs.keys())[0]
                except:
                    pass
            
            return {'status': res.status, 'title': title[:80], 'img': img}
    except urllib.error.HTTPError as e:
        return {'status': e.code, 'error': str(e)}
    except Exception as e:
        return {'status': 'ERR', 'error': str(e)}

# Test popular known Amazon France ASINs
test_asins = [
    ('Echo Pop Enceinte connectee', 'B09ZX554LH'),
    ('Fire TV Stick 4K', 'B08C17VSS9'),
    ('Quntis Lampe Ecran ScreenBar', 'B08DKQ38L8'),
    ('Support PC Portable Nulaxy', 'B0772M8BD1'),
    ('Mousseur a lait Bonsenkitchen', 'B076F3C4XP'),
    ('Balance de cuisine Etekcity', 'B0113UZJE2'),
    ('Bouteille Isotherme Ion8', 'B07K6Q1X9W')
]

for name, asin in test_asins:
    info = verify_asin(asin)
    print(f"[{info.get('status')}] {name} ({asin})")
    print(f"   Titre reel: {info.get('title')}")
    print(f"   Image reelle: {info.get('img')}")
    print()
