import requests
import re
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
    'Accept-Language': 'fr-FR,fr;q=0.9',
}

queries = [
    ("tech", "screenbar quntis"),
    ("deco", "cheminee table bioethanol"),
    ("deco", "sweat plaid polaire sherpa"),
    ("gift", "appareil raclette bougie cookut"),
    ("gift", "mini imprimante thermique smartphone"),
    ("cuisine", "mousseur a lait electrique"),
    ("deco", "sunset lamp projecteur"),
]

for cat, q in queries:
    url = f"https://www.amazon.fr/s?k={q.replace(' ', '+')}"
    resp = requests.get(url, headers=headers, timeout=10)
    print(f"Query: {q} -> Status: {resp.status_code}")
    if "api-services-support@amazon.com" in resp.text:
        print("  Captcha!")
        continue
    # Extract ASINs
    asins = re.findall(r'data-asin="([A-Z0-9]{10})"', resp.text)
    clean_asins = [a for a in asins if a]
    print(f"  Found {len(clean_asins)} asins: {clean_asins[:3]}")
    time.sleep(1)
