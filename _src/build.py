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


def main():
    for page in PAGES:
        for lang in LANGS:
            path = PAGES[page][lang]["path"]
            out = ROOT / (path.lstrip("/") + ("index.html" if path.endswith("/") else ""))
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render(page, lang))
            print("scritto", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
