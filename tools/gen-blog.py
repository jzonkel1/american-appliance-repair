# -*- coding: utf-8 -*-
"""Generates gallery.html, blog.html and blog post pages.

Add posts to POSTS with a future ISO `pub` date and they stay unpublished until
that date arrives — the weekly GitHub Action (.github/workflows/blog-drip.yml)
re-runs this script and pushes whatever has come due. Override the clock for
testing with BLOG_TODAY=YYYY-MM-DD."""
import io, os, datetime as _dt, importlib.util

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
 dict(slug="blog-dryer-fire-warning-signs.html", pub="2026-08-04",
  title="Is Your Dryer a Fire Risk? 6 Warning Signs Corpus Christi Homeowners Miss",
  meta="Thousands of home fires each year start in dryers — and lack of maintenance is the leading cause. The warning signs to watch for, from Corpus Christi's appliance pros.",
  hero="gal-commercial-dryer.jpg", chip="Safety",
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
 dict(slug="blog-refrigerator-texas-heat.html", pub="2026-08-04",
  title="Why Refrigerators Fail in the Texas Heat — and How to Keep Yours Alive",
  meta="Corpus Christi summers make refrigerators work overtime. Why fridges fail in August, the early warning signs, and what to do before the groceries spoil.",
  hero="gal-kitchen-install.jpg", chip="Seasonal",
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
 dict(slug="blog-repair-or-replace.html", pub="2026-08-04",
  title="Repair or Replace? The Honest Math We Give Corpus Christi Customers",
  meta="When is an appliance worth repairing, and when should you replace it? The honest framework American Appliance Repair uses — from the company that does both.",
  hero="gal-washer-rebuild.jpg", chip="Advice",
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
 dict(slug="blog-parts-in-stock-one-visit-repairs.html", pub="2026-08-17",
  title="Why Your Repair Finishes in One Visit (Hint: It's the Warehouse)",
  meta="Most appliance repairs elsewhere take two visits — diagnose, order the part, wait, return. American Appliance Repair stocks its own parts warehouse in Corpus Christi so yours finishes in one.",
  hero="gal-parts-aisle.jpg", chip="Behind the Scenes",
  excerpt="The industry's dirty secret is the second visit: diagnose today, order the part, see you next week. Here's how we built our way around it.",
  body="""
<p>Here's the appliance-repair industry's dirty little secret: the second visit. A technician comes out, diagnoses your dryer, and then says the words nobody wants to hear — "I'll have to order the part." Now you're a week out with wet laundry piling up.</p>
<p>We built the company specifically to avoid that conversation. At 3701 Apollo Rd, behind the repair operation, sits a full parts warehouse — aisles of factory-certified parts backed by our Marcone partnership, one of the nation's largest appliance-parts distributors. When our technician opens up your washer, the part it needs is usually already on the truck or twenty minutes away on our own shelves.</p>
<h2>What that means for you</h2>
<ul>
<li><b>One-visit repairs, more often.</b> Diagnose and fix in the same appointment — no second trip, no week of waiting.</li>
<li><b>Faster scheduling.</b> Techs aren't burning calendar slots on return visits, so there's room when you call.</li>
<li><b>The right parts.</b> OEM and quality aftermarket for every major brand — Whirlpool, Samsung, LG, GE, Frigidaire and the rest.</li>
</ul>
<h2>Fixing it yourself? We'll sell you the part.</h2>
<p>Plenty of Coastal Bend DIY-ers fix their own machines, and we're happy to help: walk up to the <a href="index.html#parts">parts counter</a> at 3701 Apollo Rd, or call <a href="tel:+13614009513">(361) 400-9513</a> with your model number and we'll pull it — we ship, too. And if the repair turns out to be more than you bargained for, the parts store and the repair team are the same building.</p>
<p>Rather have us handle the whole thing? Call <a href="tel:+13616730937">(361) 673-0937</a> — and remember, approve the repair and the trip &amp; diagnostic fee is on us.</p>
"""),
 dict(slug="blog-washer-wont-drain-or-spin.html", pub="2026-08-31",
  title="Washer Won't Drain or Spin? What's Actually Wrong — and What to Check First",
  meta="A washer full of soaked clothes and standing water is one of the most common repair calls in Corpus Christi. The 5-minute checks to try first, and what it usually is when they don't work.",
  hero="gal-washer-rebuild.jpg", chip="Troubleshooting",
  excerpt="Before you panic-shop for a new washer: drain and spin failures are among the most common calls we run, and most are affordable fixes.",
  body="""
<p>You open the lid and there it is: a drum full of soaking clothes sitting in gray water. Before you panic-shop for a new washer, know this — drain and spin failures are among the most common calls we run, and most of them are affordable fixes.</p>
<h2>Check these three things first (five minutes, no tools)</h2>
<ul>
<li><b>The drain hose.</b> Behind the machine — if it's kinked or crushed against the wall, water physically can't leave.</li>
<li><b>The load.</b> One heavy comforter wadded up on one side can keep a washer from ever reaching spin speed. Redistribute and retry.</li>
<li><b>The pump filter</b> (front-loaders). That little door low on the front hides a filter that catches coins, hair ties and baby socks. Put a towel down, open it slowly, clean it out.</li>
</ul>
<h2>If it still won't drain or spin, it's usually one of these</h2>
<ul>
<li><b>Drain pump failure</b> — humming with no draining is the classic sign.</li>
<li><b>Lid switch or door lock</b> — a washer won't spin if it doesn't believe the door is shut.</li>
<li><b>Worn belt or coupler</b> — the motor runs but the drum doesn't follow.</li>
<li><b>Control or timer faults</b> — cycles that stall at the same point every time.</li>
</ul>
<p>All of those are diagnosable in one visit — and because <a href="index.html#parts">we stock our own parts</a>, most are fixable on the spot, backed by our <a href="warranty.html">6-month parts &amp; labor warranty</a>.</p>
<p>One honest note: if your machine is old, budget-grade, and this is its third breakdown, repair may not be the smart money. We'll tell you straight — <a href="blog-repair-or-replace.html">here's the exact framework we use</a>. Ready for a diagnosis? <a href="washer-repair.html">Washer repair details here</a>, or call <a href="tel:+13616730937">(361) 673-0937</a>.</p>
"""),
 dict(slug="blog-scratch-and-dent-buying-guide.html", pub="2026-09-14",
  title="Scratch &amp; Dent Appliances: The Smartest Money on the Showroom Floor",
  meta="New, scratch-&-dent or quality used? How to pick the right price tag at the Appliances 4U showroom in Corpus Christi — buying advice from the people who repair them.",
  hero="showroom-floor.jpg", chip="Buying Guide",
  excerpt="A scratch-&-dent appliance is a brand-new machine with a blemish that spends its life six inches from a wall. Here's when it's the smartest buy — and when it isn't.",
  body="""
<p>Walk the floor at American Appliances 4U and you'll see three kinds of price tags on what looks like the same refrigerator: new, scratch-&amp;-dent, and quality used. Here's how to know which one is your smartest money.</p>
<h2>What "scratch &amp; dent" actually means</h2>
<p>A scratch-&amp;-dent appliance is a brand-new machine with a cosmetic blemish — a ding from shipping, a scuffed side panel that will spend its life six inches from a wall. Full function, full features, and at our showroom, manufactured units carry the same <b>12-month warranty</b> as new. You're paying less for a flaw you'll likely never see again after installation day.</p>
<h2>Where each option wins</h2>
<ul>
<li><b>New</b> — you want the latest features, a specific model, or it's going somewhere the finish shows.</li>
<li><b>Scratch &amp; dent</b> — the sweet spot for most families: new-machine reliability at a real discount, with the blemished side against the cabinet.</li>
<li><b>Quality used</b> — the budget pick, with a difference: ours are inspected and serviced by our own repair technicians before they hit the floor, and carry a <b>30-day warranty</b>. These aren't marketplace mystery machines.</li>
</ul>
<h2>Buying tips from the repair side of the building</h2>
<ul>
<li><b>Measure twice</b> — the appliance space, and every doorway between the truck and it.</li>
<li><b>Check the gasket and hinges</b> on anything with a door — that's where age shows first.</li>
<li><b>Ask who stands behind it.</b> Our answer: the same shop that repairs them. That's the whole point.</li>
</ul>
<p><a href="financing.html">Financing is available</a>; delivery, installation and haul-away are quoted with your purchase; and we buy appliances and take trade-ins. Come walk the floor at 3701 Apollo Rd, call <a href="tel:+13614009513">(361) 400-9513</a>, or read more about <a href="appliances-4u.html">the showroom here</a>.</p>
"""),
 dict(slug="blog-dishwasher-not-cleaning.html", pub="2026-09-28",
  title="Dishwasher Leaving Dishes Dirty? Try These 5 Fixes Before You Call Us",
  meta="A dishwasher that runs but doesn't clean is often a 5-minute fix. The checks Corpus Christi homeowners should try tonight — and the signs it's a real fault worth a service call.",
  hero="Dishwasher_Repair_Service-1.jpg", chip="Troubleshooting",
  excerpt="About half the 'it runs but the dishes come out dirty' calls we hear can be fixed tonight without a single tool. Try these five first.",
  body="""
<p>"It runs, but the dishes come out dirty" is one of the most common dishwasher complaints we hear — and often, the fix is something you can do tonight without a single tool. Try these five before you call.</p>
<h2>The 5-minute fixes</h2>
<ul>
<li><b>1. Clean the filter.</b> Most modern dishwashers have a twist-out filter under the bottom spray arm. If it's coated in grease and food film, the machine is washing your dishes with dirty water. Rinse it under hot water with a brush.</li>
<li><b>2. Free the spray arms.</b> Spin each arm by hand and check the little holes for stuck food and seeds — a toothpick clears them.</li>
<li><b>3. Start with hot water.</b> Run the kitchen tap hot before starting the cycle, so the first fill isn't cold.</li>
<li><b>4. Load for water, not capacity.</b> Nothing blocking the spray arms, tall items to the sides, dirty faces angled toward the center.</li>
<li><b>5. Refill the rinse aid.</b> Cloudy film and water spots are usually a rinse-aid problem, not a machine problem.</li>
</ul>
<h2>When it's a real fault</h2>
<p>If the fixes above don't change anything — or you're seeing standing water in the bottom, a cycle that never fills, error codes, or grinding noises — you're likely looking at a failing wash pump, water valve, or heating element. Those are repairs we do every day, usually in one visit because <a href="index.html#parts">the parts are on our shelves</a>, and always backed by the <a href="warranty.html">6-month warranty</a>.</p>
<p><a href="dishwasher-repair.html">Dishwasher repair details here</a> — or call <a href="tel:+13616730937">(361) 673-0937</a> and describe what you're seeing. We'll tell you honestly whether it sounds like a service call or a rinse-aid refill.</p>
"""),
 dict(slug="blog-preventive-maintenance-math.html", pub="2026-10-12",
  title="The Cheapest Appliance Repair Is the One That Never Happens",
  meta="Appliances rarely fail out of nowhere — belts fray and coils choke for months first. How the $19.95/mo Home Appliance Care Membership catches problems before they become breakdowns.",
  hero="americanappliancerepairteam.jpg", chip="Money",
  excerpt="Appliances almost never fail out of nowhere. A trained technician with the panel off can see it coming — that's the entire idea behind the Care Membership.",
  body="""
<p>Every week we run service calls that didn't have to happen — a dryer that ate its own belt and rollers, a refrigerator that cooked its compressor under a blanket of coil dust. The repair is real money. The maintenance visit that would have prevented it costs a fraction of that.</p>
<h2>Why breakdowns are rarely surprises</h2>
<p>Appliances almost never fail out of nowhere. A belt frays for months. Condenser coils choke gradually. Lint builds deep in a dryer cabinet one load at a time. A trained technician with the panel off can see all of it coming — which is the entire idea behind our <a href="maintenance.html">Home Appliance Care Membership</a>.</p>
<h2>What $19.95/month actually buys</h2>
<ul>
<li><b>An annual preventive maintenance visit</b> for your covered appliance (+$5.95/mo each additional) — heating system, airflow, vents, thermostats, belts, rollers, wiring, internal lint: the full safety picture.</li>
<li><b>25% off eligible repair labor and 10% off eligible parts</b> — so when something does wear out, the fix costs less.</li>
<li><b>Priority scheduling</b> — members go to the front of the line, which matters most in August when every refrigerator in Corpus Christi is fighting the heat.</li>
<li><b>A digital service history</b> — every visit documented, every recommendation on record.</li>
</ul>
<h2>The dryer-fire math</h2>
<p>Thousands of home fires a year start in dryers, and the leading cause is lack of maintenance — lint building up where you can't see it, deep in the cabinet and the exhaust vent. We wrote a whole post on <a href="blog-dryer-fire-warning-signs.html">the warning signs</a>. A membership makes that inspection automatic instead of something you have to remember.</p>
<p>Enrollment is one phone call: <a href="tel:+13616730937">(361) 673-0937</a>. We'll set up your covered appliances and schedule the first visit.</p>
"""),
 dict(slug="blog-commercial-appliance-repair.html", pub="2026-10-26",
  title="When the Machines Can't Stop: Commercial Appliance Repair in the Coastal Bend",
  meta="Laundromat dryers, restaurant ice machines, commercial kitchens — when business equipment goes down, downtime costs money. How American Appliance Repair handles commercial calls.",
  hero="gal-commercial-dryer.jpg", chip="Commercial",
  excerpt="When a restaurant's ice machine quits on a Friday in July, it's an emergency, full stop. Commercial repair isn't a sideline here — it's a specialty.",
  body="""
<p>When a home dryer breaks, it's an inconvenience. When a laundromat dryer breaks, it's a machine that stops earning money every hour it's down. And when a restaurant's ice machine quits on a Friday in July, it's an emergency, full stop. Commercial appliance repair is a different job — and around here it isn't a sideline, it's a specialty.</p>
<h2>What we service for Coastal Bend businesses</h2>
<ul>
<li><b>Commercial laundry</b> — facility and laundromat washers and dryers, the machines that run all day, every day.</li>
<li><b>Restaurant &amp; bar ice machines</b> — treated as urgent calls, because we know what "no ice" means on a Texas weekend.</li>
<li><b>Kitchen workhorses</b> — commercial ovens, ranges and refrigeration for kitchens that can't close to wait on a repair.</li>
</ul>
<h2>Why businesses keep our number</h2>
<ul>
<li><b>Speed</b> — open until 8 PM weekdays plus Saturdays, with <a href="emergency-appliance-repair.html">after-hours &amp; emergency service</a> when downtime is costing you money.</li>
<li><b>Parts on hand</b> — our own <a href="index.html#parts">parts warehouse and Marcone partnership</a> mean commercial repairs aren't waiting on a freight truck.</li>
<li><b>One relationship</b> — repair, parts and equipment under one roof, with trade accounts for restaurants, landlords and pros at the parts counter: <a href="tel:+13614009513">(361) 400-9513</a>.</li>
</ul>
<p>Run a business anywhere from <a href="service-areas.html">Kingsville to Rockport</a>? Save this number before you need it: <a href="tel:+13616730937">(361) 673-0937</a>.</p>
"""),
 dict(slug="blog-oven-ready-for-thanksgiving.html", pub="2026-11-09",
  title="Thanksgiving Is Coming — Is Your Oven Ready?",
  meta="Thanksgiving is the hardest day of the year for your oven. The 20-minute checkup to run now, the self-clean mistake to avoid, and why to book oven repair before the holiday rush.",
  hero="companytruck-bright.jpg", chip="Seasonal",
  excerpt="Every year the weeks before Thanksgiving bring a wave of the same call: 'my oven died and my family lands Thursday.' Test yours now, while the calendar is still kind.",
  body="""
<p>Thanksgiving is the single hardest day of the year for the American oven: hours at temperature, every rack loaded, a schedule with zero slack. And every year, the weeks before the holiday bring a wave of the same call — "my oven died and my family lands Thursday." Test yours now, while the calendar is still kind.</p>
<h2>The 20-minute oven checkup (do it this weekend)</h2>
<ul>
<li><b>Run a real test.</b> Don't just turn it on — bake something. Biscuits are a great diagnostic: uneven browning means uneven heat.</li>
<li><b>Time the preheat.</b> If reaching 350° takes dramatically longer than it used to, a heating element or igniter is on its way out.</li>
<li><b>Verify the temperature.</b> A cheap oven thermometer tells you whether 350 is really 320 — the classic reason the pie is pale and the turkey is late.</li>
<li><b>Look at the door seal.</b> A torn or crushed gasket leaks heat and stretches cook times.</li>
<li><b>Test every burner too</b> — the stovetop works just as hard on the big day.</li>
</ul>
<h2>One warning about self-clean</h2>
<p>Don't run the self-clean cycle the week before Thanksgiving. It's the hottest, most stressful thing an oven ever does, and it's notorious for finishing off already-weak components right before the holiday. Clean early, or wait until December.</p>
<h2>If something's off, call now — not Wednesday</h2>
<p>Found a problem? November books up fast. <a href="oven-repair.html">Oven &amp; range repair details here</a> — call <a href="tel:+13616730937">(361) 673-0937</a> and get on the schedule while there's still room. And if the oven is truly done, <a href="appliances-4u.html">the Appliances 4U showroom</a> has ranges in stock with delivery and haul-away — no holiday drama required.</p>
"""),
]

# ---- publish gating: a post goes live only once its pub date arrives ----
TODAY = os.environ.get("BLOG_TODAY") or _dt.date.today().isoformat()
PUBLISHED = [p for p in POSTS if p["pub"] <= TODAY]
SCHEDULED = sorted((p for p in POSTS if p["pub"] > TODAY), key=lambda x: x["pub"])

def disp(iso):
    d = _dt.date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"

def post_page(p):
    body = f'''
<section style="background:var(--paper);">
  <div class="wrap" style="max-width:840px;">
    <div class="rv" style="font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--flame);margin-bottom:10px;">{p["chip"]} · {disp(p["pub"])}</div>
    <div class="doc" style="padding:0 0 40px;">{p["body"]}</div>
    <div class="rv" style="border-top:1px solid var(--line);padding-top:22px;font-size:14.5px;color:var(--soft);">Written by the team at American Appliance Repair — Christian, veteran-owned appliance repair, parts &amp; sales in Corpus Christi. <a href="blog.html" style="color:var(--flame-deep);font-weight:700;">More from the blog →</a></div>
  </div>
</section>
'''
    return shell(p["slug"], p["title"] + " | American Appliance Repair Blog", p["meta"],
                 p["hero"], "Blog", p["title"].split("—")[0].split("?")[0].strip(),
                 p["excerpt"], body)

cards = "\n      ".join(
 f'''<a class="svc rv" href="{p["slug"]}" style="display:block;flex:1 1 300px;max-width:400px;"><div class="im"><img src="assets/{p["hero"]}" alt="" loading="lazy"></div><div class="bd"><div style="font-size:11.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--flame);margin-bottom:6px;">{p["chip"]} · {disp(p["pub"])}</div><h3 style="text-transform:none;font-size:17px;line-height:1.25;">{p["title"]}</h3><p style="margin-top:8px;">{p["excerpt"]}</p><span class="more" style="display:inline-flex;margin-top:12px;">Read the post →</span></div></a>'''
 for p in sorted(PUBLISHED, key=lambda x: x["pub"], reverse=True))
blog_body = f'''
<section style="background:var(--paper);">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow"><img src="assets/insignia.png" alt=""> The Blog</span>
    <h2 class="sec">Honest appliance advice, every two weeks</h2>
    <p class="lede">Maintenance, money-saving tips, and straight answers from the team that fixes it all.</p></div>
    <div class="svc-grid" style="display:flex;flex-wrap:wrap;justify-content:center;gap:24px;">
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
for p in PUBLISHED:
    io.open(os.path.join(ROOT, p["slug"]), "w", encoding="utf-8").write(post_page(p))
    print("wrote", p["slug"])
for p in SCHEDULED:
    print("scheduled for", p["pub"], "->", p["slug"])
