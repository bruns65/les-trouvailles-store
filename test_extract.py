import requests
from bs4 import BeautifulSoup
import re
import json

def test_scrape(asin):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
        'Accept-Language': 'fr-FR,fr;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    url = f'https://www.amazon.fr/dp/{asin}'
    resp = requests.get(url, headers=headers, timeout=10)
    print(f"Status: {resp.status_code}")
    if "api-services-support@amazon.com" in resp.text:
        print("Captcha encountered!")
        return None
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    # Title
    title_el = soup.find('span', id='title') or soup.find(id='productTitle')
    title = title_el.get_text(strip=True) if title_el else ""
    
    # Price
    price_whole = soup.find('span', class_='a-price-whole')
    price_fraction = soup.find('span', class_='a-price-fraction')
    price_str = ""
    if price_whole:
        w = price_whole.get_text(strip=True).replace(',', '').replace('.', '')
        f = price_fraction.get_text(strip=True) if price_fraction else "00"
        price_str = f"{w}.{f}"
    
    # Image
    image_url = ""
    # Try finding image in data attributes or landingImage
    img_tag = soup.find('img', id='landingImage') or soup.find('img', id='main-image')
    if img_tag and img_tag.get('src'):
        image_url = img_tag.get('src')
    
    if not image_url:
        # Check image blocks in mobile view
        for img in soup.find_all('img'):
            src = img.get('src') or ''
            if 'images/I/' in src and ('_SL' in src or '_AC_' in src) and not 'icon' in src:
                image_url = src
                break
                
    if not image_url:
        match = re.search(r'https://m\.media-amazon\.com/images/I/[A-Za-z0-9_\-\.\%]+\.jpg', resp.text)
        if match:
            image_url = match.group(0)

    # Rating
    rating_el = soup.find('span', class_='a-icon-alt')
    rating_str = rating_el.get_text(strip=True) if rating_el else ""
    
    return {
        "asin": asin,
        "title": title[:100],
        "price": price_str,
        "image": image_url,
        "rating": rating_str
    }

if __name__ == '__main__':
    for asin in ['B076F3C4XP', 'B08T5QN2TR']:
        res = test_scrape(asin)
        print("Result:", res)
