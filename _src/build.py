#!/usr/bin/env python3
"""Genera le pagine statiche EN e IT del sito dai template in _src/.

I template contengono i testi nell'oggetto JS `T` (en/it) e gli attributi
data-i18n / data-i18n-html. Qui li "cuociamo" nell'HTML, così Google legge
entrambe le lingue su URL distinti (/ e /it/) con hreflang.

Uso:  python3 _src/build.py   (dalla root del repo)
"""
import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
SITE = "https://www.alexdallolio.com"
LANGS = ("en", "it")

# Meta per pagina e lingua: path pubblico, title, description, og
PAGES = {
    "index": {
        "en": {
            "path": "/",
            "title": "Alex Dallolio — Film Director & AI Artist in Milan | Corporate and Brand Films",
            "description": "Film director and AI artist based in Milan. I turn the material you already have — archive, footage, product images, AI — into cinematic corporate and brand films. No traditional production required.",
            "og_title": "Alex Dallolio — Film Director & AI Artist",
            "og_description": "I turn the material you already have into cinematic brand films. No traditional production required.",
        },
        "it": {
            "path": "/it/",
            "title": "Alex Dallolio — Regista a Milano | Video aziendali, brand film e AI",
            "description": "Regista e AI artist a Milano. Trasformo il materiale che la tua azienda ha già (archivio, girato, immagini di prodotto) in video aziendali e brand film cinematografici, anche con l'AI generativa. Senza produzione tradizionale.",
            "og_title": "Alex Dallolio — Regista e AI Artist",
            "og_description": "Trasformo il materiale che hai già in video aziendali e brand film cinematografici. Senza produzione tradizionale.",
        },
    },
    "videos": {
        "en": {
            "path": "/videos.html",
            "title": "All Work — Alex Dallolio | Corporate, Fashion and AI Films",
            "description": "30 films directed by Alex Dallolio for Webuild, Prada, Fila, Canali, Luisa Spagnoli and more — corporate, fashion, documentary and AI-driven cinematic work.",
            "og_title": "All Work — Alex Dallolio",
            "og_description": "30 brand films directed by Alex Dallolio for Webuild, Prada, Fila, Canali, Luisa Spagnoli and more.",
        },
        "it": {
            "path": "/it/videos.html",
            "title": "Tutti i lavori — Alex Dallolio | Video aziendali, fashion film e AI",
            "description": "30 film diretti da Alex Dallolio per Webuild, Prada, Fila, Canali, Luisa Spagnoli e altri: video aziendali, fashion film, documentari e lavori con l'AI generativa.",
            "og_title": "Tutti i lavori — Alex Dallolio",
            "og_description": "30 film diretti da Alex Dallolio per Webuild, Prada, Fila, Canali, Luisa Spagnoli e altri.",
        },
    },
}

JSONLD_DESC = {
    "en": "Film director and AI artist based in Milan who turns existing material into cinematic corporate and brand films.",
    "it": "Regista e AI artist a Milano: trasforma il materiale esistente delle aziende in video aziendali e brand film cinematografici.",
}


def load_translations(src: str) -> dict:
    m = re.search(r"const T = (\{.*?\n\});", src, re.S)
    if not m:
        raise SystemExit("oggetto T non trovato")
    out = subprocess.run(
        ["node", "-e", f"process.stdout.write(JSON.stringify({m.group(1)}))"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def bake_i18n(src: str, t: dict) -> str:
    def repl(m, as_html):
        tag, attrs, key = m.group(1), m.group(2), m.group(3)
        if key not in t:
            return m.group(0)
        val = t[key] if as_html else html.escape(t[key], quote=False)
        return f"<{tag}{attrs}>{val}</{tag}>"

    for attr, as_html in (("data-i18n-html", True), ("data-i18n", False)):
        pat = re.compile(
            r'<(\w+)([^>]*\s' + attr + r'="([\w-]+)"[^>]*)>.*?</\1>', re.S)
        src = pat.sub(lambda m: repl(m, as_html), src)
    return src


def head_meta(page: str, lang: str) -> str:
    meta = PAGES[page][lang]
    alts = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE}{PAGES[page][l]["path"]}">'
        for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{PAGES[page]["en"]["path"]}">'
    return alts, meta


def render(page: str, lang: str) -> str:
    src = (SRC / f"{page}.template.html").read_text()
    T = load_translations(src)
    t = T[lang]
    meta = PAGES[page][lang]
    other = "it" if lang == "en" else "en"
    prefix = "/it/" if lang == "it" else "/"

    src = bake_i18n(src, t)
    src = src.replace('<html lang="en">', f'<html lang="{lang}">', 1)

    # <head>: title, description, canonical, hreflang, OG/Twitter
    e = lambda s: html.escape(s, quote=True)
    src = re.sub(r"<title>.*?</title>", f"<title>{e(meta['title'])}</title>", src, count=1)
    src = re.sub(r'<meta name="description" content="[^"]*">',
                 f'<meta name="description" content="{e(meta["description"])}">', src, count=1)
    alts, _ = head_meta(page, lang)
    src = re.sub(r'<link rel="canonical" href="[^"]*">',
                 f'<link rel="canonical" href="{SITE}{meta["path"]}">\n{alts}', src, count=1)
    for prop, key in (("og:title", "og_title"), ("og:description", "og_description"),
                      ("twitter:title", "og_title"), ("twitter:description", "og_description")):
        attr = "name" if prop.startswith("twitter") else "property"
        src = re.sub(rf'<meta {attr}="{prop}" content="[^"]*">',
                     f'<meta {attr}="{prop}" content="{e(meta[key])}">', src, count=1)
    src = re.sub(r'<meta property="og:url" content="[^"]*">',
                 f'<meta property="og:url" content="{SITE}{meta["path"]}">', src, count=1)
    loc = {"en": "en_US", "it": "it_IT"}
    src = re.sub(r'<meta property="og:locale" content="[^"]*">',
                 f'<meta property="og:locale" content="{loc[lang]}">', src, count=1)
    src = re.sub(r'<meta property="og:locale:alternate" content="[^"]*">',
                 f'<meta property="og:locale:alternate" content="{loc[other]}">', src, count=1)
    if page == "index":
        src = re.sub(r'("jobTitle": )"[^"]*"',
                     r'\1"' + ("Regista e AI Artist" if lang == "it" else "Film Director & AI Artist") + '"',
                     src, count=1)
        src = re.sub(r'("description": )"[^"]*"', r'\1"' + JSONLD_DESC[lang] + '"', src, count=1)

    # Selettore lingua: link veri tra le due versioni invece dello scambio via JS
    src = re.sub(
        r'<button class="lang-btn[^"]*" onclick="setLang\(\'en\'\)">EN</button>\s*'
        r'<button class="lang-btn[^"]*" onclick="setLang\(\'it\'\)">IT</button>',
        f'<a class="lang-btn{" active" if lang == "en" else ""}" href="{PAGES[page]["en"]["path"]}" hreflang="en">EN</a>\n'
        f'    <a class="lang-btn{" active" if lang == "it" else ""}" href="{PAGES[page]["it"]["path"]}" hreflang="it">IT</a>',
        src, count=1)

    # Percorsi assoluti (le pagine IT stanno in /it/) e link interni nella lingua giusta
    for asset in ("bg-reel.mp4", "ai-reel.mp4"):
        src = src.replace(f'src="{asset}"', f'src="/{asset}"')
    src = src.replace('href="videos.html"', f'href="{PAGES["videos"][lang]["path"]}"')
    # href="@chiave" → pagina servizio/caso nella lingua giusta
    import landing_pages as _LP
    src = re.sub(r'href="@(\w+)"', lambda m: f'href="{_LP.PAGES[m.group(1)][lang]["path"]}"', src)
    src = src.replace('href="index.html#', f'href="{prefix}#')
    src = src.replace('href="index.html"', f'href="{prefix}"')
    src = src.replace('<a href="#" class="logo">', f'<a href="{prefix}" class="logo">')

    # JS: via traduzioni e setLang, non servono più
    src = re.sub(r"// ── TRANSLATIONS ─+\nconst T = \{.*?\n\};\n\nlet currentLang = '\w+';\n\n"
                 r"function setLang\(lang\) \{.*?\n\}\n\n", "", src, count=1, flags=re.S)
    src = re.sub(r"// ── GEO DETECT ─+\n.*?\n\}\n\n", "", src, count=1, flags=re.S)
    src = src.replace("  setLang('en');\n", "").replace("detectLang();\n", "")
    if "setLang" in src or "const T" in src:
        raise SystemExit(f"{page}/{lang}: residui i18n JS nel file generato")
    if lang == "it":
        src = src.replace("&copy; 2026 Alex Dallolio. All rights reserved.",
                          "&copy; 2026 Alex Dallolio. Tutti i diritti riservati.")
        src = src.replace("Milan, Italy &mdash; Working globally", "Milano &mdash; Lavoro in tutto il mondo")
        src = src.replace('class="video-tag">Documentary<', 'class="video-tag">Documentario<')
        src = src.replace('class="video-tag">Concept &amp; Direction<', 'class="video-tag">Concept e regia<')
    return src


# ── Pagine servizi / casi studio ──────────────────────────────────
import sys
sys.path.insert(0, str(SRC))
import landing_pages as LP  # noqa: E402
import home_texts  # noqa: E402,F401


def film_html(f: dict) -> str:
    cap = f'<div class="cap"><strong>{f["t"]}</strong><span>{f["s"]}</span></div>'
    if "ig" in f:
        return (f'<div class="film film-ig"><iframe src="https://www.instagram.com/reel/{f["ig"]}/embed/" '
                f'title="{html.escape(f["t"])}" loading="lazy" scrolling="no" allowtransparency="true"></iframe>{cap}</div>')
    if "src" in f:
        return (f'<div class="film"><video src="{f["src"]}" poster="/og-image.jpg" controls playsinline preload="none" '
                f'style="width:100%;aspect-ratio:16/9;display:block;background:#111"></video>{cap}</div>')
    yt = f["yt"]
    return (f'<div class="film"><button type="button" data-yt="{yt}" aria-label="{html.escape(f["t"])}" '
            f'style="background-image:url(https://i.ytimg.com/vi/{yt}/hqdefault.jpg)"></button>{cap}</div>')


def render_landing(key: str, lang: str) -> str:
    d = LP.PAGES[key][lang]
    ui = LP.UI[lang]
    home = "/it/" if lang == "it" else "/"
    url = SITE + d["path"]
    e = lambda s: html.escape(s, quote=True)

    secs, faq_items, videos = [], [], []
    for sec in d["sections"]:
        kind, h2 = sec[0], sec[1]
        if kind == "prose":
            secs.append(f'<section><div class="prose"><h2>{h2}</h2>{sec[2]}</div></section>')
        elif kind == "films":
            secs.append(f'<section><div class="prose"><h2>{h2}</h2></div><div class="films">'
                        + "".join(film_html(f) for f in sec[2]) + "</div></section>")
            for f in sec[2]:
                if "yt" in f:
                    videos.append({"@type": "VideoObject", "name": f["t"], "description": f'{f["t"]}, {f["s"]}. Alex Dallolio.',
                                   "thumbnailUrl": f'https://i.ytimg.com/vi/{f["yt"]}/hqdefault.jpg',
                                   "embedUrl": f'https://www.youtube.com/embed/{f["yt"]}',
                                   "uploadDate": "2026-04-29"})
        elif kind == "reels":
            db_path = SRC / "aifilms.json"
            reels = json.loads(db_path.read_text()) if db_path.exists() else []
            tiles = []
            for r in reels:
                cap = html.escape(r["caption"] or "AI film")
                short = cap if len(cap) < 90 else cap[:88].rsplit(" ", 1)[0] + "…"
                tiles.append(
                    f'<figure class="reel"><button type="button" data-ig="{r["code"]}" aria-label="{short}" '
                    f'style="aspect-ratio:{r["w"]}/{r["h"]}"><video src="/aifilms/{r["code"]}.mp4" '
                    f'poster="/aifilms/{r["code"]}.jpg" muted loop playsinline preload="none"></video></button>'
                    f'<figcaption>{short}<time datetime="{r["date"]}">{r["date"][8:10]}.{r["date"][5:7]}.{r["date"][:4]}</time></figcaption></figure>')
                videos.append({"@type": "VideoObject", "name": short, "description": cap + ". Alex Dallolio, AI film.",
                               "thumbnailUrl": f'{SITE}/aifilms/{r["code"]}.jpg', "contentUrl": f'{SITE}/aifilms/{r["code"]}.mp4',
                               "uploadDate": r["date"], "duration": f'PT{int(round(r["duration"]))}S'})
            secs.append(f'<section><div class="prose"><h2>{h2}</h2></div><div class="reels">' + "".join(tiles) + "</div></section>")
        elif kind == "faq":
            items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in sec[2])
            secs.append(f'<section class="faq"><div class="prose"><h2>{h2}</h2></div>{items}</section>')
            faq_items += [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                          for q, a in sec[2]]

    rel = "".join(
        f'<a href="{LP.PAGES[k][lang]["path"]}"><strong>{LP.SHORT[k][lang][0]}</strong><span>{LP.SHORT[k][lang][1]}</span></a>'
        for k in LP.PAGES if k != key)
    secs.append(f'<section><div class="prose"><h2>{ui["related"]}</h2></div><div class="related">{rel}</div></section>')
    secs.append(f'''<section class="cta" id="contact"><h2>{ui["cta_h2"]}</h2><p>{ui["cta_p"]}</p>
<div class="cta-links"><a class="primary" href="https://calendly.com/alexdallolio" target="_blank" rel="noopener">{ui["cta_book"]}</a>
<a href="mailto:alexdallolio@alexdallolio.com">{ui["cta_email"]}</a></div></section>''')

    graph = [
        {"@type": "WebPage", "@id": url, "url": url, "name": d["title"], "description": d["description"],
         "inLanguage": lang, "author": {"@type": "Person", "name": "Alex Dallolio", "url": SITE + "/"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Alex Dallolio", "item": SITE + home},
            {"@type": "ListItem", "position": 2, "name": d["crumb"], "item": url}]},
    ]
    if key in ("archive", "ai"):
        graph.append({"@type": "Service", "name": d["crumb"], "description": d["description"],
                      "provider": {"@type": "Person", "name": "Alex Dallolio", "url": SITE + "/"},
                      "areaServed": "Worldwide", "url": url})
    if faq_items:
        graph.append({"@type": "FAQPage", "mainEntity": faq_items})
    graph += videos
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)

    alts = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{LP.PAGES[key][l]["path"]}">' for l in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{LP.PAGES[key]["en"]["path"]}">'
    lang_links = "".join(
        f'<a class="lang-btn{" active" if l == lang else ""}" href="{LP.PAGES[key][l]["path"]}" hreflang="{l}">{l.upper()}</a>'
        for l in LANGS)
    footer_links = " &middot; ".join(
        f'<a href="{LP.PAGES[k][lang]["path"]}">{LP.SHORT[k][lang][1]}</a>' for k in LP.PAGES)

    vals = {
        "lang": lang, "title": e(d["title"]), "description": e(d["description"]), "canonical": url,
        "hreflang": alts, "og_image": SITE + "/og-image.jpg", "og_locale": "it_IT" if lang == "it" else "en_US",
        "jsonld": jsonld, "home": home, "videos": PAGES["videos"][lang]["path"],
        "nav_work": ui["nav_work"], "nav_all": ui["nav_all"], "nav_contact": ui["nav_contact"],
        "lang_links": lang_links, "crumb": d["crumb"], "label": d["label"], "h1": d["h1"], "lede": d["lede"],
        "sections": "\n".join(secs), "footer_city": ui["footer_city"], "footer_links": footer_links,
    }
    out = (SRC / "landing.template.html").read_text()
    for k, v in vals.items():
        out = out.replace("{{" + k + "}}", v)
    if "{{" in out:
        raise SystemExit(f"{key}/{lang}: segnaposto non sostituiti")
    return out


def write_sitemap(groups):
    today = __import__("datetime").date.today().isoformat()
    rows = []
    for paths in groups:
        alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{paths[l]}"/>' for l in LANGS)
        alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{paths["en"]}"/>'
        for l in LANGS:
            rows.append(f"  <url>\n    <loc>{SITE}{paths[l]}</loc>\n    <lastmod>{today}</lastmod>{alts}\n  </url>")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
    print("scritto sitemap.xml")


def write(path: str, content: str):
    out = ROOT / (path.lstrip("/") + ("index.html" if path.endswith("/") else ""))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content)
    print("scritto", out.relative_to(ROOT))


# ── Home: "nuovo" (Non giro, dal 24/09/2026) oppure "classico" (Didot/oro) ──
# Per tornare al vecchio sito: HOME_STYLE = "classico", poi python3 _src/build.py e push.
# L'altra versione resta visibile (noindex) su /<nome>/ e /it/<nome>/.
HOME_STYLE = "nuovo"
ALT_HOME = {"nuovo": "classico", "classico": "nuovo"}[HOME_STYLE]


def render_home_new(lang: str, base: str, robots: str) -> str:
    import home_texts as H
    t = H.T[lang]
    other = "it" if lang == "en" else "en"
    e = lambda x: html.escape(x, quote=True)
    url = SITE + base
    frames = []
    for i, (yt, title, c_it, c_en, year) in enumerate(H.WORKS):
        sub = (c_it if lang == "it" else c_en) + (f" · {year}" if year else "")
        frames.append(
            f'      <div class="frame" data-yt="{yt}" data-t="{e(title)}"><button type="button" aria-label="{e(title)}">'
            f'<img src="https://i.ytimg.com/vi/{yt}/maxresdefault.jpg" alt="{e(title)}, {e(sub)}" loading="{"eager" if i < 3 else "lazy"}">'
            f'<span class="grain"></span><span class="lines"></span><span class="tag">{t["raw"]} · {i + 1:02d}</span>'
            f'<span class="play">{t["film"]}</span></button><div class="cap"><b>{e(title)}</b><span class="mono">{e(sub)}</span></div></div>')
    facts = "\n".join(f"  <p>{a} <span>{b}</span></p>" for a, b in t["facts"])
    links = "\n".join(f'    <a href="{h}">{txt}</a>' for txt, h in t["links"])
    alt = {l: SITE + ("/it/" if l == "it" else "/") for l in LANGS}
    hreflang = "" if robots else "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{alt[l]}">' for l in LANGS) + f'\n<link rel="alternate" hreflang="x-default" href="{alt["en"]}">'
    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "Person", "name": "Alex Dallolio", "alternateName": "Alessandro Dallolio",
        "jobTitle": "Regista e AI Artist" if lang == "it" else "Film Director & AI Artist",
        "description": t["description"], "url": SITE + "/", "image": SITE + "/og-image.jpg",
        "address": {"@type": "PostalAddress", "addressLocality": "Milano" if lang == "it" else "Milan", "addressCountry": "IT"},
        "sameAs": ["https://www.youtube.com/@alchemistfilm-d4k", "https://www.instagram.com/alexdallolio_aifilms/",
                   "https://vimeo.com/alexdallolio", "https://www.linkedin.com/in/alexdallolio/"]},
        ensure_ascii=False, indent=1)
    other_href = ("/" if lang == "it" else "/it/") + (ALT_HOME + "/" if robots else "")
    vals = {
        "lang": lang, "title": e(t["title"]), "description": e(t["description"]), "robots": robots,
        "canonical": url, "hreflang": hreflang, "og_title": e(t["og_title"]), "og_description": e(t["og_description"]),
        "og_locale": "it_IT" if lang == "it" else "en_US", "jsonld": jsonld,
        "nav1": t["nav"][0], "nav2": t["nav"][1], "nav3": t["nav"][2],
        "h1": t["h1"], "sub": t["sub"], "role": t["role"], "scroll": t["scroll"],
        "nworks": f"{len(H.WORKS):02d}", "frames": "\n".join(frames), "prev": t["prev"], "next": t["next"], "legend": t["legend"],
        "facts": facts, "links": links, "tac_h": t["tac_h"], "tac_href": t["tac_all"][1], "tac_all": t["tac_all"][0],
        "who_h": t["who_h"], "bio": t["bio"], "clients_label": t["clients_label"], "brands": H.BRANDS, "agencies": t["agencies"],
        "book": t["book"], "other_lang": t["other_lang"][0], "other_href": other_href, "other_code": other, "close": t["close"],
    }
    out = (SRC / "home.template.html").read_text()
    for k, v in vals.items():
        out = out.replace("{{" + k + "}}", v)
    if "{{" in out:
        raise SystemExit(f"home/{lang}: segnaposto non sostituiti: {re.findall(r'{{(\\w+)}}', out)}")
    return out


def noindex(src: str, lang: str, base: str) -> str:
    """Versione alternativa della home: visibile ma fuori da Google."""
    src = src.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n<meta name="robots" content="noindex, follow">', 1)
    src = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n?', "", src)
    src = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{SITE}{base}">', src, count=1)
    # selettore lingua: resta dentro la versione alternativa
    other_base = ("/" if lang == "it" else "/it/") + ALT_HOME + "/"
    src = re.sub(r'(<a class="lang-btn[^"]*" href=")/(?:it/)?(" hreflang="(?:en|it)">)',
                 lambda m: m.group(1) + (("/it/" if "it" in m.group(2) else "/") + ALT_HOME + "/") + m.group(2), src)
    return src


def main():
    groups = []
    for lang in LANGS:
        base = "/it/" if lang == "it" else "/"
        alt_base = base + ALT_HOME + "/"
        classic = render("index", lang)
        new = render_home_new(lang, base if HOME_STYLE == "nuovo" else alt_base,
                              "" if HOME_STYLE == "nuovo" else '<meta name="robots" content="noindex, follow">\n')
        if HOME_STYLE == "nuovo":
            write(base, new)
            write(alt_base, noindex(classic, lang, alt_base))
        else:
            write(base, classic)
            write(alt_base, new)
    groups.append({l: PAGES["index"][l]["path"] for l in LANGS})
    for page in PAGES:
        if page == "index":
            continue
        for lang in LANGS:
            write(PAGES[page][lang]["path"], render(page, lang))
        groups.append({l: PAGES[page][l]["path"] for l in LANGS})
    for key in LP.PAGES:
        for lang in LANGS:
            write(LP.PAGES[key][lang]["path"], render_landing(key, lang))
        groups.append({l: LP.PAGES[key][l]["path"] for l in LANGS})
    write_sitemap(groups)
    # Copia pubblica dei reel per le altre pagine (es. la home): /aifilms/reels.json
    db = SRC / "aifilms.json"
    if db.exists():
        (ROOT / "aifilms").mkdir(exist_ok=True)
        (ROOT / "aifilms" / "reels.json").write_text(db.read_text())


if __name__ == "__main__":
    main()
