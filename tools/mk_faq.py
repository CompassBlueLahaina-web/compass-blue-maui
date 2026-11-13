import re, sys
from common import *
from faqdata import FAQ
strip = lambda s: re.sub(r"<[^>]+>", "", s)
ents = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a)}} for _,_,qs in FAQ for q,a in qs]
ldjson = ld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":ents}) + "\n" + ld({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":NAME,"item":BASE},{"@type":"ListItem","position":2,"name":"Questions and answers","item":BASE+"faq.html"}]})
out = head(f"Questions and answers | {NAME}, Maui", "Straight answers about Compass Blue at Lahaina Shores, 475 Front Street, Lahaina: the view, the beach, whales and monk seals, parking, booking and getting around.", "faq.html", ldjson)
out += header("faq")
out += '<main id="main">\n<div class="page-head"><div class="wrap">\n<h1>Questions and answers</h1>\n<p class="lede">Straight answers about Compass Blue at Lahaina Shores, written by the owner. If yours is not here, message Kristie through <a href="%s">Houfy</a>, <a href="%s">Airbnb</a> or <a href="%s">VRBO</a>.</p>\n<ul class="toc">\n' % (HOUFY, AIRBNB, VRBO)
for sec, sid, _ in FAQ: out += f'<li><a href="#{sid}">{sec}</a></li>\n'
out += '</ul>\n</div></div>\n<div class="prose">\n'
for sec, sid, qs in FAQ:
    out += f'<h2 id="{sid}">{sec}</h2>\n'
    for q, a in qs: out += f'<h3 class="q">{q}</h3>\n<p>{a}</p>\n'
out += f'<p style="margin-top:3rem"><a class="btn btn-book" href="{HOUFY}" rel="noopener">Check dates and book</a></p>\n</div>\n</main>\n' + FOOT
open(sys.argv[1] + "/faq.html", "w").write(out)
