import urllib.request
import re

url = "https://www.amazon.fr/s?k=mousseur+lait"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=8) as res:
        html = res.read().decode('utf-8', errors='ignore')
        print("Page length:", len(html))
        # Find data-asin
        asins = re.findall(r'data-asin="([B0-9][A-Z0-9]{9})"', html)
        print("Found data-asin count:", len(asins))
        print("First 5 asins:", asins[:5])
        
        # Check if bot detection captcha
        if "captcha" in html.lower() or "robot" in html.lower():
            print("Amazon served robot/captcha page")
except Exception as e:
    print("Error:", e)
