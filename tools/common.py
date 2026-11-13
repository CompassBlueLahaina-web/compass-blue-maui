import json, html
BASE = "https://compassbluelahaina-web.github.io/compass-blue-maui/"
NAME = "Compass Blue at Lahaina Shores"
HOUFY = "https://www.houfy.com/329782?guests=1&amp;adults=1&amp;children=0"
AIRBNB = "https://www.airbnb.com/rooms/1554513657924432394"
VRBO = "https://www.vrbo.com/4982152"
SMS = "sms:+18086677088"
TEL = "tel:+18086677088"
MAIL = "mailto:CompassBlueLahaina@gmail.com?subject=Compass%20Blue%20at%20Lahaina%20Shores%20%E2%80%93%20dates%20and%20a%20question"
OG_IMG = BASE + "assets/img/share.jpg"

ROSE = '''<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22" fill="#fff" stroke="#0f2a43" stroke-width="2"/><path d="M24 5l5 19-5 19-5-19z" fill="#0f2a43"/><path d="M24 5l5 19h-10z" fill="#2a654d"/><path d="M5 24l19-4 19 4-19 4z" fill="#1b5aa6" opacity=".55"/><circle cx="24" cy="24" r="2.6" fill="#ffc83d"/></svg>'''

def head(title, desc, path, extra_ld=""):
    url = BASE + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{html.escape(OG_IMG)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f2a43">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/young-serif-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/figtree-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
{extra_ld}
<!-- Google Analytics (Kristie's existing free tag). Delete this block to remove tracking. -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-EWM16TSZFX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-EWM16TSZFX');</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def header(current):
    def a(href, label, key, cls=""):
        cur = ' aria-current="page"' if key == current else ""
        c = f' class="{cls}"' if cls else ""
        return f'<a href="{href}"{c}{cur}>{label}</a>'
    return f'''<header class="top">
  <div class="wrap">
    <a class="brand" href="./" aria-label="{NAME}, home">{ROSE}<span>Compass Blue <span>at Lahaina Shores</span></span></a>
    <nav class="nav" aria-label="Main">
      {a("./#studio", "The studio", "x", "hide-s")}
      {a("./#location", "Location", "x", "hide-s")}
      {a("guide.html", "Guest guide", "guide")}
      {a("faq.html", "FAQ", "faq")}
      <a class="btn btn-book btn-small hide-s" href="{HOUFY}" rel="noopener">Check dates</a>
    </nav>
  </div>
</header>
'''

FOOT = f'''<footer class="foot">
  <div class="wrap foot-grid">
    <div>
      <h2>{NAME}</h2>
      <p>Lahaina Shores Beach Resort<br>475 Front Street, Lahaina, HI 96761<br>Kaanapali area, West Maui</p>
      <p>Owner-hosted by Kristie. Not affiliated with Compass real estate.</p>
      <p>To book or ask a question, use Houfy, Airbnb or VRBO.<br>Phone 808-667-7088. Email CompassBlueLahaina@gmail.com</p>
    </div>
    <div>
      <h2>Book or message</h2>
      <ul>
        <li><a href="{HOUFY}" rel="noopener">Check dates on Houfy</a></li>
        <li><a href="{AIRBNB}" rel="noopener">Airbnb listing</a></li>
        <li><a href="{VRBO}" rel="noopener">VRBO listing</a></li>
      </ul>
    </div>
    <div>
      <h2>More</h2>
      <ul>
        <li><a href="guide.html">Guest guide</a></li>
        <li><a href="faq.html">Questions and answers</a></li>
        <li><a href="https://instagram.com/compassbluelahaina" rel="noopener">Instagram</a></li>
        <li><a href="https://facebook.com/compassbluelahaina" rel="noopener">Facebook</a></li>
      </ul>
      <p class="small" style="color:rgba(255,255,255,.7)">Hawaii TAT ID TA-099-540-7360-01R<br>Hawaii GET ID GE-099-540-7360-01R<br>TMK 4-6-002-007-0070</p>
    </div>
  </div>
</footer>
<div class="bar">
  <a class="btn btn-book" href="{HOUFY}" rel="noopener">Check dates and book</a>
  <a class="btn btn-line" href="./#book">Airbnb or VRBO</a>
</div>
</body>
</html>
'''

def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, indent=2, ensure_ascii=False) + '\n</script>'

import os
from PIL import Image
IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "img") + "/"
def pic(name, alt, sizes="(min-width: 900px) 40vw, 92vw", eager=False, cls=""):
    w, h = Image.open(IMG + name + ".jpg").size
    srcs = [f"assets/img/{name}-{W}.webp {min(W, w) if W==1280 else W}w" for W in (640, 1280) if os.path.exists(f"{IMG}{name}-{W}.webp")]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return f'<picture><source type="image/webp" srcset="{", ".join(srcs)}" sizes="{sizes}"><img{c} src="assets/img/{name}.jpg" alt="{alt}" width="{w}" height="{h}" {load} decoding="async"></picture>'
