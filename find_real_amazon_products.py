import urllib.request
import urllib.parse
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.fr/'
}

def search_amazon_france(query):
    encoded_q = urllib.parse.quote_plus(query)
    url = f'https://www.amazon.fr/s?k={encoded_q}'
    print(f"Recherche sur Amazon.fr pour: '{query}'...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as res:
            html = res.read().decode('utf-8', errors='ignore')
            
            # Rechercher les blocs de résultats avec asin, title, image, price
            # data-asin="B0..."
            items = []
            asin_blocks = re.findall(r'data-asin="([B0-9][A-Z0-9]{9})"[^>]*>(.*?)</div>\s*</div>\s*</div>', html, re.DOTALL)
            
            # Alternative: regex directe sur les liens produits
            matches = re.findall(r'href="\/([^\/]+)\/dp\/([B0-9][A-Z0-9]{9})[^"]*"', html)
            seen_asins = set()
            
            for slug, asin in matches:
                if asin in seen_asins or len(slug) < 3:
                    continue
                seen_asins.add(asin)
                
                # Chercher l'image associée dans le html autour de cet asin
                img_m = re.search(rf'{asin}.*?src="(https://m\.media-amazon\.com/images/I/[^"]+\.jpg)"', html, re.DOTALL)
                if not img_m:
                    img_m = re.search(rf'src="(https://m\.media-amazon\.com/images/I/[^"]+\.jpg)".*?{asin}', html, re.DOTALL)
                
                img_url = img_m.group(1) if img_m else None
                clean_title = urllib.parse.unquote(slug).replace('-', ' ')
                
                items.append({
                    'asin': asin,
                    'title': clean_title[:80],
                    'slug': slug,
                    'img': img_url,
                    'url': f'https://www.amazon.fr/dp/{asin}'
                })
                if len(items) >= 2:
                    break
                    
            return items
    except Exception as e:
        print(f"Erreur recherche '{query}':", e)
        return []

searches = [
    "lampe bureau ecran screenbar",
    "support pc portable aluminium",
    "chargeur sans fil 3 en 1",
    "diffuseur huile essentielle flamme",
    "sunset lamp projecteur",
    "mini imprimante thermique smartphone",
    "lampe lune 3d levitation",
    "mousseur lait electrique",
    "pulverisateur huile air fryer"
]

results = {}
for q in searches:
    found = search_amazon_france(q)
    results[q] = found
    for item in found:
        print(f"  -> [{item['asin']}] {item['title']}")
        print(f"     Image: {item['img']}")
        print(f"     Lien: {item['url']}")
    print()

with open("verified_scraped_products.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
