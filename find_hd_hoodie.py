import urllib.request
import re

url = 'https://cataloniastore.com/products/oversized-wearable-blanket-hoodie-sweatshirt'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8')
        imgs = re.findall(r'//cataloniastore\.com/cdn/shop/files/[^\s"\'<>]+\.jpg', html)
        for i in set(imgs):
            if 'x64' not in i and 'thumb' not in i:
                print('https:' + i.split('?')[0])
except Exception as e:
    print('Error:', e)
