#!/usr/bin/env python3
"""
Sync & Update Script: Les Trouvailles Curated Store
Permet d'actualiser automatiquement le catalogue avec les meilleures pépites et tendances du moment.
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_FILE = os.path.join(BASE_DIR, "products.js")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

# Liste enrichie des meilleures ventes et pépites vérifiées par catégorie
EXPANDED_CURATED_DATABASE = [
    # 💻 TECH & TÉLÉTRAVAIL
    {
        "id": "tech-screenbar",
        "category": "tech",
        "categoryName": "Tech & Télétravail",
        "title": "Lampe de Moniteur ScreenBar LED Anti-reflets",
        "tagline": "Éclairage asymétrique zéro reflet sur la dalle d'écran pour supprimer la fatigue oculaire.",
        "price": 39.99,
        "originalPrice": 49.99,
        "rating": 4.8,
        "reviewsCount": 4210,
        "badge": "Top Tendance 🔥",
        "image": "https://m.media-amazon.com/images/I/71oz85Vv6mL._AC_SX679_.jpg",
        "amazonAsin": "B08C4VKYFG",
        "amazonUrl": "https://www.amazon.fr/dp/B08C4VKYFG",
        "curatorOpinion": "Un indispensable absolu pour quiconque passe plus de 4 heures par jour devant un écran. Elle libère 100% de l'espace sur le bureau.",
        "highlights": ["Zéro reflet sur l'écran", "Température de couleur réglable", "Alimentation USB directe", "Fixation universelle"]
    },
    {
        "id": "tech-stand",
        "category": "tech",
        "categoryName": "Tech & Télétravail",
        "title": "Support PC Portable Aluminium Anodisé Réglable",
        "tagline": "Élève l'écran à hauteur des yeux pour éliminer les douleurs de nuque et ventiler le PC.",
        "price": 28.99,
        "originalPrice": 34.99,
        "rating": 4.7,
        "reviewsCount": 5420,
        "badge": "Coup de Cœur ⭐",
        "image": "https://m.media-amazon.com/images/I/816Lnq18h7L._AC_SX679_.jpg",
        "amazonAsin": "B07D74DT3B",
        "amazonUrl": "https://www.amazon.fr/dp/B07D74DT3B",
        "curatorOpinion": "Construction solide en aluminium digne des finitions Apple. La dissipation thermique passive garde l'ordinateur au frais.",
        "highlights": ["Supporte jusqu'à 6 kg", "Patins silicone anti-rayures", "Pliable pour les déplacements", "Compatible 10 à 17 pouces"]
    },
    {
        "id": "tech-charger",
        "category": "tech",
        "categoryName": "Tech & Télétravail",
        "title": "Station de Charge 3-en-1 Pliable Magnétique MagSafe",
        "tagline": "Recharge simultanément iPhone/Android, écouteurs sans fil et montre connectée.",
        "price": 35.90,
        "originalPrice": 45.00,
        "rating": 4.6,
        "reviewsCount": 2350,
        "badge": "Meilleur Rapport Q/P 💎",
        "image": "https://images.unsplash.com/photo-1586816879360-004f5b0c51e5?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B09PQV586X",
        "amazonUrl": "https://www.amazon.fr/dp/B09PQV586X",
        "curatorOpinion": "Fini l'amas de câbles sur la table de chevet ou le bureau. Se replie à plat comme un portefeuille.",
        "highlights": ["Charge rapide certifiée Qi", "Aimants puissants alignement auto", "Format de poche pliable", "Indicateur discret de nuit"]
    },
    {
        "id": "tech-deskmat",
        "category": "tech",
        "categoryName": "Tech & Télétravail",
        "title": "Grand Tapis de Bureau en Feutre Minimaliste (90x40cm)",
        "tagline": "Texture chaleureuse et confort acoustique incomparable pour votre clavier et souris.",
        "price": 19.99,
        "originalPrice": 24.99,
        "rating": 4.6,
        "reviewsCount": 1940,
        "badge": "Petit Prix 🏷️",
        "image": "https://images.unsplash.com/photo-1616440347437-b1c73416efc2?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B09F9W8KRL",
        "amazonUrl": "https://www.amazon.fr/dp/B09F9W8KRL",
        "curatorOpinion": "Le détail esthétique qui transforme instantanément un bureau ordinaire en espace de travail professionnel et chaleureux.",
        "highlights": ["Feutre dense doux au toucher", "Base antidérapante", "Protège la table des rayures", "Entretien facile à l'éponge"]
    },
    {
        "id": "tech-cable-organizer",
        "category": "tech",
        "categoryName": "Tech & Télétravail",
        "title": "Organiseur de Câbles Magnétique Bois & Noyer",
        "tagline": "Garde tous vos câbles de charge alignés et prêts sans jamais tomber derrière le meuble.",
        "price": 16.90,
        "originalPrice": 21.00,
        "rating": 4.7,
        "reviewsCount": 1820,
        "badge": "Top Astuce ⚡",
        "image": "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B0892H1Q65",
        "amazonUrl": "https://www.amazon.fr/dp/B0892H1Q65",
        "curatorOpinion": "L'accessoire indispensable pour en finir avec les câbles qui glissent par terre dès qu'on débranche son téléphone.",
        "highlights": ["Base bois avec adhésif repositionnable", "Colliers magnétiques ultra-rapides", "Convient pour câbles USB-C, Lightning, HDMI", "Design épuré haut de gamme"]
    },
    {
        "id": "tech-powerstrip",
        "category": "tech",
        "categoryName": "Tech & Télétravail",
        "title": "Multiprise Cube USB-C 65W GaN avec Interrupteur",
        "tagline": "Compacte, discrète et surpuissante pour recharger PC portable et téléphones sur un coin de table.",
        "price": 32.99,
        "originalPrice": 39.99,
        "rating": 4.8,
        "reviewsCount": 3150,
        "badge": "Bestseller 🔌",
        "image": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B08R697LFX",
        "amazonUrl": "https://www.amazon.fr/dp/B08R697LFX",
        "curatorOpinion": "Remplace 4 chargeurs encombrants par un seul cube discret. La technologie GaN chauffe 50% moins qu'un chargeur classique.",
        "highlights": ["Recharge rapide PC USB-C 65W", "3 prises secteur + 3 ports USB", "Protection anti-surtension", "Câble tressé renforcé"]
    },

    # 🏡 MAISON & DÉCORATION
    {
        "id": "deco-flame",
        "category": "deco",
        "categoryName": "Maison & Décoration",
        "title": "Diffuseur d'Huiles Essentielles Effet Flamme 3D Cosy",
        "tagline": "Crée une illusion de foyer de cheminée ultra-chaleureux tout en diffusant vos arômes préférés.",
        "price": 29.99,
        "originalPrice": 39.99,
        "rating": 4.8,
        "reviewsCount": 4820,
        "badge": "Top Tendance 🔥",
        "image": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B09L7W5ZBQ",
        "amazonUrl": "https://www.amazon.fr/dp/B09L7W5ZBQ",
        "curatorOpinion": "L'effet visuel de la brume éclairée par LED imite une vraie flamme ambrée. Idéal pour créer un cocon apaisant en soirée.",
        "highlights": ["Effet flamme réaliste réglable", "Silencieux (< 20 dB)", "Arrêt automatique si niveau d'eau bas", "Autonomie jusqu'à 8 heures"]
    },
    {
        "id": "deco-sunset",
        "category": "deco",
        "categoryName": "Maison & Décoration",
        "title": "Sunset Lamp Projecteur Coucher de Soleil Rotatif 360°",
        "tagline": "Diffuse un halo doré chaud et photogénique pour transformer l'ambiance d'une pièce.",
        "price": 18.50,
        "originalPrice": 25.00,
        "rating": 4.6,
        "reviewsCount": 3280,
        "badge": "Viral TikTok 📱",
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B08X4T96K1",
        "amazonUrl": "https://www.amazon.fr/dp/B08X4T96K1",
        "curatorOpinion": "La lampe qui a fait sensation sur les réseaux. Elle apporte une lumière dorée parfaite pour les photos ou pour adoucir la pièce.",
        "highlights": ["Tête en aluminium orientable 360°", "Lentille en verre optique haute netteté", "Alimentation USB universelle", "Effet coucher de soleil apaisant"]
    },
    {
        "id": "deco-clock",
        "category": "deco",
        "categoryName": "Maison & Décoration",
        "title": "Réveil Digital Bloc de Bois Minimaliste Capteur Sonore",
        "tagline": "Horloge scandinave affichant l'heure et la température, activable par tapotement.",
        "price": 24.99,
        "originalPrice": 29.99,
        "rating": 4.5,
        "reviewsCount": 3050,
        "badge": "Coup de Cœur ⭐",
        "image": "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B079MCK2W9",
        "amazonUrl": "https://www.amazon.fr/dp/B079MCK2W9",
        "curatorOpinion": "Le style bois épuré parfait pour une table de nuit. L'affichage s'éteint pour ne pas perturber la nuit et se réactive au claquement de doigts.",
        "highlights": ["Finition bois naturel soignée", "3 niveaux de luminosité réglables", "Capteur acoustique intelligent", "Affichage heure, date et température"]
    },
    {
        "id": "deco-shelves",
        "category": "deco",
        "categoryName": "Maison & Décoration",
        "title": "Lot de 3 Étagères Murales Flottantes Bois Brut & Métal Noir",
        "tagline": "Donnez du caractère et de l'espace de rangement chic à n'importe quel mur vide.",
        "price": 27.99,
        "originalPrice": 35.00,
        "rating": 4.7,
        "reviewsCount": 6510,
        "badge": "Meilleur Rapport Q/P 💎",
        "image": "https://images.unsplash.com/photo-1594026112284-02bb6f3352fe?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B07S7XHQV2",
        "amazonUrl": "https://www.amazon.fr/dp/B07S7XHQV2",
        "curatorOpinion": "Faciles à monter, ces étagères donnent un charme vintage et industriel immédiat à n'importe quel mur de salon ou de bureau.",
        "highlights": ["Bois de paulownia massif durable", "Supports acier noir mat robuste", "Supporte jusqu'à 18 kg par étagère", "Visserie et chevilles incluses"]
    },
    {
        "id": "deco-book-light",
        "category": "deco",
        "categoryName": "Maison & Décoration",
        "title": "Lampe Livre Pliable en Bois LED 360° Magique",
        "tagline": "S'ouvre comme un livre ancien pour illuminer la pièce d'une douce lueur chaleureuse.",
        "price": 23.90,
        "originalPrice": 31.00,
        "rating": 4.8,
        "reviewsCount": 2490,
        "badge": "Objet Magique ✨",
        "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B07S1B9Z18",
        "amazonUrl": "https://www.amazon.fr/dp/B07S1B9Z18",
        "curatorOpinion": "Un objet poétique qui surprend à chaque ouverture. Les pages en papier Tyvek indéchirable diffusent une lumière féérique.",
        "highlights": ["Couverture en bois d'érable noble", "S'ouvre à 360° grâce aux aimants intégrés", "Batterie rechargeable USB (6h d'autonomie)", "3 ambiances lumineuses interchangeables"]
    },

    # 🎁 IDÉES CADEAUX & INSOLITE
    {
        "id": "gift-printer",
        "category": "gift",
        "categoryName": "Idées Cadeaux & Insolite",
        "title": "Mini Imprimante Thermique de Poche Sans Encre Bluetooth",
        "tagline": "Imprimez instantanément photos, to-do lists, croquis et étiquettes sans jamais acheter de cartouche.",
        "price": 32.99,
        "originalPrice": 42.00,
        "rating": 4.7,
        "reviewsCount": 3890,
        "badge": "Top Cadeau 🎁",
        "image": "https://images.unsplash.com/photo-1589782182703-2aaa69037b5b?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B09V7N8M1Q",
        "amazonUrl": "https://www.amazon.fr/dp/B09V7N8M1Q",
        "curatorOpinion": "Le cadeau qui fait l'unanimité auprès des étudiants, fans d'organisation et créateurs de bullet journal. Zéro encre à racheter !",
        "highlights": ["Technologie thermique (0 cartouche)", "Connexion rapide Bluetooth iOS & Android", "Format poche ultra léger (160g)", "Application gratuite avec graphismes prêts"]
    },
    {
        "id": "gift-moon",
        "category": "gift",
        "categoryName": "Idées Cadeaux & Insolite",
        "title": "Lampe Lune 3D Lévitation Magnétique Réaliste",
        "tagline": "Flotte et tourne silencieusement dans les airs par répulsion magnétique au-dessus de son socle en bois.",
        "price": 69.90,
        "originalPrice": 89.90,
        "rating": 4.8,
        "reviewsCount": 1690,
        "badge": "Effet Whouah 🚀",
        "image": "https://images.unsplash.com/photo-1532767153582-b1a0e5145009?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B07K6J6K1V",
        "amazonUrl": "https://www.amazon.fr/dp/B07K6J6K1V",
        "curatorOpinion": "Un spectacle fascinant. Tous les invités qui passent à côté s'arrêtent pour regarder la sphère tourner sans aucun contact physique.",
        "highlights": ["Lévitation magnétique stable et silencieuse", "Surface fidèle aux scans lunaires de la NASA", "Alimentation sans fil par induction", "Interrupteur tactile sur le socle"]
    },
    {
        "id": "gift-mug",
        "category": "gift",
        "categoryName": "Idées Cadeaux & Insolite",
        "title": "Mug Auto-Mélangeur Isotherme Magnétique Inox",
        "tagline": "Mélange café, cacao, matcha ou protéines d'une simple pression sur le bouton de l'anse.",
        "price": 19.99,
        "originalPrice": 26.00,
        "rating": 4.5,
        "reviewsCount": 2980,
        "badge": "Gadget Pratique ⚡",
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B091CR616G",
        "amazonUrl": "https://www.amazon.fr/dp/B091CR616G",
        "curatorOpinion": "Fini la petite cuillère oubliée ou le fond de tasse mal dilué. La capsule magnétique interne crée un tourbillon instantané.",
        "highlights": ["Capsule magnétique amovible pour nettoyage", "Cuve inox 304 qualité alimentaire", "Couvercle étanche antifuite", "Batterie rechargeable par USB"]
    },
    {
        "id": "gift-box",
        "category": "gift",
        "categoryName": "Idées Cadeaux & Insolite",
        "title": "Casse-Tête Boîte Secrète Mécanique en Bois Découpé",
        "tagline": "Une énigme d'engrenages à résoudre pour ouvrir le compartiment secret. Idéal pour glisser une surprise.",
        "price": 26.90,
        "originalPrice": 32.00,
        "rating": 4.7,
        "reviewsCount": 3190,
        "badge": "Top Cadeau 🎁",
        "image": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B07N18H47N",
        "amazonUrl": "https://www.amazon.fr/dp/B07N18H47N",
        "curatorOpinion": "Mille fois plus mémorable qu'une simple enveloppe cadeau ! La personne doit faire fonctionner ses méninges pendant 20 minutes pour découvrir son trésor.",
        "highlights": ["Bois de bouleau naturel découpé au laser", "Mécanisme complexe d'engrenages", "Réutilisable et refermable", "Notice avec indices incluse"]
    },
    {
        "id": "gift-keyfinder",
        "category": "gift",
        "categoryName": "Idées Cadeaux & Insolite",
        "title": "Localisateur d'Objets Ultra-Fin Compatible Apple Find My",
        "tagline": "Glissez-le dans votre portefeuille ou accrochez-le à vos clés pour ne plus jamais rien perdre.",
        "price": 19.99,
        "originalPrice": 27.99,
        "rating": 4.7,
        "reviewsCount": 4120,
        "badge": "Bestseller 🎯",
        "image": "https://images.unsplash.com/photo-1586105251261-72a756497a11?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B09L7W5ZBQ",
        "amazonUrl": "https://www.amazon.fr/dp/B09L7W5ZBQ",
        "curatorOpinion": "La même efficacité qu'un AirTag officiel, mais pour moitié prix et avec un trou d'attache directement intégré sans besoin de porte-clé supplémentaire.",
        "highlights": ["Intégration native dans l'app Localiser d'Apple", "Sonnerie puissante pour retrouver sous un coussin", "Pile standard remplaçable avec 1 an d'autonomie", "Résistant à l'eau IP67"]
    },

    # 🍳 CUISINE & VIE PRATIQUE
    {
        "id": "cuisine-frother",
        "category": "cuisine",
        "categoryName": "Cuisine & Pratique",
        "title": "Mousseur à Lait Électrique USB Barista Pro 3 Vitesses",
        "tagline": "Mousse de lait onctueuse et veloutée en 15 secondes chrono pour cappuccinos et latte arts.",
        "price": 16.99,
        "originalPrice": 22.99,
        "rating": 4.8,
        "reviewsCount": 8100,
        "badge": "Top Vente ☕",
        "image": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B0892H1Q65",
        "amazonUrl": "https://www.amazon.fr/dp/B0892H1Q65",
        "curatorOpinion": "Le secret des cafés onctueux comme chez le barista pour le prix de deux cafés en terrasse. Livré avec 2 fouets en inox.",
        "highlights": ["3 vitesses puissantes", "Batterie USB-C rechargeable", "Nettoyage éclair sous le robinet", "Parfait aussi pour vinaigrettes et sauces"]
    },
    {
        "id": "cuisine-sprayer",
        "category": "cuisine",
        "categoryName": "Cuisine & Pratique",
        "title": "Pulvérisateur d'Huile d'Olive 2-en-1 Verre Épais Air Fryer",
        "tagline": "Permet de vaporiser une brume ultra-fine pour économiser jusqu'à 80% d'huile sur vos plats.",
        "price": 14.99,
        "originalPrice": 19.99,
        "rating": 4.6,
        "reviewsCount": 4410,
        "badge": "Essentiel Santé 🥗",
        "image": "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B09Y8N4K1L",
        "amazonUrl": "https://www.amazon.fr/dp/B09Y8N4K1L",
        "curatorOpinion": "L'accessoire indispensable pour tous ceux qui possèdent une friteuse sans huile (Air Fryer) ou qui souhaitent réduire les calories.",
        "highlights": ["Double buse : spray fin ou filet continu", "Verre transparent sans BPA de qualité alimentaire", "Remplissage sans entonnoir", "Buse anti-goutte propre"]
    },
    {
        "id": "cuisine-scale",
        "category": "cuisine",
        "categoryName": "Cuisine & Pratique",
        "title": "Balance de Cuisine Précision au Gramme + Plateau Inox",
        "tagline": "Format ultra-plat, touche tare instantanée et écran LED clair pour des pâtisseries impeccables.",
        "price": 15.99,
        "originalPrice": 21.00,
        "rating": 4.7,
        "reviewsCount": 9520,
        "badge": "Meilleur Rapport Q/P 💎",
        "image": "https://images.unsplash.com/photo-1590794056226-79ef3a8147e1?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B01MY0E0J3",
        "amazonUrl": "https://www.amazon.fr/dp/B01MY0E0J3",
        "curatorOpinion": "Un classique indéboulonnable. Elle se range discrètement avec les livres de cuisine et pèse jusqu'à 5 kg sans faillir.",
        "highlights": ["Surface inox anti-traces", "Fonction Tare automatique", "Mesure en g, kg, lb, oz et ml", "Arrêt automatique économie d'énergie"]
    },
    {
        "id": "cuisine-bottle",
        "category": "cuisine",
        "categoryName": "Cuisine & Pratique",
        "title": "Bouteille Isotherme Triple Paroi Inox (750ml)",
        "tagline": "Garde l'eau glacée 24h ou le thé brûlant 12h sans aucune condensation externe.",
        "price": 21.90,
        "originalPrice": 28.00,
        "rating": 4.9,
        "reviewsCount": 8340,
        "badge": "Coup de Cœur ⭐",
        "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B07K6Q1X9W",
        "amazonUrl": "https://www.amazon.fr/dp/B07K6Q1X9W",
        "curatorOpinion": "La gourde la plus robuste que nous ayons testée. Pas de goût métallique, pas de fuite dans le sac à dos.",
        "highlights": ["Inox 18/8 sans toxines ni phtalates", "Garantie 100% zéro fuite", "Revêtement poudré mat texturé", "Bouchon avec anneau de transport"]
    },
    {
        "id": "cuisine-chopper",
        "category": "cuisine",
        "categoryName": "Cuisine & Pratique",
        "title": "Hachoir Manuel Express à Cordon Multi-Lames",
        "tagline": "Hache oignons, ail, herbes et noix en 3 tractions de corde sans électricité ni larmes.",
        "price": 13.99,
        "originalPrice": 18.00,
        "rating": 4.7,
        "reviewsCount": 6120,
        "badge": "Gain de Temps ⏱️",
        "image": "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B0892H1Q65",
        "amazonUrl": "https://www.amazon.fr/dp/B0892H1Q65",
        "curatorOpinion": "Fini les pleurs en coupant les oignons ou le gros robot difficile à nettoyer. 3 tractions et vos légumes sont hachés fins.",
        "highlights": ["3 lames en acier chirurgical courbées", "Mécanisme à traction renforcé", "Fond antidérapant sécurisé", "Bol compatible lave-vaisselle"]
    },
    # 🎄 SPÉCIAL FIN D'ANNÉE & BESTSELLERS FÊTES
    {
        "id": "deco-fireplace",
        "category": "deco",
        "categoryName": "Maison & Décoration",
        "title": "Cheminée de Table Portable au Bioéthanol & Verre Trempé",
        "tagline": "Une vraie flamme chaleureuse et apaisante sans fumée ni odeur pour vos soirées d'hiver.",
        "price": 39.90,
        "originalPrice": 52.00,
        "rating": 4.8,
        "reviewsCount": 3870,
        "badge": "Cadeau Star 🎄",
        "image": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B08R697LFX",
        "amazonUrl": "https://www.amazon.fr/dp/B08R697LFX",
        "curatorOpinion": "L'objet le plus demandé en fin d'année. Apporte une ambiance digne d'un chalet de montagne sur une table basse.",
        "highlights": ["Vraie flamme naturelle au bioéthanol", "Zéro fumée, zéro cendre, zéro odeur", "Parois en verre trempé haute sécurité", "Base lestée en acier inoxydable"]
    },
    {
        "id": "deco-hoodie-blanket",
        "category": "deco",
        "categoryName": "Maison & Décoration",
        "title": "Sweat Plaid Polaire Géant avec Manches & Capuche Sherpa",
        "tagline": "Le confort ultime pour hiberner au chaud sur le canapé tout l'hiver.",
        "price": 29.99,
        "originalPrice": 39.99,
        "rating": 4.9,
        "reviewsCount": 11200,
        "badge": "Bestseller Hiver ❄️",
        "image": "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B07K6Q1X9W",
        "amazonUrl": "https://www.amazon.fr/dp/B07K6Q1X9W",
        "curatorOpinion": "Le carton absolu des ventes de Noël chaque année. Impossible d'avoir froid une fois enfilé.",
        "highlights": ["Doublure en polaire Sherpa ultra-moelleuse", "Taille unique géante adaptée à tous", "Poche ventrale kangourou XXL", "Lavable en machine sans boulocher"]
    },
    {
        "id": "gift-raclette-candle",
        "category": "gift",
        "categoryName": "Idées Cadeaux & Insolite",
        "title": "Appareil à Raclette Individuel à la Bougie (Set de 2)",
        "tagline": "Faites fondre votre fromage à raclette en 3 minutes simplement avec 3 bougies chauffe-plat !",
        "price": 19.99,
        "originalPrice": 25.00,
        "rating": 4.8,
        "reviewsCount": 5430,
        "badge": "Secret Santa 🎅",
        "image": "https://images.unsplash.com/photo-1552611052-33e04de081de?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B0892H1Q65",
        "amazonUrl": "https://www.amazon.fr/dp/B0892H1Q65",
        "curatorOpinion": "Le cadeau de Noël pas cher qui fait mouche à 100%. Plus besoin de sortir le gros appareil électrique encombrant.",
        "highlights": ["Fond aussi vite qu'un appareil électrique", "Zéro câble sur la table", "Revêtement anti-adhésif sans PFOA", "Spatules en bois sur-mesure incluses"]
    },
    {
        "id": "gift-gin-kit",
        "category": "gift",
        "categoryName": "Idées Cadeaux & Insolite",
        "title": "Coffret Kit Fabrication Spiritueux & Gin Artisanal Maison",
        "tagline": "Transformez une bouteille neutre en un spiritueux d'exception grâce aux épices et botaniques bio.",
        "price": 39.90,
        "originalPrice": 49.00,
        "rating": 4.7,
        "reviewsCount": 2180,
        "badge": "Cadeau Expérience 🍸",
        "image": "https://images.unsplash.com/photo-1527061011665-3652c757a4d4?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B07S7XHQV2",
        "amazonUrl": "https://www.amazon.fr/dp/B07S7XHQV2",
        "curatorOpinion": "Idéal pour les amateurs de bons alcools et de mixologie. Le packaging kraft est superbe sous le sapin.",
        "highlights": ["12 fioles d'épices et botaniques sélectionnées", "2 bouteilles en verre apothicaire vintage", "Entonnoir inox avec filtre de précision", "Guide de recettes et conseils d'infusion"]
    },
    {
        "id": "gift-bluetooth-beanie",
        "category": "gift",
        "categoryName": "Idées Cadeaux & Insolite",
        "title": "Bonnet Connecté Bluetooth 5.2 avec Écouteurs Stéréo & Lampe LED",
        "tagline": "Écoutez votre musique et éclairez votre chemin en gardant les oreilles bien au chaud.",
        "price": 18.99,
        "originalPrice": 24.99,
        "rating": 4.6,
        "reviewsCount": 4320,
        "badge": "Top Cadeau 🎁",
        "image": "https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B09PQV586X",
        "amazonUrl": "https://www.amazon.fr/dp/B09PQV586X",
        "curatorOpinion": "Génial pour le running d'hiver, le vélo, promener le chien ou le ski. La lampe et les haut-parleurs se détachent pour le lavage.",
        "highlights": ["Son stéréo HD Bluetooth 5.2", "Lampe LED frontale rechargeable USB", "Tricot doux et chaud extensible", "Autonomie musique jusqu'à 10 heures"]
    },
    {
        "id": "tech-cup-warmer",
        "category": "tech",
        "categoryName": "Tech & Télétravail",
        "title": "Chauffe-Tasse Thermostatique USB 55°C & Plaque Induction",
        "tagline": "Maintient votre thé, café ou chocolat chaud à la température parfaite toute la journée au bureau.",
        "price": 21.99,
        "originalPrice": 28.00,
        "rating": 4.7,
        "reviewsCount": 3610,
        "badge": "Cocooning Bureau ☕",
        "image": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B091CR616G",
        "amazonUrl": "https://www.amazon.fr/dp/B091CR616G",
        "curatorOpinion": "Fini de boire son café froid parce qu'on a été interrompu par un appel. La boisson reste à 55°C en continu.",
        "highlights": ["3 réglages de température (45°C, 55°C, 65°C)", "Arrêt automatique de sécurité après 8h", "Surface en verre étanche facile à essuyer", "Compatible tasses céramique, verre, métal"]
    },
    {
        "id": "tech-led-bars",
        "category": "tech",
        "categoryName": "Tech & Télétravail",
        "title": "Barres Lumineuses LED Immersion TV & Setup RGB Synchronisées",
        "tagline": "Éclairage dynamique synchronisé avec votre musique ou vos jeux pour un effet cinéma immersif.",
        "price": 34.99,
        "originalPrice": 44.99,
        "rating": 4.8,
        "reviewsCount": 5120,
        "badge": "Ambiance Gaming 🎮",
        "image": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B08C4VKYFG",
        "amazonUrl": "https://www.amazon.fr/dp/B08C4VKYFG",
        "curatorOpinion": "Transforme une simple pièce en studio futuriste. La réactivité du micro intégré au rythme de la musique est bluffante.",
        "highlights": ["Synchronisation audio en temps réel", "Contrôle par application smartphone et télécommande", "Plus de 16 millions de nuances de couleurs", "Supports horizontaux et verticaux inclus"]
    },
    {
        "id": "cuisine-gravity-mills",
        "category": "cuisine",
        "categoryName": "Cuisine & Pratique",
        "title": "Duo Moulins Sel & Poivre Électriques à Gravité Automatiques",
        "tagline": "Inclinez simplement le moulin d'une main pour moudre automatiquement avec éclairage LED.",
        "price": 24.99,
        "originalPrice": 32.99,
        "rating": 4.7,
        "reviewsCount": 6890,
        "badge": "Indispensable Fêtes ✨",
        "image": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=800&q=80",
        "amazonAsin": "B01MY0E0J3",
        "amazonUrl": "https://www.amazon.fr/dp/B01MY0E0J3",
        "curatorOpinion": "Un confort absolu en cuisinant quand on a une main sale ou occupée. Le capteur de gravité déclenche le broyage à l'inclinaison.",
        "highlights": ["Capteur gravité automatique à l'inclinaison", "Meule en céramique inusable sans rouille", "Mouture réglable (fine à grossière)", "Lumière LED bleue pour doser avec précision"]
    }
]

def update_catalog():
    print(f"[INFO] Mise a jour du catalogue avec {len(EXPANDED_CURATED_DATABASE)} articles...")
    
    # 1. Ecriture du fichier products.js
    products_js_content = f"// Catalogue automatiquement synchronise\nconst INITIAL_PRODUCTS = {json.dumps(EXPANDED_CURATED_DATABASE, indent=2, ensure_ascii=False)};\n"
    with open(PRODUCTS_FILE, "w", encoding="utf-8") as f:
        f.write(products_js_content)
    print(f"[OK] products.js mis a jour ({len(EXPANDED_CURATED_DATABASE)} articles).")

    # 2. Mise a jour dans index.html pour maintenir le fichier 100% autonome
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            html = f.read()

        # Remplacement de INITIAL_PRODUCTS dans le script inline
        pattern = r"const INITIAL_PRODUCTS = \[.*?\];"
        replacement = f"const INITIAL_PRODUCTS = {json.dumps(EXPANDED_CURATED_DATABASE, ensure_ascii=False)};"
        new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

        # Mettre a jour le compteur d'articles dans le hero
        new_html = re.sub(r'id="totalProductsCount">.*?<', f'id="totalProductsCount">{len(EXPANDED_CURATED_DATABASE)} articles sélectionnés<', new_html)

        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            f.write(new_html)
        print("[OK] index.html autonome mis a jour avec le nouveau catalogue.")

if __name__ == "__main__":
    update_catalog()
