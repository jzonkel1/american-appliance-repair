# -*- coding: utf-8 -*-
"""Generates the 11 service-area city pages (appliance-repair-<city>.html).
Shares nav/footer/reviews with gen-service-pages.py. Edit CITIES, re-run."""
import io, os, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("gsp", os.path.join(HERE, "gen-service-pages.py"))
gsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gsp)

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9z"/></svg>'

CITIES = [
 dict(slug="corpus-christi", name="Corpus Christi",
  intro="We're headquartered right here — shop, parts counter and showroom at 3701 Apollo Rd. From Calallen to Flour Bluff, Padre Island to the South Side, our techs are already in your neighborhood.",
  note="Home base — no travel considerations. Often same-day citywide.", review="peter"),
 dict(slug="portland", name="Portland",
  intro="Just across the bridge, Portland is part of our everyday routes — refrigerators, washers, dryers and every appliance in between, often the same day you call.",
  note="Regular routes across the harbor bridge — quick response for Portland homes and businesses.", review="wanda"),
 dict(slug="port-aransas", name="Port Aransas",
  intro="From island rentals to year-round homes, we keep Port A's appliances running — including the refrigerators and ice machines that vacation season depends on.",
  note="Trip fees vary by distance and are quoted up front when you book — no surprises.", review="clay"),
 dict(slug="rockport", name="Rockport",
  intro="Rockport homeowners and businesses call us for honest, warrantied repair — and our techs make the trip up Highway 35 regularly, weekends included when it matters.",
  note="Trip fees vary by distance and are quoted up front when you book — no surprises.", review="teri"),
 dict(slug="ingleside", name="Ingleside",
  intro="Ingleside is minutes from our routes across the bay — dependable repair for every major brand, residential and commercial.",
  note="Regular service area — quick response, trip fee quoted up front if applicable.", review="domingo"),
 dict(slug="aransas-pass", name="Aransas Pass",
  intro="From home kitchens to commercial equipment, Aransas Pass counts on us for repairs done right the first time — backed by our 6-month warranty.",
  note="Regular service area — trip fee quoted up front if applicable.", review="heather"),
 dict(slug="robstown", name="Robstown",
  intro="Just west of Corpus, Robstown is well inside our everyday coverage — often same-day for refrigerators, washers, dryers, ovens and more.",
  note="Regular service area — quick response for Robstown homes and businesses.", review="hannah"),
 dict(slug="kingsville", name="Kingsville",
  intro="Kingsville families and businesses don't have to settle for whoever answers the phone — our techs make the trip with parts in hand and a 6-month warranty on the work.",
  note="Trip fees vary by distance and are quoted up front when you book — no surprises.", review="domingo"),
 dict(slug="alice", name="Alice",
  intro="We bring honest, warrantied appliance repair to Alice — every major brand, residential and commercial, with up-front pricing before any work starts.",
  note="Trip fees vary by distance and are quoted up front when you book — no surprises.", review="cathy"),
 dict(slug="sinton", name="Sinton",
  intro="Sinton is part of our regular Coastal Bend coverage — dependable repairs from a veteran-owned team your neighbors already trust.",
  note="Regular service area — trip fee quoted up front if applicable.", review="alice"),
 dict(slug="mathis", name="Mathis",
  intro="From Mathis to Lake Corpus Christi, we keep appliances running with honest diagnosis, parts on hand, and a warranty on every repair.",
  note="Trip fees vary by distance and are quoted up front when you book — no surprises.", review="wanda"),
]

SVC_LINKS = [
 ("refrigerator-ice-machine-repair.html","Refrigerators &amp; Ice Machines"),
 ("washer-repair.html","Washers"),
 ("dryer-repair.html","Dryers"),
 ("dishwasher-repair.html","Dishwashers"),
 ("oven-repair.html","Ovens"),
 ("stove-repair.html","Stoves &amp; Cooktops"),
 ("vent-hood-repair.html","Vent Hoods"),
 ("garbage-disposal-repair.html","Garbage Disposals"),
]

def rev_card(key):
    chip, text, av, nm, src = gsp.REVIEWS[key]
    return f'<div class="rev-card"><div class="top"><span class="stars">★★★★★</span><span class="chip">{chip}</span></div><p>{text}</p><div class="who"><div class="av">{av}</div><div><div class="nm">{nm}</div><div class="src">{src}</div></div></div></div>'

def build(c):
    svcs = "\n      ".join(
        f'<a class="sy rv" href="{f}" style="font-weight:700;color:var(--ink);"><span class="ck">✓</span><span>{label} repair in {c["name"]}</span></a>'
        for f, label in SVC_LINKS)
    others = " ".join(
        f'<a class="chip2" href="appliance-repair-{o["slug"]}.html">{o["name"]}</a>'
        for o in CITIES if o["slug"] != c["slug"])
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
<title>Appliance Repair in {c["name"]}, TX | American Appliance Repair</title>
<meta name="description" content="Appliance repair in {c["name"]}, TX — refrigerators, washers, dryers, ovens & more. Veteran-owned, often same-day, 6-month warranty on every repair. Call (361) 673-0937.">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png?v=2">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png?v=2">
<link rel="icon" type="image/png" sizes="192x192" href="assets/favicon-192.png?v=2">
<link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..900&family=Fraunces:ital,opsz,wght@1,9..144,500;1,9..144,600&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
{gsp.head_seo(f"appliance-repair-{c['slug']}.html", f"Appliance Repair in {c['name']}, TX", f"Appliance repair in {c['name']}, TX — veteran-owned, often same-day, 6-month warranty.")}
</head>
<body>

{gsp.nav_html("")}

<section class="page-hero">
  <div class="bg" style="background-image:url('assets/american-Appliance-repair-service-website02.png');"></div>
  <div class="shade"></div>
  <div class="wrap">
    <div class="crumb h-in"><a href="index.html">Home</a><span class="sep">›</span><a href="index.html#area">Service Area</a><span class="sep">›</span><span>{c["name"]}</span></div>
    <h1 class="h-in d1">Appliance repair<br><span style="color:#FFB25E;">in {c["name"]}, TX</span></h1>
    <p class="lede h-in d2">{c["intro"]}</p>
    <div class="ctas h-in d3">
      <a href="tel:+13616730937" class="btn btn-flame">{PHONE_SVG}Call (361) 673-0937</a>
      <button class="btn btn-white hcp-button" onClick="HCPWidget.openModal()">Book Online</button>
    </div>
  </div>
</section>

<!-- trust strip -->
<div class="trust-wrap">
  <div class="trust rv in">
    <div class="tcell"><span class="big">4.8</span><div class="t"><b>Google Rating</b><span class="stars">★★★★★</span> 194 reviews</div></div>
    <div class="tcell"><img src="assets/award-best.png" alt="Best of 2026 Award Winner — BusinessRate"><div class="t"><b>Best of 2026</b>BusinessRate · powered by Google Reviews</div></div>
    <div class="tcell"><img src="assets/veteran-badge.png" alt="Military Veteran Owned"><div class="t"><b>Veteran-Owned</b>Military discounts honored</div></div>
    <div class="tcell"><span class="big" style="color:var(--flame);">6</span><div class="t"><b>6-Month Warranty</b>Parts &amp; labor, every repair</div></div>
  </div>
</div>

<!-- services in city -->
<section class="sympt">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> What We Fix in {c["name"]}</span>
      <h2 class="sec">Every appliance. Every major brand.</h2>
      <p class="lede">Residential and commercial — tap an appliance for details:</p>
    </div>
    <div class="sympt-grid">
      {svcs}
    </div>
    <div class="svc-cta rv">
      <a href="tel:+13616730937" class="btn btn-navy">Call (361) 673-0937 — often same-day</a>
      <div class="note">{c["note"]}</div>
    </div>
  </div>
</section>

<!-- why band -->
<section class="parts-adv">
  <div class="wrap">
    <div>
      <span class="eyebrow rv" style="color:var(--gold);"><img src="assets/insignia.png" alt=""> Why {c["name"]} Calls Us</span>
      <h2 class="sec rv">Parts on hand. Warranty in writing.</h2>
      <p class="lede rv">We run our own parts store in Corpus Christi — backed by our Marcone partnership — so repairs finish in one visit more often. And every repair is covered by our 6-month parts &amp; labor warranty.</p>
      <ul>
        <li class="rv"><span class="ck">✓</span><span><b>Approve the repair — trip &amp; diagnostic fee is on us</b></span></li>
        <li class="rv"><span class="ck">✓</span><span><b>Often same-day</b> · open until 8 PM weekdays, Sat 9–4</span></li>
        <li class="rv"><span class="ck">✓</span><span><b>After-hours &amp; emergency service</b> available — <a href="emergency-appliance-repair.html" style="color:#FFB25E;font-weight:700;">learn more</a></span></li>
      </ul>
    </div>
    <div class="rv">
        {rev_card(c["review"])}
    </div>
  </div>
</section>

<!-- other cities -->
<div class="more-svcs">
  <div class="wrap">
    <h3 class="rv">We also serve</h3>
    <div class="chips rv">{others} <a class="chip2 hot" href="index.html#area">Full service area →</a></div>
  </div>
</div>

<!-- CTA band -->
<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow rv" style="color:var(--gold);"><img src="assets/insignia.png" alt=""> Swift Solutions</span>
    <h2 class="rv">Broken appliance in {c["name"]}?</h2>
    <p class="lede rv" style="max-width:52ch;">Call now — often we can be out the same day — or book online and pick your time.</p>
    <div class="ctas rv">
      <a href="tel:+13616730937" class="btn btn-flame">{PHONE_SVG}Call (361) 673-0937</a>
      <button class="btn btn-white hcp-button" onClick="HCPWidget.openModal()">Book Online</button>
    </div>
    <div class="fine rv">Approve the repair &amp; the trip + diagnostic fee is on us · 6-month warranty on every repair</div>
  </div>
</section>

{gsp.FOOTER}

<script src="assets/site.js"></script>
<script async src="https://online-booking.housecallpro.com/script.js?token=fddc363afc284aaaa03239c46fb59c0b&orgName=American-Appliance-Repair"></script>
</body>
</html>
'''

for c in CITIES:
    io.open(os.path.join(ROOT, f"appliance-repair-{c['slug']}.html"), "w", encoding="utf-8").write(build(c))
    print("wrote", f"appliance-repair-{c['slug']}.html")
print("done —", len(CITIES), "city pages")
