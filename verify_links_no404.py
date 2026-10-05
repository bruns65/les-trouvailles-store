import urllib.request
import urllib.parse

links = [
    ("Mousseur Bonsenkitchen (ASIN direct)", "https://www.amazon.fr/dp/B076F3C4XP"),
    ("Chargeur Anker GaN (ASIN direct)", "https://www.amazon.fr/dp/B08T5QN2TR"),
    ("ScreenBar Lampe Ecran (Search garanti)", "https://www.amazon.fr/s?k=quntis+barre+lumineuse+ecran"),
    ("Raclette Bougie (Search garanti)", "https://www.amazon.fr/s?k=appareil+raclette+bougie+cookut"),
    ("Cheminee Table Bioethanol (Search garanti)", "https://www.amazon.fr/s?k=cheminee+table+bioethanol+verre"),
    ("Sweat Plaid Geant (Search garanti)", "https://www.amazon.fr/s?k=sweat+plaid+geant+oversize+sherpa"),
    ("Mini Imprimante Thermique (Search garanti)", "https://www.amazon.fr/s?k=mini+imprimante+thermique+smartphone"),
    ("Sunset Lamp (Search garanti)", "https://www.amazon.fr/s?k=sunset+lamp+projecteur+coucher+de+soleil")
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8'
}

print("Verification de la validite des liens...")
for name, url in links:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as res:
            print(f"OK [200]: {name}")
    except urllib.error.HTTPError as e:
        print(f"FAILED [{e.code}]: {name} -> {url}")
    except Exception as e:
        print(f"ERROR: {name} -> {e}")
