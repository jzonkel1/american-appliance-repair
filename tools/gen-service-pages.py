# -*- coding: utf-8 -*-
"""Generates the 8 service pages from SERVICES data. Edit data, re-run, commit.
Run:  python tools/gen-service-pages.py   (from the site root or anywhere)"""
import io, os


BASE = "https://americanappliancerepaircc.com"
def head_seo(fname, title, desc):
    url = BASE + "/" if fname == "index.html" else f"{BASE}/{fname}"
    t = title.replace('"', "&quot;"); d = desc.replace('"', "&quot;")
    return f"""<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="American Appliance Repair, LLC">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="American Appliance Repair — appliance repair, parts &amp; sales in Corpus Christi, TX. (361) 673-0937">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}/assets/og-cover.jpg">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"American Appliance Repair, LLC","image":"{BASE}/assets/logo.png","url":"{BASE}/","telephone":"+13616730937","address":{{"@type":"PostalAddress","streetAddress":"3701 Apollo Rd","addressLocality":"Corpus Christi","addressRegion":"TX","postalCode":"78413","addressCountry":"US"}},"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"20:00"}},{{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"16:00"}}],"sameAs":["https://www.facebook.com/p/American-Appliance-Repair-61554373376502/","https://www.instagram.com/american__appliance_repair/"]}}</script>"""

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------- real Google reviews (verbatim from homepage) ----------------
REVIEWS = {
 "rb":      ("Refrigerator","“The techs were knowledgeable and courteous and in constant contact with the Master Tech by phone. My high-end KitchenAid 42″ built-in is now working like new.”","RB","R. B.","Google review"),
 "teri":    ("Refrigerator","“Big shout out to Chris and the office staff for getting out here Saturday. Mariana is an angel for helping arrange it. This company is honest and went above and beyond. HIGHLY RECOMMEND.”","TD","Teri Dysarz","Google review · Rockport"),
 "heather": ("Washer","“This is a veteran-owned company — I received a discount for my service in the military, which was awesome. Chris and his son fixed my washer in no time. Very affordable as well.”","HH","Heather Hirst","Google review"),
 "jackie":  ("Washer","“My washer started making an awful sound. Chris came and fixed it — the culprit was a tiny rubber ducky from my daughter's pocket! Working just fine now. 😂”","JM","Jackie Mendez","Google review"),
 "hannah":  ("Dishwasher","“No BS — hooked up my dishwasher and found the problem. Wear-and-tear fix for under $150. Respectful, kind, and cleaned up before they left.”","HP","Hannah Poe","Google review"),
 "priscilla":("Freezer","“Our freezer was leaking water — the technician found the problem immediately on the first visit. Back on the promised day, installed the part, very reasonable price. Very satisfied.”","PD","Priscilla Diers","Google review"),
 "alice":   ("Dryer","“Caesar was an awesome repairman. Correctly diagnosed the problem, ordered parts and completed all repairs on our dryer in a timely fashion. We'll definitely use this company again!”","AR","Alice R.","Google review"),
 "peter":   ("Refrigerator","“Greg says what he does and does what he says! Once he's on the way, a text gives you a live map of his arrival. Now my refrigerator works perfectly again.”","PW","Peter Wesner","Google review"),
 "clay":    ("Scheduling","“Super nice techs and on time too! The office kept me up to date with appointment information from the beginning. Very honest and trustworthy company.”","CP","Clay Petsch","Google review · Port Aransas"),
 "domingo": ("Diagnosis","“Very informative! Diagnosed within 5 minutes and had the job done in 30. All up-front pricing with warranty on work!”","DH","Domingo Hernandez","Google review"),
 "cathy":   ("Honest Advice","“Although my washer wasn't cost-effective to repair, Chris was phenomenal and did all he could. Thank you for being so kind and helpful during this process.”","CP","Cathy Peterson","Google review"),
 "patricia":("Samsung Washer","“Chris and Aaron were great! They fixed my Samsung washer very quickly and explained everything they did. I will definitely call them in the future!”","PC","Patricia Contreras","Google review"),
 "wanda":   ("Local Trust","“A true, honest Christian company. We need more companies like them!”","WM","Wanda Martino","Google review"),
}

FAQ_QUOTE = ("How much will the repair cost?",
  "You get an up-front quote after diagnosis, before any work starts — and here's the best part: <b>approve the repair, and your trip and diagnostic fee is on us.</b> If a repair isn't worth it, we'll tell you straight; our Appliances 4U showroom has affordable new, scratch-&-dent and quality used replacements.")
FAQ_SAMEDAY = ("Can you come out today?",
  "Often, yes. We're open until 8 PM Monday through Friday plus Saturdays 9–4, and when you call in the morning we can often have a technician out the same day. After-hours and emergency service is available too — just call.")
FAQ_WARRANTY = ("Is the repair guaranteed?",
  "Yes — every repair is backed by our 6-month warranty on parts replaced and labor. If something isn't right, we make it right. Full details on our <a href=\"warranty.html\" style=\"color:var(--flame);font-weight:700;\">warranty page</a>.")

SERVICES = [
 dict(file="refrigerator-ice-machine-repair.html", img="AAR_Appliance_Service_IMG-1.jpg",
  name="Refrigerator & Ice Machine Repair", short="Refrigerators & Ice Machines",
  title="Refrigerator & Ice Machine Repair in Corpus Christi, TX",
  meta="Often same-day refrigerator, freezer & ice machine repair in Corpus Christi — residential & commercial. Veteran-owned, 6-month warranty on every repair. Call (361) 673-0937.",
  h1="Refrigerator &amp; ice machine repair",
  lede="Cooling loss, leaks, and ice makers on strike — fixed before the groceries spoil. Residential fridges to commercial ice machines, our experienced techs handle every major brand — often the same day you call.",
  sympt_intro="If your fridge or ice machine is doing any of this, it's time to call:",
  symptoms=["<b>Not cooling</b> — or the fridge is cold but the freezer isn't (or vice versa)","<b>Leaking water</b> onto the floor or pooling under the crisper drawers","<b>Ice maker stopped</b> — no ice, hollow cubes, or a frozen-up line","<b>Frost buildup</b> in the freezer or on the back wall","<b>Running loud</b> — clicking, buzzing, or a compressor that never shuts off","<b>Commercial ice machine down</b> — restaurant &amp; bar units serviced too"],
  reviews=["rb","teri","peter"],
  faqs=[FAQ_SAMEDAY, ("My fridge is warm but still running — should I unplug it?","Keep it closed and call us right away — the less warm air you let in, the more of your food we can save. Same-day appointments exist for exactly this emergency."), FAQ_QUOTE, FAQ_WARRANTY]),

 dict(file="washer-repair.html", img="AAR_Appliance_Service_IMG-3.jpg",
  name="Washer Repair", short="Washer Repair",
  title="Washer Repair in Corpus Christi, TX",
  meta="Often same-day washing machine repair in Corpus Christi — drainage, spin, leaks & error codes on every major brand. Veteran-owned, warranty on every repair. Call (361) 673-0937.",
  h1="Washing machine repair",
  lede="Drainage, spin and no-start problems fixed efficiently and affordably — on every major brand, from top-load workhorses to high-efficiency front-loaders.",
  sympt_intro="If your washer is doing any of this, it's time to call:",
  symptoms=["<b>Won't drain</b> — clothes sitting in a tub of water","<b>Won't spin</b> — or clothes come out soaking wet","<b>Won't start</b> — dead panel, or it fills and just sits there","<b>Leaking</b> — water on the floor during or after a cycle","<b>Banging &amp; shaking</b> — walking across the laundry room on spin","<b>Error codes</b> — or a door that won't lock or unlock"],
  reviews=["heather","jackie","patricia"],
  faqs=[FAQ_SAMEDAY, FAQ_QUOTE, ("Is my washer worth repairing?","We'll tell you honestly after diagnosis. Most drainage, spin, and pump problems are affordable fixes — and when a machine truly isn't worth it, we say so and can set you up with a replacement from our Appliances 4U showroom instead."), FAQ_WARRANTY]),

 dict(file="dryer-repair.html", img="AAR_Appliance_Service_IMG-2.jpg",
  name="Dryer Repair", short="Dryer Repair",
  title="Dryer Repair in Corpus Christi, TX",
  meta="Often same-day dryer repair in Corpus Christi — no-heat, drum & vent issues on gas and electric dryers, every major brand. Veteran-owned, warranty included. Call (361) 673-0937.",
  h1="Dryer repair",
  lede="Swift diagnosis for no-heat, drum and vent issues on gas and electric dryers — so laundry day stays on schedule.",
  sympt_intro="If your dryer is doing any of this, it's time to call:",
  symptoms=["<b>No heat</b> — tumbles fine but clothes stay wet","<b>Takes forever</b> — two or three cycles for one load","<b>Won't tumble</b> — hums or won't start at all","<b>Squealing or thumping</b> — belt, rollers or bearings on the way out","<b>Burning smell</b> — stop the dryer and call; lint and heat are a bad mix","<b>Weak airflow</b> — vent or blower problems that waste time &amp; energy"],
  reviews=["alice","domingo","clay"],
  faqs=[FAQ_SAMEDAY, ("Gas or electric — do you work on both?","Yes, our technicians service both gas and electric dryers from every major brand, along with the vents and ducts that keep them running safely."), FAQ_QUOTE, FAQ_WARRANTY]),

 dict(file="dishwasher-repair.html", img="AAR_Appliance_Service_IMG-4.jpg",
  name="Dishwasher Repair", short="Dishwasher Repair",
  title="Dishwasher Repair in Corpus Christi, TX",
  meta="Often same-day dishwasher repair in Corpus Christi — cleaning problems, leaks, drainage & pumps on every major brand. Veteran-owned, warranty on every repair. Call (361) 673-0937.",
  h1="Dishwasher repair",
  lede="From cleaning problems to leaks and failed pumps — enjoy uninterrupted dishwashing again, without paying big-box service-call prices.",
  sympt_intro="If your dishwasher is doing any of this, it's time to call:",
  symptoms=["<b>Dishes come out dirty</b> — film, grit, or spots that weren't there before","<b>Won't drain</b> — standing water in the bottom after every cycle","<b>Leaking at the door</b> — or water creeping out underneath","<b>Won't start or latch</b> — dead panel, blinking lights, error codes","<b>Bad odor</b> — that no amount of cleaner seems to fix","<b>Detergent door stuck</b> — or rinse aid never dispensing"],
  reviews=["hannah","cathy","domingo"],
  faqs=[FAQ_SAMEDAY, FAQ_QUOTE, ("Do you install dishwashers too?","Yes — we handle installation and haul-away, whether the new unit comes from our own Appliances 4U showroom or somewhere else."), FAQ_WARRANTY]),

 dict(file="oven-repair.html", img="AAR_Appliance_Service_IMG-5.jpg",
  name="Oven Repair", short="Oven Repair",
  title="Oven Repair in Corpus Christi, TX",
  meta="Often same-day oven repair in Corpus Christi — heating elements, igniters, controls & uneven baking on every major brand. Veteran-owned, warranty included. Call (361) 673-0937.",
  h1="Oven repair",
  lede="Prompt repairs on heating elements, igniters and controls — your kitchen stays functional, whether it's a builder-grade range or a double wall oven.",
  sympt_intro="If your oven is doing any of this, it's time to call:",
  symptoms=["<b>Won't heat</b> — or takes forever to preheat","<b>Uneven baking</b> — burnt on one side, raw on the other","<b>Element or igniter out</b> — bake works but broil doesn't, or vice versa","<b>Gas igniter clicking</b> — glowing but never lighting","<b>Temperature runs off</b> — set 350°, get something else entirely","<b>Control panel dead</b> — error codes, stuck buttons, blank display"],
  reviews=["domingo","clay","wanda"],
  faqs=[FAQ_SAMEDAY, ("Do you repair both gas and electric ovens?","Yes — gas and electric, freestanding ranges, slide-ins, wall ovens and commercial units, across every major brand."), FAQ_QUOTE, FAQ_WARRANTY]),

 dict(file="stove-repair.html", img="AAR_Appliance_Service_IMG-6.jpg",
  name="Stove & Cooktop Repair", short="Stove Repair",
  title="Stove & Cooktop Repair in Corpus Christi, TX",
  meta="Often same-day stove & cooktop repair in Corpus Christi — burners, elements, switches & controls on gas and electric, every major brand. Warranty included. Call (361) 673-0937.",
  h1="Stove &amp; cooktop repair",
  lede="Stove malfunctions handled quickly — burners, elements, switches and controls — keeping your kitchen ready to cook again.",
  sympt_intro="If your stove or cooktop is doing any of this, it's time to call:",
  symptoms=["<b>Burner won't light</b> — endless clicking on a gas burner","<b>Element won't heat</b> — or only heats on high","<b>Sparking or tripping the breaker</b> — stop using it and call","<b>Broken knobs or switches</b> — burners stuck on or off","<b>Indicator light stays on</b> — even with everything off","<b>Glass cooktop damage</b> — cracked or scorched surface elements"],
  reviews=["domingo","wanda","clay"],
  faqs=[FAQ_SAMEDAY, ("I smell gas near my stove — what should I do?","Leave the house and call your gas provider or 911 first — a suspected leak is an emergency, not a repair appointment. Once the utility has made things safe, we'll handle the stove-side repair."), FAQ_QUOTE, FAQ_WARRANTY]),

 dict(file="vent-hood-repair.html", img="AAR_Appliance_Service_IMG-7.jpg",
  name="Vent Hood Repair", short="Vent Hood Repair",
  title="Vent Hood Repair in Corpus Christi, TX",
  meta="Vent hood repair in Corpus Christi — fans, lighting & ductwork serviced for a safer kitchen, every major brand. Veteran-owned, warranty included. Call (361) 673-0937.",
  h1="Vent hood repair",
  lede="Fans, lighting and ductwork serviced for maximum ventilation and a safer kitchen — smoke and grease belong outside, not on your ceiling.",
  sympt_intro="If your vent hood is doing any of this, it's time to call:",
  symptoms=["<b>Fan not running</b> — buttons light up, nothing spins","<b>Weak suction</b> — smoke rolls out instead of up","<b>Loud rattle or grinding</b> — motor or fan blades on the way out","<b>Lights out</b> — sockets or wiring, not just bulbs","<b>Grease dripping back</b> — filters and ducts past saturation","<b>Switches unresponsive</b> — speeds missing or stuck on one setting"],
  reviews=["wanda","clay","domingo"],
  faqs=[FAQ_SAMEDAY, ("Is a weak vent hood really a problem?","Yes — a hood that can't clear smoke and grease means both end up on your walls, cabinets and lungs, and grease buildup is a genuine fire risk in any kitchen, home or commercial."), FAQ_QUOTE, FAQ_WARRANTY]),

 dict(file="garbage-disposal-repair.html", img="AAR_Appliance_Service_IMG-8.jpg",
  name="Garbage Disposal Repair", short="Garbage Disposal",
  title="Garbage Disposal Repair in Corpus Christi, TX",
  meta="Garbage disposal repair & replacement in Corpus Christi — jams, leaks, hums & no-starts fixed fast. Veteran-owned, warranty on every repair. Call (361) 673-0937.",
  h1="Garbage disposal repair",
  lede="Professional repair that keeps your kitchen hygienic, efficient and odor-free — and honest advice on when a worn-out disposal is cheaper to replace than fix.",
  sympt_intro="If your disposal is doing any of this, it's time to call:",
  symptoms=["<b>Humming but not spinning</b> — jammed flywheel or a seized motor","<b>Completely dead</b> — no hum, no reset-button rescue","<b>Leaking underneath</b> — from the sink flange, hoses or the body itself","<b>Draining slow</b> — backing up into the sink when it runs","<b>Persistent odor</b> — that cleaning and citrus peels won't cure","<b>Loud metal-on-metal</b> — something's in there that shouldn't be"],
  reviews=["hannah","domingo","wanda"],
  faqs=[FAQ_SAMEDAY, ("Repair or replace my disposal?","Jams and resets are quick, cheap fixes. But if the motor is seized or the body is leaking, replacement is usually the better money — we'll give you the honest math and can supply and install the new unit same visit."), FAQ_QUOTE, FAQ_WARRANTY]),
]

# ---------------- template pieces ----------------
NAV_CITIES = [
    ("appliance-repair-corpus-christi.html", "Corpus Christi"),
    ("appliance-repair-portland.html", "Portland"),
    ("appliance-repair-port-aransas.html", "Port Aransas"),
    ("appliance-repair-rockport.html", "Rockport"),
    ("appliance-repair-ingleside.html", "Ingleside"),
    ("appliance-repair-aransas-pass.html", "Aransas Pass"),
    ("appliance-repair-robstown.html", "Robstown"),
    ("appliance-repair-kingsville.html", "Kingsville"),
    ("appliance-repair-alice.html", "Alice"),
    ("appliance-repair-sinton.html", "Sinton"),
    ("appliance-repair-mathis.html", "Mathis"),
]

def nav_html(active_file):
    dd = "\n".join(
        f'          <a href="{s["file"]}"><span class="di"></span>{s["short"]}</a>'
        for s in SERVICES)
    dd_areas = "\n".join(
        f'          <a href="{f}"><span class="di"></span>{n}</a>'
        for f, n in NAV_CITIES)
    m_services = "".join(f'<a href="{s["file"]}">{s["short"]}</a>' for s in SERVICES)
    m_areas = "".join(f'<a href="{f}">{n}</a>' for f, n in NAV_CITIES)
    return f'''<header class="nav" id="nav">
  <div class="topline"><img src="assets/insignia.png" alt=""> Christian Veteran-Owned &amp; Operated<span class="tl-loc">&nbsp;· Corpus Christi, TX</span><span class="open-now" data-open-now hidden></span></div>
  <div class="wrap">
    <a class="logo" href="index.html"><img src="assets/logo-mark.png" alt="American Appliance Repair, LLC"><span class="lt"><b>American Appliance</b><small>Repair, LLC</small></span></a>
    <nav class="navlinks">
      <div class="has-dd">
        <a href="index.html#services">Services <span class="car">▼</span></a>
        <div class="dd"><div class="dd-card two">
{dd}
          <a href="maintenance.html"><span class="di"></span><span>Care Membership<span class="sub">From $19.95/mo · prevent breakdowns</span></span></a>
          <a class="dd-cta" href="tel:+13616730937">Often same-day — (361) 673-0937</a>
        </div></div>
      </div>
      <div class="has-dd">
        <a href="index.html#parts" class="store-link">Store <span class="car">▼</span></a>
        <div class="dd"><div class="dd-card">
          <a href="index.html#parts"><span class="di"></span><span>OEM &amp; Aftermarket Parts<span class="sub">Official Marcone SSB</span></span></a>
          <a href="index.html#parts"><span class="di"></span><span>Walk-In Parts Counter<span class="sub">3701 Apollo Rd</span></span></a>
          <a href="index.html#parts"><span class="di"></span><span>Trade Accounts<span class="sub">Restaurants, landlords &amp; pros</span></span></a>
          <a class="dd-cta" href="tel:+13614009513">Parts &amp; Sales — (361) 400-9513</a>
        </div></div>
      </div>
      <div class="has-dd">
        <a href="index.html#divisions">Divisions <span class="car">▼</span></a>
        <div class="dd"><div class="dd-card">
          <a href="index.html#services"><img class="dc" src="assets/logo-mark.png" alt=""><span>Appliance Repair<span class="sub">Service &amp; repair division</span></span></a>
          <a href="index.html#parts"><img class="dc" src="assets/div-parts.png?v=2" alt=""><span>Parts Store<span class="sub">Parts &amp; supply division</span></span></a>
          <a href="appliances-4u.html"><img class="dc" src="assets/div-sales.png?v=2" alt=""><span>Appliances 4U<span class="sub">New &amp; used appliance sales</span></span></a>
          <a href="american-power.html"><img class="dc" src="assets/div-power.png?v=3" alt=""><span>American Power<span class="sub">Solar, battery &amp; EV charging</span></span></a>
        </div></div>
      </div>
      <div class="has-dd">
        <a href="service-areas.html">Areas <span class="car">▼</span></a>
        <div class="dd"><div class="dd-card two">
{dd_areas}
          <a class="dd-cta" href="service-areas.html">View Full Coverage Map</a>
        </div></div>
      </div>
      <a href="about.html">About</a>
      <a href="warranty.html">Warranty</a>
      <a href="faq.html">FAQ</a>
      <div class="has-dd dd-end">
        <a href="about.html">More <span class="car">▼</span></a>
        <div class="dd"><div class="dd-card">
          <a href="financing.html"><span class="di"></span><span>Financing<span class="sub">Buy now, pay on your terms</span></span></a>
          <a href="maintenance.html"><span class="di"></span><span>Care Membership<span class="sub">From $19.95/mo</span></span></a>
          <a href="emergency-appliance-repair.html"><span class="di"></span><span>Emergency Service<span class="sub">After-hours &amp; urgent calls</span></span></a>
          <a href="reviews.html"><span class="di"></span><span>Reviews<span class="sub">4.8★ from 194 neighbors</span></span></a>
          <a href="gallery.html"><span class="di"></span><span>Photo Gallery<span class="sub">The shop, trucks &amp; team</span></span></a>
          <a href="blog.html"><span class="di"></span><span>Blog<span class="sub">Honest appliance advice</span></span></a>
        </div></div>
      </div>
    </nav>
    <div class="cta">
      <button class="btn btn-white book hcp-button" onClick="HCPWidget.openModal()">Book Online</button>
      <a href="tel:+13616730937" class="btn btn-flame"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9z"/></svg><span>(361) 673-0937</span></a>
      <button class="burger" aria-label="Menu">☰</button>
    </div>
  </div>
  <div id="mnav">
    <button class="mgroup" type="button">Services<span class="mcar">▼</span></button>
    <div class="msub">{m_services}<a href="maintenance.html">Care Membership</a></div>
    <a href="index.html#parts">Parts Store</a>
    <button class="mgroup" type="button">Divisions<span class="mcar">▼</span></button>
    <div class="msub msub-div"><a href="index.html#services"><img class="mdc" src="assets/logo-mark.png" alt="">Appliance Repair</a><a href="index.html#parts"><img class="mdc" src="assets/div-parts.png?v=2" alt="">Parts Store</a><a href="appliances-4u.html"><img class="mdc" src="assets/div-sales.png?v=2" alt="">Appliances 4U</a><a href="american-power.html"><img class="mdc" src="assets/div-power.png?v=3" alt="">American Power</a></div>
    <button class="mgroup" type="button">Service Areas<span class="mcar">▼</span></button>
    <div class="msub"><a href="service-areas.html">All Service Areas</a>{m_areas}</div>
    <a href="about.html">About</a>
    <a href="warranty.html">Warranty</a>
    <a href="faq.html">FAQ</a>
    <button class="mgroup" type="button">More<span class="mcar">▼</span></button>
    <div class="msub"><a href="reviews.html">Reviews</a><a href="gallery.html">Photo Gallery</a><a href="blog.html">Blog</a><a href="maintenance.html">Care Membership</a><a href="financing.html">Financing</a><a href="emergency-appliance-repair.html">Emergency Service</a></div>
    <a href="#" onclick="HCPWidget.openModal();return false;">Book Online</a><a href="tel:+13616730937">Call (361) 673-0937</a>
  </div>
</header>'''

FOOTER = '''<footer>
  <div class="wrap">
    <div>
      <div class="flogo"><img src="assets/logo.png" alt="American Appliance Repair, LLC"></div>
      <div class="verse">“For all things I have the strength through the one who gives me power.”</div>
      <div class="ref">Philippians 4:13</div>
    </div>
    <div>
      <h4>Services</h4>
      <a href="refrigerator-ice-machine-repair.html">Refrigerator &amp; Ice Machine</a><a href="washer-repair.html">Washer Repair</a><a href="dryer-repair.html">Dryer Repair</a><a href="dishwasher-repair.html">Dishwasher Repair</a><a href="oven-repair.html">Oven &amp; Stove Repair</a><a href="vent-hood-repair.html">Vent Hood &amp; Disposal</a>
    </div>
    <div>
      <h4>Company</h4>
      <a href="about.html">About Us</a><a href="appliances-4u.html">Appliances 4U Showroom</a><a href="american-power.html">American Power Solar</a><a href="index.html#parts">Parts Store</a><a href="warranty.html">Our Warranty</a><a href="maintenance.html">Care Membership</a><a href="financing.html">Financing</a><a href="emergency-appliance-repair.html">Emergency Service</a><a href="service-areas.html">Service Area</a><a href="reviews.html">Reviews</a><a href="gallery.html">Gallery</a><a href="blog.html">Blog</a><a href="faq.html">FAQ</a>
    </div>
    <div>
      <h4>Contact</h4>
      <a href="tel:+13616730937">Service: (361) 673-0937</a>
      <a href="tel:+13614009513">Parts &amp; Sales: (361) 400-9513</a>
      <a href="index.html#contact">3701 Apollo Rd, Corpus Christi</a>
      <div class="soc"><a class="soc-fb" href="https://www.facebook.com/p/American-Appliance-Repair-61554373376502/" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#fff" d="M15.6 8.4h-1.7c-.34 0-.6.28-.6.66V11h2.28l-.3 2.28h-1.98v6.22h-2.38v-6.22H9V11h1.94V9.02c0-1.94 1.12-3.02 2.9-3.02.85 0 1.58.06 1.76.09z"/></svg></a><a class="soc-ig" href="https://www.instagram.com/american__appliance_repair/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="6" width="12" height="12" rx="3.6" fill="none" stroke="#fff" stroke-width="1.7"/><circle cx="12" cy="12" r="3.1" fill="none" stroke="#fff" stroke-width="1.7"/><circle cx="16.1" cy="7.9" r="1.05" fill="#fff"/></svg></a></div>
    </div>
  </div>
  <div class="wrap fbot">
    <span>© 2026 American Appliance Repair, LLC · Corpus Christi, TX</span>
    <span><a href="privacy-policy.html">Privacy Policy</a> · <a href="terms-of-service.html">Terms of Service</a></span>
    <span>Website by <a href="https://zonkelmedia.com" target="_blank" rel="noopener">Zonkel Media</a></span>
  </div>
</footer>'''

def rev_card(key):
    chip, text, av, nm, src = REVIEWS[key]
    return f'<div class="rev-card"><div class="top"><span class="stars">★★★★★</span><span class="chip">{chip}</span></div><p>{text}</p><div class="who"><div class="av">{av}</div><div><div class="nm">{nm}</div><div class="src">{src}</div></div></div></div>'

def page_html(s):
    symp = "\n      ".join(f'<div class="sy rv"><span class="ck">✓</span><span>{x}</span></div>' for x in s["symptoms"])
    faqs = "\n    ".join(
        f'<details class="rv"{" open" if i==0 else ""}><summary>{q}<span class="pm">+</span></summary><div class="ans">{a}</div></details>'
        for i,(q,a) in enumerate(s["faqs"]))
    others = " ".join(
        f'<a class="chip2" href="{o["file"]}">{o["short"]}</a>'
        for o in SERVICES if o["file"] != s["file"])
    revs = "\n        ".join(rev_card(k) for k in s["reviews"][:1])
    revs_row = "\n      ".join(rev_card(k) for k in s["reviews"][1:])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>document.documentElement.className += ' js';</script>
<title>{s["title"]} | American Appliance Repair</title>
<meta name="description" content="{s["meta"]}">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png?v=2">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png?v=2">
<link rel="icon" type="image/png" sizes="192x192" href="assets/favicon-192.png?v=2">
<link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png?v=2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..900&family=Fraunces:ital,opsz,wght@1,9..144,500;1,9..144,600&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
{head_seo(s["file"], s["title"] + " | American Appliance Repair", s["meta"])}
</head>
<body>

{nav_html(s["file"])}

<!-- page hero -->
<section class="page-hero">
  <div class="bg" style="background-image:url('assets/{s["img"]}');"></div>
  <div class="shade"></div>
  <div class="wrap">
    <div class="crumb h-in"><a href="index.html">Home</a><span class="sep">›</span><a href="index.html#services">Services</a><span class="sep">›</span><span>{s["short"]}</span></div>
    <h1 class="h-in d1">{s["h1"]}<br><span style="color:#FFB25E;">in Corpus Christi, TX</span></h1>
    <p class="lede h-in d2">{s["lede"]}</p>
    <div class="ctas h-in d3">
      <a href="tel:+13616730937" class="btn btn-flame"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9z"/></svg>Call (361) 673-0937</a>
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

<!-- symptoms -->
<section class="sympt">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> Sound Familiar?</span>
      <h2 class="sec">Problems we fix every week</h2>
      <p class="lede">{s["sympt_intro"]}</p>
    </div>
    <div class="sympt-grid">
      {symp}
    </div>
    <div class="svc-cta rv">
      <a href="tel:+13616730937" class="btn btn-navy">Yes, that's mine — Call (361) 673-0937</a>
      <div class="note">Open until 8 PM Mon–Fri · Sat 9–4 · Same-day whenever the schedule allows</div>
    </div>
  </div>
</section>

<!-- how it works -->
<section class="steps-band">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> Simple &amp; Up-Front</span>
      <h2 class="sec">How a repair works with us</h2>
    </div>
    <div class="steps">
      <div class="step rv"><div class="n">1</div><h3>Call or request online</h3><p>Tell us what's acting up. We'll set a time that works — often the same day — and keep you updated on arrival.</p></div>
      <div class="step rv"><div class="n">2</div><h3>Diagnosis &amp; up-front quote</h3><p>A certified tech finds the real problem and quotes the fix before any work starts. No surprises on the invoice.</p></div>
      <div class="step rv"><div class="n">3</div><h3>Fixed — with a warranty</h3><p>Most repairs finish on the spot, because we stock our own parts. Every repair is backed by our warranty.</p></div>
    </div>
  </div>
</section>

<!-- parts advantage -->
<section class="parts-adv">
  <div class="wrap">
    <div>
      <span class="eyebrow rv" style="color:var(--gold);"><img src="assets/insignia.png" alt=""> The Home-Field Advantage</span>
      <h2 class="sec rv">Why we finish repairs other companies reschedule</h2>
      <p class="lede rv">Most repair companies diagnose your appliance, then order the part and come back next week. We run our own parts store — backed by our Marcone partnership — right here in Corpus Christi.</p>
      <ul>
        <li class="rv"><span class="ck">✓</span><span><b>Parts in stock locally</b> — repairs finish in one visit more often</span></li>
        <li class="rv"><span class="ck">✓</span><span><b>OEM &amp; aftermarket options</b> — the right part at the right price</span></li>
        <li class="rv"><span class="ck">✓</span><span><b>Every major brand</b> — Samsung, LG, GE, Whirlpool, Bosch &amp; more</span></li>
      </ul>
    </div>
    <div class="rv">
        {revs}
    </div>
  </div>
</section>

<!-- reviews row -->
<section style="background:var(--cool);border-top:1px solid var(--line-cool);">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> What Your Neighbors Say</span>
      <h2 class="sec">4.8 stars across 194 Google reviews</h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;">
      {revs_row}
    </div>
    <div class="svc-cta rv" style="margin-top:30px;">
      <a href="https://share.google/RAXAsmJPynMQHcw33" target="_blank" rel="noopener" class="btn btn-ghost">Read them all on Google</a>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="faq">
  <div class="wrap">
    <div class="sec-head rv" style="text-align:center;margin-left:auto;margin-right:auto;">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> Good Questions</span>
      <h2 class="sec">{s["short"]} FAQs</h2>
    </div>
    {faqs}
  </div>
</section>

<!-- other services -->
<div class="more-svcs">
  <div class="wrap">
    <h3 class="rv">We also repair</h3>
    <div class="chips rv">{others} <a class="chip2 hot" href="index.html#services">All services →</a></div>
  </div>
</div>

<!-- CTA band -->
<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow rv" style="color:var(--gold);"><img src="assets/insignia.png" alt=""> Swift Solutions</span>
    <h2 class="rv">Your fix could be one call away</h2>
    <p class="lede rv" style="max-width:52ch;">Call now for same-day {s["short"].lower()} service across Corpus Christi &amp; the Coastal Bend — or send a request and we'll get right back to you.</p>
    <div class="ctas rv">
      <a href="tel:+13616730937" class="btn btn-flame"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9z"/></svg>Call (361) 673-0937</a>
      <button class="btn btn-white hcp-button" onClick="HCPWidget.openModal()">Book Online</button>
    </div>
    <div class="fine rv">Approve the repair &amp; the trip + diagnostic fee is on us · Mon–Fri 8–8 · Sat 9–4 · After-hours available</div>
  </div>
</section>

{FOOTER}

<script src="assets/site.js"></script>
<script async src="https://online-booking.housecallpro.com/script.js?token=fddc363afc284aaaa03239c46fb59c0b&orgName=American-Appliance-Repair"></script>
</body>
</html>
'''

for s in SERVICES:
    path = os.path.join(ROOT, s["file"])
    io.open(path, "w", encoding="utf-8").write(page_html(s))
    print("wrote", s["file"])
print("done —", len(SERVICES), "pages")
