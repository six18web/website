#!/usr/bin/env python3
"""Six18 Web Starter Site generator.

Builds a one-page, phone-first client website from a JSON config.

  python3 tools/starter/starter.py tools/starter/config.example.json  out/sample

Output folder gets: index.html, robots.txt, sitemap.xml, CNAME (if domain set).
Put client photos in the output folder and list them in "photos" / "hero_photo" / "logo".
Every page section and the Google structured data come from the config, so the
same template works for roofers, salons, auto shops, and restaurants.
"""
import html, json, sys, datetime
from pathlib import Path

e = lambda s: html.escape(str(s), quote=True)


def tel(phone):
    digits = "".join(c for c in phone if c.isdigit())
    return "+1" + digits[-10:] if len(digits) >= 10 else digits


def build(cfg, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    c = cfg
    town_st = f'{c["town"]}, {c["state"]}'
    url = f'https://{c["domain"]}/' if c.get("domain") else "/"
    title = f'{c["trade"]} in {town_st} | {c["business"]}'
    desc = c["tagline"] + " " + f'Call {c["phone"]} for a free estimate.' if c.get("phone") else c["tagline"]
    desc = desc[:158]
    brand, accent = c["colors"]["brand"], c["colors"]["accent"]
    phone_href = "tel:" + tel(c["phone"])

    schema = {
        "@context": "https://schema.org",
        "@type": c.get("schema_type") or "LocalBusiness",
        "name": c["business"], "url": url, "telephone": c["phone"],
        "email": c.get("email") or None, "description": c["tagline"],
        "image": (url + c["hero_photo"]) if c.get("hero_photo") else None,
        "logo": (url + c["logo"]) if c.get("logo") else None,
        "address": {"@type": "PostalAddress", "addressLocality": c["town"], "addressRegion": c["state"],
                    "postalCode": c["zip"], "addressCountry": "US",
                    **({"streetAddress": c["street"]} if c.get("show_address") and c.get("street") else {})},
        "areaServed": [{"@type": "City", "name": f"{t}, {c['state']}"} for t in c["service_area"]],
        "sameAs": [u for u in (c.get("facebook"), c.get("instagram"), c.get("google_reviews_url")) if u],
        "foundingDate": c.get("year_founded") or None,
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "description": s["text"]}}
                       for s in c["services"]],
    }
    schema = {k: v for k, v in schema.items() if v not in (None, [], "")}

    badges = "".join(f"<li>{e(b)}</li>" for b in c.get("badges", []))
    services = "".join(f'<article class="svc"><h3>{e(s["name"])}</h3><p>{e(s["text"])}</p></article>' for s in c["services"])
    photos = "".join(f'<img src="{e(p["src"])}" alt="{e(p["alt"])}" loading="lazy" width="800" height="600">'
                     for p in c.get("photos", []))
    reviews = "".join(f'<figure class="rev"><blockquote>“{e(r["quote"])}”</blockquote><figcaption>{e(r["name"])} · {e(r.get("source", "Google"))}</figcaption></figure>'
                      for r in c.get("reviews", []))
    hours = "".join(f"<tr><th>{e(d)}</th><td>{e(h)}</td></tr>" for d, h in c.get("hours", []))
    towns = "".join(f"<li>{e(t)}</li>" for t in c["service_area"])
    map_q = (c["street"] + ", " if c.get("show_address") and c.get("street") else "") + f'{c["town"]}, {c["state"]} {c["zip"]}'
    socials = "".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{n}</a>' for n, u in
                      (("Facebook", c.get("facebook")), ("Instagram", c.get("instagram")), ("Google reviews", c.get("google_reviews_url"))) if u)
    logo = f'<img src="{e(c["logo"])}" alt="{e(c["business"])} logo" height="40">' if c.get("logo") else f'<span class="wordmark">{e(c["short_name"])}</span>'
    hero_bg = f"background-image:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,.55)),url('{e(c['hero_photo'])}');background-size:cover;background-position:center;" if c.get("hero_photo") else ""
    address_line = e(c["street"]) + "<br>" if c.get("show_address") and c.get("street") else ""
    reviews_section = f'<section class="band reviews" id="reviews"><div class="wrap"><h2>What customers say</h2><div class="rev-grid">{reviews}</div>' + \
        (f'<p class="more"><a href="{e(c["google_reviews_url"])}" target="_blank" rel="noopener">Read more reviews on Google →</a></p>' if c.get("google_reviews_url") else "") + \
        "</div></section>" if reviews else ""
    photos_section = f'<div class="gallery">{photos}</div>' if photos else ""

    form = c.get("form", {})
    if form.get("kind") == "google" and form.get("google_form_action"):
        form_js = f"""const ACTION={json.dumps(form["google_form_action"])};const FIELDS={json.dumps(form["fields"])};
const body=new URLSearchParams();Object.entries(FIELDS).forEach(([id,entry])=>body.append(entry,v(id)));
await fetch(ACTION,{{method:'POST',mode:'no-cors',body}});"""
    else:
        form_js = f"""location.href='mailto:'+{json.dumps(c.get("email", ""))}+'?subject='+encodeURIComponent('Estimate request from '+v('f-name'))+'&body='+encodeURIComponent(['Name: '+v('f-name'),'Phone: '+v('f-phone'),'Email: '+v('f-email'),'Service: '+v('f-svc'),'',v('f-msg')].join('\\n'));"""
    svc_options = "".join(f"<option>{e(s['name'])}</option>" for s in c["services"]) + "<option>Something else</option>"

    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{e(url)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{e(url)}">
{f'<meta property="og:image" content="{e(url + c["hero_photo"])}">' if c.get("hero_photo") else ""}
<meta name="theme-color" content="{e(brand)}">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
<style>
:root{{--brand:{brand};--accent:{accent};--ink:#16191F;--muted:#535B66;--bg:#FFFFFF;--soft:#F3F5F8;--line:#DDE2E8}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}
body{{margin:0;font:400 1.0625rem/1.6 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:var(--bg);padding-bottom:72px}}
img{{max-width:100%;height:auto;display:block}}a{{color:var(--brand)}}
h1,h2,h3{{line-height:1.12;margin:0;letter-spacing:-.01em}}
h2{{font-size:clamp(1.7rem,4vw,2.4rem);margin-bottom:1.25rem}}
.wrap{{max-width:1100px;margin:0 auto;padding:0 max(16px,env(safe-area-inset-left))}}
section{{padding:clamp(48px,8vw,88px) 0}}.band{{background:var(--soft)}}
:focus-visible{{outline:3px solid var(--accent);outline-offset:3px}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;font-weight:700;padding:.95rem 1.4rem;border-radius:999px;text-decoration:none;border:2px solid transparent;cursor:pointer;font-size:1rem}}
.btn-accent{{background:var(--accent);color:#fff}}.btn-line{{border-color:currentColor;color:inherit;background:transparent}}
header{{position:sticky;top:0;z-index:10;background:#fff;border-bottom:1px solid var(--line)}}
header .wrap{{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding-block:.7rem}}
.wordmark{{font-weight:800;font-size:1.2rem;color:var(--brand)}}
header nav{{display:flex;gap:1.25rem;font-weight:600}}header nav a{{text-decoration:none;color:var(--muted)}}
@media(max-width:760px){{header nav,header .btn{{display:none}}}}
.hero{{background:var(--brand);color:#fff;{hero_bg}}}
.hero h1{{font-size:clamp(2.2rem,6vw,3.8rem);font-weight:800;max-width:18ch}}.hero h1 em{{font-style:normal;color:var(--accent)}}
.hero p.intro{{font-size:1.15rem;max-width:56ch;margin:1.1rem 0 1.75rem;opacity:.92}}
.ctas{{display:flex;flex-wrap:wrap;gap:.75rem}}
.badges{{list-style:none;padding:0;margin:1.75rem 0 0;display:flex;flex-wrap:wrap;gap:.5rem}}
.badges li{{background:rgba(255,255,255,.14);padding:.45rem .8rem;border-radius:999px;font-size:.9rem;font-weight:600}}
.svc-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem}}
.svc{{border:1px solid var(--line);border-top:4px solid var(--accent);border-radius:12px;padding:1.4rem;background:#fff}}
.svc p{{color:var(--muted);margin:.5rem 0 0}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,5vw,56px);align-items:start}}@media(max-width:820px){{.two{{grid-template-columns:1fr}}}}
.gallery{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:.6rem;margin-top:1.5rem}}.gallery img{{border-radius:10px;aspect-ratio:4/3;object-fit:cover}}
.rev-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}}
.rev{{margin:0;background:#fff;border-radius:12px;padding:1.4rem;border:1px solid var(--line)}}
.rev blockquote{{margin:0 0 .75rem;font-size:1.05rem}}.rev figcaption{{color:var(--muted);font-weight:600;font-size:.92rem}}
.more{{margin-top:1.25rem;font-weight:700}}
table{{border-collapse:collapse;width:100%}}th,td{{text-align:left;padding:.55rem 0;border-bottom:1px solid var(--line)}}th{{font-weight:600;width:40%}}
.towns{{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:.45rem}}.towns li{{border:1px solid var(--line);border-radius:999px;padding:.35rem .75rem;background:#fff;font-size:.92rem}}
.map{{width:100%;aspect-ratio:4/3;border:0;border-radius:12px;margin-top:1rem}}
form{{display:grid;gap:.9rem}}label{{font-weight:600;font-size:.92rem;display:block;margin-bottom:.3rem}}
input,select,textarea{{width:100%;font:inherit;padding:.75rem .85rem;border:1.5px solid var(--line);border-radius:8px;background:#fff}}
input:focus,select:focus,textarea:focus{{outline:none;border-color:var(--brand)}}textarea{{min-height:110px}}
.ok{{background:var(--soft);padding:1rem;border-radius:10px;font-weight:600}}
footer{{background:var(--ink);color:#C9CFD8;padding:2.5rem 0 1.5rem;font-size:.95rem}}footer a{{color:#fff}}
footer .wrap{{display:flex;flex-wrap:wrap;justify-content:space-between;gap:1.5rem}}.credit{{opacity:.7;font-size:.85rem}}
.callbar{{position:fixed;left:0;right:0;bottom:0;z-index:20;display:flex;gap:.5rem;padding:.6rem max(12px,env(safe-area-inset-left)) calc(.6rem + env(safe-area-inset-bottom));background:#fff;border-top:1px solid var(--line)}}
.callbar .btn{{flex:1;padding:.85rem}}@media(min-width:900px){{.callbar{{display:none}}body{{padding-bottom:0}}}}
</style>
</head>
<body>
<header><div class="wrap">
  <a href="#top" style="text-decoration:none">{logo}</a>
  <nav aria-label="Main"><a href="#services">Services</a><a href="#about">About</a>{'<a href="#reviews">Reviews</a>' if reviews else ''}<a href="#contact">Contact</a></nav>
  <a class="btn btn-accent" href="{phone_href}">Call {e(c["phone"])}</a>
</div></header>
<main id="top">
<section class="hero"><div class="wrap">
  <p style="font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.85rem;opacity:.85">{e(c["trade"])} · {e(town_st)}</p>
  <h1>{c["headline"]}</h1>
  <p class="intro">{e(c["intro"])}</p>
  <div class="ctas"><a class="btn btn-accent" href="#contact">{e(c["primary_cta"])}</a><a class="btn btn-line" href="{phone_href}">Call {e(c["phone"])}</a></div>
  <ul class="badges">{badges}</ul>
</div></section>
<section id="services"><div class="wrap">
  <h2>{e(c.get("services_title") or "Services in " + c["town"])}</h2>
  <div class="svc-grid">{services}</div>
</div></section>
<section class="band" id="about"><div class="wrap{' two' if photos else ''}">
  <div style="max-width:68ch"><h2>About {e(c["short_name"])}</h2><p>{e(c["about"])}</p></div>
  {f'<div>{photos_section}</div>' if photos else ''}
</div></section>
{reviews_section}
<section id="area"><div class="wrap two">
  <div><h2>Where we work</h2><p>Based in {e(town_st)}, serving:</p><ul class="towns">{towns}</ul>
    <iframe class="map" title="Map of {e(c['town'])}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={e(map_q.replace(' ', '+'))}&output=embed"></iframe></div>
  <div><h2>Hours</h2><table>{hours}</table></div>
</div></section>
<section class="band" id="contact"><div class="wrap two">
  <div><h2>{e(c["primary_cta"])}</h2><p>Call or text <a href="{phone_href}"><b>{e(c["phone"])}</b></a>{f', email <a href="mailto:{e(c["email"])}">{e(c["email"])}</a>' if c.get("email") else ''}, or send the form and we'll get back to you within one business day.</p></div>
  <form id="f" novalidate>
    <div><label for="f-name">Name</label><input id="f-name" autocomplete="name" required></div>
    <div><label for="f-phone">Phone</label><input id="f-phone" type="tel" autocomplete="tel" required></div>
    <div><label for="f-email">Email (optional)</label><input id="f-email" type="email" autocomplete="email"></div>
    <div><label for="f-svc">What do you need?</label><select id="f-svc">{svc_options}</select></div>
    <div><label for="f-msg">Details (optional)</label><textarea id="f-msg"></textarea></div>
    <button class="btn btn-accent" type="submit">Send request</button>
    <p class="ok" id="f-ok" hidden>Thanks! We got your request and will be in touch soon.</p>
  </form>
</div></section>
</main>
<footer><div class="wrap">
  <div><b style="color:#fff">{e(c["business"])}</b><br>{address_line}{e(town_st)} {e(c["zip"])}<br><a href="{phone_href}">{e(c["phone"])}</a></div>
  <div>{socials}</div>
  <div class="credit">© <span id="yr">{datetime.date.today().year}</span> {e(c["business"])}<br>Website by <a href="https://six18web.com/">Six18 Web</a></div>
</div></footer>
<div class="callbar"><a class="btn btn-accent" href="{phone_href}">Call now</a><a class="btn btn-line" style="color:var(--brand)" href="#contact">{e(c.get("bar_cta", "Get a quote"))}</a></div>
<script>
document.getElementById('yr').textContent=new Date().getFullYear();
const v=id=>document.getElementById(id).value.trim();
document.getElementById('f').addEventListener('submit',async ev=>{{ev.preventDefault();
const ok=document.getElementById('f-ok');
if(!v('f-name')||!v('f-phone')){{ok.textContent='Please add your name and phone number.';ok.hidden=false;return;}}
try{{ {form_js} }}catch(err){{}}
ok.textContent='Thanks! We got your request and will be in touch soon.';ok.hidden=false;}});
</script>
</body>
</html>
"""
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n" + (f"\nSitemap: {url}sitemap.xml\n" if c.get("domain") else ""), encoding="utf-8")
    if c.get("domain"):
        (out / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{url}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url></urlset>\n', encoding="utf-8")
        (out / "CNAME").write_text(c["domain"] + "\n", encoding="utf-8")
    return out / "index.html"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: starter.py <config.json> <output folder>")
    print(build(json.loads(Path(sys.argv[1]).read_text()), sys.argv[2]))
