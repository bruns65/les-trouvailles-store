import requests
import re
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
    'Accept-Language': 'fr-FR,fr;q=0.9',
}

def scan_amazon_coupons():
    url = "https://www.amazon.fr/coupons"
    resp = requests.get(url, headers=headers, timeout=12)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    # Extract links to dp
    dp_links = set(re.findall(r'/dp/([A-Z0-9]{10})', resp.text))
    print(f"Total ASINs on /coupons: {len(dp_links)}")
    return list(dp_links)

if __name__ == '__main__':
    asins = scan_amazon_coupons()
    print("Premiers ASINs découverts:", asins[:8])
