import urllib.request
import re

url = 'https://cataloniastore.com/collections/wearable-blankets'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8')
        imgs = re.findall(r'//cataloniastore\.com/cdn/shop/files/[^\s"\'<>]+\.(?:jpg|png|webp)', html)
        print('Found images:', len(imgs))
        for img in list(set(imgs))[:6]:
            clean_img = 'https:' + img.split('&')[0].split('?')[0]
            print(clean_img)
except Exception as e:
    print('Error:', e)
