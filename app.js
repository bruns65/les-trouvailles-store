// ==========================================
// LES TROUVAILLES - CURATED STORE & CO
// Moteur Multilingue (FR, EN, DE, ES, IT) & Affiliation Internationale
// ==========================================

const STORAGE_KEY_PRODUCTS = "curated_boutique_v16_tiktok_trends";
const STORAGE_KEY_AMAZON_TAG = "curated_boutique_amazon_tag";
const STORAGE_KEY_LANG = "curated_boutique_lang";
const DEFAULT_AMAZON_TAG = "lestrouvai0c0-21"; // Votre ID Partenaire officiel Amazon

// Domaines Amazon par langue
const AMAZON_DOMAINS = {
  fr: "https://www.amazon.fr",
  en: "https://www.amazon.co.uk",
  de: "https://www.amazon.de",
  es: "https://www.amazon.es",
  it: "https://www.amazon.it"
};

// Dictionnaire de traductions de l'interface
const I18N = {
  fr: {
    flag: "🇫🇷",
    code: "FR",
    name: "Français",
    taglineBadge: "Les 1% qui valent vraiment le coup • Zéro camelote",
    heroTitle: "Les pépites du web,<br><span class=\"text-transparent bg-clip-text bg-gradient-to-r from-amber-600 via-amber-700 to-stone-900\">sans le fouillis d'Amazon.</span>",
    heroDesc: "Arrêtez de scroller et de comparer pendant des heures. Nous analysons des milliers d'avis pour ne retenir que les objets indispensables, durables et notés plus de 4.5★ — livrés chez vous par Amazon au prix officiel.",
    countSuffix: "pépites sélectionnées",
    avgRating: "Moyenne clients : 4.8 / 5",
    primeBadge: "Livraison Prime & Retours 30j",
    topNotice: "Sélection 100% vérifiée • Livraison rapide & Retours gratuits Amazon",
    tabAll: "Tout voir",
    tabTech: "Tech & Télétravail",
    tabDeco: "Maison & Décoration",
    tabGift: "Idées Cadeaux & Insolite",
    tabCuisine: "Cuisine & Pratique",
    priceLabel: "Prix :",
    priceAll: "Tous",
    priceUnder20: "< 20 €",
    price2035: "20 € - 35 €",
    price35plus: "35 € +",
    sortFeatured: "Pertinence & Bestsellers",
    sortPriceAsc: "Prix : croissant",
    sortPriceDesc: "Prix : décroissant",
    sortRating: "Mieux notés d'abord",
    searchPlaceholder: "Rechercher une pépite, un gadget, un besoin...",
    seeAmazonBtn: "Voir l'offre sur Amazon",
    viewDetails: "Voir les détails & avis",
    primeAvailable: "Livraison Prime disponible",
    freeReturns: "Retours gratuits sous 30 jours",
    secureOrder: "Achat sécurisé traité directement par Amazon",
    orderAmazonBtn: "Commander au meilleur prix sur Amazon",
    curatorOpinionTitle: "L'avis de notre curateur",
    highlightsTitle: "Points forts vérifiés :",
    emptyTitle: "Aucun produit ne correspond à votre recherche",
    emptyDesc: "Essayez d'ajuster vos filtres ou de vider la barre de recherche.",
    resetFilters: "Réinitialiser les filtres",
    trustTitle: "Pourquoi faire confiance à notre sélection ?",
    trustDesc: "Nous appliquons une charte d'exigence stricte sur chaque pépite listée.",
    trust1Title: "Filtre anti-camelote",
    trust1Desc: "Seuls les produits notés plus de 4.4/5 avec des centaines d'avis clients vérifiés peuvent intégrer notre sélection.",
    trust2Title: "Garantie & Sécurité Amazon",
    trust2Desc: "Vous commandez directement sur Amazon avec vos avantages habituels : livraison Prime express, paiement crypté et retours gratuits 30 jours.",
    trust3Title: "Le meilleur prix officiel",
    trust3Desc: "Pas de surcoût ni de marge cachée. Vous payez exactement le tarif officiel et bénéficiez des réductions et ventes flash du jour.",
    disclaimer: "En tant que Partenaire Amazon, ce site réalise un bénéfice sur les achats remplissant les conditions requises."
  },
  en: {
    flag: "🇬🇧",
    code: "EN",
    name: "English",
    taglineBadge: "Top 1% vetted finds • Zero junk guaranteed",
    heroTitle: "The best finds on the web,<br><span class=\"text-transparent bg-clip-text bg-gradient-to-r from-amber-600 via-amber-700 to-stone-900\">without Amazon's clutter.</span>",
    heroDesc: "Stop endlessly scrolling and comparing. We test and filter thousands of reviews to keep only genuinely useful, durable items rated 4.5★+ — delivered to you by Amazon at the best official price.",
    countSuffix: "curated finds",
    avgRating: "Customer rating: 4.8 / 5",
    primeBadge: "Prime Delivery & 30-day Returns",
    topNotice: "100% Verified Selection • Fast Delivery & Free Amazon Returns",
    tabAll: "All Finds",
    tabTech: "Tech & Home Office",
    tabDeco: "Home & Living",
    tabGift: "Unique Gift Ideas",
    tabCuisine: "Kitchen & Everyday",
    priceLabel: "Price:",
    priceAll: "All",
    priceUnder20: "< 20 €",
    price2035: "20 € - 35 €",
    price35plus: "35 € +",
    sortFeatured: "Popularity & Bestsellers",
    sortPriceAsc: "Price: Low to High",
    sortPriceDesc: "Price: High to Low",
    sortRating: "Highest Rated",
    searchPlaceholder: "Search for a gem, gadget, gift idea...",
    seeAmazonBtn: "View Deal on Amazon",
    viewDetails: "View details & reviews",
    primeAvailable: "Prime delivery available",
    freeReturns: "Free 30-day returns",
    secureOrder: "Secure checkout processed directly by Amazon",
    orderAmazonBtn: "Order at best price on Amazon",
    curatorOpinionTitle: "Curator's Note",
    highlightsTitle: "Verified Highlights:",
    emptyTitle: "No products match your search",
    emptyDesc: "Try adjusting your filters or clearing the search bar.",
    resetFilters: "Reset filters",
    trustTitle: "Why trust our curated selection?",
    trustDesc: "We apply a strict quality filter to every single product listed.",
    trust1Title: "Zero Junk Filter",
    trust1Desc: "Only items rated 4.4/5+ with hundreds of verified reviews make our curated list.",
    trust2Title: "Amazon Guarantee & Safety",
    trust2Desc: "You buy directly from Amazon with your usual benefits: fast Prime shipping, secure payments and easy 30-day returns.",
    trust3Title: "Best Official Price",
    trust3Desc: "No markups or hidden fees. You get the exact official Amazon price and enjoy daily lightning deals.",
    disclaimer: "As an Amazon Associate, this site earns from qualifying purchases."
  },
  de: {
    flag: "🇩🇪",
    code: "DE",
    name: "Deutsch",
    taglineBadge: "Die besten 1% Fundstücke • Garantiert kein Schrott",
    heroTitle: "Die besten Fundstücke des Webs,<br><span class=\"text-transparent bg-clip-text bg-gradient-to-r from-amber-600 via-amber-700 to-stone-900\">ohne das Amazon-Chaos.</span>",
    heroDesc: "Schluss mit stundenlangem Suchen. Wir analysieren tausende Bewertungen, um nur nützliche, langlebige Produkte mit 4.5★+ auszuwählen — geliefert von Amazon zum offiziellen Bestpreis.",
    countSuffix: "geprüfte Fundstücke",
    avgRating: "Kundenbewertung: 4.8 / 5",
    primeBadge: "Prime-Lieferung & 30 Tage Rückgabe",
    topNotice: "100% geprüfte Auswahl • Schnelle Lieferung & kostenlose Rücksendung",
    tabAll: "Alle ansehen",
    tabTech: "Tech & Homeoffice",
    tabDeco: "Wohnen & Dekoration",
    tabGift: "Geschenkideen & Gadgets",
    tabCuisine: "Küche & Haushalt",
    priceLabel: "Preis:",
    priceAll: "Alle",
    priceUnder20: "< 20 €",
    price2035: "20 € - 35 €",
    price35plus: "35 € +",
    sortFeatured: "Beliebtheit & Bestseller",
    sortPriceAsc: "Preis: aufsteigend",
    sortPriceDesc: "Preis: absteigend",
    sortRating: "Bestbewertet zuerst",
    searchPlaceholder: "Nach Gadget, Geschenk oder Produkt suchen...",
    seeAmazonBtn: "Auf Amazon ansehen",
    viewDetails: "Details & Bewertungen",
    primeAvailable: "Prime-Lieferung verfügbar",
    freeReturns: "Kostenlose 30-Tage-Rückgabe",
    secureOrder: "Sichere Bezahlung direkt über Amazon",
    orderAmazonBtn: "Zum Bestpreis bei Amazon bestellen",
    curatorOpinionTitle: "Kuratoren-Fazit",
    highlightsTitle: "Geprüfte Highlights:",
    emptyTitle: "Keine Produkte gefunden",
    emptyDesc: "Versuchen Sie, Ihre Filter anzupassen oder das Suchfeld zu leeren.",
    resetFilters: "Filter zurücksetzen",
    trustTitle: "Warum unserer Auswahl vertrauen?",
    trustDesc: "Wir wenden strenge Qualitätskriterien auf jedes empfohlene Produkt an.",
    trust1Title: "Strikter Qualitätsfilter",
    trust1Desc: "Nur Produkte mit mindestens 4.4/5 Sternen und hunderten Kundenbewertungen werden aufgenommen.",
    trust2Title: "Amazon Garantie & Schutz",
    trust2Desc: "Sie bestellen direkt über Amazon mit Prime-Versand, sicherem Bezahlen und unkomplizierter Rückgabe.",
    trust3Title: "Bester offizieller Preis",
    trust3Desc: "Keine versteckten Aufschläge. Sie zahlen den offiziellen Amazon-Preis inklusive aller Rabatte.",
    disclaimer: "Als Amazon-Partner verdiene ich an qualifizierten Verkäufen."
  },
  es: {
    flag: "🇪🇸",
    code: "ES",
    name: "Español",
    taglineBadge: "El 1% que merece la pena • Cero artículos mediocres",
    heroTitle: "Las mejores joyas de la web,<br><span class=\"text-transparent bg-clip-text bg-gradient-to-r from-amber-600 via-amber-700 to-stone-900\">sin el caos de Amazon.</span>",
    heroDesc: "Deja de buscar y comparar durante horas. Analizamos miles de reseñas para quedarnos solo con objetos indispensables y valorados en más de 4.5★ — con envío seguro por Amazon al mejor precio oficial.",
    countSuffix: "artículos seleccionados",
    avgRating: "Valoración media: 4.8 / 5",
    primeBadge: "Envío Prime y Devolución 30 días",
    topNotice: "Selección 100% verificada • Envío rápido y devoluciones gratuitas en Amazon",
    tabAll: "Ver todo",
    tabTech: "Tech y Teletrabajo",
    tabDeco: "Hogar y Decoración",
    tabGift: "Ideas de Regalo y Curiosidades",
    tabCuisine: "Cocina y Práctico",
    priceLabel: "Precio:",
    priceAll: "Todos",
    priceUnder20: "< 20 €",
    price2035: "20 € - 35 €",
    price35plus: "35 € +",
    sortFeatured: "Relevancia y Bestsellers",
    sortPriceAsc: "Precio: menor a mayor",
    sortPriceDesc: "Precio: mayor a menor",
    sortRating: "Mejor valorados",
    searchPlaceholder: "Buscar un producto, gadget, idea...",
    seeAmazonBtn: "Ver oferta en Amazon",
    viewDetails: "Ver detalles y opiniones",
    primeAvailable: "Envío Prime disponible",
    freeReturns: "Devoluciones gratis en 30 días",
    secureOrder: "Compra segura gestionada directamente por Amazon",
    orderAmazonBtn: "Comprar al mejor precio en Amazon",
    curatorOpinionTitle: "Opinión del Curador",
    highlightsTitle: "Puntos clave verificados:",
    emptyTitle: "No se encontraron productos",
    emptyDesc: "Prueba a cambiar tus filtros o vaciar la barra de búsqueda.",
    resetFilters: "Restablecer filtros",
    trustTitle: "¿Por qué confiar en nuestra selección?",
    trustDesc: "Aplicamos criterios estrictos de calidad a cada producto seleccionado.",
    trust1Title: "Filtro anti-chascos",
    trust1Desc: "Solo productos con más de 4.4/5 estrellas y cientos de opiniones reales entran en la tienda.",
    trust2Title: "Garantía y Seguridad Amazon",
    trust2Desc: "Compras directamente en Amazon con envío Prime rápido, pago cifrado y devoluciones sin complicaciones.",
    trust3Title: "Mejor precio oficial",
    trust3Desc: "Sin sobrecostes ni márgenes ocultos. Pagas el precio oficial exacto de Amazon.",
    disclaimer: "En calidad de Afiliado de Amazon, obtengo ingresos por las compras adscritas que cumplen los requisitos aplicables."
  },
  it: {
    flag: "🇮🇹",
    code: "IT",
    name: "Italiano",
    taglineBadge: "L'1% che vale davvero • Zero prodotti scadenti",
    heroTitle: "Le migliori scoperte del web,<br><span class=\"text-transparent bg-clip-text bg-gradient-to-r from-amber-600 via-amber-700 to-stone-900\">senza il caos di Amazon.</span>",
    heroDesc: "Smetti di scorrere e confrontare per ore. Analizziamo migliaia di recensioni per scegliere solo oggetti indispensabili e valutati oltre 4.5★ — consegnati da Amazon al miglior prezzo ufficiale.",
    countSuffix: "prodotti selezionati",
    avgRating: "Valutazione clienti: 4.8 / 5",
    primeBadge: "Spedizione Prime & Resi 30 giorni",
    topNotice: "Selezione 100% verificata • Spedizione veloce e resi gratuiti su Amazon",
    tabAll: "Mostra tutto",
    tabTech: "Tech e Smart Working",
    tabDeco: "Casa e Arredamento",
    tabGift: "Idee Regalo e Curiosità",
    tabCuisine: "Cucina e Pratico",
    priceLabel: "Prezzo:",
    priceAll: "Tutti",
    priceUnder20: "< 20 €",
    price2035: "20 € - 35 €",
    price35plus: "35 € +",
    sortFeatured: "Popolarità e Bestseller",
    sortPriceAsc: "Prezzo: dal più basso",
    sortPriceDesc: "Prezzo: dal più alto",
    sortRating: "Valutazione più alta",
    searchPlaceholder: "Cerca un gadget, un'idea regalo...",
    seeAmazonBtn: "Vedi offerta su Amazon",
    viewDetails: "Vedi dettagli e recensioni",
    primeAvailable: "Spedizione Prime disponibile",
    freeReturns: "Resi gratuiti entro 30 giorni",
    secureOrder: "Acquisto sicuro gestito direttamente da Amazon",
    orderAmazonBtn: "Ordina al miglior prezzo su Amazon",
    curatorOpinionTitle: "Il parere del Curatore",
    highlightsTitle: "Punti di forza verificati:",
    emptyTitle: "Nessun prodotto trovato",
    emptyDesc: "Prova a modificare i filtri o cancella la barra di ricerca.",
    resetFilters: "Reimposta filtri",
    trustTitle: "Perché fidarsi della nostra selezione?",
    trustDesc: "Applichiamo standard rigorosi a ogni singolo prodotto consigliato.",
    trust1Title: "Filtro anti-delusioni",
    trust1Desc: "Solo prodotti con almeno 4.4/5 stelle e centinaia di recensioni verificate entrano nel catalogo.",
    trust2Title: "Garanzia & Sicurezza Amazon",
    trust2Desc: "Acquisti direttamente su Amazon con spedizione Prime, pagamento sicuro e reso facile entro 30 giorni.",
    trust3Title: "Miglior prezzo ufficiale",
    trust3Desc: "Nessun costo nascosto. Paghi il prezzo ufficiale Amazon e approfitti delle offerte lampo.",
    disclaimer: "In qualità di Affiliato Amazon, ricevo un guadagno per ciascun acquisto idoneo."
  }
};

// Traductions des noms de catégories
const CATEGORY_NAMES_I18N = {
  tech: { fr: "Tech & Télétravail", en: "Tech & Home Office", de: "Tech & Homeoffice", es: "Tech y Teletrabajo", it: "Tech e Smart Working" },
  deco: { fr: "Maison & Décoration", en: "Home & Living", de: "Wohnen & Dekoration", es: "Hogar y Decoración", it: "Casa e Arredamento" },
  gift: { fr: "Idées Cadeaux & Insolite", en: "Unique Gift Ideas", de: "Geschenkideen & Gadgets", es: "Ideas de Regalo y Curiosidades", it: "Idee Regalo e Curiosità" },
  cuisine: { fr: "Cuisine & Pratique", en: "Kitchen & Everyday", de: "Küche & Haushalt", es: "Cocina y Práctico", it: "Cucina e Pratico" }
};

// État global de l'application
let state = {
  products: [],
  activeCategory: "all",
  activePrice: "all",
  searchQuery: "",
  sortBy: "featured",
  amazonTag: DEFAULT_AMAZON_TAG,
  lang: "fr"
};

// Initialisation au chargement
document.addEventListener("DOMContentLoaded", () => {
  loadData();
  setupEventListeners();
  applyLanguage(state.lang);
  lucide.createIcons();
});

function detectBrowserLanguage() {
  const nav = (navigator.language || navigator.userLanguage || "fr").toLowerCase();
  if (nav.startsWith("de")) return "de";
  if (nav.startsWith("es")) return "es";
  if (nav.startsWith("it")) return "it";
  if (nav.startsWith("en")) return "en";
  return "fr";
}

// 1. Chargement des données (LocalStorage ou catalogue initial)
function loadData() {
  const savedLang = localStorage.getItem(STORAGE_KEY_LANG);
  if (savedLang && I18N[savedLang]) {
    state.lang = savedLang;
  } else {
    // Calage automatique par rapport à l'acheteur
    state.lang = detectBrowserLanguage();
  }

  const savedTag = localStorage.getItem(STORAGE_KEY_AMAZON_TAG);
  if (savedTag) {
    state.amazonTag = savedTag;
  } else {
    state.amazonTag = DEFAULT_AMAZON_TAG;
    localStorage.setItem(STORAGE_KEY_AMAZON_TAG, DEFAULT_AMAZON_TAG);
  }
  updateTagDisplay();

  // Toujours synchroniser avec le catalogue officiel à jour
  state.products = [...INITIAL_PRODUCTS];
  saveProducts();
}

function saveProducts() {
  localStorage.setItem(STORAGE_KEY_PRODUCTS, JSON.stringify(state.products));
}

// 2. Formatage des liens Amazon avec le Tag affilié et le domaine du pays actif
function buildAffiliateUrl(rawUrlOrAsin) {
  const tag = state.amazonTag || DEFAULT_AMAZON_TAG;
  const baseDomain = AMAZON_DOMAINS[state.lang] || AMAZON_DOMAINS.fr;

  if (!rawUrlOrAsin) return `${baseDomain}/?tag=${encodeURIComponent(tag)}`;

  // Cas 1 : URL complète (recherche ou produit direct)
  if (rawUrlOrAsin.startsWith("http://") || rawUrlOrAsin.startsWith("https://")) {
    try {
      const url = new URL(rawUrlOrAsin);
      const targetBase = new URL(baseDomain);
      url.protocol = targetBase.protocol;
      url.host = targetBase.host;
      url.searchParams.set("tag", tag);
      return url.toString();
    } catch (e) {
      // fallback
    }
  }

  // Cas 2 : ASIN pur (ex: B076F3C4XP)
  const asinMatch = rawUrlOrAsin.match(/\b([B0-9][A-Z0-9]{9})\b/i);
  if (asinMatch) {
    return `${baseDomain}/dp/${asinMatch[1]}?tag=${encodeURIComponent(tag)}`;
  }

  // Cas 3 : Mots-clés de recherche
  return `${baseDomain}/s?k=${encodeURIComponent(rawUrlOrAsin)}&tag=${encodeURIComponent(tag)}`;
}

// 3. Application de la langue dans le DOM
function applyLanguage(lang) {
  if (!I18N[lang]) lang = "fr";
  state.lang = lang;
  localStorage.setItem(STORAGE_KEY_LANG, lang);
  const t = I18N[lang];

  // Sélecteur de langue UI
  const currentLangBtn = document.getElementById("currentLangDisplay");
  if (currentLangBtn) {
    currentLangBtn.innerHTML = `<span>${t.flag}</span> <span class="font-bold uppercase">${t.code}</span>`;
  }

  // Header & Top notice
  const topNoticeEl = document.getElementById("topNoticeText");
  if (topNoticeEl) topNoticeEl.textContent = t.topNotice;

  // Hero Section
  const heroBadgeEl = document.getElementById("heroBadgeText");
  if (heroBadgeEl) heroBadgeEl.textContent = t.taglineBadge;

  const heroTitleEl = document.getElementById("heroTitle");
  if (heroTitleEl) heroTitleEl.innerHTML = t.heroTitle;

  const heroDescEl = document.getElementById("heroDesc");
  if (heroDescEl) heroDescEl.textContent = t.heroDesc;

  const primeBadgeEl = document.getElementById("primeBadgeText");
  if (primeBadgeEl) primeBadgeEl.textContent = t.primeBadge;

  // Onglets Catégories
  const tabAllSpan = document.querySelector('.category-tab[data-category="all"] span:first-of-type');
  if (tabAllSpan) tabAllSpan.textContent = t.tabAll;

  const tabTechSpan = document.querySelector('.category-tab[data-category="tech"] span:first-of-type');
  if (tabTechSpan) tabTechSpan.textContent = t.tabTech;

  const tabDecoSpan = document.querySelector('.category-tab[data-category="deco"] span:first-of-type');
  if (tabDecoSpan) tabDecoSpan.textContent = t.tabDeco;

  const tabGiftSpan = document.querySelector('.category-tab[data-category="gift"] span:first-of-type');
  if (tabGiftSpan) tabGiftSpan.textContent = t.tabGift;

  const tabCuisineSpan = document.querySelector('.category-tab[data-category="cuisine"] span:first-of-type');
  if (tabCuisineSpan) tabCuisineSpan.textContent = t.tabCuisine;

  // Filtres Prix
  const priceLabelEl = document.getElementById("priceFilterLabel");
  if (priceLabelEl) priceLabelEl.textContent = t.priceLabel;

  const priceAllBtn = document.querySelector('.price-btn[data-price="all"]');
  if (priceAllBtn) priceAllBtn.textContent = t.priceAll;

  // Search input placeholders
  const searchInput = document.getElementById("searchInput");
  if (searchInput) searchInput.placeholder = t.searchPlaceholder;
  const mobileSearchInput = document.getElementById("mobileSearchInput");
  if (mobileSearchInput) mobileSearchInput.placeholder = t.searchPlaceholder;

  // Section Réassurance (Trust)
  const trustTitleEl = document.getElementById("trustSectionTitle");
  if (trustTitleEl) trustTitleEl.textContent = t.trustTitle;
  const trustDescEl = document.getElementById("trustSectionDesc");
  if (trustDescEl) trustDescEl.textContent = t.trustDesc;

  const trust1T = document.getElementById("trust1Title");
  if (trust1T) trust1T.textContent = t.trust1Title;
  const trust1D = document.getElementById("trust1Desc");
  if (trust1D) trust1D.textContent = t.trust1Desc;

  const trust2T = document.getElementById("trust2Title");
  if (trust2T) trust2T.textContent = t.trust2Title;
  const trust2D = document.getElementById("trust2Desc");
  if (trust2D) trust2D.textContent = t.trust2Desc;

  const trust3T = document.getElementById("trust3Title");
  if (trust3T) trust3T.textContent = t.trust3Title;
  const trust3D = document.getElementById("trust3Desc");
  if (trust3D) trust3D.textContent = t.trust3Desc;

  // Disclaimer légal
  const disclaimerEl = document.getElementById("affiliateDisclaimerText");
  if (disclaimerEl) disclaimerEl.textContent = t.disclaimer;

  renderCounters();
  renderProducts();
  lucide.createIcons();
}

// 4. Rendu des compteurs dans les onglets
function renderCounters() {
  const counts = {
    all: state.products.length,
    tech: state.products.filter(p => p.category === "tech").length,
    deco: state.products.filter(p => p.category === "deco").length,
    gift: state.products.filter(p => p.category === "gift").length,
    cuisine: state.products.filter(p => p.category === "cuisine").length,
  };

  const countAll = document.getElementById("count-all");
  if (countAll) countAll.textContent = counts.all;
  const countTech = document.getElementById("count-tech");
  if (countTech) countTech.textContent = counts.tech;
  const countDeco = document.getElementById("count-deco");
  if (countDeco) countDeco.textContent = counts.deco;
  const countGift = document.getElementById("count-gift");
  if (countGift) countGift.textContent = counts.gift;
  const countCuisine = document.getElementById("count-cuisine");
  if (countCuisine) countCuisine.textContent = counts.cuisine;

  const totalCountEl = document.getElementById("totalProductsCount");
  if (totalCountEl) {
    const t = I18N[state.lang] || I18N.fr;
    totalCountEl.textContent = `${counts.all} ${t.countSuffix}`;
  }
}

// 5. Filtrage et tri des produits
function getFilteredProducts() {
  return state.products
    .filter(product => {
      if (state.activeCategory !== "all" && product.category !== state.activeCategory) {
        return false;
      }
      
      if (state.activePrice === "under-20" && product.price >= 20) return false;
      if (state.activePrice === "20-35" && (product.price < 20 || product.price > 35)) return false;
      if (state.activePrice === "35-plus" && product.price <= 35) return false;

      if (state.searchQuery.trim() !== "") {
        const query = state.searchQuery.toLowerCase();
        const searchable = [
          product.title,
          product.tagline,
          product.curatorOpinion || "",
          (product.highlights || []).join(" "),
          product.categoryName || ""
        ].join(" ").toLowerCase();

        if (!searchable.includes(query)) return false;
      }

      return true;
    })
    .sort((a, b) => {
      if (state.sortBy === "price-asc") return a.price - b.price;
      if (state.sortBy === "price-desc") return b.price - a.price;
      if (state.sortBy === "rating") return b.rating - a.rating;
      return 0;
    });
}

// 6. Rendu de la grille des produits
function renderProducts() {
  const grid = document.getElementById("productGrid");
  const emptyState = document.getElementById("emptyState");
  const resultsCount = document.getElementById("resultsCount");
  const filtered = getFilteredProducts();
  const t = I18N[state.lang] || I18N.fr;

  if (resultsCount) {
    resultsCount.textContent = `${filtered.length} ${t.countSuffix}`;
  }

  if (filtered.length === 0) {
    grid.innerHTML = "";
    emptyState.classList.remove("hidden");
    return;
  }

  emptyState.classList.add("hidden");

  grid.innerHTML = filtered.map(product => {
    const affiliateUrl = buildAffiliateUrl(product.amazonUrl || product.amazonAsin);
    const hasDiscount = product.originalPrice && product.originalPrice > product.price;
    const discountPercent = hasDiscount 
      ? Math.round(((product.originalPrice - product.price) / product.originalPrice) * 100) 
      : 0;

    const catName = (CATEGORY_NAMES_I18N[product.category] && CATEGORY_NAMES_I18N[product.category][state.lang]) 
      || product.categoryName;

    return `
      <div class="bg-white rounded-2xl border border-stone-200/90 overflow-hidden shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col group relative">
        
        <!-- Direct Amazon Clickable Header (Image + Badges) -->
        <a 
          href="${affiliateUrl}" 
          target="_blank" 
          rel="noopener noreferrer" 
          class="relative aspect-square overflow-hidden bg-stone-100 block cursor-pointer"
          title="${escapeHtml(product.title)} - ${t.seeAmazonBtn}"
        >
          <img 
            src="${product.image}" 
            alt="${escapeHtml(product.title)}" 
            loading="lazy" 
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          >

          <!-- Top Badge -->
          ${product.badge ? `
            <div class="absolute top-3 left-3 bg-stone-900/90 backdrop-blur-md text-amber-300 text-[11px] font-bold px-2.5 py-1 rounded-full shadow-sm flex items-center gap-1">
              <span>${escapeHtml(product.badge)}</span>
            </div>
          ` : ""}

          <!-- Discount Pill -->
          ${hasDiscount ? `
            <div class="absolute top-3 right-3 bg-rose-600 text-white text-[11px] font-extrabold px-2 py-0.5 rounded-full shadow-sm">
              -${discountPercent}%
            </div>
          ` : ""}

          <!-- Immediate Buy Overlay on Hover -->
          <div class="absolute inset-0 bg-stone-900/25 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center p-4">
            <span class="bg-amber-500 hover:bg-amber-400 text-stone-950 text-xs font-black px-4 py-2.5 rounded-full shadow-xl flex items-center gap-2 transform translate-y-2 group-hover:translate-y-0 transition-all scale-100 group-hover:scale-105">
              <span>${t.seeAmazonBtn}</span>
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </span>
          </div>
        </a>

        <!-- Content -->
        <div class="p-5 flex flex-col flex-1">
          <!-- Category & Rating -->
          <div class="flex items-center justify-between text-xs text-stone-500 mb-2">
            <span class="font-bold text-amber-700 uppercase tracking-wider text-[10px] bg-amber-50 px-2 py-0.5 rounded">
              ${escapeHtml(catName)}
            </span>
            <div class="flex items-center gap-1 text-stone-700 font-semibold">
              <i data-lucide="star" class="w-3.5 h-3.5 fill-amber-400 text-amber-400"></i>
              <span>${product.rating.toFixed(1)}</span>
              <span class="text-stone-400 text-[11px]">(${product.reviewsCount.toLocaleString()})</span>
            </div>
          </div>

          <!-- Title (Direct Click to Amazon) -->
          <a 
            href="${affiliateUrl}" 
            target="_blank" 
            rel="noopener noreferrer"
            class="font-bold text-stone-900 text-sm leading-snug line-clamp-2 hover:text-amber-600 transition-colors cursor-pointer mb-2 block"
          >
            ${escapeHtml(product.title)}
          </a>

          <!-- Tagline -->
          <p class="text-xs text-stone-500 line-clamp-2 leading-relaxed mb-4">
            ${escapeHtml(product.tagline)}
          </p>

          <!-- Price & Buy Block -->
          <div class="mt-auto pt-3 border-t border-stone-100">
            <!-- Official Amazon Coupon Badge if present -->
            ${product.coupon ? `
              <div class="mb-2.5 bg-emerald-50 border border-emerald-200/80 rounded-lg p-2 flex items-center justify-between text-[11px] text-emerald-800 font-semibold shadow-xs">
                <span class="flex items-center gap-1.5">
                  <i data-lucide="ticket" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i>
                  <span>${escapeHtml(product.coupon)}</span>
                </span>
                <span class="bg-emerald-600 text-white text-[9px] font-black px-1.5 py-0.5 rounded tracking-wide uppercase shrink-0">Actif</span>
              </div>
            ` : ""}

            <div class="flex items-baseline justify-between mb-3">
              <div class="flex items-baseline gap-2">
                <span class="text-lg font-extrabold text-stone-900">${product.price.toFixed(2)} €</span>
                ${hasDiscount ? `
                  <span class="text-xs text-stone-400 line-through">${product.originalPrice.toFixed(2)} €</span>
                ` : ""}
              </div>
              <span class="inline-flex items-center gap-1 text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full">
                <i data-lucide="truck" class="w-3 h-3"></i> Prime
              </span>
            </div>

            <!-- Amazon Direct Buy Button -->
            <a 
              href="${affiliateUrl}" 
              target="_blank" 
              rel="noopener noreferrer" 
              class="w-full py-2.5 px-4 bg-amber-500 hover:bg-amber-600 text-stone-950 font-black text-xs rounded-xl flex items-center justify-center gap-2 transition-all duration-200 shadow-sm hover:shadow hover:scale-[1.01] active:scale-[0.99]"
            >
              <span>${t.seeAmazonBtn}</span>
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </a>

            <!-- Optional quick view details trigger -->
            <button 
              type="button"
              onclick="openProductModal('${product.id}')"
              class="w-full mt-2 py-1 text-[11px] text-stone-400 hover:text-stone-700 font-medium transition-colors flex items-center justify-center gap-1"
            >
              <i data-lucide="info" class="w-3 h-3"></i>
              <span>${t.viewDetails}</span>
            </button>
          </div>

        </div>
      </div>
    `;
  }).join("");

  lucide.createIcons();
}

// 7. Modal de détail du produit
window.openProductModal = function(productId) {
  const product = state.products.find(p => p.id === productId);
  if (!product) return;

  const modal = document.getElementById("productModal");
  const content = document.getElementById("modalContent");
  const affiliateUrl = buildAffiliateUrl(product.amazonUrl || product.amazonAsin);
  const t = I18N[state.lang] || I18N.fr;

  const catName = (CATEGORY_NAMES_I18N[product.category] && CATEGORY_NAMES_I18N[product.category][state.lang]) 
    || product.categoryName;

  content.innerHTML = `
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
      <!-- Image column -->
      <div class="relative rounded-2xl overflow-hidden bg-stone-100 aspect-square">
        <img src="${product.image}" alt="${escapeHtml(product.title)}" class="w-full h-full object-cover">
        ${product.badge ? `
          <div class="absolute top-3 left-3 bg-stone-900/90 text-amber-300 text-xs font-bold px-3 py-1 rounded-full shadow">
            ${escapeHtml(product.badge)}
          </div>
        ` : ""}
      </div>

      <!-- Information column -->
      <div class="flex flex-col">
        <div class="flex items-center gap-2 text-xs mb-2">
          <span class="font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded-full uppercase tracking-wider text-[10px]">
            ${escapeHtml(catName)}
          </span>
          <div class="flex items-center gap-1 font-bold text-stone-800">
            <i data-lucide="star" class="w-4 h-4 fill-amber-400 text-amber-400"></i>
            <span>${product.rating.toFixed(1)} / 5</span>
            <span class="text-stone-400 font-normal">(${product.reviewsCount.toLocaleString()})</span>
          </div>
        </div>

        <h2 class="text-xl font-extrabold text-stone-900 leading-snug mb-3">
          ${escapeHtml(product.title)}
        </h2>

        <p class="text-sm text-stone-600 leading-relaxed mb-4">
          ${escapeHtml(product.tagline)}
        </p>

        <!-- Curator's Note -->
        ${product.curatorOpinion ? `
          <div class="bg-amber-50/70 border-l-4 border-amber-500 p-3.5 rounded-r-xl mb-4">
            <h4 class="text-xs font-bold text-amber-900 uppercase tracking-wider mb-1 flex items-center gap-1">
              <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-600"></i>
              ${t.curatorOpinionTitle}
            </h4>
            <p class="text-xs text-amber-800 leading-relaxed italic">
              "${escapeHtml(product.curatorOpinion)}"
            </p>
          </div>
        ` : ""}

        <!-- Highlights -->
        ${product.highlights && product.highlights.length > 0 ? `
          <div class="mb-5">
            <h4 class="text-xs font-bold text-stone-800 uppercase tracking-wider mb-2">${t.highlightsTitle}</h4>
            <ul class="space-y-1.5 text-xs text-stone-600">
              ${product.highlights.map(h => `
                <li class="flex items-start gap-2">
                  <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
                  <span>${escapeHtml(h)}</span>
                </li>
              `).join("")}
            </ul>
          </div>
        ` : ""}

        <!-- Price & Action -->
        <div class="mt-auto pt-4 border-t border-stone-200">
          ${product.coupon ? `
            <div class="mb-3 bg-emerald-50 border border-emerald-200 rounded-xl p-3 flex items-center justify-between text-xs text-emerald-900 font-bold shadow-xs">
              <span class="flex items-center gap-2">
                <i data-lucide="ticket" class="w-4 h-4 text-emerald-600 shrink-0"></i>
                <span>${escapeHtml(product.coupon)}</span>
              </span>
              <span class="bg-emerald-600 text-white text-[10px] font-black px-2 py-0.5 rounded tracking-wide uppercase shrink-0">Code Actif</span>
            </div>
          ` : ""}

          <div class="flex items-baseline justify-between mb-3">
            <div>
              <span class="text-2xl font-extrabold text-stone-900">${product.price.toFixed(2)} €</span>
              ${product.originalPrice ? `
                <span class="text-sm text-stone-400 line-through ml-2">${product.originalPrice.toFixed(2)} €</span>
              ` : ""}
            </div>
            <div class="text-right">
              <span class="text-xs font-bold text-emerald-700 flex items-center gap-1">
                <i data-lucide="truck" class="w-3.5 h-3.5"></i> ${t.primeAvailable}
              </span>
              <span class="text-[10px] text-stone-400 block">${t.freeReturns}</span>
            </div>
          </div>

          <a 
            href="${affiliateUrl}" 
            target="_blank" 
            rel="noopener noreferrer" 
            class="w-full py-3.5 px-6 bg-amber-500 hover:bg-amber-600 text-stone-950 font-bold text-sm rounded-xl flex items-center justify-center gap-2 shadow-md hover:shadow-lg transition-all"
          >
            <span>${t.orderAmazonBtn}</span>
            <i data-lucide="external-link" class="w-4 h-4"></i>
          </a>

          <p class="text-center text-[10px] text-stone-400 mt-2">
            ${t.secureOrder}
          </p>
        </div>
      </div>
    </div>
  `;

  modal.classList.remove("hidden");
  document.body.classList.add("overflow-hidden");
  lucide.createIcons();
};

function closeProductModal() {
  const modal = document.getElementById("productModal");
  modal.classList.add("hidden");
  document.body.classList.remove("overflow-hidden");
}

// 8. Gestion des Événements & Filtres
function setupEventListeners() {
  // Sélecteur de langue Dropdown
  const langDropdownBtn = document.getElementById("langDropdownBtn");
  const langDropdownMenu = document.getElementById("langDropdownMenu");

  if (langDropdownBtn && langDropdownMenu) {
    langDropdownBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      langDropdownMenu.classList.toggle("hidden");
    });

    document.querySelectorAll(".lang-choice-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const lang = btn.dataset.lang;
        applyLanguage(lang);
        langDropdownMenu.classList.add("hidden");
      });
    });

    document.addEventListener("click", () => {
      langDropdownMenu.classList.add("hidden");
    });
  }

  // Onglets Catégories
  document.querySelectorAll(".category-tab").forEach(tab => {
    tab.addEventListener("click", () => {
      document.querySelectorAll(".category-tab").forEach(t => {
        t.classList.remove("active", "bg-stone-900", "text-white");
        t.classList.add("bg-stone-100", "text-stone-700");
      });
      tab.classList.add("active", "bg-stone-900", "text-white");
      tab.classList.remove("bg-stone-100", "text-stone-700");

      state.activeCategory = tab.dataset.category;
      renderProducts();
    });
  });

  // Filtres Prix
  document.querySelectorAll(".price-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".price-btn").forEach(b => {
        b.classList.remove("active", "bg-stone-900", "text-white");
        b.classList.add("bg-stone-100", "text-stone-600");
      });
      btn.classList.add("active", "bg-stone-900", "text-white");
      btn.classList.remove("bg-stone-100", "text-stone-600");

      state.activePrice = btn.dataset.price;
      renderProducts();
    });
  });

  // Tri
  document.getElementById("sortSelect")?.addEventListener("change", (e) => {
    state.sortBy = e.target.value;
    renderProducts();
  });

  // Barre de Recherche
  const searchInput = document.getElementById("searchInput");
  const mobileSearchInput = document.getElementById("mobileSearchInput");
  const clearSearchBtn = document.getElementById("clearSearchBtn");

  const handleSearch = (val) => {
    state.searchQuery = val;
    if (searchInput) searchInput.value = val;
    if (mobileSearchInput) mobileSearchInput.value = val;
    
    if (clearSearchBtn) {
      if (val.length > 0) clearSearchBtn.classList.remove("hidden");
      else clearSearchBtn.classList.add("hidden");
    }
    renderProducts();
  };

  if (searchInput) {
    searchInput.addEventListener("input", (e) => handleSearch(e.target.value));
  }
  if (mobileSearchInput) {
    mobileSearchInput.addEventListener("input", (e) => handleSearch(e.target.value));
  }
  if (clearSearchBtn) {
    clearSearchBtn.addEventListener("click", () => handleSearch(""));
  }

  // Reset filters
  document.getElementById("resetFiltersBtn")?.addEventListener("click", () => {
    state.activeCategory = "all";
    state.activePrice = "all";
    state.searchQuery = "";
    document.querySelector('.category-tab[data-category="all"]')?.click();
    document.querySelector('.price-btn[data-price="all"]')?.click();
    handleSearch("");
  });

  // Product modal
  document.getElementById("closeModalBtn")?.addEventListener("click", closeProductModal);
  document.getElementById("productModal")?.addEventListener("click", (e) => {
    if (e.target.id === "productModal") closeProductModal();
  });

  // Tag Modal
  const tagModal = document.getElementById("tagModal");
  document.getElementById("openTagModalBtn")?.addEventListener("click", () => {
    document.getElementById("tagInput").value = state.amazonTag;
    tagModal.classList.remove("hidden");
  });
  document.getElementById("closeTagModalBtn")?.addEventListener("click", () => tagModal.classList.add("hidden"));
  document.getElementById("cancelTagBtn")?.addEventListener("click", () => tagModal.classList.add("hidden"));
  document.getElementById("saveTagBtn")?.addEventListener("click", () => {
    const val = document.getElementById("tagInput").value.trim();
    if (val) {
      state.amazonTag = val;
      localStorage.setItem(STORAGE_KEY_AMAZON_TAG, val);
    } else {
      state.amazonTag = DEFAULT_AMAZON_TAG;
      localStorage.setItem(STORAGE_KEY_AMAZON_TAG, DEFAULT_AMAZON_TAG);
    }
    updateTagDisplay();
    tagModal.classList.add("hidden");
    renderProducts();
    alert("ID Partenaire enregistré : " + state.amazonTag);
  });

  // Admin Modal
  const adminModal = document.getElementById("adminModal");
  document.getElementById("openAdminBtn")?.addEventListener("click", () => adminModal.classList.remove("hidden"));
  document.getElementById("closeAdminModalBtn")?.addEventListener("click", () => adminModal.classList.add("hidden"));

  // Ajout de nouveau produit
  document.getElementById("addProductForm")?.addEventListener("submit", (e) => {
    e.preventDefault();

    const category = document.getElementById("newCat").value;
    const categoryNames = {
      tech: "Tech & Télétravail",
      deco: "Maison & Décoration",
      gift: "Idées Cadeaux & Insolite",
      cuisine: "Cuisine & Pratique"
    };

    const highlightsStr = document.getElementById("newHighlights").value;
    const highlights = highlightsStr 
      ? highlightsStr.split(",").map(s => s.trim()).filter(Boolean) 
      : [];

    const newProduct = {
      id: "custom-" + Date.now(),
      category: category,
      categoryName: categoryNames[category],
      title: document.getElementById("newTitle").value.trim(),
      tagline: document.getElementById("newTagline").value.trim(),
      price: parseFloat(document.getElementById("newPrice").value),
      originalPrice: document.getElementById("newOrigPrice").value ? parseFloat(document.getElementById("newOrigPrice").value) : null,
      rating: parseFloat(document.getElementById("newRating").value) || 4.7,
      reviewsCount: parseInt(document.getElementById("newReviews").value) || 850,
      badge: document.getElementById("newBadge").value.trim() || "Sélection Spéciale ✨",
      image: document.getElementById("newImage").value.trim(),
      amazonUrl: document.getElementById("newUrl").value.trim(),
      curatorOpinion: document.getElementById("newOpinion").value.trim(),
      highlights: highlights
    };

    state.products.unshift(newProduct);
    saveProducts();
    renderCounters();
    renderProducts();

    e.target.reset();
    adminModal.classList.add("hidden");
    alert("Produit ajouté avec succès !");
  });

  // Export JSON
  document.getElementById("exportJsonBtn")?.addEventListener("click", () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(state.products, null, 2));
    const downloadAnchor = document.createElement("a");
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `catalogue_trouvailles_${Date.now()}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
  });

  // Reset catalogue
  document.getElementById("resetDefaultBtn")?.addEventListener("click", () => {
    if (confirm("Réinitialiser le catalogue avec les pépites d'origine ?")) {
      state.products = [...INITIAL_PRODUCTS];
      saveProducts();
      renderCounters();
      renderProducts();
      alert("Catalogue réinitialisé !");
    }
  });

  // Escape key
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeProductModal();
      document.getElementById("tagModal")?.classList.add("hidden");
      document.getElementById("adminModal")?.classList.add("hidden");
      document.getElementById("langDropdownMenu")?.classList.add("hidden");
    }
  });
}

function updateTagDisplay() {
  const display = document.getElementById("currentTagDisplay");
  if (!display) return;
  display.textContent = state.amazonTag;
  display.classList.remove("text-stone-400");
  display.classList.add("text-emerald-400");
}

function escapeHtml(text) {
  if (!text) return "";
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
