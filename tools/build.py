#!/usr/bin/env python3
"""
Byggeskript for Grimstad Bokseklubb.

Skriver ferdige, statiske HTML-sider til prosjektroten. Rediger innholdet her
og kjør:

    python3 tools/build.py

Ingen avhengigheter utenom Python 3.
"""

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://grimstadbk.com"
PHONE = "+47 917 91 563"
PHONE_HREF = "+4791791563"
EMAIL = "grimstadbk@gmail.com"
FB = "https://www.facebook.com/GRIMSTAD.BK/"
IG = "https://www.instagram.com/grimstad_bokseklubb/"
FB_GROUP = "https://www.facebook.com/groups/213753828680277/"

# --------------------------------------------------------------------------
# Små hjelpere
# --------------------------------------------------------------------------


def asset_widths(name):
    widths = [
        w for w in (640, 1024, 1600) if (ROOT / f"assets/img/{name}-{w}.webp").exists()
    ]
    return widths or [640]


def image(name, alt, prefix="", sizes="100vw", eager=False, cls=""):
    widths = asset_widths(name)
    largest = widths[-1]
    srcset = ", ".join(
        f"{prefix}assets/img/{name}-{w}.webp {w}w" for w in widths
    )
    loading = "eager" if eager else "lazy"
    fetch = ' fetchpriority="high"' if eager else ""
    klass = f' class="{cls}"' if cls else ""
    return (
        f'<img src="{prefix}assets/img/{name}-{largest}.webp" '
        f'srcset="{srcset}" sizes="{sizes}" width="{largest}" '
        f'height="{largest}" alt="{alt}" loading="{loading}" decoding="async"{fetch}{klass}>'
    )


def largest(name, prefix=""):
    return f"{prefix}assets/img/{name}-{asset_widths(name)[-1]}.webp"


ICON_FB = (
    '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M13.5 22v-8h2.8l.4-3.2h-3.2V8.7c0-.9.3-1.6 1.7-1.6h1.6V4.2c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.4-4 4.1v2.6H7.5V14h2.9v8h3.1z"/>'
    "</svg>"
)
ICON_IG = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
    '<rect x="3.5" y="3.5" width="17" height="17" rx="4.5"/>'
    '<circle cx="12" cy="12" r="4"/>'
    '<circle cx="17.2" cy="6.8" r="1" fill="currentColor" stroke="none"/>'
    "</svg>"
)
ICON_PIN = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
    '<path d="M12 21s7-5.4 7-11a7 7 0 1 0-14 0c0 5.6 7 11 7 11z"/>'
    '<circle cx="12" cy="10" r="2.5"/>'
    "</svg>"
)
ICON_PHONE = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
    '<path d="M6.5 3.5h3l1.5 4-2 1.5a12 12 0 0 0 6 6l1.5-2 4 1.5v3a2 2 0 0 1-2.2 2A17 17 0 0 1 4.5 5.7a2 2 0 0 1 2-2.2z"/>'
    "</svg>"
)
ICON_MAIL = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
    '<rect x="3.5" y="5.5" width="17" height="13" rx="1.5"/>'
    '<path d="m4.5 7 7.5 6 7.5-6"/>'
    "</svg>"
)
ICON_ARROW = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
    '<path d="M4 12h15M13 6l6 6-6 6"/></svg>'
)

# --------------------------------------------------------------------------
# Felles tekster
# --------------------------------------------------------------------------

NAV = {
    "no": [
        ("index.html", "Hjem"),
        ("om-oss.html", "Om oss"),
        ("trening.html", "Trening"),
        ("kontakt.html", "Kontakt"),
    ],
    "en": [
        ("index.html", "Home"),
        ("about.html", "About"),
        ("training.html", "Training"),
        ("contact.html", "Contact"),
    ],
}

UI = {
    "no": {
        "lang": "nb",
        "lang_label": "Norsk",
        "skip": "Hopp til innhold",
        "menu": "Meny",
        "main_nav": "Hovedmeny",
        "brand_home": "Grimstad Bokseklubb – til forsiden",
        "logo_alt": "Grimstad Bokseklubb logo",
        "cta": "Prøv gratis",
        "footer_pages": "Sider",
        "footer_contact": "Kontakt",
        "footer_support": "Støtt klubben",
        "footer_tagline": "Boksing for alle i Grimstad siden 1972. Mosjon, mestring og kamp – i samme klubb.",
        "privacy": "Personvern",
        "copyright": "Grimstad Bokseklubb",
        "social_label": "Grimstad Bokseklubb på Facebook",
        "social_ig": "Grimstad Bokseklubb på Instagram",
        "follow": "Følg oss",
        "since": "Boksing for alle siden 1972",
        "lightbox": "Bildegalleri",
        "prev": "Forrige bilde",
        "next": "Neste bilde",
        "close": "Lukk",
    },
    "en": {
        "lang": "en",
        "lang_label": "English",
        "skip": "Skip to content",
        "menu": "Menu",
        "main_nav": "Main navigation",
        "brand_home": "Grimstad Bokseklubb – home",
        "logo_alt": "Grimstad Bokseklubb logo",
        "cta": "Try for free",
        "footer_pages": "Pages",
        "footer_contact": "Contact",
        "footer_support": "Support the club",
        "footer_tagline": "Boxing for everyone in Grimstad since 1972. Fitness, confidence and competition under one roof.",
        "privacy": "Privacy",
        "copyright": "Grimstad Bokseklubb",
        "social_label": "Grimstad Bokseklubb on Facebook",
        "social_ig": "Grimstad Bokseklubb on Instagram",
        "follow": "Follow us",
        "since": "Boxing for everyone since 1972",
        "lightbox": "Photo gallery",
        "prev": "Previous image",
        "next": "Next image",
        "close": "Close",
    },
}

WEEK = {
    "no": {
        "day": "Dag",
        "time": "Tid",
        "class": "Økt",
        "desc": "Beskrivelse",
        "note": "Treningstidene kan endres i ferier og på stevnehelger. Sjekk Facebook eller Instagram før du kommer.",
    },
    "en": {
        "day": "Day",
        "time": "Time",
        "class": "Session",
        "desc": "Description",
        "note": "Times can change during holidays and competition weekends. Check Facebook or Instagram before you come.",
    },
}

SCHEDULE = {
    "no": [
        ("Mandag", "19:00–20:30", "Boksing, viderekomne", "Teknikk og sparring for deg som har trent en stund."),
        ("Tirsdag", "18:00–19:30", "Boksing, alle", "Grunnleggende teknikk og allsidig trening for alle nivåer."),
        ("Onsdag", "18:00–19:00", "Sekkøkt, alle", "Kondisjon og slagteknikk på sekken."),
        ("Torsdag", "17:30–18:30", "Boks stødig", "Rolig økt med balanse, fotarbeid og teknikk."),
        ("Torsdag", "19:00–20:30", "Boksing, alle", "Boksing for alle – en god avslutning på uken."),
    ],
    "en": [
        ("Monday", "19:00–20:30", "Boxing, advanced", "Technique and sparring for members with some experience."),
        ("Tuesday", "18:00–19:30", "Boxing, all levels", "Basic technique and all-round training for every level."),
        ("Wednesday", "18:00–19:00", "Bag session, all", "Conditioning and punching technique on the heavy bag."),
        ("Thursday", "17:30–18:30", "Steady boxing", "A calmer session focused on balance, footwork and technique."),
        ("Thursday", "19:00–20:30", "Boxing, all levels", "Boxing for everyone – a good way to end the week."),
    ],
}


def schedule(lang, light=False, with_desc=True):
    rows = SCHEDULE[lang]
    labels = WEEK[lang]
    cls = "schedule schedule--light" if light else "schedule"
    head = f'<th scope="col">{labels["day"]}</th><th scope="col">{labels["time"]}</th><th scope="col">{labels["class"]}</th>'
    if with_desc:
        head += f'<th scope="col">{labels["desc"]}</th>'
    body = ""
    for day, time, name, desc in rows:
        body += f'<tr><td class="day">{day}</td><td class="time">{time}</td><td>{name}</td>'
        if with_desc:
            body += f'<td class="desc">{desc}</td>'
        body += "</tr>"
    return (
        f'<div class="schedule-wrap"><table class="{cls}">'
        f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"
    )


def support_block(lang, prefix=""):
    no = lang == "no"
    title = "Hjelp oss å holde ringen åpen" if no else "Help us keep the ring open"
    text = (
        "Klubben drives av frivillige og medlemskontingent. Vil du sponse, bidra på dugnad eller gi en støtte, setter vi stor pris på det."
        if no
        else "The club is run by volunteers and membership fees. If you want to sponsor us, help out or make a donation, we are very grateful."
    )
    return f"""
<section class="section">
  <div class="container">
    <div class="support" data-reveal>
      <div>
        <span class="eyebrow">{"Støtt klubben" if no else "Support the club"}</span>
        <h2>{title}</h2>
        <p>{text}</p>
        <p class="u-mt-2"><a class="btn" href="{FILES[lang]["contact"]}">{"Ta kontakt" if no else "Get in touch"} {ICON_ARROW}</a></p>
      </div>
    </div>
  </div>
</section>
"""


def cta_band(lang, prefix="", title=None, text=None):
    no = lang == "no"
    title = title or ("Første trening er gratis" if no else "Your first session is free")
    text = text or (
        "Bare møt opp i treningstøy – vi viser deg rundt og hjelper deg i gang."
        if no
        else "Just show up in training clothes – we will show you around and help you get started."
    )
    href = FILES[lang]["contact"]
    label = "Prøv en trening" if no else "Try a session"
    return f"""
<section class="section section--tight">
  <div class="container">
    <div class="cta-band" data-reveal>
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <a class="btn" href="{href}">{label} {ICON_ARROW}</a>
    </div>
  </div>
</section>
"""


GALLERY_ITEMS = [
    {
        "img": "hero",
        "wide": True,
        "alt_no": "To boksere sparrer i ringen mens en trener følger med",
        "alt_en": "Two boxers sparring in the ring while a coach watches",
        "cap_no": "Sparring i ringen – treneren følger med fra siden.",
        "cap_en": "Sparring in the ring – the coach watches from the side.",
    },
    {
        "img": "bout1",
        "alt_no": "Kamp i ringen mellom bokser i rødt og bokser i blått",
        "alt_en": "Bout in the ring between a boxer in red and a boxer in blue",
        "cap_no": "Kamp mellom rød og blå bokser.",
        "cap_en": "Bout between the red and the blue boxer.",
    },
    {
        "img": "corner2",
        "alt_no": "Treneren snakker med bokseren i blått som sitter i hjørnet",
        "alt_en": "The coach talking to the boxer in blue seated in the corner",
        "cap_no": "Råd i hjørnet mellom rundene.",
        "cap_en": "Advice in the corner between rounds.",
    },
    {
        "img": "sparring2",
        "alt_no": "To boksere med svart bokserhjelm sparrer mens dommeren ser på",
        "alt_en": "Two boxers in black headgear sparring while the referee watches",
        "cap_no": "Sparring med dommeren i ringen.",
        "cap_en": "Sparring with the referee in the ring.",
    },
    {
        "img": "trening",
        "alt_no": "Tre boksere fra Grimstad Bokseklubb i treningstøy",
        "alt_en": "Three boxers from Grimstad Bokseklubb in training kit",
        "cap_no": "Klare for trening i Frivoldveien.",
        "cap_en": "Ready for training in Frivoldveien.",
    },
    {
        "img": "group1",
        "wide": True,
        "alt_no": "Gruppbilde av klubbens boksere på de røde mattene",
        "alt_en": "Group photo of the club's boxers on the red mats",
        "cap_no": "Klubben samlet på de røde mattene.",
        "cap_en": "The club gathered on the red mats.",
    },
    {
        "img": "corner3",
        "alt_no": "Treneren gir råd til bokseren i rødt gjennom ringtauene",
        "alt_en": "The coach giving advice to the boxer in red through the ropes",
        "cap_no": "Samtale gjennom ringtauene.",
        "cap_en": "A talk through the ropes.",
    },
    {
        "img": "group2",
        "wide": True,
        "alt_no": "Gruppbilde foran sekkestativene og klubbflaggene",
        "alt_en": "Group photo in front of the punching bags and club flags",
        "cap_no": "Lagbilde i hallen.",
        "cap_en": "Team photo in the gym.",
    },
    {
        "img": "bout2",
        "alt_no": "Kamp i ringen med dommeren og publikum langs ringtauene",
        "alt_en": "Bout in the ring with the referee and spectators along the ropes",
        "cap_no": "Kamp med publikum langs ringen.",
        "cap_en": "Bout with spectators along the ropes.",
    },
    {
        "img": "group3",
        "wide": True,
        "alt_no": "Stort gruppbilde av klubben med flagg og røde matter",
        "alt_en": "Large group photo of the club with flags and red mats",
        "cap_no": "Hele klubben samlet for bilde.",
        "cap_en": "The whole club gathered for a photo.",
    },
    {
        "img": "bout3",
        "alt_no": "Kamp i ringen med boksere i rødt og blått og dommeren tett på",
        "alt_en": "Bout in the ring with boxers in red and blue and the referee close by",
        "cap_no": "Kamp med dommeren tett på.",
        "cap_en": "Bout with the referee close by.",
    },
    {
        "img": "corner1",
        "wide": True,
        "alt_no": "Treneren står på kne ved bokseren i rødt som hviler på gulvet",
        "alt_en": "The coach kneeling beside the boxer in red resting on the floor",
        "cap_no": "En rolig stund med treneren på gulvet.",
        "cap_en": "A quiet moment with the coach on the floor.",
    },
]


def gallery_grid(lang, prefix, limit=None):
    items = GALLERY_ITEMS[:limit] if limit else GALLERY_ITEMS
    out = []
    for item in items:
        wide = " gallery-item--wide" if item.get("wide") else ""
        sizes = (
            "(max-width: 900px) 100vw, 66vw"
            if item.get("wide")
            else "(max-width: 900px) 100vw, 33vw"
        )
        alt = item[f"alt_{lang}"]
        cap = item[f"cap_{lang}"]
        src = largest(item["img"], prefix)
        out.append(
            f'<figure class="gallery-item{wide}">'
            f'{image(item["img"], alt, prefix, sizes=sizes)}'
            f'<figcaption>{cap}</figcaption>'
            f'<button class="gallery-zoom" type="button" data-lightbox '
            f'data-full="{src}" data-caption="{cap}" data-alt="{alt}" '
            f'aria-label="{ui_label(lang, "lightbox")}: {alt}"></button>'
            f"</figure>"
        )
    return '<div class="gallery">' + "".join(out) + "</div>"


def ui_label(lang, key):
    return UI[lang][key]


# --------------------------------------------------------------------------
# Sidemaler
# --------------------------------------------------------------------------


NO_FILES = {
    "index": "index.html",
    "about": "om-oss.html",
    "training": "trening.html",
    "contact": "kontakt.html",
    "privacy": "personvern.html",
}
EN_FILES = {
    "index": "index.html",
    "about": "about.html",
    "training": "training.html",
    "contact": "contact.html",
    "privacy": "privacy.html",
}
FILES = {"no": NO_FILES, "en": EN_FILES}


def other_lang_href(lang, key):
    if lang == "no":
        return "en/" + EN_FILES[key]
    return "../" + NO_FILES[key]


def header(lang, current, prefix):
    ui = UI[lang]
    other = "en" if lang == "no" else "no"
    current_file = FILES[lang][current]
    links = []
    for href, label in NAV[lang]:
        current_attr = ' aria-current="page"' if href == current_file else ""
        links.append(f'<a href="{href}"{current_attr}>{label}</a>')

    lang_links = (
        f'<a href="{other_lang_href(lang, current)}" hreflang="{other}" lang="{other}">'
        f'{"EN" if lang == "no" else "NO"}</a>'
        f'<span aria-current="true">{"NO" if lang == "no" else "EN"}</span>'
    )

    return f"""
<a class="skip-link" href="#main">{ui["skip"]}</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="{ui["brand_home"]}">
      <img src="{prefix}assets/img/logo-256.webp" width="54" height="54" alt="{ui["logo_alt"]}">
      <span class="brand-text">
        <span class="brand-name">Grimstad</span>
        <span class="brand-sub">Bokseklubb</span>
      </span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      <span class="bars" aria-hidden="true"><i></i><i></i><i></i></span>
      {ui["menu"]}
    </button>
    <nav class="nav" id="site-nav" aria-label="{ui["main_nav"]}">
      {"".join(links)}
      <div class="lang">{lang_links}</div>
      <a class="btn btn--small" href="{FILES[lang]["contact"]}">{ui["cta"]}</a>
    </nav>
  </div>
</header>
"""


def footer(lang, prefix):
    ui = UI[lang]
    pages = "".join(
        f'<li><a href="{href}">{label}</a></li>' for href, label in NAV[lang]
    )
    privacy = FILES[lang]["privacy"]
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="{prefix}assets/img/logo-256.webp" width="88" height="88" alt="{ui["logo_alt"]}">
          <span class="brand-text">
            <span class="brand-name">Grimstad</span>
            <span class="brand-sub">Bokseklubb</span>
          </span>
        </div>
        <p class="footer-tagline">{ui["footer_tagline"]}</p>
        <div class="socials">
          <a href="{FB}" target="_blank" rel="noopener" aria-label="{ui["social_label"]}">{ICON_FB}</a>
          <a href="{IG}" target="_blank" rel="noopener" aria-label="{ui["social_ig"]}">{ICON_IG}</a>
        </div>
      </div>
      <div>
        <h2>{ui["footer_contact"]}</h2>
        <address>
          Frivoldveien 11–13<br>
          4877 Grimstad<br>
          <a href="tel:{PHONE_HREF}">{PHONE}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </address>
      </div>
      <div>
        <h2>{ui["footer_pages"]}</h2>
        <ul>{pages}<li><a href="{privacy}">{ui["privacy"]}</a></li></ul>
      </div>
      <div>
        <h2>{ui["footer_support"]}</h2>
        <ul>
          <li><a href="{IG}" target="_blank" rel="noopener">{ui["follow"]} →</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> {ui["copyright"]}</span>
      <span><a href="{privacy}">{ui["privacy"]}</a> · {ui["since"]}</span>
    </div>
  </div>
</footer>
"""


def page_hero(img, alt, title, lead, prefix, eager=True, sizes="100vw"):
    return f"""
<section class="page-hero">
  <div class="hero-media">{image(img, alt, prefix, sizes=sizes, eager=eager)}</div>
  <div class="container hero-inner">
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""


def lightbox(lang):
    ui = UI[lang]
    return f"""
<dialog class="lightbox" id="lightbox" aria-label="{ui["lightbox"]}">
  <img data-lightbox-image alt="">
  <div class="lightbox-bar">
    <p class="lightbox-cap"><span data-lightbox-count></span> · <span data-lightbox-caption></span></p>
    <div class="lightbox-ctrl">
      <button class="icon-btn" type="button" data-lightbox-prev aria-label="{ui["prev"]}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>
      </button>
      <button class="icon-btn" type="button" data-lightbox-next aria-label="{ui["next"]}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>
      </button>
      <button class="icon-btn" type="button" data-lightbox-close aria-label="{ui["close"]}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
      </button>
    </div>
  </div>
</dialog>
"""


def canonical_path(lang, key):
    if lang == "no":
        return "/" if key == "index" else "/" + NO_FILES[key]
    return "/en/" if key == "index" else "/en/" + EN_FILES[key]


def shell(lang, key, title, description, body, prefix="", hero_image="og-cover.jpg", body_class=""):
    ui = UI[lang]
    html_lang = "en" if lang == "en" else "nb"
    canonical = SITE + canonical_path(lang, key)
    other_lang = "en" if lang == "no" else "no"
    other_path = canonical_path(other_lang, key)
    og_image = SITE + "/assets/img/" + hero_image
    jsonld = (
        '{"@context":"https://schema.org","@type":"SportsOrganization",'
        '"name":"Grimstad Bokseklubb","alternateName":"GBK",'
        '"foundingDate":"1972","sport":"Boxing",'
        f'"url":"{SITE}/","logo":"{SITE}/assets/img/logo-512.webp",'
        f'"image":"{og_image}",'
        f'"email":"{EMAIL}","telephone":"{PHONE_HREF}",'
        '"address":{"@type":"PostalAddress","streetAddress":"Frivoldveien 11–13",'
        '"postalCode":"4877","addressLocality":"Grimstad","addressCountry":"NO"},'
        f'"sameAs":["{FB}","{IG}"]}}'
    )

    return f"""<!doctype html>
<!-- Generated by tools/build.py. Edit the generator, not this file. -->
<html lang="{html_lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#0a0a0b">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="{html_lang}" href="{canonical}">
  <link rel="alternate" hreflang="{other_lang}" href="{SITE}{other_path}">
  <link rel="alternate" hreflang="x-default" href="{SITE}{canonical_path("no", key)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Grimstad Bokseklubb">
  <meta property="og:locale" content="{'nb_NO' if lang == 'no' else 'en_GB'}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og_image}">
  <link rel="icon" href="{prefix}favicon.ico" sizes="any">
  <link rel="icon" href="{prefix}favicon-32.png" sizes="32x32" type="image/png">
  <link rel="icon" href="{prefix}favicon-64.png" sizes="64x64" type="image/png">
  <link rel="apple-touch-icon" href="{prefix}apple-touch-icon.png">
  <link rel="stylesheet" href="{prefix}css/style.css?v=20261118">
  <script type="application/ld+json">{jsonld}</script>
</head>
<body{(' class="' + body_class + '"') if body_class else ""}>
{header(lang, key, prefix)}
<main id="main">
{body}
</main>
{footer(lang, prefix)}
{lightbox(lang) if key == "index" else ""}
<script src="{prefix}js/main.js?v=20261124" defer></script>
</body>
</html>
"""


def ticker(lang):
    items = (
        ["Gratis prøvetime", "Boksing for alle", "Siden 1972", "Frivoldveien 11–13", "Mosjon · mestring · kamp"]
        if lang == "no"
        else ["Free trial session", "Boxing for everyone", "Since 1972", "Frivoldveien 11–13", "Fitness · confidence · competition"]
    )
    row = "".join(f"<li>{item}</li>" for item in items)
    return (
        '<div class="ticker" aria-hidden="true"><div class="ticker-track">'
        f'<ul class="ticker-list">{row}</ul><ul class="ticker-list">{row}</ul>'
        "</div></div>"
    )


def home(lang, prefix):
    no = lang == "no"
    t = {
        "no": {
            "eyebrow": "Grimstad Bokseklubb · stiftet 1972",
            "h1": "Boksing<br><span class='accent'>for alle.</span>",
            "lead": "Enten du vil komme i form, lære å bokse eller satse mot ringen, har du plass hos oss. Klubben holder til bak Grimstad Vertshus – første trening er gratis.",
            "cta1": "Prøv en gratis trening",
            "cta2": "Se treningstider",
            "intro_eyebrow": "Velkommen inn",
            "intro_h2": "En klubb med plass til alle",
            "intro_lead": "Grimstad Bokseklubb har holdt det gående siden 1972. Her trener nybegynnere, mosjonister og konkurranseboksere side om side – i samme ring og med samme respekt.",
            "intro_p": "Vi har egen boksering, sekker og et lite styrkerom. Du trenger ingen erfaring for å begynne. Møt opp i treningstøy, så hjelper vi deg i gang.",
            "ticks": ["Gratis prøvetime – bare møt opp", "Grupper for ungdom og voksne", "Mulighet for kamp og konkurranse", "Trenere og frivillige med lang erfaring"],
            "intro_link": "Les mer om klubben",
            "caption": "Sparring i Grimstad Bokseklubb.",
            "stats": [("1972", "Stiftet"), ("5", "Økter i uken"), ("0 kr", "Første trening"), ("1", "Ring i Grimstad")],
            "cards_eyebrow": "Treningstilbud",
            "cards_h2": "Like mange grunner som boksere",
            "cards_lead": "Om du vil ha en bedre hverdag, lære en ny idrett eller gå kamper, finner du en økt som passer.",
            "cards": [
                ("01", "Nybegynner", "Grunnleggende teknikk, fotarbeid og slag – i rolig tempo."),
                ("02", "Mosjon", "Kondisjon, koordinasjon og styrke. Ingen kamper, bare god trening."),
                ("03", "Kampboksing", "For deg som vil konkurrere. Teknikk, sparring og stevner."),
                ("04", "Styrkerom", "Et lite helsestudio med vekter og apparater du kan bruke."),
            ],
            "sched_eyebrow": "Ukens økter",
            "sched_h2": "Trening i Frivoldveien",
            "sched_lead": "Alle økter foregår i klubbens lokaler bak Grimstad Vertshus. Dørene åpnes 15 minutter før.",
            "sched_cta": "Se hele treningsopplegget",
            "gal_eyebrow": "Galleri",
            "gal_h2": "Fra trening og stevner",
            "gal_lead": "Bilder fra klubben – i hallen, på stevner og på reise.",
        },
        "en": {
            "eyebrow": "Grimstad Bokseklubb · founded 1972",
            "h1": "Boxing<br><span class='accent'>for everyone.</span>",
            "lead": "Whether you want to get fit, learn to box or step into the ring, there is a place for you here. The club is behind Grimstad Vertshus – your first session is free.",
            "cta1": "Try a free session",
            "cta2": "See training times",
            "intro_eyebrow": "Welcome in",
            "intro_h2": "A club with room for everyone",
            "intro_lead": "Grimstad Bokseklubb has been going since 1972. Beginners, fitness boxers and competitors train side by side – in the same ring and with the same respect.",
            "intro_p": "We have our own ring, heavy bags and a small strength room. You do not need any experience to start. Show up in training clothes and we will help you get going.",
            "ticks": ["Free trial session – just show up", "Groups for young people and adults", "Opportunities to compete", "Coaches and volunteers with years of experience"],
            "intro_link": "Read more about the club",
            "caption": "Sparring at Grimstad Bokseklubb.",
            "stats": [("1972", "Founded"), ("5", "Sessions per week"), ("0 kr", "First session"), ("1", "Ring in Grimstad")],
            "cards_eyebrow": "What we offer",
            "cards_h2": "As many reasons as there are boxers",
            "cards_lead": "Whether you want to feel better, learn a new sport or compete, there is a session for you.",
            "cards": [
                ("01", "Beginners", "Basic technique, footwork and punching at a calm pace."),
                ("02", "Fitness", "Conditioning, coordination and strength. No fights, just good training."),
                ("03", "Competition", "For members who want to compete. Technique, sparring and events."),
                ("04", "Strength room", "A small gym with weights and equipment you can use."),
            ],
            "sched_eyebrow": "This week",
            "sched_h2": "Training in Frivoldveien",
            "sched_lead": "All sessions take place at the club behind Grimstad Vertshus. Doors open 15 minutes before.",
            "sched_cta": "See the full training programme",
            "gal_eyebrow": "Gallery",
            "gal_h2": "Training and competition",
            "gal_lead": "Photos from the club – in the gym, at events and on the road.",
        },
    }[lang]

    cards = "".join(
        f'<article class="card"><span class="num">{num}</span><h3>{title}</h3><p>{text}</p></article>'
        for num, title, text in t["cards"]
    )
    ticks = "".join(f"<li>{item}</li>" for item in t["ticks"])
    stats = "".join(f'<div class="stat"><b>{value}</b><span>{label}</span></div>' for value, label in t["stats"])

    hero_img = (
        f'<img src="{prefix}assets/img/Gemini_Generated_Image_e8euyhe8euyhe8eu.jpg" alt="Sparring i Grimstad Bokseklubb sin ring" loading="eager" decoding="async" fetchpriority="high">'
        if no
        else f'<img src="{prefix}assets/img/Gemini_Generated_Image_e8euyhe8euyhe8eu.jpg" alt="Sparring at Grimstad Bokseklubb" loading="eager" decoding="async" fetchpriority="high">'
    )

    return f"""
<section class="hero">
  <div class="hero-media">{hero_img}</div>
  <div class="container hero-inner">
    <div class="hero-content">
      <span class="eyebrow">{t["eyebrow"]}</span>
      <h1>{t["h1"]}</h1>
      <p class="hero-lead">{t["lead"]}</p>
      <div class="hero-actions">
        <a class="btn" href="{'kontakt.html' if no else 'contact.html'}">{t["cta1"]} {ICON_ARROW}</a>
        <a class="btn btn--ghost" href="{'trening.html' if no else 'training.html'}">{t["cta2"]}</a>
      </div>
      <div class="hero-meta">
        <span>Frivoldveien 11–13, Grimstad</span>
        <a href="tel:{PHONE_HREF}">{PHONE}</a>
        <a href="{IG}" target="_blank" rel="noopener">@grimstad_bokseklubb</a>
      </div>
    </div>
  </div>
  <span class="hero-est">Est. 1972 · Grimstad</span>
</section>
{ticker(lang)}
<section class="section">
  <div class="container">
    <div class="split">
      <div class="split-copy" data-reveal>
        <span class="eyebrow">{t["intro_eyebrow"]}</span>
        <h2>{t["intro_h2"]}</h2>
        <p class="lead">{t["intro_lead"]}</p>
        <p>{t["intro_p"]}</p>
        <ul class="ticks">{ticks}</ul>
        <p class="u-mt-2"><a class="link-arrow" href="{'om-oss.html' if no else 'about.html'}">{t["intro_link"]} →</a></p>
      </div>
      <figure class="split-media" data-reveal>
        {image("hero", "To boksere sparrer i ringen" if no else "Two boxers sparring in the ring", prefix, sizes="(max-width: 900px) 100vw, 45vw")}
        <figcaption>{t["caption"]}</figcaption>
      </figure>
    </div>
    <div class="stats">{stats}</div>
  </div>
</section>
<section class="section section--paper2">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["cards_eyebrow"]}</span>
        <h2>{t["cards_h2"]}</h2>
      </div>
      <p class="lead">{t["cards_lead"]}</p>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>
<section class="section section--dark">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["sched_eyebrow"]}</span>
        <h2>{t["sched_h2"]}</h2>
      </div>
      <p class="lead">{t["sched_lead"]}</p>
    </div>
    {schedule(lang)}
    <p class="note">{WEEK[lang]["note"]}</p>
    <p class="u-mt-2"><a class="btn" href="{'trening.html' if no else 'training.html'}">{t["sched_cta"]} {ICON_ARROW}</a></p>
  </div>
</section>
<section class="section section--paper2">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["gal_eyebrow"]}</span>
        <h2>{t["gal_h2"]}</h2>
      </div>
      <p class="lead">{t["gal_lead"]}</p>
    </div>
    {gallery_grid(lang, prefix)}
    <p class="note note--light u-mt-3">{'Alle bilder er tatt fra klubbens egne innlegg på Instagram og Facebook. Vil du at et bilde blir fjernet? Ta kontakt med oss.' if no else 'All photos come from the club’s own Instagram and Facebook posts. If you want a photo removed, please contact us.'}</p>
  </div>
</section>
{support_block(lang, prefix)}
{cta_band(lang, prefix)}
"""


def about(lang, prefix):
    no = lang == "no"
    t = {
        "no": {
            "title": "Siden<br><span class='accent'>1972</span>",
            "lead": "En liten klubb med lang historie – og plass til flere.",
            "story_eyebrow": "Historien",
            "story_h2": "Boksing i Grimstad siden 1972",
            "story": [
                "Grimstad Bokseklubb ble stiftet i 1972, og har siden den gang vært et fast tilbud for folk som vil trene boksing i Grimstad.",
                "Klubben holder til i Frivoldveien 11–13, innerst i grusveien bak Grimstad Vertshus. Her har vi ring, sekker og et lite styrkerom – og et miljø der nybegynnere og erfarne boksere trener sammen.",
                "I 2012 ble klubben kåret til beste klubb under NM. Gjennom årene har klubben hatt boksere i norske mesterskap, rekruttserier og internasjonale stevner. I 2019 vant Jamshid Nazari sin femte profesjonelle kamp.",
                "I dag satser vi bredt: mosjonister, ungdom og boksere som vil konkurrere. Like viktig som resultater er fellesskapet – og at alle føler seg velkommen i hallen.",
            ],
            "facts": [("Adresse", "Frivoldveien 11–13, 4877 Grimstad"), ("Stiftet", "1972"), ("Tilhørighet", "Norges Bokseforbund")],
            "timeline_eyebrow": "Milepæler",
            "timeline_h2": "Klubben gjennom årene",
            "timeline": [
                ("1972", "Klubben stiftes", "Grimstad Bokseklubb ser dagens lys."),
                ("2012", "Beste klubb i NM", "Klubben kåres til beste klubb under NM."),
                ("2019", "Profesjonell seier", "Jamshid Nazari vinner sin femte proffkamp."),
                ("2026", "Nye generasjoner", "Klubbens ungdommer bokser rekruttserier og stevner, og klubben arrangerer egne sparringsstevner."),
            ],
            "values_eyebrow": "Verdier",
            "values_h2": "Slik trener vi",
            "values": [
                ("Fellesskap", "Alle trener sammen, uansett nivå. Ingen står alene i hallen."),
                ("Respekt", "Vi møter hverandre, trenerne og motstanderne med respekt."),
                ("Disiplin", "Møt opp, gjør jobben, bli bedre – én økt om gangen."),
            ],
            "people_eyebrow": "Menneskene",
            "people_h2": "Rundt ringen",
            "person_name": "Henning Lillejord",
            "person_role": "Leder og hovedtrener",
            "person_text": "Henning har vært en del av klubben i mange år og er den som tar imot nye medlemmer. Ta kontakt hvis du vil vite mer om trening, kontingent eller hvordan du kommer i gang.",
            "vol_title": "Frivillige og trenere",
            "vol_text": "Et team av trenere, dommere, foreldre og frivillige gjør treningene og stevnene mulig. Blant dem sørger en av de frivillige for at hallen er ren og ryddig.",
        },
        "en": {
            "title": "Since<br><span class='accent'>1972</span>",
            "lead": "A small club with a long history – and room for more.",
            "story_eyebrow": "Our story",
            "story_h2": "Boxing in Grimstad since 1972",
            "story": [
                "Grimstad Bokseklubb was founded in 1972 and has been a regular part of boxing in Grimstad ever since.",
                "The club is based at Frivoldveien 11–13, at the end of the gravel road behind Grimstad Vertshus. We have a ring, heavy bags and a small strength room – and an environment where beginners and experienced boxers train together.",
                "In 2012 the club was named best club at the Norwegian championships. Over the years our boxers have competed in national championships, recruit series and international events. In 2019 Jamshid Nazari won his fifth professional bout.",
                "Today we work across the board: fitness members, young people and boxers who want to compete. Results matter, but so does the community – and making sure everyone feels welcome in the gym.",
            ],
            "facts": [("Address", "Frivoldveien 11–13, 4877 Grimstad"), ("Founded", "1972"), ("Affiliation", "Norwegian Boxing Federation")],
            "timeline_eyebrow": "Milestones",
            "timeline_h2": "The club through the years",
            "timeline": [
                ("1972", "The club is founded", "Grimstad Bokseklubb comes to life."),
                ("2012", "Best club in Norway", "The club is named best club at the national championships."),
                ("2019", "Professional win", "Jamshid Nazari wins his fifth professional bout."),
                ("2026", "A new generation", "Our young boxers compete in recruit series and events, and the club hosts its own sparring events."),
            ],
            "values_eyebrow": "Values",
            "values_h2": "How we train",
            "values": [
                ("Community", "Everyone trains together, whatever their level. Nobody stands alone in the gym."),
                ("Respect", "We treat each other, the coaches and our opponents with respect."),
                ("Discipline", "Show up, do the work, get better – one session at a time."),
            ],
            "people_eyebrow": "The people",
            "people_h2": "Around the ring",
            "person_name": "Henning Lillejord",
            "person_role": "Chair and head coach",
            "person_text": "Henning has been part of the club for many years and is the person who welcomes new members. Get in touch if you want to know more about training, fees or how to get started.",
            "vol_title": "Volunteers and coaches",
            "vol_text": "A team of coaches, judges, parents and volunteers make training and events possible. Among them, one of the volunteers keeps the gym clean and tidy.",
        },
    }[lang]

    story = "".join(f"<p>{p}</p>" for p in t["story"])
    facts = "".join(f"<li><span>{label}</span><strong>{value}</strong></li>" for label, value in t["facts"])
    timeline = "".join(
        f'<div class="timeline-item"><span class="year">{year}</span><div><h3>{title}</h3><p>{text}</p></div></div>'
        for year, title, text in t["timeline"]
    )
    values = "".join(
        f'<article class="card"><h3>{title}</h3><p>{text}</p></article>'
        for title, text in t["values"]
    )

    return f"""
<section class="page-hero">
  <div class="hero-media"><img src="{prefix}assets/img/Gemini_Generated_Image_e8euyhe8euyhe8eu.jpg" alt="{'Sparring i Grimstad Bokseklubb sin ring' if no else 'Sparring at Grimstad Bokseklubb'}" loading="eager" decoding="async" fetchpriority="high"></div>
  <div class="container hero-inner">
    <h1>{t["title"]}</h1>
    <p class="lead">{t["lead"]}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split split--reverse">
      <div class="split-copy" data-reveal>
        <span class="eyebrow">{t["story_eyebrow"]}</span>
        <h2>{t["story_h2"]}</h2>
        {story}
      </div>
      <figure class="split-media" data-reveal>
        {image("hero", "To boksere sparrer i ringen" if no else "Two boxers sparring in the ring", prefix, sizes="(max-width: 900px) 100vw, 45vw")}
        <figcaption>{'Sparring i Grimstad Bokseklubb.' if no else 'Sparring at Grimstad Bokseklubb.'}</figcaption>
      </figure>
    </div>
    <ul class="facts u-mt-3">{facts}</ul>
  </div>
</section>
<section class="section section--paper2">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["people_eyebrow"]}</span>
        <h2>{t["people_h2"]}</h2>
      </div>
    </div>
    <div class="person" data-reveal>
      <div>
        <figure class="person-media" data-reveal>
          <img src="{prefix}assets/img/Henning Lillejord.jpg" alt="{t['person_name']}, {t['person_role']}" loading="lazy" decoding="async">
        </figure>
        <h3>{t["person_name"]}</h3>
        <p class="role">{t["person_role"]}</p>
        <p>{t["person_text"]}</p>
        <div class="person-meta">
          <a href="tel:{PHONE_HREF}">{PHONE}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
      </div>
      <div>
        <h3>{t["vol_title"]}</h3>
        <p>{t["vol_text"]}</p>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["timeline_eyebrow"]}</span>
        <h2>{t["timeline_h2"]}</h2>
      </div>
    </div>
    <div class="timeline" data-reveal>{timeline}</div>
  </div>
</section>
<section class="section section--paper2">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["values_eyebrow"]}</span>
        <h2>{t["values_h2"]}</h2>
      </div>
    </div>
    <div class="cards cards--3">{values}</div>
  </div>
</section>
{cta_band(lang, prefix)}
"""


def training(lang, prefix):
    no = lang == "no"
    t = {
        "no": {
            "title": "Trening",
            "lead": "Boksing trener hele kroppen: kondisjon, styrke, koordinasjon og fokus. Du trenger ingen erfaring for å begynne.",
            "sched_eyebrow": "Treningstider",
            "sched_h2": "Ukens økter",
            "sched_lead": "Vi trener i klubbens lokaler i Frivoldveien. Kom 15 minutter før, så rekker du å skifte og hilse på trenerne.",
            "steps_eyebrow": "Kom i gang",
            "steps_h2": "Fire steg inn i ringen",
            "steps": [
                ("Møt opp", "Kom 15 minutter før økten begynner, så viser vi deg rundt."),
                ("Prøv gratis", "Første trening er alltid gratis. Du trenger ikke melde deg på."),
                ("Lån utstyr", "Vi har hansker og utstyr du kan låne i starten."),
                ("Bli med", "Etter prøveøkten avtaler vi kontingent og medlemskap."),
            ],
            "gear_eyebrow": "Praktisk",
            "gear_h2": "Hva bør jeg ha med?",
            "gear_lead": "Du trenger ikke mye utstyr for å komme i gang. Dette er en god start:",
            "gear": ["Treningsbukse og t-skjorte", "Innesko – vi bruker ikke utesko i hallen", "Vannflaske", "Håndkle", "Egne hansker når du har kommet i gang"],
            "gear_note": "Har du ikke utstyr? Du kan låne hos oss i starten.",
            "comp_eyebrow": "Konkurranse",
            "comp_h2": "Vil du gå kamper?",
            "comp_p1": "For å konkurrere må du ha gyldig startbok og godkjent legeattest. Vi hjelper deg med påmelding til stevner og følger deg opp gjennom sesongen.",
            "comp_p2": "Klubben stiller i rekruttserier, regionale stevner og nasjonale mesterskap – og arrangerer egne sparringsstevner i Grimstad.",
            "comp_caption": "Sparring i ringen med treneren på plass.",
            "faq_eyebrow": "Spørsmål og svar",
            "faq_h2": "Lurer du på noe?",
            "faq": [
                ("Må jeg være godt trent?", "Nei. Du begynner i ditt eget tempo, og trenerne tilpasser øktene etter nivået ditt."),
                ("Kan jenter trene hos oss?", "Ja. Boksing passer like godt for jenter og gutter, kvinner og menn."),
                ("Trenger jeg eget utstyr?", "Nei, du kan låne hansker og utstyr i starten. Etter hvert anbefaler vi egne hansker."),
                ("Er boksing farlig?", "Boksing er en kontaktsport, men treningen tilpasses nivået ditt. Nybegynnere starter med teknikk og lette øvelser – ikke hard sparring."),
                ("Hva koster det?", "Første trening er gratis. Kontakt oss for kontingent og medlemskap."),
            ],
        },
        "en": {
            "title": "Training",
            "lead": "Boxing trains the whole body: fitness, strength, coordination and focus. You do not need any experience to start.",
            "sched_eyebrow": "Training times",
            "sched_h2": "This week's sessions",
            "sched_lead": "We train at the club in Frivoldveien. Arrive 15 minutes early so you have time to change and meet the coaches.",
            "steps_eyebrow": "Get started",
            "steps_h2": "Four steps into the ring",
            "steps": [
                ("Show up", "Come 15 minutes before the session starts and we will show you around."),
                ("Try for free", "Your first session is always free. No sign-up needed."),
                ("Borrow equipment", "We have gloves and equipment you can borrow at the start."),
                ("Join", "After your trial we will agree on fees and membership."),
            ],
            "gear_eyebrow": "Practical",
            "gear_h2": "What should I bring?",
            "gear_lead": "You do not need much equipment to get started. This is a good start:",
            "gear": ["Training trousers and a t-shirt", "Indoor shoes – we do not wear outdoor shoes in the gym", "Water bottle", "Towel", "Your own gloves once you are settled in"],
            "gear_note": "Do not have equipment? You can borrow from us at the start.",
            "comp_eyebrow": "Competition",
            "comp_h2": "Want to compete?",
            "comp_p1": "To compete you need a valid boxing licence and a medical certificate. We help you enter events and support you through the season.",
            "comp_p2": "The club takes part in recruit series, regional events and national championships – and hosts its own sparring events in Grimstad.",
            "comp_caption": "Sparring in the ring with the coach present.",
            "faq_eyebrow": "Questions",
            "faq_h2": "Anything you wonder about?",
            "faq": [
                ("Do I need to be fit?", "No. You start at your own pace and the coaches adapt the sessions to your level."),
                ("Can women train here?", "Yes. Boxing suits women and men, girls and boys equally well."),
                ("Do I need my own equipment?", "No, you can borrow gloves and equipment at the start. Later we recommend getting your own gloves."),
                ("Is boxing dangerous?", "Boxing is a contact sport, but training is adapted to your level. Beginners start with technique and light drills – not hard sparring."),
                ("How much does it cost?", "Your first session is free. Contact us for fees and membership."),
            ],
        },
    }[lang]

    steps = "".join(
        f'<div class="step"><h3>{title}</h3><p>{text}</p></div>'
        for title, text in t["steps"]
    )
    gear = "".join(f"<li>{item}</li>" for item in t["gear"])
    faq = "".join(
        f'<details><summary>{q}</summary><div class="faq-body"><p>{a}</p></div></details>'
        for q, a in t["faq"]
    )

    return f"""
{page_hero("trening", "Tre boksere fra klubben" if no else "Three boxers from the club", t["title"], t["lead"], prefix)}
<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["sched_eyebrow"]}</span>
        <h2>{t["sched_h2"]}</h2>
      </div>
      <p class="lead">{t["sched_lead"]}</p>
    </div>
    {schedule(lang, light=True)}
    <p class="note note--light">{WEEK[lang]["note"]}</p>
  </div>
</section>
<section class="section section--paper2">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["steps_eyebrow"]}</span>
        <h2>{t["steps_h2"]}</h2>
      </div>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split">
      <div class="split-copy" data-reveal>
        <span class="eyebrow">{t["gear_eyebrow"]}</span>
        <h2>{t["gear_h2"]}</h2>
        <p class="lead">{t["gear_lead"]}</p>
        <ul class="ticks">{gear}</ul>
        <p class="note note--light">{t["gear_note"]}</p>
      </div>
      <figure class="split-media split-media--wide" data-reveal>
        {image("trening", "Tre boksere fra klubben" if no else "Three boxers from the club", prefix, sizes="(max-width: 900px) 100vw, 45vw")}
        <figcaption>{'Tre boksere fra klubben.' if no else 'Three boxers from the club.'}</figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="section section--dark">
  <div class="container">
    <div class="split split--reverse">
      <div class="split-copy" data-reveal>
        <span class="eyebrow">{t["comp_eyebrow"]}</span>
        <h2>{t["comp_h2"]}</h2>
        <p class="lead">{t["comp_p1"]}</p>
        <p>{t["comp_p2"]}</p>
        <p class="u-mt-2"><a class="btn" href="{'kontakt.html' if no else 'contact.html'}">{'Snakk med oss' if no else 'Talk to us'} {ICON_ARROW}</a></p>
      </div>
      <figure class="split-media split-media--wide" data-reveal>
        {image("hero", "Sparring i ringen" if no else "Sparring in the ring", prefix, sizes="(max-width: 900px) 100vw, 45vw")}
        <figcaption>{t["comp_caption"]}</figcaption>
      </figure>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <span class="eyebrow">{t["faq_eyebrow"]}</span>
        <h2>{t["faq_h2"]}</h2>
      </div>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>
{cta_band(lang, prefix)}
"""


def contact(lang, prefix):
    no = lang == "no"
    t = {
        "no": {
            "title": "Kontakt",
            "lead": "Kom innom, ring eller send en melding. Vi svarer så fort vi kan.",
            "visit": "Besøk oss",
            "address": "Frivoldveien 11–13<br>4877 Grimstad<br>Kjør inn på grusveien bak Grimstad Vertshus.",
            "call": "Ring oss",
            "call_name": "Henning Lillejord, leder og hovedtrener",
            "mail": "Send e-post",
            "mail_note": "Vi svarer vanligvis innen et par dager.",
            "social": "Følg oss",
            "social_note": "Kamper, treninger og hverdagsliv i hallen.",
            "form_h2": "Send oss en melding",
            "form_p": "Fyll ut skjemaet, så åpnes e-postprogrammet ditt med meldingen klar til å sendes.",
            "name": "Navn",
            "email": "E-post",
            "phone": "Telefon (valgfritt)",
            "topic": "Gjelder",
            "topics": ["Prøvetime", "Medlemskap", "Kamp og konkurranse", "Sponsing og støtte", "Annet"],
            "message": "Melding",
            "send": "Send melding",
            "form_note": "Skjemaet bruker e-postprogrammet ditt. Du kan også skrive direkte til grimstadbk@gmail.com.",
            "map": "Kart",
        },
        "en": {
            "title": "Contact",
            "lead": "Drop by, call us or send a message. We will get back to you as soon as we can.",
            "visit": "Visit us",
            "address": "Frivoldveien 11–13<br>4877 Grimstad<br>Turn into the gravel road behind Grimstad Vertshus.",
            "call": "Call us",
            "call_name": "Henning Lillejord, chair and head coach",
            "mail": "Send an e-mail",
            "mail_note": "We usually reply within a couple of days.",
            "social": "Follow us",
            "social_note": "Bouts, training and everyday life in the gym.",
            "form_h2": "Send us a message",
            "form_p": "Fill in the form and your e-mail app will open with the message ready to send.",
            "name": "Name",
            "email": "E-mail",
            "phone": "Phone (optional)",
            "topic": "Topic",
            "topics": ["Trial session", "Membership", "Competition", "Sponsorship", "Other"],
            "message": "Message",
            "send": "Send message",
            "form_note": "The form uses your e-mail app. You can also write directly to grimstadbk@gmail.com.",
            "map": "Map",
        },
    }[lang]
    topics = "".join(f'<option value="{topic}">{topic}</option>' for topic in t["topics"])

    return f"""
{page_hero("hero", "Sparring i ringen i Grimstad" if no else "Sparring in the ring at Grimstad", t["title"], t["lead"], prefix)}
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-list">
        <div class="contact-item">
          <span class="icon">{ICON_PIN}</span>
          <div>
            <h2>{t["visit"]}</h2>
            <address>{t["address"]}</address>
          </div>
        </div>
        <div class="contact-item">
          <span class="icon">{ICON_PHONE}</span>
          <div>
            <h2>{t["call"]}</h2>
            <p>{t["call_name"]}<br><a href="tel:{PHONE_HREF}">{PHONE}</a></p>
          </div>
        </div>
        <div class="contact-item">
          <span class="icon">{ICON_MAIL}</span>
          <div>
            <h2>{t["mail"]}</h2>
            <p><a href="mailto:{EMAIL}">{EMAIL}</a><br>{t["mail_note"]}</p>
          </div>
        </div>
        <div class="contact-item">
          <span class="icon">{ICON_IG}</span>
          <div>
            <h2>{t["social"]}</h2>
            <p><a href="{IG}" target="_blank" rel="noopener">Instagram · @grimstad_bokseklubb</a><br><a href="{FB}" target="_blank" rel="noopener">Facebook · Grimstad Bokseklubb</a><br>{t["social_note"]}</p>
          </div>
        </div>
      </div>
      <div class="form-card" data-reveal>
        <h2>{t["form_h2"]}</h2>
        <p>{t["form_p"]}</p>
        <form id="contact-form" data-lang="{lang}" novalidate>
          <div class="form-row">
            <div class="field">
              <label for="name">{t["name"]}</label>
              <input id="name" name="name" type="text" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="email">{t["email"]}</label>
              <input id="email" name="email" type="email" autocomplete="email" required>
            </div>
          </div>
          <div class="form-row">
            <div class="field">
              <label for="phone">{t["phone"]}</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel">
            </div>
            <div class="field">
              <label for="topic">{t["topic"]}</label>
              <select id="topic" name="topic">{topics}</select>
            </div>
          </div>
          <div class="field">
            <label for="message">{t["message"]}</label>
            <textarea id="message" name="message" required></textarea>
          </div>
          <div class="form-actions">
            <button class="btn" type="submit">{t["send"]} {ICON_ARROW}</button>
            <p class="form-note">{t["form_note"]}</p>
          </div>
          <p class="form-status" data-form-status role="status"></p>
        </form>
      </div>
    </div>
    <div class="map">
      <iframe
        title="{t["map"]}: Frivoldveien 11–13, Grimstad"
        src="https://www.google.com/maps?q=Frivoldveien+11-13,+4877+Grimstad,+Norway&output=embed&hl={'no' if no else 'en'}"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        allowfullscreen></iframe>
    </div>
  </div>
</section>
{support_block(lang, prefix)}
"""


def privacy(lang, prefix):
    no = lang == "no"
    title = "Personvern" if no else "Privacy"
    body = (
        """
        <p>Denne nettsiden bruker ingen cookies, ingen sporing og ingen tredjeparts annonser.</p>
        <p>Kontaktskjemaet åpner din egen e-postklient. Vi mottar bare opplysningene du selv velger å sende oss, og bruker dem kun til å svare på henvendelsen.</p>
        <p>Bilder og tekst på siden er hentet fra klubbens egne innlegg på Instagram og Facebook, eller produsert for klubben. Ønsker du at et bilde skal fjernes, ta kontakt på <a href="mailto:grimstadbk@gmail.com">grimstadbk@gmail.com</a>.</p>
        <p>Kartet på kontaktsiden lastes fra Google Maps. Når kartet vises, kan Google samle inn opplysninger i tråd med sin egen personvernerklæring.</p>
        """
        if no
        else """
        <p>This website uses no cookies, no tracking and no third-party advertising.</p>
        <p>The contact form opens your own e-mail app. We only receive the information you choose to send us and use it solely to answer your enquiry.</p>
        <p>Photos and text on this site come from the club's own Instagram and Facebook posts, or were produced for the club. If you want a photo removed, please contact <a href="mailto:grimstadbk@gmail.com">grimstadbk@gmail.com</a>.</p>
        <p>The map on the contact page is loaded from Google Maps. When the map is shown, Google may collect information under its own privacy policy.</p>
        """
    )
    return f"""
<section class="section" style="padding-top:calc(var(--header-h) + 4rem)">
  <div class="container" style="max-width:820px">
    <span class="eyebrow">{'Personvern' if no else 'Privacy'}</span>
    <h1>{title}</h1>
    <div class="u-mt-2" style="font-size:1.02rem">{body}</div>
    <p class="u-mt-3"><a class="btn" href="index.html">{'Til forsiden' if no else 'Back to home'} {ICON_ARROW}</a></p>
  </div>
</section>
"""


PAGES = [
    ("no", "index", home, "Grimstad Bokseklubb – boksing for alle siden 1972", "Boksing for alle i Grimstad siden 1972. Prøv en gratis trening i Frivoldveien 11–13, bak Grimstad Vertshus. Mosjon, mestring og kamp.", "og-cover.jpg"),
    ("no", "about", about, "Om oss – Grimstad Bokseklubb", "Grimstad Bokseklubb ble stiftet i 1972. Les om historien, verdiene og menneskene bak klubben i Frivoldveien.", "og-cover.jpg"),
    ("no", "training", training, "Trening og treningstider – Grimstad Bokseklubb", "Treningstider, hvordan du kommer i gang og hva du bør ha med. Første trening er gratis.", "trening-1024.webp"),
    ("no", "contact", contact, "Kontakt – Grimstad Bokseklubb", "Kontakt Grimstad Bokseklubb: Frivoldveien 11–13, 4877 Grimstad. Telefon 917 91 563, grimstadbk@gmail.com.", "og-cover.jpg"),
    ("no", "privacy", privacy, "Personvern – Grimstad Bokseklubb", "Hvordan Grimstad Bokseklubb håndterer opplysninger på nettsiden.", "og-cover.jpg"),
    ("en", "index", home, "Grimstad Bokseklubb – boxing for everyone since 1972", "Boxing for everyone in Grimstad since 1972. Try a free session at Frivoldveien 11–13, behind Grimstad Vertshus. Fitness, confidence and competition.", "og-cover.jpg"),
    ("en", "about", about, "About – Grimstad Bokseklubb", "Grimstad Bokseklubb was founded in 1972. Read about our history, values and the people behind the club.", "og-cover.jpg"),
    ("en", "training", training, "Training and times – Grimstad Bokseklubb", "Training times, how to get started and what to bring. Your first session is free.", "trening-1024.webp"),
    ("en", "contact", contact, "Contact – Grimstad Bokseklubb", "Contact Grimstad Bokseklubb: Frivoldveien 11–13, 4877 Grimstad. Phone +47 917 91 563, grimstadbk@gmail.com.", "og-cover.jpg"),
    ("en", "privacy", privacy, "Privacy – Grimstad Bokseklubb", "How Grimstad Bokseklubb handles information on this website.", "og-cover.jpg"),
]


def sitemap_xml():
    keys = ["index", "about", "training", "contact", "privacy"]
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for key in keys:
        for lang in ("no", "en"):
            lines.append("  <url>")
            lines.append("    <loc>" + escape(SITE + canonical_path(lang, key)) + "</loc>")
            for alt, hreflang in (("no", "nb"), ("en", "en")):
                href = escape(SITE + canonical_path(alt, key))
                lines.append(
                    f'    <xhtml:link rel="alternate" hreflang="{hreflang}" href="{href}"/>'
                )
            default = escape(SITE + canonical_path("no", key))
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="x-default" href="{default}"/>'
            )
            lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def robots_txt():
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITE}/sitemap.xml\n"
    )


def main():
    for lang, key, fn, title, desc, og in PAGES:
        prefix = "" if lang == "no" else "../"
        body = fn(lang, prefix)
        html = shell(lang, key, title, desc, body, prefix=prefix, hero_image=og)
        folder = ROOT if lang == "no" else ROOT / "en"
        folder.mkdir(exist_ok=True)
        target = folder / FILES[lang][key]
        target.write_text(html, encoding="utf-8")
        print("skrev", target.relative_to(ROOT))

    (ROOT / "sitemap.xml").write_text(sitemap_xml(), encoding="utf-8")
    (ROOT / "robots.txt").write_text(robots_txt(), encoding="utf-8")
    print("skrev sitemap.xml og robots.txt")


if __name__ == "__main__":
    main()
