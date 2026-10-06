import json
import os

with open("logos_b64.json", "r", encoding="utf-8") as f:
    logos = json.load(f)

loupe_b64 = "data:image/jpeg;base64," + logos["loupe"]

with open("products.js", "r", encoding="utf-8") as f:
    products_code = f.read()

with open("app.js", "r", encoding="utf-8") as f:
    app_code = f.read()

html_template = f"""<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ABCompare | Le Comparateur Malin des Pépites du Web (Amazon, Cdiscount, Fnac, AliExpress)</title>
  <meta name="description" content="ABCompare compare en direct les meilleurs prix des pépites du web entre Amazon, Cdiscount, Fnac et AliExpress pour vous garantir l'offre la moins chère.">
  <link rel="icon" type="image/jpeg" href="{loupe_b64}">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Google Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
          }},
          colors: {{
            brand: {{
              50: '#fbf9f5',
              100: '#f5f1ea',
              200: '#eadecf',
              500: '#c59a68',
              600: '#b28551',
              900: '#141414',
            }},
            amazon: {{
              gold: '#ff9900',
              dark: '#131921',
              hover: '#e88b00',
            }}
          }}
        }}
      }}
    }}
  </script>

  <style>
    body {{
      background-color: #faf9f6;
      color: #1f2937;
    }}
    .no-scrollbar::-webkit-scrollbar {{
      display: none;
    }}
    .no-scrollbar {{
      -ms-overflow-style: none;
      scrollbar-width: none;
    }}
  </style>
</head>
<body class="min-h-screen flex flex-col font-sans antialiased selection:bg-blue-100 selection:text-blue-900">

  <!-- ================= TOP NOTICE BANNER ================= -->
  <div class="bg-stone-950 text-stone-300 text-xs py-2 px-4 border-b border-stone-800">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center justify-center bg-blue-600 text-white font-extrabold text-[10px] px-1.5 py-0.5 rounded tracking-wide">ABCOMPARE</span>
        <span id="topNoticeText">⚖️ Comparateur A/B en direct • Meilleurs prix vérifiés entre Amazon, Cdiscount, Fnac & AliExpress</span>
      </div>
      <div class="flex items-center gap-4 text-stone-400">
        <button id="openTagModalBtn" class="hover:text-amber-400 transition-colors flex items-center gap-1.5">
          <i data-lucide="tag" class="w-3.5 h-3.5 text-amber-500"></i>
          <span>Tag Partenaire : <strong id="currentTagDisplay" class="text-emerald-400">lestrouvai0c0-21</strong></span>
        </button>
        <button id="openAdminBtn" class="hover:text-white transition-colors flex items-center gap-1 bg-stone-800 hover:bg-stone-700 px-2.5 py-0.5 rounded text-[11px]">
          <i data-lucide="sliders" class="w-3 h-3 text-amber-400"></i>
          <span>Gérer le catalogue</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ================= NAVIGATION HEADER ================= -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-stone-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-4">
      
      <!-- Brand Logo ABCompare -->
      <a href="#" class="flex items-center gap-3.5 group shrink-0">
        <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-blue-700 via-indigo-600 to-amber-500 shadow-md flex items-center justify-center text-white font-black text-xl tracking-tighter group-hover:scale-105 transition-transform border border-white/20">
          <span>AB</span>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="text-2xl font-black tracking-tight text-stone-950 block leading-tight">AB<span class="text-blue-600">Compare</span></span>
            <span class="bg-blue-100 text-blue-800 text-[9px] font-black px-1.5 py-0.5 rounded uppercase">PRO</span>
          </div>
          <span class="text-[11px] font-bold text-stone-500 tracking-wider">Le Comparateur Malin des Pépites</span>
        </div>
      </a>

      <!-- Search Input Desktop -->
      <div class="flex-1 max-w-md hidden md:block">
        <div class="relative">
          <i data-lucide="search" class="w-4 h-4 text-stone-400 absolute left-3.5 top-1/2 -translate-y-1/2"></i>
          <input 
            type="text" 
            id="searchInput" 
            placeholder="Rechercher une pépite, un gadget, un écran..." 
            class="w-full pl-10 pr-4 py-2.5 text-sm bg-stone-50 border border-stone-200 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all placeholder:text-stone-400"
          >
          <button id="clearSearchBtn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-stone-400 hover:text-stone-600">
            <i data-lucide="x" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>

      <!-- Right controls: Languages & Trust indicators -->
      <div class="flex items-center gap-3 sm:gap-5">
        
        <!-- Language Selector Dropdown -->
        <div class="relative">
          <button 
            id="langDropdownBtn" 
            class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-800 text-xs font-bold border border-stone-200 transition-all shadow-sm"
            title="Changer de langue / Change language"
          >
            <span id="currentLangDisplay" class="flex items-center gap-1">
              <span>🇫🇷</span> <span class="font-bold uppercase">FR</span>
            </span>
            <i data-lucide="chevron-down" class="w-3.5 h-3.5 text-stone-500"></i>
          </button>

          <!-- Dropdown menu -->
          <div id="langDropdownMenu" class="hidden absolute right-0 mt-2 w-40 bg-white rounded-2xl shadow-2xl border border-stone-200 py-2 z-50">
            <div class="px-3 py-1 text-[10px] uppercase tracking-wider font-bold text-stone-400 border-b border-stone-100 mb-1">
              Pays & Langue
            </div>
            <button data-lang="fr" class="lang-choice-btn w-full text-left px-3.5 py-1.5 text-xs text-stone-700 hover:bg-amber-50 hover:text-amber-900 flex items-center justify-between font-semibold">
              <span class="flex items-center gap-2"><span>🇫🇷</span> <span>Français</span></span>
              <span class="text-[10px] text-stone-400 font-normal">Amazon.fr</span>
            </button>
            <button data-lang="en" class="lang-choice-btn w-full text-left px-3.5 py-1.5 text-xs text-stone-700 hover:bg-amber-50 hover:text-amber-900 flex items-center justify-between font-semibold">
              <span class="flex items-center gap-2"><span>🇬🇧</span> <span>English</span></span>
              <span class="text-[10px] text-stone-400 font-normal">Amazon.co.uk</span>
            </button>
            <button data-lang="de" class="lang-choice-btn w-full text-left px-3.5 py-1.5 text-xs text-stone-700 hover:bg-amber-50 hover:text-amber-900 flex items-center justify-between font-semibold">
              <span class="flex items-center gap-2"><span>🇩🇪</span> <span>Deutsch</span></span>
              <span class="text-[10px] text-stone-400 font-normal">Amazon.de</span>
            </button>
            <button data-lang="es" class="lang-choice-btn w-full text-left px-3.5 py-1.5 text-xs text-stone-700 hover:bg-amber-50 hover:text-amber-900 flex items-center justify-between font-semibold">
              <span class="flex items-center gap-2"><span>🇪🇸</span> <span>Español</span></span>
              <span class="text-[10px] text-stone-400 font-normal">Amazon.es</span>
            </button>
            <button data-lang="it" class="lang-choice-btn w-full text-left px-3.5 py-1.5 text-xs text-stone-700 hover:bg-amber-50 hover:text-amber-900 flex items-center justify-between font-semibold">
              <span class="flex items-center gap-2"><span>🇮🇹</span> <span>Italiano</span></span>
              <span class="text-[10px] text-stone-400 font-normal">Amazon.it</span>
            </button>
          </div>
        </div>

        <!-- Trust Badges Desktop -->
        <div class="hidden lg:flex items-center gap-4 text-xs text-stone-600 font-medium">
          <div class="flex items-center gap-1.5">
            <i data-lucide="scale" class="w-4 h-4 text-blue-600"></i>
            <span>Comparateur Certifié</span>
          </div>
        </div>

      </div>
    </div>

    <!-- Mobile Search Bar (sous le header) -->
    <div class="p-3 border-t border-stone-100 md:hidden bg-white">
      <div class="relative">
        <i data-lucide="search" class="w-4 h-4 text-stone-400 absolute left-3 top-1/2 -translate-y-1/2"></i>
        <input 
          type="text" 
          id="mobileSearchInput" 
          placeholder="Rechercher une pépite..." 
          class="w-full pl-9 pr-3 py-2 text-sm bg-stone-50 border border-stone-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500"
        >
      </div>
    </div>
  </header>

  <!-- ================= HERO SECTION COMPARATEUR ================= -->
  <section class="bg-gradient-to-b from-blue-50/50 via-stone-50 to-transparent pt-12 pb-8 border-b border-stone-200/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      
      <!-- Badge d'autorité -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-blue-100/70 border border-blue-300/80 text-blue-950 text-xs font-bold mb-4 shadow-sm">
        <i data-lucide="scale" class="w-3.5 h-3.5 text-blue-600"></i>
        <span id="heroBadgeText">ABCompare • Comparateur A/B des Pépites du Web</span>
      </div>

      <!-- Titre principal percutant -->
      <h1 id="heroTitle" class="text-3xl sm:text-5xl lg:text-6xl font-black tracking-tight text-stone-950 max-w-4xl mx-auto leading-[1.12]">
        Comparez et trouvez le vrai meilleur prix,<br>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 via-indigo-600 to-amber-600">
          entre Amazon, Fnac, Cdiscount et AliExpress.
        </span>
      </h1>

      <!-- Sous-titre rassurant et explicite -->
      <p id="heroDesc" class="mt-4 text-base sm:text-lg text-stone-600 max-w-2xl mx-auto leading-relaxed font-normal">
        Ne payez plus jamais trop cher. ABCompare analyse et compare chaque pépite pour vous indiquer où commander au meilleur prix ou avec la livraison la plus rapide.
      </p>

      <!-- Badges de réassurance -->
      <div class="mt-8 flex flex-wrap items-center justify-center gap-6 sm:gap-10 text-xs sm:text-sm text-stone-500 font-semibold">
        <div class="flex items-center gap-2">
          <div class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></div>
          <span id="totalProductsCount">20 pépites comparées</span>
        </div>
        <div class="flex items-center gap-2">
          <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i>
          <span>Offres A/B comparées en direct</span>
        </div>
        <div class="flex items-center gap-2">
          <i data-lucide="shield-check" class="w-4 h-4 text-blue-600"></i>
          <span id="primeBadgeText">Redirection officielle 100% sécurisée</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= LES ONGLETS PRINCIPAUX ================= -->
  <section class="sticky top-20 z-30 bg-white/95 backdrop-blur-md border-b border-stone-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-2 py-3 overflow-x-auto no-scrollbar" id="categoryTabsContainer">
        
        <!-- Tab: Tous -->
        <button 
          data-category="all" 
          class="category-tab active px-4 py-2.5 rounded-full text-xs sm:text-sm font-bold transition-all whitespace-nowrap flex items-center gap-2 bg-stone-900 text-white shadow-sm"
        >
          <i data-lucide="layout-grid" class="w-4 h-4"></i>
          <span>Tout comparer</span>
          <span class="ml-1 text-[11px] px-2 py-0.2 rounded-full bg-stone-700 text-stone-200" id="count-all">20</span>
        </button>

        <!-- Tab 1: Tech & Télétravail -->
        <button 
          data-category="tech" 
          class="category-tab px-4 py-2.5 rounded-full text-xs sm:text-sm font-bold transition-all whitespace-nowrap flex items-center gap-2 bg-stone-100 text-stone-700 hover:bg-stone-200"
        >
          <i data-lucide="laptop" class="w-4 h-4 text-blue-600"></i>
          <span>Tech & Télétravail</span>
          <span class="ml-1 text-[11px] px-2 py-0.2 rounded-full bg-stone-200 text-stone-700" id="count-tech">8</span>
        </button>

        <!-- Tab 2: Maison & Décoration -->
        <button 
          data-category="deco" 
          class="category-tab px-4 py-2.5 rounded-full text-xs sm:text-sm font-bold transition-all whitespace-nowrap flex items-center gap-2 bg-stone-100 text-stone-700 hover:bg-stone-200"
        >
          <i data-lucide="home" class="w-4 h-4 text-emerald-600"></i>
          <span>Maison & Décoration</span>
          <span class="ml-1 text-[11px] px-2 py-0.2 rounded-full bg-stone-200 text-stone-700" id="count-deco">7</span>
        </button>

        <!-- Tab 3: Idées Cadeaux & Insolite -->
        <button 
          data-category="gift" 
          class="category-tab px-4 py-2.5 rounded-full text-xs sm:text-sm font-bold transition-all whitespace-nowrap flex items-center gap-2 bg-stone-100 text-stone-700 hover:bg-stone-200"
        >
          <i data-lucide="gift" class="w-4 h-4 text-rose-500"></i>
          <span>Idées Cadeaux & Insolite</span>
          <span class="ml-1 text-[11px] px-2 py-0.2 rounded-full bg-stone-200 text-stone-700" id="count-gift">8</span>
        </button>

        <!-- Tab 4: Cuisine & Vie Pratique -->
        <button 
          data-category="cuisine" 
          class="category-tab px-4 py-2.5 rounded-full text-xs sm:text-sm font-bold transition-all whitespace-nowrap flex items-center gap-2 bg-stone-100 text-stone-700 hover:bg-stone-200"
        >
          <i data-lucide="coffee" class="w-4 h-4 text-amber-600"></i>
          <span>Cuisine & Pratique</span>
          <span class="ml-1 text-[11px] px-2 py-0.2 rounded-full bg-stone-200 text-stone-700" id="count-cuisine">6</span>
        </button>
      </div>
    </div>
  </section>

  <!-- ================= SOUS-FILTRES & TRI ================= -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 pb-2">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-stone-200">
      
      <!-- Filtres Prix -->
      <div class="flex items-center gap-2 overflow-x-auto no-scrollbar text-xs">
        <span id="priceFilterLabel" class="text-stone-400 font-medium">Prix :</span>
        <button data-price="all" class="price-btn active px-3 py-1.5 rounded-lg bg-stone-900 text-white font-semibold">Tous</button>
        <button data-price="under-20" class="price-btn px-3 py-1.5 rounded-lg bg-stone-100 text-stone-600 hover:bg-stone-200 font-medium">&lt; 20 €</button>
        <button data-price="20-35" class="price-btn px-3 py-1.5 rounded-lg bg-stone-100 text-stone-600 hover:bg-stone-200 font-medium">20 € - 35 €</button>
        <button data-price="35-plus" class="price-btn px-3 py-1.5 rounded-lg bg-stone-100 text-stone-600 hover:bg-stone-200 font-medium">35 € +</button>
      </div>

      <!-- Tri & Compteur -->
      <div class="flex items-center justify-between sm:justify-end gap-3">
        <span class="text-xs text-stone-500 font-semibold" id="resultsCount">29 pépites trouvées</span>
        <div class="relative">
          <select id="sortSelect" class="text-xs bg-white border border-stone-200 rounded-lg px-3 py-1.5 font-medium text-stone-700 focus:outline-none focus:ring-1 focus:ring-amber-500">
            <option value="featured">Pertinence & Bestsellers</option>
            <option value="price-asc">Prix : croissant</option>
            <option value="price-desc">Prix : décroissant</option>
            <option value="rating">Mieux notés d'abord</option>
          </select>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= GRILLE DE PRODUITS ================= -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1">
    
    <!-- État vide si aucune trouvaille trouvée -->
    <div id="emptyState" class="hidden text-center py-20">
      <div class="w-16 h-16 rounded-full bg-stone-100 flex items-center justify-center mx-auto text-stone-400 mb-4">
        <i data-lucide="search-x" class="w-8 h-8"></i>
      </div>
      <h3 class="text-lg font-bold text-stone-800">Aucun produit ne correspond à votre recherche</h3>
      <p class="text-stone-500 text-sm mt-1">Essayez d'ajuster vos filtres ou de vider la barre de recherche.</p>
      <button id="resetFiltersBtn" class="mt-4 px-4 py-2 rounded-lg bg-stone-900 text-white text-xs font-semibold hover:bg-stone-800">
        Réinitialiser les filtres
      </button>
    </div>

    <!-- Grille des articles -->
    <div id="productGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6"></div>
  </main>

  <!-- ================= POURQUOI NOUS CHOISIR ================= -->
  <section class="bg-stone-100/70 border-t border-stone-200 py-12 mt-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-xl mx-auto mb-8">
        <h2 id="trustSectionTitle" class="text-2xl font-extrabold text-stone-900">Pourquoi faire confiance à notre sélection ?</h2>
        <p id="trustSectionDesc" class="text-stone-500 text-sm mt-1">Nous appliquons une charte d'exigence stricte sur chaque pépite listée.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-2xl border border-stone-200/80 shadow-sm flex flex-col items-start">
          <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-700 flex items-center justify-center font-bold mb-4">
            <i data-lucide="filter" class="w-5 h-5"></i>
          </div>
          <h3 id="trust1Title" class="font-bold text-stone-900 text-base">Filtre anti-camelote</h3>
          <p id="trust1Desc" class="text-stone-600 text-sm mt-2 leading-relaxed">
            Seuls les produits notés plus de 4.4/5 avec des centaines d'avis clients vérifiés peuvent intégrer notre sélection.
          </p>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-stone-200/80 shadow-sm flex flex-col items-start">
          <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold mb-4">
            <i data-lucide="shield" class="w-5 h-5"></i>
          </div>
          <h3 id="trust2Title" class="font-bold text-stone-900 text-base">Garantie & Sécurité Amazon</h3>
          <p id="trust2Desc" class="text-stone-600 text-sm mt-2 leading-relaxed">
            Vous commandez directement sur Amazon France avec vos avantages habituels : livraison Prime express, paiement crypté et retours gratuits 30 jours.
          </p>
        </div>

        <div class="bg-white p-6 rounded-2xl border border-stone-200/80 shadow-sm flex flex-col items-start">
          <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-700 flex items-center justify-center font-bold mb-4">
            <i data-lucide="badge-percent" class="w-5 h-5"></i>
          </div>
          <h3 id="trust3Title" class="font-bold text-stone-900 text-base">Le meilleur prix officiel</h3>
          <p id="trust3Desc" class="text-stone-600 text-sm mt-2 leading-relaxed">
            Pas de surcoût ni de marge cachée. Vous payez exactement le tarif officiel et bénéficiez des réductions et ventes flash du jour.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= FOOTER LÉGAL ABCOMPARE ================= -->
  <footer class="bg-stone-950 text-stone-400 text-xs py-10 border-t border-stone-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-stone-800/80">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-700 via-indigo-600 to-amber-500 shadow-md flex items-center justify-center text-white font-black text-sm shrink-0">
            <span>AB</span>
          </div>
          <div>
            <span class="text-white font-extrabold text-sm block">ABCompare — Le Comparateur Malin des Pépites</span>
            <span class="text-stone-500 text-[11px]">Comparateur indépendant de prix et de boutiques en ligne</span>
          </div>
        </div>

        <div class="flex items-center gap-6 text-stone-400 text-xs">
          <a href="#" class="hover:text-white transition-colors">Mentions Légales</a>
          <a href="#" class="hover:text-white transition-colors">Transparence & Affiliation</a>
          <a href="#" class="hover:text-white transition-colors">Contact</a>
        </div>
      </div>

      <!-- Legal Affiliate Disclaimer -->
      <div class="mt-6 text-stone-500 text-[11px] leading-relaxed max-w-4xl">
        <p class="mb-2" id="affiliateDisclaimerText">
          <strong>Transparence & Indépendance :</strong> ABCompare est un comparateur de prix indépendant. Nous comparons les offres réelles sur Amazon, Cdiscount, Fnac et AliExpress. En tant que partenaire affilié, ce site peut percevoir une rémunération sur les achats éligibles sans aucun coût supplémentaire pour le consommateur. Les prix affichés sont indicatifs et vérifiés en continu.
        </p>
        <p>
          © 2026 ABCompare. Tous droits réservés.
        </p>
      </div>
    </div>
  </footer>

  <!-- ================= MODALE FICHE PRODUIT ================= -->
  <div id="productModal" class="fixed inset-0 z-50 hidden bg-stone-950/70 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl relative border border-stone-200">
      <button id="closeModalBtn" class="absolute right-4 top-4 z-10 w-9 h-9 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-600 flex items-center justify-center transition-colors">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
      <div id="modalContent" class="p-6 sm:p-8"></div>
    </div>
  </div>

  <!-- ================= MODALE ID PARTENAIRE ================= -->
  <div id="tagModal" class="fixed inset-0 z-50 hidden bg-stone-950/70 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-md w-full p-6 shadow-2xl border border-stone-200">
      <div class="flex items-center justify-between pb-4 border-b border-stone-100">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center font-bold">
            <i data-lucide="tag" class="w-4 h-4"></i>
          </div>
          <h3 class="font-bold text-stone-900 text-base">Votre ID Partenaire Amazon</h3>
        </div>
        <button id="closeTagModalBtn" class="text-stone-400 hover:text-stone-600">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="mt-4 space-y-3">
        <p class="text-xs text-stone-600 leading-relaxed">
          Votre compte Partenaire officiel est configuré : <strong class="text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded font-mono">lestrouvai0c0-21</strong>.
        </p>
        <p class="text-xs text-stone-500">
          ⚡ <strong>Tous les boutons d'achat du site</strong> intègrent immédiatement votre lien affilié pour vous créditer les commissions !
        </p>

        <div>
          <label class="block text-xs font-semibold text-stone-700 mb-1">Votre Tracking ID Amazon :</label>
          <input 
            type="text" 
            id="tagInput" 
            value="lestrouvai0c0-21"
            class="w-full px-3 py-2 text-sm border border-stone-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500/20 focus:border-amber-500 font-mono"
          >
        </div>

        <div class="pt-2 flex items-center justify-end gap-2">
          <button id="cancelTagBtn" class="px-4 py-2 text-xs font-medium text-stone-600 hover:bg-stone-100 rounded-lg">Fermer</button>
          <button id="saveTagBtn" class="px-4 py-2 text-xs font-semibold bg-stone-900 text-white rounded-lg hover:bg-stone-800 flex items-center gap-1.5">
            <i data-lucide="check" class="w-3.5 h-3.5"></i>
            Enregistrer
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= MODALE GESTIONNAIRE DE CATALOGUE ================= -->
  <div id="adminModal" class="fixed inset-0 z-50 hidden bg-stone-950/70 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-3xl w-full max-h-[92vh] overflow-y-auto p-6 sm:p-8 shadow-2xl border border-stone-200">
      
      <div class="flex items-center justify-between pb-4 border-b border-stone-100">
        <div>
          <h3 class="font-bold text-stone-900 text-lg flex items-center gap-2">
            <i data-lucide="sliders" class="w-5 h-5 text-amber-600"></i>
            Gestionnaire de Catalogue
          </h3>
          <p class="text-xs text-stone-500">Ajoutez, modifiez ou exportez des produits pour enrichir les 4 univers.</p>
        </div>
        <button id="closeAdminModalBtn" class="text-stone-400 hover:text-stone-600">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- Actions Rapides -->
      <div class="my-4 flex flex-wrap gap-2 text-xs">
        <button id="exportJsonBtn" class="px-3 py-1.5 rounded-lg bg-stone-100 hover:bg-stone-200 text-stone-700 font-medium flex items-center gap-1.5">
          <i data-lucide="download" class="w-3.5 h-3.5"></i>
          Exporter le catalogue (JSON)
        </button>
        <button id="resetDefaultBtn" class="px-3 py-1.5 rounded-lg bg-red-50 hover:bg-red-100 text-red-600 font-medium flex items-center gap-1.5">
          <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
          Réinitialiser au catalogue d'origine
        </button>
      </div>

      <!-- Formulaire d'ajout de produit -->
      <form id="addProductForm" class="space-y-4 pt-2 border-t border-stone-100">
        <h4 class="font-semibold text-stone-800 text-sm flex items-center gap-1.5">
          <i data-lucide="plus-circle" class="w-4 h-4 text-emerald-600"></i>
          Ajouter une nouvelle pépite
        </h4>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div>
            <label class="block font-medium text-stone-700 mb-1">Catégorie (Onglet) *</label>
            <select id="newCat" required class="w-full px-3 py-2 border border-stone-300 rounded-lg bg-white">
              <option value="tech">💻 Tech & Télétravail</option>
              <option value="deco">🏡 Maison & Décoration</option>
              <option value="gift">🎁 Idées Cadeaux & Insolite</option>
              <option value="cuisine">🍳 Cuisine & Pratique</option>
            </select>
          </div>

          <div>
            <label class="block font-medium text-stone-700 mb-1">Badge attractif</label>
            <input type="text" id="newBadge" placeholder="ex: Top Tendance 🔥, Coup de Cœur ⭐" class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div class="sm:col-span-2">
            <label class="block font-medium text-stone-700 mb-1">Titre de l'article *</label>
            <input type="text" id="newTitle" required placeholder="ex: Lampe de bureau LED ScreenBar" class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div class="sm:col-span-2">
            <label class="block font-medium text-stone-700 mb-1">Accroche vendeuse *</label>
            <input type="text" id="newTagline" required placeholder="ex: Élimine les reflets sur votre écran et réduit la fatigue visuelle." class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div>
            <label class="block font-medium text-stone-700 mb-1">Prix indicatif (€) *</label>
            <input type="number" step="0.01" id="newPrice" required placeholder="29.99" class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div>
            <label class="block font-medium text-stone-700 mb-1">Prix barré (€ - optionnel)</label>
            <input type="number" step="0.01" id="newOrigPrice" placeholder="39.99" class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div>
            <label class="block font-medium text-stone-700 mb-1">Note moyenne</label>
            <input type="number" step="0.1" max="5" id="newRating" value="4.7" class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div>
            <label class="block font-medium text-stone-700 mb-1">Nombre d'avis vérifiés</label>
            <input type="number" id="newReviews" value="1500" class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div class="sm:col-span-2">
            <label class="block font-medium text-stone-700 mb-1">Lien Amazon ou ASIN *</label>
            <input type="text" id="newUrl" required placeholder="https://www.amazon.fr/dp/... ou B08C4VKYFG" class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div class="sm:col-span-2">
            <label class="block font-medium text-stone-700 mb-1">URL de la photo *</label>
            <input type="url" id="newImage" required placeholder="https://images.unsplash.com/..." class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>

          <div class="sm:col-span-2">
            <label class="block font-medium text-stone-700 mb-1">Avis du Curateur</label>
            <textarea id="newOpinion" rows="2" placeholder="Pourquoi cet article est exceptionnel..." class="w-full px-3 py-2 border border-stone-300 rounded-lg"></textarea>
          </div>

          <div class="sm:col-span-2">
            <label class="block font-medium text-stone-700 mb-1">Points Forts (séparés par des virgules)</label>
            <input type="text" id="newHighlights" placeholder="Zéro reflet, USB direct, Garantie 2 ans" class="w-full px-3 py-2 border border-stone-300 rounded-lg">
          </div>
        </div>

        <div class="pt-3 flex justify-end gap-2">
          <button type="submit" class="px-5 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-stone-950 font-bold text-xs flex items-center gap-1.5 transition-colors shadow-sm">
            <i data-lucide="plus" class="w-4 h-4"></i>
            Ajouter au catalogue
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- SCRIPT COMPLET EMBARQUÉ (AUTONOME & SANS DÉPENDANCE) -->
  <script>
{products_code}

{app_code}
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("index.html généré avec succès en version multilingue et tag officiel !")
