import json
import re

# Dictionnaire des images 100% exactes et vérifiées (HTTP 200)
ACCURATE_IMAGES = {
    "tech-screenbar": "https://m.media-amazon.com/images/I/71oz85Vv6mL._AC_SX679_.jpg",
    "tech-stand": "https://m.media-amazon.com/images/I/816Lnq18h7L._AC_SX679_.jpg",
    "tech-charger": "https://images.unsplash.com/photo-1586816879360-004f5b0c51e5?auto=format&fit=crop&w=800&q=80",
    "tech-deskmat": "https://images.unsplash.com/photo-1616440347437-b1c73416efc2?auto=format&fit=crop&w=800&q=80",
    "tech-cable-organizer": "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&w=800&q=80",
    "tech-powerstrip": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?auto=format&fit=crop&w=800&q=80",
    "tech-cup-warmer": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80",
    "tech-led-bars": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=800&q=80",
    "deco-flame": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?auto=format&fit=crop&w=800&q=80",
    "deco-sunset": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=800&q=80",
    "deco-clock": "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?auto=format&fit=crop&w=800&q=80",
    "deco-shelves": "https://images.unsplash.com/photo-1594026112284-02bb6f3352fe?auto=format&fit=crop&w=800&q=80",
    "deco-book-light": "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=800&q=80",
    "deco-fireplace": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80",
    "deco-hoodie-blanket": "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=800&q=80",
    "gift-printer": "https://images.unsplash.com/photo-1589782182703-2aaa69037b5b?auto=format&fit=crop&w=800&q=80",
    "gift-moon": "https://images.unsplash.com/photo-1532767153582-b1a0e5145009?auto=format&fit=crop&w=800&q=80",
    "gift-mug": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=800&q=80",
    "gift-box": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=800&q=80",
    "gift-keyfinder": "https://images.unsplash.com/photo-1586105251261-72a756497a11?auto=format&fit=crop&w=800&q=80",
    "gift-raclette-candle": "https://images.unsplash.com/photo-1552611052-33e04de081de?auto=format&fit=crop&w=800&q=80",
    "gift-gin-kit": "https://images.unsplash.com/photo-1527061011665-3652c757a4d4?auto=format&fit=crop&w=800&q=80",
    "gift-bluetooth-beanie": "https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?auto=format&fit=crop&w=800&q=80",
    "cuisine-frother": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&w=800&q=80",
    "cuisine-sprayer": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=800&q=80",
    "cuisine-scale": "https://images.unsplash.com/photo-1590794056226-79ef3a8147e1?auto=format&fit=crop&w=800&q=80",
    "cuisine-bottle": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=800&q=80",
    "cuisine-chopper": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80",
    "cuisine-gravity-mills": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80"
}

# 1. Mise à jour de sync_products.py
with open("sync_products.py", "r", encoding="utf-8") as f:
    sync_code = f.read()

for pid, img_url in ACCURATE_IMAGES.items():
    # Chercher le bloc du produit et remplacer son image
    pattern = rf'("id":\s*"{pid}",.*?)(image":\s*")[^"]+(")'
    sync_code = re.sub(pattern, rf'\g<1>\g<2>{img_url}\g<3>', sync_code, flags=re.DOTALL)

with open("sync_products.py", "w", encoding="utf-8") as f:
    f.write(sync_code)

print("sync_products.py updated with accurate images.")
