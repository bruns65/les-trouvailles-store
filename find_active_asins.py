import urllib.request
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8'
}

candidates = [
    # Tech
    ('Support PC Nulaxy / BoYata', 'B0772M8BD1'),
    ('Support PC BoYata Alu', 'B07H774DFQ'),
    ('Support PC Ergonomique', 'B08F9YV1R7'),
    ('Lampe bureau LED BenQ/Quntis', 'B08DKQ38L8'),
    ('Tapis de bureau feutre', 'B09F9W8KRL'),
    ('Tapis de bureau cuir', 'B07DCP6J38'),
    ('Chargeur Anker 65W GaN', 'B08T5QN2TR'),
    ('Chargeur Anker USB-C', 'B099F34ZMG'),
    # Cuisine
    ('Mousseur lait Bonsenkitchen', 'B076F3C4XP'),
    ('Balance cuisine Etekcity Inox', 'B0113UZJE2'),
    ('Balance cuisine Beurer', 'B00140P84A'),
    ('Gourde inox 750ml', 'B074QM2468'),
    ('Gourde inox Super Sparrow', 'B075FRK759'),
    # Maison
    ('Diffuseur huiles essentielles', 'B07QW55365'),
    ('Diffuseur huiles Cecotec', 'B07PP9HGB5'),
    ('Reveil bois LED scandinave', 'B079MCK2W9'),
    ('Reveil bois mat', 'B0892D5Z5D'),
    # Cadeaux
    ('Appareil raclette bougie Cookut', 'B07659K345'),
    ('Appareil raclette bougie', 'B08K39X77N'),
    ('Mini imprimante thermique Phomemo', 'B08D383XFS'),
    ('Mini imprimante Phomemo M02', 'B07S7XHQV2')
]

verified = []
for label, asin in candidates:
    url = f'https://www.amazon.fr/dp/{asin}'
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as res:
            html = res.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<span id=["\']productTitle["\'][^>]*>\s*([^<]+)\s*</span>', html)
            title = title_m.group(1).strip() if title_m else 'Sans titre'
            
            img_m = re.search(r'id=["\']landingImage["\'][^>]*data-a-dynamic-image=["\']([^"\']+)["\']', html)
            img = None
            if img_m:
                try:
                    imgs = json.loads(img_m.group(1).replace('&quot;', '"'))
                    img = list(imgs.keys())[0]
                except:
                    pass
            
            print(f"VERIFIED [200]: {label} ({asin})")
            print(f"   Titre: {title[:75]}")
            print(f"   Img: {img}")
            verified.append({'label': label, 'asin': asin, 'title': title, 'img': img})
    except urllib.error.HTTPError as e:
        # print(f"FAIL [{e.code}]: {label} ({asin})")
        pass
    except Exception as e:
        pass

print(f"\nTotal verified working products: {len(verified)}")
with open('real_working_asins.json', 'w', encoding='utf-8') as f:
    json.dump(verified, f, indent=2, ensure_ascii=False)
