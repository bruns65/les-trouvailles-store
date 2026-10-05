import amazon_scraper
import json
import re

with open('products.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract all ASINs
asins = re.findall(r'amazonAsin:\s*"([A-Z0-9]+)"', text)
print(f"Total ASINs à vérifier: {len(asins)}")

results = {}
for a in asins:
    data = amazon_scraper.scrape_amazon_product(a)
    if data['success']:
        results[a] = {
            'price': data['price'],
            'title': data['title'][:50]
        }
        print(f"ASIN {a}: {data['price']} € | {data['title'][:40]}")
    else:
        print(f"ASIN {a}: ERREUR {data.get('error')}")

with open('lowest_prices_audit.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
