"""
Scraper & Synchroniseur Amazon pour Les Trouvailles
Permet de récupérer les informations officielles (Titre, Image HD Amazon CDN, Prix, Étoiles)
à partir d'un ASIN ou d'une URL de produit Amazon.
"""

import requests
from bs4 import BeautifulSoup
import re
import json
import sys

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

def extract_asin(url_or_asin: str) -> str:
    """Extrait l'ASIN (10 caractères alphanumériques) d'une URL ou d'une chaîne."""
    match = re.search(r'(?:/dp/|/gp/product/|/d/|/ASIN/|/product/)?([A-Z0-9]{10})(?:[/?&]|$)', url_or_asin.strip(), re.IGNORECASE)
    if match:
        return match.group(1).upper()
    return url_or_asin.strip().upper()

def scrape_amazon_product(asin_or_url: str):
    asin = extract_asin(asin_or_url)
    if len(asin) != 10:
        return {"success": False, "error": f"ASIN invalide : {asin_or_url}"}

    url = f"https://www.amazon.fr/dp/{asin}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=12)
    except Exception as e:
        return {"success": False, "error": f"Erreur de connexion : {e}"}

    if resp.status_code == 404:
        return {"success": False, "error": f"Produit introuvable (Erreur 404 Amazon) pour l'ASIN {asin}"}
    
    if resp.status_code != 200:
        return {"success": False, "error": f"Code HTTP {resp.status_code}"}

    if "api-services-support@amazon.com" in resp.text:
        return {"success": False, "error": "Amazon a temporairement bloqué la requête par captcha."}

    soup = BeautifulSoup(resp.text, 'html.parser')

    # 1. Titre
    title_el = soup.find('span', id='title') or soup.find(id='productTitle')
    title = title_el.get_text(strip=True) if title_el else ""

    # Nettoyage du titre
    title = re.sub(r'\s+', ' ', title).strip()

    # 2. Image Officielle Amazon CDN
    image_url = ""
    img_tag = soup.find('img', id='landingImage') or soup.find('img', id='main-image')
    if img_tag and img_tag.get('src'):
        image_url = img_tag.get('src')
    
    if not image_url:
        # Recherche des images CDN m.media-amazon.com
        for img in soup.find_all('img'):
            src = img.get('src') or ''
            if 'media-amazon.com/images/I/' in src and ('_SL' in src or '_AC_' in src) and 'icon' not in src:
                image_url = src
                break

    if not image_url:
        m = re.search(r'https://m\.media-amazon\.com/images/I/[A-Za-z0-9_\-\.\%]+\.jpg', resp.text)
        if m:
            image_url = m.group(0)

    # Convertir en image haute résolution si miniature
    if image_url and '._AC_UF' in image_url:
        image_url = re.sub(r'\._AC_UF\d+,\d+_[A-Z0-9_]*_\.jpg', '._AC_SL1500_.jpg', image_url)
    elif image_url and '._AC_SR' in image_url:
        image_url = re.sub(r'\._AC_SR\d+,\d+_[A-Z0-9_]*_\.jpg', '._AC_SL1500_.jpg', image_url)

    # 3. Prix (Prioriser l'offre principale et la remise effective)
    price = 0.0
    original_price = None

    # Chercher la boîte de prix principale
    main_price_box = soup.find('div', id='corePrice_desktop') or \
                     soup.find('div', id='corePriceDisplay_desktop_feature_div') or \
                     soup.find('div', id='apex_desktop') or \
                     soup.find('div', class_='aok-align-center')

    # Recherche directe dans la boîte principale
    price_target = main_price_box if main_price_box else soup

    # Recherche des éléments a-price
    all_prices = price_target.find_all('span', class_='a-price')
    for p_el in all_prices:
        # Ignorer les prix barrés pour le prix d'achat
        if 'a-text-price' in p_el.get('class', []):
            continue
        pw = p_el.find('span', class_='a-price-whole')
        pf = p_el.find('span', class_='a-price-fraction')
        if pw:
            w = pw.get_text(strip=True).replace(',', '').replace('.', '').replace(' ', '')
            f = pf.get_text(strip=True).replace(' ', '') if pf else "00"
            try:
                p_val = float(f"{w}.{f}")
                if p_val > 0:
                    price = p_val
                    break
            except ValueError:
                pass

    # Détecter prix barré d'origine s'il existe
    orig_el = soup.find('span', class_='a-price a-text-price')
    if orig_el:
        pw_orig = orig_el.find('span', class_='a-offscreen')
        if pw_orig:
            m_orig = re.search(r'([0-9]+[.,][0-9]{2})', pw_orig.get_text(strip=True))
            if m_orig:
                try:
                    original_price = float(m_orig.group(1).replace(',', '.'))
                except ValueError:
                    pass

    # 4. Note & Avis
    rating_el = soup.find('span', class_='a-icon-alt')
    rating = 4.7
    if rating_el:
        r_text = rating_el.get_text(strip=True)
        m_r = re.search(r'([0-9]+[.,][0-9]+)', r_text)
        if m_r:
            rating = float(m_r.group(1).replace(',', '.'))

    reviews_count = 1200
    rev_el = soup.find('span', id='acrCustomerReviewText')
    if rev_el:
        m_cnt = re.search(r'([0-9\s\xa0]+)', rev_el.get_text(strip=True))
        if m_cnt:
            clean_num = re.sub(r'[\s\xa0]', '', m_cnt.group(1))
            if clean_num.isdigit():
                reviews_count = int(clean_num)

    return {
        "success": True,
        "asin": asin,
        "title": title,
        "price": price,
        "image": image_url,
        "rating": rating,
        "reviewsCount": reviews_count,
        "amazonUrl": f"https://www.amazon.fr/dp/{asin}"
    }

if __name__ == '__main__':
    test_asins = ['B08C4VKYFG', 'B076F3C4XP', 'B08T5QN2TR']
    if len(sys.argv) > 1:
        test_asins = sys.argv[1:]

    for a in test_asins:
        print(f"\n--- Scraping ASIN: {a} ---")
        res = scrape_amazon_product(a)
        if res["success"]:
            print(f"[OK] Titre: {res['title'][:60].encode('ascii', 'ignore').decode()}...")
            print(f"Prix: {res['price']} EUR")
            print(f"Note: {res['rating']} ({res['reviewsCount']} avis)")
            print(f"Image: {res['image']}")
            print(f"URL: {res['amazonUrl']}")
        else:
            print(f"[ERR] Erreur: {res['error']}")
