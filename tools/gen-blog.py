# -*- coding: utf-8 -*-
"""Generates gallery.html, blog.html and blog post pages. Add posts to POSTS, re-run."""
import io, os, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("gsp", os.path.join(HERE, "gen-service-pages.py"))
gsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gsp)
P = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9z"/></svg>'

def shell(fname, title, meta, hero_img, crumb, h1, lede, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>document.documentElement.className += ' js';</script>
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png?v=2">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png?v=2">
<link rel="icon" type="image/png" sizes="192x192" href="assets/favicon-192.png?v=2">
<link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..900&family=Fraunces:ital,opsz,wght@1,9..144,500;1,9..144,600&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
{gsp.head_seo(fname, title, meta)}
</head>
<body>
{gsp.nav_html(fname)}
<section class="page-hero">
  <div class="bg" style="background-image:url('assets/{hero_img}');"></div>
  <div class="shade"></div>
  <div class="wrap">
    <div class="crumb h-in"><a href="index.html">Home</a><span class="sep">›</span><span>{crumb}</span></div>
    <h1 class="h-in d1">{h1}</h1>
    <p class="lede h-in d2">{lede}</p>
    <div class="ctas h-in d3">
      <a href="tel:+13616730937" class="btn btn-flame">{P}Call (361) 673-0937</a>
      <button class="btn btn-white hcp-button" onClick="HCPWidget.openModal()">Book Online</button>
    </div>
  </div>
</section>
{body}
{gsp.FOOTER}
<script src="assets/site.js"></script>
<script async src="https://online-booking.housecallpro.com/script.js?token=fddc363afc284aaaa03239c46fb59c0b&orgName=American-Appliance-Repair"></script>
</body>
</html>
'''

# ---------------- GALLERY ----------------
SHOTS = [
 ("gal-washer-rebuild.jpg","Hands-on in the shop: one of our technicians rebuilding a washer drive assembly at 3701 Apollo Rd."),
 ("gal-kitchen-install.jpg","On-site in a Corpus Christi kitchen — appliance and vent work done clean, with the workspace protected."),
 ("gal-commercial-dryer.jpg","Commercial dryer service — one of our technicians deep inside a laundry-facility machine. Commercial equipment isn't a sideline here; it's a specialty."),
 ("gal-parts-aisle.jpg","Aisles of factory-certified parts — Whirlpool, FSP and every major brand, stocked deep so repairs finish in one visit."),
 ("gal-warehouse-shelving.jpg","The parts warehouse keeps growing — new shelving going up to hold even more inventory."),
 ("gal-parts-room.jpg","Inside the parts room: hundreds of labeled bins mean your repair isn't waiting on a shipment from Michigan."),
 ("gal-pallets.jpg","Delivery day — pallets of appliance parts arriving at the shop, headed straight for the shelves."),
 ("gal-new-parts.jpg","New parts arriving weekly — inventory moves fast when the whole Coastal Bend calls one shop."),
 ("gal-parts-stock.jpg","Stocked and organized: OEM and aftermarket parts for every major appliance brand."),
 ("gal-warehouse-rows.jpg","Rows of new inventory at the Appliances 4U warehouse — refrigerators, ranges, washers and more."),
 ("showroom-floor.jpg","The Appliances 4U showroom floor — new, scratch-&-dent and quality used appliances, every price range."),
 ("gal-warehouse.jpg","Inside the warehouse at 3701 Apollo Rd — repair shop, parts store and showroom under one roof."),
 ("companytruck-bright.jpg","One of our service trucks, loaded and ready for the day's route across Corpus Christi."),
 ("americanappliancerepairteam.jpg","Team training meeting — every technician learns the same standard: show up, do it right, stand behind it."),
 ("team-bowling.jpg","Off the clock: company bowling night. More than coworkers — family."),
 ("businessrate-award.jpg","Receiving the BusinessRate Best of 2026 award — powered by real Google reviews from your neighbors."),
]
figs = "\n    ".join(
 f'<figure class="rv"><img src="assets/{img}" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
 for img, cap in SHOTS)
gallery_body = f'''
<section style="background:var(--paper);">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow"><img src="assets/insignia.png" alt=""> Real Work, Real People</span>
    <h2 class="sec">Around the shop &amp; on the job</h2>
    <p class="lede">The trucks, the parts room, the showroom, the team — this is what a working appliance company looks like.</p></div>
    <div class="gal">
    {figs}
    </div>
  </div>
</section>
'''
io.open(os.path.join(ROOT, "gallery.html"), "w", encoding="utf-8").write(shell(
 "gallery.html", "Photo Gallery | American Appliance Repair, Corpus Christi",
 "Inside American Appliance Repair — the shop, the parts room, the Appliances 4U showroom, and the team at work across Corpus Christi & the Coastal Bend.",
 "gal-warehouse-rows.jpg", "Gallery", 'Around the shop<br><span style="color:#FFB25E;">&amp; on the job</span>',
 "The trucks, the parts room, the showroom floor, and the people doing the work.", gallery_body))
print("wrote gallery.html")

# ---------------- BLOG ----------------
POSTS = [
 dict(slug="blog-dryer-fire-warning-signs.html", date="August 4, 2026",
  title="Is Your Dryer a Fire Risk? 6 Warning Signs Corpus Christi Homeowners Miss",
  meta="Thousands of home fires each year start in dryers — and lack of maintenance is the leading cause. The warning signs to watch for, from Corpus Christi's appliance pros.",
  hero="AAR_Appliance_Service_IMG-2.jpg", chip="Safety",
  excerpt="Most homeowners clean the lint filter and think they're covered. The dangerous buildup is where you can't see it — inside the cabinet and the exhaust vent.",
  body="""
<p>Thousands of home fires every year trace back to one appliance: the clothes dryer. And the leading cause isn't faulty equipment — it's lack of maintenance.</p>
<p>Here's the part most homeowners don't know: cleaning the lint filter after every load is good, but it's not enough. The dangerous buildup happens where you can't see it — <b>inside the dryer cabinet and the exhaust vent</b>. When lint accumulates there, airflow chokes, heat can't escape, components overheat, your energy bill climbs, and fire risk rises dramatically.</p>
<h2>6 warning signs your dryer needs attention</h2>
<ul>
<li><b>Clothes take more than one cycle to dry.</b> The #1 early sign of restricted airflow.</li>
<li><b>The dryer feels unusually hot</b> — or the laundry room turns hot and humid.</li>
<li><b>A burning smell.</b> Stop the dryer and call — this one isn't a "keep an eye on it."</li>
<li><b>Lint collecting around and behind the machine.</b></li>
<li><b>The dryer shuts off unexpectedly</b> mid-cycle — often an overheating thermostat protecting itself.</li>
<li><b>Your electric bill suddenly climbs</b> with no other explanation.</li>
</ul>
<h2>What a professional maintenance visit covers</h2>
<p>When we service a dryer, we inspect the heating system, airflow, vent restrictions, thermal fuse, thermostats, belt, rollers, idler pulley, blower wheel, wiring, and internal lint — the whole safety picture, not just the filter.</p>
<p>That's also exactly what's included in our <a href="maintenance.html">Home Appliance Care Membership</a>: an annual preventive maintenance visit per covered appliance from $19.95/month, plus 25% off eligible repair labor and priority scheduling. A simple maintenance visit today costs far less than the repairs — or the fire — it prevents.</p>
<p>Seeing the warning signs right now? <a href="dryer-repair.html">Our dryer repair page</a> has the details, or call <a href="tel:+13616730937">(361) 673-0937</a> — often we can be out the same day.</p>
"""),
 dict(slug="blog-refrigerator-texas-heat.html", date="August 4, 2026",
  title="Why Refrigerators Fail in the Texas Heat — and How to Keep Yours Alive",
  meta="Corpus Christi summers make refrigerators work overtime. Why fridges fail in August, the early warning signs, and what to do before the groceries spoil.",
  hero="AAR_Appliance_Service_IMG-1.jpg", chip="Seasonal",
  excerpt="August in Corpus Christi is peak season for refrigerator calls. Here's why the heat kills fridges — and the early signs yours is struggling.",
  body="""
<p>Every August, our phones tell the same story: refrigerator after refrigerator giving up in the Corpus Christi heat. It's not a coincidence — summer is genuinely the hardest season of a fridge's life.</p>
<h2>Why heat kills refrigerators</h2>
<p>A refrigerator doesn't make cold — it moves heat out. The hotter your kitchen or garage, the harder the compressor and condenser work to dump that heat. Add dusty condenser coils (insulation the machine never asked for), worn door gaskets leaking cool air, and a compressor that never gets to rest, and an aging fridge that limped through spring simply runs out of margin in August.</p>
<h2>Early warning signs yours is struggling</h2>
<ul>
<li><b>It never stops running</b> — the compressor cycling constantly is a fridge working at its limit.</li>
<li><b>The fridge is cold but the freezer isn't</b> (or vice versa) — airflow or defrost trouble.</li>
<li><b>Water pooling</b> under the crisper drawers or on the floor.</li>
<li><b>Warm spots</b> — milk on the door shelf going off before its date.</li>
<li><b>Clicking or buzzing</b> — a compressor trying and failing to start.</li>
</ul>
<h2>What you can do today</h2>
<p>Give it breathing room (a couple of inches off the wall), vacuum the condenser coils, check that the door gasket grips a dollar bill firmly, and don't set it colder than the manual says — that makes things worse, not better.</p>
<h2>If it's already failing</h2>
<p>Keep the doors closed — every minute of warm air costs you food — and call us at <a href="tel:+13616730937">(361) 673-0937</a>. Refrigerator calls are treated as urgent, we stock parts locally, and <a href="emergency-appliance-repair.html">after-hours help</a> is available. If it does turn out to be the end of the road, we'll tell you honestly — and the <a href="appliances-4u.html">Appliances 4U showroom</a> has replacements at every price point.</p>
"""),
 dict(slug="blog-repair-or-replace.html", date="August 4, 2026",
  title="Repair or Replace? The Honest Math We Give Corpus Christi Customers",
  meta="When is an appliance worth repairing, and when should you replace it? The honest framework American Appliance Repair uses — from the company that does both.",
  hero="AAR_Appliance_Service_IMG-5.jpg", chip="Advice",
  excerpt="We repair appliances AND sell them — which means we have no reason to steer you wrong. Here's the actual framework we use.",
  body="""
<p>"Is this thing even worth fixing?" We hear it every day — and because we both <em>repair</em> appliances and <em>sell</em> them, we're one of the few shops with no reason to steer you either direction. Here's the honest framework.</p>
<h2>The 50% rule (and its fine print)</h2>
<p>The classic rule: if a repair costs more than half the price of a comparable replacement, think hard about replacing. It's a good starting point — but age matters just as much. A $200 repair on a 4-year-old washer is easy money. The same repair on a 14-year-old washer that's already had two other fixes? Different conversation.</p>
<h2>When repair usually wins</h2>
<ul>
<li>The appliance is under 8 years old and this is its first major problem</li>
<li>It's a simple, known failure — pumps, belts, elements, thermostats, door seals</li>
<li>It's a high-end unit that was built to be serviced</li>
</ul>
<h2>When replacement usually wins</h2>
<ul>
<li>Compressor or drum failures on older, budget-grade machines</li>
<li>Repeat breakdowns — the third repair rarely makes financial sense</li>
<li>Rust-through, control board failures on discontinued models, or damage that voids safety</li>
</ul>
<h2>How we make it easy either way</h2>
<p>You get an up-front quote after diagnosis — and if you approve the repair, your trip and diagnostic fee is on us. Every repair carries our <a href="warranty.html">6-month parts &amp; labor warranty</a>. And when replacement is the smarter money, the <a href="appliances-4u.html">Appliances 4U showroom</a> has new, scratch-&amp;-dent and quality used units — with <a href="financing.html">financing available</a>, delivery, and haul-away of the old one. We'll even buy appliances or take trade-ins.</p>
<p>Not sure which side of the math you're on? Call <a href="tel:+13616730937">(361) 673-0937</a> and describe what's happening — we'll tell you straight.</p>
"""),
]

def post_page(p):
    body = f'''
<section style="background:var(--paper);">
  <div class="wrap" style="max-width:840px;">
    <div class="rv" style="font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--flame);margin-bottom:10px;">{p["chip"]} · {p["date"]}</div>
    <div class="doc" style="padding:0 0 40px;">{p["body"]}</div>
    <div class="rv" style="border-top:1px solid var(--line);padding-top:22px;font-size:14.5px;color:var(--soft);">Written by the team at American Appliance Repair — Christian, veteran-owned appliance repair, parts &amp; sales in Corpus Christi. <a href="blog.html" style="color:var(--flame-deep);font-weight:700;">More from the blog →</a></div>
  </div>
</section>
'''
    return shell(p["slug"], p["title"] + " | American Appliance Repair Blog", p["meta"],
                 p["hero"], "Blog", p["title"].split("—")[0].split("?")[0].strip(),
                 p["excerpt"], body)

cards = "\n      ".join(
 f'''<a class="svc rv" href="{p["slug"]}" style="display:block;"><div class="im"><img src="assets/{p["hero"]}" alt="" loading="lazy"></div><div class="bd"><div style="font-size:11.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--flame);margin-bottom:6px;">{p["chip"]} · {p["date"]}</div><h3 style="text-transform:none;font-size:17px;line-height:1.25;">{p["title"]}</h3><p style="margin-top:8px;">{p["excerpt"]}</p><span class="more" style="display:inline-flex;margin-top:12px;">Read the post →</span></div></a>'''
 for p in POSTS)
blog_body = f'''
<section style="background:var(--paper);">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow"><img src="assets/insignia.png" alt=""> The Blog</span>
    <h2 class="sec">Honest appliance advice, every two weeks</h2>
    <p class="lede">Maintenance, money-saving tips, and straight answers from the team that fixes it all.</p></div>
    <div class="svc-grid" style="grid-template-columns:repeat(3,1fr);">
      {cards}
    </div>
  </div>
</section>
'''
io.open(os.path.join(ROOT, "blog.html"), "w", encoding="utf-8").write(shell(
 "blog.html", "Blog — Appliance Advice from Corpus Christi Pros | American Appliance Repair",
 "Honest appliance advice from American Appliance Repair: maintenance tips, repair-or-replace math, safety warnings and seasonal guides for the Coastal Bend.",
 "AAR_Appliance_Service_IMG-3.jpg", "Blog", 'The blog:<br><span style="color:#FFB25E;">honest appliance advice</span>',
 "Every two weeks: maintenance tips, money math, and safety advice from the team your neighbors trust.", blog_body))
print("wrote blog.html")
for p in POSTS:
    io.open(os.path.join(ROOT, p["slug"]), "w", encoding="utf-8").write(post_page(p))
    print("wrote", p["slug"])
