# -*- coding: utf-8 -*-
"""Generates appliances-4u, reviews, faq, service-areas, maintenance pages
plus sitemap.xml, robots.txt and _redirects. Shares nav/footer with gsp."""
import io, os, glob, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("gsp", os.path.join(HERE, "gen-service-pages.py"))
gsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gsp)

P = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9z"/></svg>'

def rev(k):
    chip, text, av, nm, src = gsp.REVIEWS[k]
    return f'<div class="rev-card"><div class="top"><span class="stars">★★★★★</span><span class="chip">{chip}</span></div><p>{text}</p><div class="who"><div class="av">{av}</div><div><div class="nm">{nm}</div><div class="src">{src}</div></div></div></div>'

def cta(h2, lede, phone="+13616730937", plabel="Call (361) 673-0937"):
    return f'''<section class="cta-band"><div class="wrap">
<span class="eyebrow rv" style="color:var(--gold);"><img src="assets/insignia.png" alt=""> Swift Solutions</span>
<h2 class="rv">{h2}</h2><p class="lede rv" style="max-width:52ch;">{lede}</p>
<div class="ctas rv"><a href="tel:{phone}" class="btn btn-flame">{P}{plabel}</a>
<button class="btn btn-white hcp-button" onClick="HCPWidget.openModal()">Book Online</button></div>
<div class="fine rv">Mon–Fri 8–8 · Sat 9–4 · 3701 Apollo Rd, Corpus Christi, TX</div></div></section>'''

CITY_LIST = [("corpus-christi","Corpus Christi"),("portland","Portland"),("port-aransas","Port Aransas"),("rockport","Rockport"),("ingleside","Ingleside"),("aransas-pass","Aransas Pass"),("robstown","Robstown"),("kingsville","Kingsville"),("alice","Alice"),("sinton","Sinton"),("mathis","Mathis")]

PAGES = []

PAGES.append(dict(file="appliances-4u.html",
 title="American Appliances 4U — New, Scratch-&-Dent & Used Appliances | Corpus Christi",
 meta="Appliance showroom at 3701 Apollo Rd, Corpus Christi — new, scratch-&-dent & quality used appliances from every major brand. Financing, delivery, trade-ins. (361) 400-9513.",
 hero="showroom-floor.jpg", crumb="Appliances 4U",
 h1='The showroom:<br><span style="color:#FFB25E;">American Appliances 4U</span>',
 lede="New, scratch-&-dent and quality used appliances — every major brand, backed by warranty, with financing available and delivery to your door.",
 body=f'''
<section class="sympt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow"><img src="assets/insignia.png" alt=""> What's On The Floor</span>
<h2 class="sec">Three ways to save on your next appliance</h2></div>
<div class="steps">
<div class="step rv"><div class="n">NEW</div><h3>Brand-new units</h3><p>Full manufacturer lineup with a <b>12-month warranty</b> — refrigerators, washers, dryers, ranges, dishwashers and more.</p></div>
<div class="step rv"><div class="n">S&amp;D</div><h3>Scratch &amp; dent</h3><p>Cosmetic blemish, full function — the smartest money in appliances, same 12-month warranty on manufactured units.</p></div>
<div class="step rv"><div class="n">USED</div><h3>Quality pre-owned</h3><p>Inspected and serviced by our own technicians, with a <b>30-day warranty</b> — honest machines at honest prices.</p></div>
</div>
<div class="sec-head rv" style="margin-top:48px;"><h2 class="sec" style="font-size:clamp(22px,2.6vw,30px);">Brands you'll find</h2>
<p class="lede">Samsung · LG · GE · Whirlpool · Frigidaire · Bosch · Amana · Electrolux · Miele · Speed Queen — and more, rotating through the floor weekly.</p>
<div style="display:flex;align-items:center;gap:20px;flex-wrap:wrap;margin-top:18px;">
<span style="font-size:12.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--soft);">Authorized dealer:</span>
<img src="assets/frigidaire-brand-logo.jpg" alt="Frigidaire authorized dealer" style="height:30px;width:auto;">
<img src="assets/logo-electrolux-.jpg" alt="Electrolux authorized dealer" style="height:30px;width:auto;">
</div></div>
<div class="sympt-grid" style="grid-template-columns:1fr 1fr;">
<div class="sy rv"><span class="ck">✓</span><span><b>Authorized dealer</b> for Frigidaire &amp; Electrolux</span></div>
<div class="sy rv"><span class="ck">✓</span><span><b>$99/yr extended warranties</b> — even on appliances bought somewhere else · <a href="warranty.html" style="color:var(--flame-deep);font-weight:700;">details</a></span></div>
<div class="sy rv"><span class="ck">✓</span><span><b>Financing available</b> — <a href="financing.html" style="color:var(--flame-deep);font-weight:700;">see how it works</a></span></div>
<div class="sy rv"><span class="ck">✓</span><span><b>Delivery, installation &amp; haul-away</b> — quoted with your purchase</span></div>
<div class="sy rv"><span class="ck">✓</span><span><b>We buy appliances &amp; take trade-ins</b> — old unit becomes money</span></div>
<div class="sy rv"><span class="ck">✓</span><span><b>Backed by the repair shop</b> — the team that fixes them, sells them</span></div>
</div>
<div class="svc-cta rv"><a href="tel:+13614009513" class="btn btn-navy">Parts &amp; Sales: (361) 400-9513</a>
<div class="note">3701 Apollo Rd, Corpus Christi · Mon–Fri 8–8 · Sat 9–4</div></div>
</div></section>
{cta("Come walk the floor", "See the inventory in person — and if you're not sure whether to repair or replace, bring the question. We'll give you the honest math.", "+13614009513", "Call (361) 400-9513")}
'''))

PAGES.append(dict(file="reviews.html",
 title="Reviews — 4.8★ on Google | American Appliance Repair, Corpus Christi",
 meta="American Appliance Repair reviews: 4.8 stars across 194 Google reviews from Corpus Christi & the Coastal Bend. Real customers, real repairs — read them all.",
 hero="americanappliancerepairteam.jpg", crumb="Reviews",
 h1='4.8 stars.<br><span style="color:#FFB25E;">Your neighbors said it, not us.</span>',
 lede="194 Google reviews and counting from Corpus Christi & the Coastal Bend — here's what real customers say about our work.",
 body=f'''
<section style="background:var(--cool);"><div class="wrap">
<div class="rev-top rv"><div><span class="eyebrow"><img src="assets/insignia.png" alt=""> What Your Neighbors Say</span>
<div class="rev-score" style="margin-top:14px;"><div class="big">4.8</div>
<div class="meta"><span class="stars">★★★★★</span><a href="https://share.google/RAXAsmJPynMQHcw33" target="_blank" rel="noopener">194 Google reviews</a> · Corpus Christi &amp; the Coastal Bend</div></div></div>
<div class="rev-acts"><a href="https://search.google.com/local/writereview?placeid=ChIJsdAL8HFfaIYRbToTbtoxJ_k" target="_blank" rel="noopener" class="btn btn-flame" style="padding:12px 24px;font-size:14.5px;">Leave us a review</a><a href="https://share.google/RAXAsmJPynMQHcw33" target="_blank" rel="noopener" class="btn btn-ghost" style="padding:12px 24px;font-size:14.5px;">Read them all on Google</a></div></div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:20px;">
{"".join(rev(k) for k in gsp.REVIEWS)}
</div>
<div class="svc-cta rv" style="margin-top:34px;"><a href="https://search.google.com/local/writereview?placeid=ChIJsdAL8HFfaIYRbToTbtoxJ_k" target="_blank" rel="noopener" class="btn btn-navy">Leave us a review on Google</a>
<div class="note">Had us out recently? Two minutes of your time helps your neighbors find honest service.</div></div>
</div></section>
{cta("Ready when you are", "Join a few hundred Coastal Bend families who found their appliance people.")}
'''))

FAQ_ITEMS = [
 ("General", [
  ("What types of appliances do you repair?","All the household workhorses: refrigerators and freezers, ice machines, ovens and stoves, dishwashers, washers and dryers, vent hoods, and garbage disposals — for both homes and businesses. Every major brand."),
  ("How quickly can you respond?","Often same-day. We're open until 8 PM Monday–Friday plus Saturdays 9–4, and after-hours &amp; emergency service is available — <a href='emergency-appliance-repair.html' style='color:var(--flame);font-weight:700;'>details here</a>."),
  ("What does the service call cost?","Approve the repair, and your trip and diagnostic fee is on us. You always get an up-front quote after diagnosis, before any work starts."),
  ("Is the repair guaranteed?","Yes — every repair is backed by our 6-month warranty on parts replaced and labor. Full details on our <a href='warranty.html' style='color:var(--flame);font-weight:700;'>warranty page</a>."),
  ("Do you sell parts too?","Yes — full parts counter at 3701 Apollo Rd backed by our Marcone partnership, and we ship. Call <a href='tel:+13614009513' style='color:var(--flame);font-weight:700;'>(361) 400-9513</a>."),
 ]),
 ("Refrigerators & Freezers", [
  ("My fridge is warm but still running — should I unplug it?","Keep it closed and call us right away — the less warm air you let in, the more of your food we can save."),
  ("Do you work on commercial ice machines?","Yes — restaurant and bar units are a specialty, and they're treated as urgent calls."),
 ]),
 ("Laundry", [
  ("Is my washer worth repairing?","We'll tell you honestly after diagnosis. Most drainage, spin and pump problems are affordable fixes — and when a machine isn't worth it, our <a href='appliances-4u.html' style='color:var(--flame);font-weight:700;'>Appliances 4U showroom</a> has replacements."),
  ("Gas or electric dryers?","Both — plus the vents and ducts that keep them running safely. A burning smell means stop the dryer and call."),
 ]),
 ("Kitchen", [
  ("Do you repair both gas and electric ovens?","Yes — freestanding ranges, slide-ins, wall ovens and commercial units, gas and electric."),
  ("I smell gas near my stove — what do I do?","Leave the house and call your gas provider or 911 first. Once the utility has made things safe, we handle the stove-side repair."),
  ("Do you install dishwashers?","Yes — installation and haul-away, whether the unit comes from our showroom or somewhere else."),
 ]),
 ("Buying, Delivery & Membership", [
  ("Do you offer financing?","Yes, on appliance purchases at the showroom — <a href='financing.html' style='color:var(--flame);font-weight:700;'>here's how it works</a>."),
  ("Do you deliver?","Yes — delivery, installation and haul-away are available for a fee quoted with your purchase."),
  ("What's the Home Appliance Care Membership?","From $19.95/mo: an annual maintenance visit, 25% off eligible repair labor, 10% off eligible parts, and priority scheduling — <a href='maintenance.html' style='color:var(--flame);font-weight:700;'>full details</a>."),
  ("Do you offer extended warranties?","Yes — even if you bought your appliance somewhere else. A full year of extended warranty protection is <b>$99</b> (about 27&cent; a day). Have your receipt handy — you may qualify. Call <a href='tel:+13614009513' style='color:var(--flame);font-weight:700;'>(361) 400-9513</a>. Eligibility, coverage, exclusions and restrictions may apply."),
 ]),
]
faq_html = ""
for cat, items in FAQ_ITEMS:
    faq_html += f'<h2 class="sec rv" style="font-size:clamp(20px,2.4vw,27px);margin:34px 0 14px;">{cat}</h2>\n'
    for i,(q,a) in enumerate(items):
        faq_html += f'<details class="rv"><summary>{q}<span class="pm">+</span></summary><div class="ans">{a}</div></details>\n'

PAGES.append(dict(file="faq.html",
 title="FAQ — Appliance Repair Questions Answered | American Appliance Repair",
 meta="Answers to the questions Corpus Christi asks us most — costs, same-day service, warranties, brands, financing, delivery and the Home Appliance Care Membership.",
 hero="AAR_Appliance_Service_IMG-4.jpg", crumb="FAQ",
 h1='Good questions.<br><span style="color:#FFB25E;">Straight answers.</span>',
 lede="Everything Corpus Christi asks us most — and if your question isn't here, the phone works great too.",
 body=f'''
<section class="faq" style="background:var(--paper);"><div class="wrap">
{faq_html}
</div></section>
{cta("Still have a question?", "Call us — a real person here in Corpus Christi answers, not a call center.")}
'''))

city_cards = "\n".join(
 f'<a class="sy rv" href="appliance-repair-{s}.html" style="font-weight:700;color:var(--ink);"><span class="ck">📍</span><span>Appliance repair in <b>{n}</b></span></a>'
 for s, n in CITY_LIST)
PAGES.append(dict(file="service-areas.html",
 title="Service Area — Corpus Christi & the Coastal Bend | American Appliance Repair",
 meta="We repair appliances across the Coastal Bend: Corpus Christi, Portland, Port Aransas, Rockport, Ingleside, Aransas Pass, Robstown, Kingsville, Alice, Sinton & Mathis.",
 hero="companytruck.jpg", crumb="Service Area",
 h1='Serving Corpus Christi<br><span style="color:#FFB25E;">&amp; the Coastal Bend</span>',
 lede="From Padre Island to Kingsville, Rockport to Mathis — our techs are already on the road. Tap your city.",
 body=f'''
<section class="sympt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow"><img src="assets/insignia.png" alt=""> Where We Work</span>
<h2 class="sec">Pick your city</h2>
<p class="lede">Trip fees vary by distance and are always quoted up front when you book — no surprises.</p></div>
<div class="sympt-grid">
{city_cards}
</div>
<div style="margin-top:44px;border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow-md);border:1px solid var(--line);aspect-ratio:16/7;" class="rv">
<iframe title="American Appliance Repair service area map" src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d451812.7630225273!2d-97.3558544!3d27.78553!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1620fefb6ee9b4b%3A0x30b4cb4318530b87!2sAmerican%20Appliance%20Repair!5e0!3m2!1sen!2sus!4v1704480450355!5m2!1sen!2sus" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen style="width:100%;height:100%;border:0;display:block;"></iframe>
</div>
</div></section>
{cta("Not sure if we reach you?", "Call — if we can get a truck to you, we will, and we'll quote the trip up front.")}
'''))

PAGES.append(dict(file="maintenance.html",
 title="Home Appliance Care Membership — from $19.95/mo | American Appliance Repair",
 meta="Home Appliance Care Membership from $19.95/mo: annual preventive maintenance, 25% off repair labor, 10% off parts, priority scheduling. Prevent dryer fires & breakdowns.",
 hero="gal-washer-rebuild.jpg", crumb="Care Membership",
 h1='Protect your appliances<br><span style="color:#FFB25E;">before they break</span>',
 lede="The Home Appliance Care Membership: professional preventive maintenance from $19.95/month — because a dryer fire costs a lot more than a checkup.",
 body=f'''
<section class="sympt"><div class="wrap">
<div class="sec-head rv"><span class="eyebrow"><img src="assets/insignia.png" alt=""> Why It Matters</span>
<h2 class="sec">Thousands of home fires start in dryers</h2>
<p class="lede">Lack of maintenance is the leading cause. Lint builds up where you can't see it — inside the cabinet and the exhaust vent — airflow chokes, components overheat, bills climb, and fire risk rises. Most homeowners only clean the lint filter; the danger lives deeper.</p></div>
<div class="sympt-grid">
<div class="sy rv"><span class="ck">⚠</span><span><b>Clothes take more than one cycle</b> to dry</span></div>
<div class="sy rv"><span class="ck">⚠</span><span><b>The dryer feels unusually hot</b> — or the room gets hot &amp; humid</span></div>
<div class="sy rv"><span class="ck">⚠</span><span><b>Burning smell</b> — stop the dryer and call now</span></div>
<div class="sy rv"><span class="ck">⚠</span><span><b>Lint collecting around the machine</b></span></div>
<div class="sy rv"><span class="ck">⚠</span><span><b>Shuts off unexpectedly</b> mid-cycle</span></div>
<div class="sy rv"><span class="ck">⚠</span><span><b>Electric bill suddenly climbing</b></span></div>
</div>
</div></section>
<section class="steps-band"><div class="wrap">
<div class="sec-head rv" style="text-align:center;margin-left:auto;margin-right:auto;"><span class="eyebrow"><img src="assets/insignia.png" alt=""> The Membership</span>
<h2 class="sec">Home Appliance Care Membership</h2></div>
<div class="steps">
<div class="step rv" style="text-align:center;border:2px solid var(--flame);"><div class="n" style="font-size:44px;">$19.95<span style="font-size:15px;color:var(--soft);">/mo</span></div><h3>First appliance</h3><p>Each additional appliance just <b>+$5.95/mo</b>. Cancel anytime.</p></div>
<div class="step rv"><div class="n">✓</div><h3>What members get</h3><p>One annual preventive maintenance visit per covered appliance · complete safety inspection · digital service history &amp; recommendations · exclusive member promotions.</p></div>
<div class="step rv"><div class="n">%</div><h3>Member pricing</h3><p><b>25% off eligible repair labor</b> · <b>10% off eligible replacement parts</b> · priority scheduling when something does go wrong.</p></div>
</div>
<div class="sec-head rv" style="margin-top:40px;"><h2 class="sec" style="font-size:clamp(20px,2.4vw,27px);">Every visit, we inspect:</h2>
<p class="lede">Heating system · airflow · vent restrictions · thermal fuse · thermostats · belt · rollers · idler pulley · blower wheel · wiring · internal lint · overall safety.</p></div>
<div class="svc-cta rv"><a href="tel:+13616730937" class="btn btn-navy">Enroll by phone: (361) 673-0937</a>
<div class="note">Preventive maintenance costs far less than replacing an appliance — or repairing fire damage.</div></div>
</div></section>
{cta("Protect your home for less than a dollar a day", "Call to enroll — we'll set up your covered appliances and schedule your first maintenance visit.")}
'''))

def build(p):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-EW7D249HKK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-EW7D249HKK');
</script>
<script>document.documentElement.className += ' js';</script>
<title>{p["title"]}</title>
<meta name="description" content="{p["meta"]}">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png?v=2">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png?v=2">
<link rel="icon" type="image/png" sizes="192x192" href="assets/favicon-192.png?v=2">
<link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..900&family=Fraunces:ital,opsz,wght@1,9..144,500;1,9..144,600&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
{gsp.head_seo(p["file"], p["title"], p["meta"])}
</head>
<body>

{gsp.nav_html(p["file"])}

<section class="page-hero">
  <div class="bg" style="background-image:url('assets/{p["hero"]}');"></div>
  <div class="shade"></div>
  <div class="wrap">
    <div class="crumb h-in"><a href="index.html">Home</a><span class="sep">›</span><span>{p["crumb"]}</span></div>
    <h1 class="h-in d1">{p["h1"]}</h1>
    <p class="lede h-in d2">{p["lede"]}</p>
    <div class="ctas h-in d3">
      <a href="tel:+13616730937" class="btn btn-flame">{P}Call (361) 673-0937</a>
      <button class="btn btn-white hcp-button" onClick="HCPWidget.openModal()">Book Online</button>
    </div>
  </div>
</section>

{p["body"]}

{gsp.FOOTER}

<script src="assets/site.js"></script>
<script async src="https://online-booking.housecallpro.com/script.js?token=fddc363afc284aaaa03239c46fb59c0b&orgName=American-Appliance-Repair"></script>
</body>
</html>
'''

for p in PAGES:
    io.open(os.path.join(ROOT, p["file"]), "w", encoding="utf-8").write(build(p))
    print("wrote", p["file"])

# ---------------- sitemap / robots / redirects ----------------
skip = {"privacy-policy.html", "terms-of-service.html", "thank-you.html", "404.html"}
pages = sorted(os.path.basename(f) for f in glob.glob(os.path.join(ROOT, "*.html")))
urls = []
for f in pages:
    if f in skip: continue
    loc = gsp.BASE + "/" if f == "index.html" else f"{gsp.BASE}/{f}"
    pri = "1.0" if f == "index.html" else ("0.8" if "repair" in f or f in ("appliances-4u.html","american-power.html","reviews.html","maintenance.html") else "0.6")
    urls.append(f"  <url><loc>{loc}</loc><priority>{pri}</priority></url>")
io.open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
io.open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *\n"
    "Allow: /\n"
    "Disallow: /tools/\n"
    "Disallow: /thank-you.html\n\n"
    f"Sitemap: {gsp.BASE}/sitemap.xml\n")
# Netlify-style redirects mapping old WP URLs -> new pages (for domain cutover)
io.open(os.path.join(ROOT, "_redirects"), "w", encoding="utf-8").write("""/services/refrigerator-repair-in-corpus-christi/ /refrigerator-ice-machine-repair.html 301
/services/washer-repair-in-corpus-christi/ /washer-repair.html 301
/services/dryer-repair-in-corpus-christi/ /dryer-repair.html 301
/services/dishwasher-repair-in-corpus-christi/ /dishwasher-repair.html 301
/services/oven-repair-in-corpus-christi/ /oven-repair.html 301
/services/stove-repair-in-corpus-christi/ /stove-repair.html 301
/services/vent-hood-repair-in-corpus-christi/ /vent-hood-repair.html 301
/services/garbage-disposal-repair-in-corpus-christi/ /garbage-disposal-repair.html 301
/services/ /#services 301
/service-area/ /service-areas.html 301
/about-us/ /about.html 301
/contact-us/ /#contact 301
/blog/ /blog.html 301
/gallery/ /gallery.html 301
/tools/* /404.html 404
""")
print("sitemap.xml, robots.txt, _redirects written —", len(urls), "urls")

# ---------------- llms.txt ----------------
# Plain-language map of the site for AI assistants that cite local businesses.
B = gsp.BASE
io.open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(f"""# American Appliance Repair, LLC

> Christian, veteran-owned appliance repair, parts and appliance sales in Corpus Christi, Texas.
> Founded 2021 by Rafael, a U.S. Army veteran (13 years of service). Repair shop, parts store and
> appliance showroom under one roof at 3701 Apollo Rd. 4.8 stars across 194 Google reviews.

## Key facts
- Service phone: (361) 673-0937 · Parts & Sales: (361) 400-9513
- Address: 3701 Apollo Rd, Corpus Christi, TX 78413
- Hours: Mon-Fri 8 AM - 8 PM, Sat 9 AM - 4 PM, Sun closed. After-hours & emergency service available.
- Often same-day service. Approve the repair and the trip & diagnostic fee is waived.
- Every repair carries a 6-month warranty on parts replaced and labor.
- Extended warranties available for $99/year, even on appliances bought elsewhere.
- Repairs all major brands, residential and commercial (including restaurant ice machines
  and commercial laundry equipment).
- Authorized dealer for Frigidaire and Electrolux. Parts backed by a Marcone partnership.
- Serves Corpus Christi, Portland, Port Aransas, Rockport, Ingleside, Aransas Pass, Robstown,
  Kingsville, Alice, Sinton and Mathis, Texas.

## Services
- [Refrigerator & ice machine repair]({B}/refrigerator-ice-machine-repair.html)
- [Washer repair]({B}/washer-repair.html)
- [Dryer repair]({B}/dryer-repair.html)
- [Dishwasher repair]({B}/dishwasher-repair.html)
- [Oven repair]({B}/oven-repair.html)
- [Stove repair]({B}/stove-repair.html)
- [Vent hood repair]({B}/vent-hood-repair.html)
- [Garbage disposal repair]({B}/garbage-disposal-repair.html)
- [Emergency & after-hours appliance repair]({B}/emergency-appliance-repair.html)
- [Home Appliance Care Membership]({B}/maintenance.html): preventive maintenance from $19.95/month,
  25% off eligible repair labor, 10% off eligible parts, priority scheduling.

## Divisions
- [Appliance repair]({B}/#services): residential & commercial service and repair.
- [Parts store]({B}/#parts): OEM and aftermarket parts, retail and wholesale. We ship. Walk-in counter.
- [American Appliances 4U]({B}/appliances-4u.html): new, scratch-&-dent and quality used appliances.
  New units carry a 12-month warranty, pre-owned 30 days. Financing, delivery, installation,
  haul-away, trade-ins.
- [American Power]({B}/american-power.html): renewable energy division. Residential solar,
  battery backup and EV charging, $0 down, free custom energy analysis.

## Company
- [About]({B}/about.html) · [Reviews]({B}/reviews.html) · [Warranty]({B}/warranty.html)
- [Financing]({B}/financing.html) · [Service area]({B}/service-areas.html) · [FAQ]({B}/faq.html)
- [Photo gallery]({B}/gallery.html) · [Blog]({B}/blog.html)

## Notes for citation
- Trip fees vary by city and are quoted up front when booking; no public price list.
- "Often same-day" is accurate; same-day service is not guaranteed.
- The online parts store is not open yet; parts are sold by phone and at the counter.
""")
print("llms.txt written")
