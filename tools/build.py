#!/usr/bin/env python3
"""Builds the shared head, header and footer for every page, the service pages,
404 page, sitemap.xml and robots.txt.

Run from the repo root:  python3 tools/build.py
Page content lives in tools/pages.py; the home page body lives in index.html
between the <!--HEADER--> and <!--FOOTER--> markers.
"""
import json, re, sys, datetime, html
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from pages import PAGES  # noqa: E402
from towns import TOWNS as TOWN_PAGES  # noqa: E402
from pages import STEPS as STEPS_HTML  # noqa: E402
TOWN_LINK = {t['name']: f"/{t['slug']}/" for t in TOWN_PAGES}

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://six18web.com"
TODAY = datetime.date.today().isoformat()
EMAIL = "six18web@gmail.com"
SOCIAL = [
    ("Facebook", "https://www.facebook.com/six18web"),
    ("Instagram", "https://www.instagram.com/six18web"),
    ("TikTok", "https://www.tiktok.com/@six18.web"),
    ("X", "https://x.com/six18web"),
]
TOWNS = ["Edwardsville", "Glen Carbon", "Maryville", "Collinsville", "Troy",
         "Granite City", "Alton", "Highland"]
SERVICES = [  # (path, nav label, schema name)
    ("/web-design/", "Web design", "Small business web design"),
    ("/website-repair/", "Website fixes", "Website repair and fixes"),
    ("/local-seo/", "Local SEO", "Local SEO and Google Business Profile management"),
]

BUSINESS = {
    "@type": "ProfessionalService",
    "@id": f"{SITE}/#business",
    "name": "Six18 Web",
    "alternateName": "Six18 Web Co.",
    "url": f"{SITE}/",
    "email": EMAIL,
    "logo": f"{SITE}/logo.png",
    "image": f"{SITE}/og-image.png",
    "description": "Web design, website fixes, and local SEO for small businesses. "
                   "Based in Edwardsville and Glen Carbon, Illinois, serving small businesses nationwide.",
    "slogan": "Websites that make your phone ring.",
    "priceRange": "$199–$2,800",
    "address": {"@type": "PostalAddress", "addressLocality": "Edwardsville",
                "addressRegion": "IL", "postalCode": "62025", "addressCountry": "US"},
    "areaServed": [{"@type": "City", "name": f"{t}, IL"} for t in TOWNS]
                  + [{"@type": "Country", "name": "United States"}],
    "knowsAbout": ["Web design", "Website repair", "Local SEO", "Google Business Profile",
                   "Website accessibility (WCAG 2.1 AA)", "Mobile-friendly websites"],
    "sameAs": [u for _, u in SOCIAL],
    "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Six18 Web services",
        "itemListElement": [
            {"@type": "Offer", "name": "Site Fix-It", "price": "199", "priceCurrency": "USD",
             "description": "Fixes for an existing website, starting at $199.",
             "url": f"{SITE}/website-repair/"},
            {"@type": "Offer", "name": "Starter Site", "price": "950", "priceCurrency": "USD",
             "description": "One-page, phone-first website with Google Business Profile setup.",
             "url": f"{SITE}/web-design/"},
            {"@type": "Offer", "name": "Business Site", "price": "2800", "priceCurrency": "USD",
             "description": "Up to 6 pages, quote or booking form, town pages, and local SEO setup.",
             "url": f"{SITE}/web-design/"},
            {"@type": "Offer", "name": "Care Plan", "price": "89", "priceCurrency": "USD",
             "description": "Hosting, updates, backups, and up to 1 hour of edits a month.",
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": "89",
                                    "priceCurrency": "USD", "unitText": "MONTH"},
             "url": f"{SITE}/#pricing"},
            {"@type": "Offer", "name": "Local Search", "price": "399", "priceCurrency": "USD",
             "description": "Monthly Google Business Profile, reviews, listings, and reporting.",
             "priceSpecification": {"@type": "UnitPriceSpecification", "price": "399",
                                    "priceCurrency": "USD", "unitText": "MONTH"},
             "url": f"{SITE}/local-seo/"},
        ],
    },
}
WEBSITE = {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/",
           "name": "Six18 Web", "publisher": {"@id": f"{SITE}/#business"}}


def faq_schema(faqs, url):
    return {"@type": "FAQPage", "@id": f"{url}#faq", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in faqs]}


def head(title, desc, path, graph, extra=""):
    url = SITE + path
    assert len(desc) <= 158, f"description too long ({len(desc)}): {path}"
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    ensure_ascii=False, separators=(",", ":"))
    e = html.escape
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Six18 Web">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Six18 Web: websites that make your phone ring">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@six18web">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/og-image.png">
<meta name="theme-color" content="#13213B">
<meta name="format-detection" content="telephone=no">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/logo.png">
<script type="application/ld+json">{ld}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="/styles.css">{extra}
</head>
<body>
"""


def header(current=""):
    links = "".join(
        f'<a href="{p}"{" aria-current=\"page\"" if p == current else ""}>{label}</a>'
        for p, label, _ in SERVICES)
    return f"""<header class="site-head">
  <div class="wrap">
    <a class="logo" href="/" aria-label="Six18 Web home"><span class="logo-mark" aria-hidden="true">618</span><span data-bind="name">Six18 Web</span></a>
    <nav class="nav" aria-label="Main">
      {links}<a href="/#pricing">Pricing</a>
      <a href="/#faq">FAQ</a>
    </nav>
    <a class="btn btn-primary head-call" href="/#contact">Free review</a>
  </div>
</header>
"""


def town_link(t, cls=""):
    if t in TOWN_LINK:
        c = f' class="{cls}"' if cls else ""
        return f'<a href="{TOWN_LINK[t]}"{c}>{t}</a>'
    return t


def linkify_area(h):
    """Turn the town chips (<span>Town</span> inside .area) into links where a town page exists."""
    def chips(m):
        inner = re.sub(r'<span( class="home")?>([^<]+)</span>',
                       lambda c: f'<a href="{TOWN_LINK[c.group(2)]}"{c.group(1) or ""}>{c.group(2)}</a>'
                       if c.group(2) in TOWN_LINK else c.group(0), m.group(2))
        return m.group(1) + inner + "</div>"
    return re.sub(r'(<div class="area">)(.*?)</div>', chips, h, flags=re.S)


def footer():
    svc = "".join(f'<li><a href="{p}">{label}</a></li>' for p, label, _ in SERVICES)
    soc = "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)
    return f"""<footer>
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <a class="logo" href="/"><span class="logo-mark" aria-hidden="true">618</span><span>Six18 Web</span></a>
      <p>Web design, website fixes, and local SEO for small businesses. Based in Edwardsville &amp; Glen Carbon, Illinois. Working with shops nationwide.</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <nav aria-label="Services"><p class="foot-h">Services</p><ul>{svc}<li><a href="/#pricing">Pricing</a></li></ul></nav>
    <div><p class="foot-h">Service area</p><p class="foot-towns">{" · ".join(town_link(t) for t in TOWNS)}, and anywhere in the U.S. by video call.</p></div>
  </div>
  <div class="wrap foot-bottom">
    <span>© <span id="yr">2026</span> Six18 Web · Built in the 618, for shops everywhere</span>
    <nav class="socials" aria-label="Social media">{soc}</nav>
  </div>
</footer>
"""


SUB_SCRIPT = """<script>document.getElementById('yr').textContent = new Date().getFullYear();</script>
</body>
</html>
"""


def breadcrumb(path, name):
    return {"@type": "BreadcrumbList", "@id": f"{SITE}{path}#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": f"{SITE}{path}"}]}


def faq_html(faqs):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)


def build_service(p):
    path = p["path"]
    url = SITE + path
    graph = [
        BUSINESS, WEBSITE,
        {"@type": "WebPage", "@id": url, "url": url, "name": p["title"],
         "description": p["desc"], "isPartOf": {"@id": f"{SITE}/#website"},
         "breadcrumb": {"@id": f"{url}#breadcrumb"}, "about": {"@id": f"{url}#service"}},
        {"@type": "Service", "@id": f"{url}#service", "name": p["service_name"],
         "serviceType": p["service_name"], "provider": {"@id": f"{SITE}/#business"},
         "areaServed": BUSINESS["areaServed"], "description": p["desc"],
         "offers": {"@type": "Offer", "price": p["price"], "priceCurrency": "USD",
                    "url": url}},
        breadcrumb(path, p["crumb"]),
        faq_schema(p["faqs"], url),
    ]
    other = "".join(f'<a class="svc-link" href="{sp}"><span>{label}</span><span aria-hidden="true">→</span></a>'
                    for sp, label, _ in SERVICES if sp != path)
    body = f"""{header(path)}
<main id="top">
  <section class="hero sub-hero">
    <div class="wrap sub-hero-wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span aria-current="page">{p["crumb"]}</span></nav>
      <p class="eyebrow">{p["eyebrow"]}</p>
      <h1>{p["h1"]}</h1>
      <p class="lede">{p["lede"]}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="/#contact">Get a free 10-minute review</a>
        <a class="btn btn-ghost" href="/#pricing">See all pricing</a>
      </div>
      <p class="towns">{p["price_line"]}</p>
    </div>
  </section>
{p["body"]}
  <section class="sub-faq" id="faq">
    <div class="wrap two">
      <div>
        <p class="eyebrow">Questions</p>
        <h2 style="margin-top:.75rem">{p["faq_h2"]}</h2>
        <p class="lede" style="margin-top:1rem">Something else on your mind? Email <a href="mailto:{EMAIL}">{EMAIL}</a> and you'll hear back within one business day.</p>
        <div class="svc-links"><p class="foot-h" style="color:var(--muted)">Other services</p>{other}</div>
      </div>
      <div>{faq_html(p["faqs"])}</div>
    </div>
  </section>
  <section class="cta-band">
    <div class="wrap">
      <h2>{p["cta_h2"]}</h2>
      <p class="lede">Tell us about your business. We'll look at your site and Google listing and reply within one business day with what we found. No pressure, no obligation.</p>
      <a class="btn btn-primary" href="/#contact">Request my free review</a>
    </div>
  </section>
</main>
{footer()}{SUB_SCRIPT}"""
    out = ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head(p["title"], p["desc"], path, graph) + "\n" + linkify_area(body), encoding="utf-8")


def build_town(t):
    path = f"/{t['slug']}/"
    url = SITE + path
    city = {"@type": "City", "name": f"{t['name']}, IL"}
    graph = [
        BUSINESS, WEBSITE,
        {"@type": "WebPage", "@id": url, "url": url, "name": t["title"], "description": t["desc"],
         "isPartOf": {"@id": f"{SITE}/#website"}, "breadcrumb": {"@id": f"{url}#breadcrumb"},
         "about": {"@id": f"{url}#service"}},
        {"@type": "Service", "@id": f"{url}#service",
         "name": f"Web design and local SEO in {t['name']}, IL",
         "serviceType": "Web design, website repair, and local SEO",
         "provider": {"@id": f"{SITE}/#business"}, "areaServed": city, "description": t["desc"]},
        breadcrumb(path, f"{t['name']}, IL"),
        faq_schema(t["faqs"], url),
    ]
    by = {x["slug"]: x for x in TOWN_PAGES}
    nearby = "".join(f'<a class="svc-link" href="/{s}/"><span>{by[s]["name"]}, IL</span><span aria-hidden="true">→</span></a>'
                     for s in t["nearby"])
    local = "".join(f"<p>{x}</p>" for x in t["local"])
    body = f"""{header()}
<main id="top">
  <section class="hero sub-hero">
    <div class="wrap sub-hero-wrap">
      <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span aria-current="page">{t["name"]}, IL</span></nav>
      <p class="eyebrow">{t["name"]}, Illinois {t["zip"]} · Web design &amp; local SEO</p>
      <h1>{t["h1"]}</h1>
      <p class="lede">{t["lede"]}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="/#contact">Get a free 10-minute review</a>
        <a class="btn btn-ghost" href="/#pricing">See pricing</a>
      </div>
      <p class="towns">Fixes from <b>$199</b> · Websites from <b>$950</b> · Local SEO <b>$399/month</b></p>
    </div>
  </section>

  <section>
    <div class="wrap two">
      <div class="prose">
        <p class="eyebrow">Local search in {t["name"]}</p>
        <h2 style="margin-top:.75rem">{t["local_h2"]}</h2>
        {local}
      </div>
      <div>
        <p class="eyebrow">What we do for {t["name"]} businesses</p>
        <ul class="feature-grid one-col">
          <li><h3><a href="/web-design/">New websites</a></h3><p>Phone-first sites with tap-to-call, your services and photos, and page titles that name {t["name"]}. Starter Site $950, Business Site $2,800.</p></li>
          <li><h3><a href="/website-repair/">Website fixes</a></h3><p>"Not secure" warnings, phone links that don't dial, broken forms, and old pages, fixed where your site lives now. From $199.</p></li>
          <li><h3><a href="/local-seo/">Local SEO</a></h3><p>Google Business Profile, reviews, and matching listings so you show up when someone in {t["name"]} searches. $399/month, no contract.</p></li>
        </ul>
        <p class="price-note">{t["meet"]} Prefer not to meet? Everything works over the phone or a short video call.</p>
      </div>
    </div>
  </section>
""" + STEPS_HTML + f"""
  <section class="sub-faq" id="faq">
    <div class="wrap two">
      <div>
        <p class="eyebrow">Questions</p>
        <h2 style="margin-top:.75rem">{t["name"]} questions.</h2>
        <p class="lede" style="margin-top:1rem">Something else on your mind? Email <a href="mailto:{EMAIL}">{EMAIL}</a> and you'll hear back within one business day.</p>
        <div class="svc-links"><p class="foot-h" style="color:var(--muted)">Nearby towns we serve</p>{nearby}</div>
      </div>
      <div>{faq_html(t["faqs"])}</div>
    </div>
  </section>
  <section class="cta-band">
    <div class="wrap">
      <h2>See how your {t["name"]} business shows up.</h2>
      <p class="lede">Tell us about your business. We'll look at your site and Google listing and reply within one business day with what we found. No pressure, no obligation.</p>
      <a class="btn btn-primary" href="/#contact">Request my free review</a>
    </div>
  </section>
</main>
{footer()}{SUB_SCRIPT}"""
    out = ROOT / t["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head(t["title"], t["desc"], path, graph) + "\n" + body, encoding="utf-8")


def build_home():
    f = ROOT / "index.html"
    h = f.read_text(encoding="utf-8")
    faqs = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>",
                      h.split('id="faq"', 1)[1])
    graph = [BUSINESS, WEBSITE,
             {"@type": "WebPage", "@id": f"{SITE}/", "url": f"{SITE}/",
              "name": HOME_TITLE, "description": HOME_DESC,
              "isPartOf": {"@id": f"{SITE}/#website"}, "about": {"@id": f"{SITE}/#business"}},
             faq_schema(faqs, f"{SITE}/")]
    new_head = head(HOME_TITLE, HOME_DESC, "/", graph)
    h = new_head + h.split("<body>\n", 1)[1]
    h = re.sub(r"<!--HEADER-->.*?<!--/HEADER-->",
               lambda m: "<!--HEADER-->\n" + header("") + "<!--/HEADER-->", h, flags=re.S)
    h = re.sub(r"<!--FOOTER-->.*?<!--/FOOTER-->",
               lambda m: "<!--FOOTER-->\n" + footer() + "<!--/FOOTER-->", h, flags=re.S)
    f.write_text(linkify_area(h), encoding="utf-8")


def build_404():
    body = f"""{header()}
<main id="top">
  <section class="hero sub-hero">
    <div class="wrap sub-hero-wrap">
      <p class="eyebrow">Error 404</p>
      <h1>That page took a wrong turn.</h1>
      <p class="lede">The link may be old or mistyped. Here's where most people are headed:</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="/">Go to the home page</a>
        <a class="btn btn-ghost" href="/#contact">Get a free site review</a>
      </div>
    </div>
  </section>
</main>
{footer()}{SUB_SCRIPT}"""
    h = head("Page not found | Six18 Web", "This page doesn't exist. Head back to Six18 Web for web design, website fixes, and local SEO.", "/404.html", [BUSINESS])
    h = h.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    (ROOT / "404.html").write_text(h + "\n" + body, encoding="utf-8")


def build_seo_files():
    urls = ["/"] + [p["path"] for p in PAGES] + [f"/{t['slug']}/" for t in TOWN_PAGES]
    items = "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + items + "</urlset>\n",
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")


HOME_TITLE = "Web Design & Local SEO in Edwardsville, IL | Six18 Web"
HOME_DESC = ("Web design, website fixes & local SEO for small businesses in Edwardsville, "
             "Glen Carbon & the Metro East. Flat prices. Free 10-minute site review.")

if __name__ == "__main__":
    build_home()
    for p in PAGES:
        build_service(p)
    for t in TOWN_PAGES:
        build_town(t)
    build_404()
    build_seo_files()
    print("built:", ["/"] + [p["path"] for p in PAGES] + [t["slug"] for t in TOWN_PAGES] + ["/404.html", "sitemap.xml", "robots.txt"])
