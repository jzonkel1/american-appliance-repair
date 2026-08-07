# -*- coding: utf-8 -*-
"""Generates about.html, warranty.html, financing.html, emergency-appliance-repair.html.
Shares nav/footer with gen-service-pages.py. Edit bodies, re-run."""
import io, os, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("gsp", os.path.join(HERE, "gen-service-pages.py"))
gsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gsp)

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7A2 2 0 0 1 22 16.9z"/></svg>'

def cta_band(lede):
    return f'''<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow rv" style="color:var(--gold);"><img src="assets/insignia.png" alt=""> Swift Solutions</span>
    <h2 class="rv">Your fix could be one call away</h2>
    <p class="lede rv" style="max-width:52ch;">{lede}</p>
    <div class="ctas rv">
      <a href="tel:+13616730937" class="btn btn-flame">{PHONE_SVG}Call (361) 673-0937</a>
      <button class="btn btn-white hcp-button" onClick="HCPWidget.openModal()">Book Online</button>
    </div>
    <div class="fine rv">Approve the repair &amp; the trip + diagnostic fee is on us · Mon–Fri 8–8 · Sat 9–4 · After-hours available</div>
  </div>
</section>'''

PAGES = []

# ---------------- ABOUT ----------------
PAGES.append(dict(file="about.html",
 title="About Us | American Appliance Repair, Corpus Christi TX",
 meta="Christian veteran-owned appliance company in Corpus Christi — founder Rafael served 13 years in the U.S. Army. Repair, parts store and appliance showroom under one roof at 3701 Apollo Rd.",
 noindex=False,
 hero_img="americanappliancerepairteam.jpg",
 crumb="About Us",
 h1="The team behind<br><span style=\"color:#FFB25E;\">your peace of mind</span>",
 lede="A Christian, veteran-owned family of companies — built on integrity, service, quality, innovation and faith.",
 body=f'''
<!-- story -->
<section style="background:var(--paper);">
  <div class="wrap about-grid">
    <div>
      <span class="eyebrow rv"><img src="assets/insignia.png" alt=""> Our Story</span>
      <h2 class="sec rv">13 years in the Army.<br>One standard of service.</h2>
      <p class="lede rv" style="margin-bottom:18px;">American Appliance Repair was founded in 2021 by Rafael, a U.S. Army veteran who served our country for 13 years — and runs his company the way the Army taught him: show up, do it right, and stand behind your work.</p>
      <p class="rv" style="margin-bottom:14px;">What started as a repair service has grown into a family of companies under one roof at 3701 Apollo Rd: a full <b>repair division</b> for homes and businesses, a stocked <b>parts store</b> backed by our Marcone partnership, the <b>Appliances 4U</b> showroom with new, scratch-&amp;-dent and quality used appliances — and now <b><a href="american-power.html" style="color:var(--flame);">American Power</a></b>, our renewable energy division.</p>
      <p class="rv">Faith is at the center of how we work. It's on our logo, it's in how we treat people, and it's why your neighbors call us honest before they call us anything else.</p>
      <div class="verse rv" style="font-family:'Fraunces',serif;font-style:italic;font-weight:500;font-size:17px;color:var(--ink);margin:22px 0 4px;line-height:1.5;">“For all things I have the strength through the one who gives me power.”</div>
      <div class="ref rv" style="font-size:12.5px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--flame);">Philippians 4:13</div>
      <div class="rv" style="display:flex;gap:18px;align-items:center;margin-top:24px;flex-wrap:wrap;"><img src="assets/veteran-badge.png" alt="Military Veteran Owned Business" style="height:64px;width:auto;"></div>
    </div>
    <div class="rv" style="border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow-lg);"><img src="assets/americanappliancerepairteam.jpg" alt="The American Appliance Repair team in a training meeting"></div>
  </div>
</section>

<!-- values -->
<section class="steps-band">
  <div class="wrap">
    <div class="sec-head rv" style="text-align:center;margin-left:auto;margin-right:auto;">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> What We Stand On</span>
      <h2 class="sec">One family of companies, one standard</h2>
    </div>
    <div class="steps five">
      <div class="step rv"><div class="n">✝</div><h3>Faith</h3><p>We trust God in everything — and it shows in how we treat people.</p></div>
      <div class="step rv"><div class="n">★</div><h3>Integrity</h3><p>We do what's right. Always. Even when it costs us the sale.</p></div>
      <div class="step rv"><div class="n">🤝</div><h3>Service</h3><p>Customers first — with live updates and plain-English answers.</p></div>
      <div class="step rv"><div class="n">✓</div><h3>Quality</h3><p>We stand behind our work with a 6-month warranty on every repair.</p></div>
      <div class="step rv"><div class="n">⚡</div><h3>Innovation</h3><p>We embrace better solutions — from booking online to parts on demand.</p></div>
    </div>
  </div>
</section>

<!-- Best of 2026 award -->
<section style="background:var(--paper);">
  <div class="wrap about-grid">
    <div>
      <span class="eyebrow rv"><img src="assets/insignia.png" alt=""> Best of 2026</span>
      <h2 class="sec rv">&ldquo;Success is my duty.&rdquo;</h2>
      <p class="lede rv" style="margin-bottom:18px;">The sign on the office wall says it all — and in 2026 it paid off. BusinessRate named American Appliance Repair the <b>Best Appliance Repair Service in Corpus Christi for 2026</b>, an award powered by real Google reviews.</p>
      <p class="rv">That means it wasn't earned with advertising. It was earned in your neighbors' kitchens and laundry rooms — one honest diagnosis, one clean repair, one kept promise at a time.</p>
      <div class="rv" style="display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin-top:26px;">
        <img src="assets/award-best.png" alt="BusinessRate Best of 2026 Award Winner" style="height:84px;width:auto;">
        <div style="background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px 20px;"><span style="display:block;font-size:10.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);">Google Rating</span><span style="display:block;font-family:'Archivo',sans-serif;font-stretch:125%;font-weight:800;font-size:19px;color:var(--ink);">4.8 <span style="color:var(--gold);font-size:15px;">★★★★★</span></span></div>
        <div style="background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px 20px;"><span style="display:block;font-size:10.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);">Real Reviews</span><span style="display:block;font-family:'Archivo',sans-serif;font-stretch:125%;font-weight:800;font-size:19px;color:var(--ink);">176 on Google</span></div>
      </div>
      <div class="rv" style="margin-top:26px;"><a class="btn btn-flame" href="reviews.html">Read the Reviews</a></div>
    </div>
    <div class="rv" style="border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow-lg);"><img src="assets/businessrate-award.jpg" alt="Rafael holding the BusinessRate Best of 2026 award for Best Appliance Repair Service in Corpus Christi, in front of the 'Success is my duty' wall"></div>
  </div>
</section>

<!-- team photo band -->
<section style="background:var(--cool);border-top:1px solid var(--line-cool);">
  <div class="wrap about-grid flip">
    <div class="rv" style="border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow-lg);"><img src="assets/team-bowling.jpg" alt="The American Appliance Repair team on a company outing"></div>
    <div>
      <span class="eyebrow rv"><img src="assets/insignia.png" alt=""> More Than Coworkers</span>
      <h2 class="sec rv">Real people. Real family.</h2>
      <p class="lede rv" style="margin-bottom:16px;">Ever wonder who's fixing your fridge? These are the faces — technicians, office staff, and family, often side by side on the same job.</p>
      <p class="rv">When you call us, you're not routed through a national call center. You're talking to a Corpus Christi family business that answers to its neighbors — and to a higher standard.</p>
      <div class="rv" style="display:flex;gap:14px;flex-wrap:wrap;margin-top:24px;">
        <div style="background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px 20px;"><span style="display:block;font-size:10.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);">Service</span><a href="tel:+13616730937" style="display:block;font-family:'Archivo',sans-serif;font-stretch:125%;font-weight:800;font-size:19px;color:var(--ink);">(361) 673-0937</a></div>
        <div style="background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px 20px;"><span style="display:block;font-size:10.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);">Parts &amp; Sales</span><a href="tel:+13614009513" style="display:block;font-family:'Archivo',sans-serif;font-stretch:125%;font-weight:800;font-size:19px;color:var(--ink);">(361) 400-9513</a></div>
      </div>
    </div>
  </div>
</section>

<!-- Kingdom Business Live -->
<section style="background:linear-gradient(165deg,var(--ink),var(--navy));color:#fff;">
  <div class="wrap about-grid">
    <div>
      <span class="eyebrow rv" style="color:var(--gold);"><img src="assets/insignia.png" alt=""> Kingdom Business Live</span>
      <h2 class="sec rv" style="color:#fff;">Faith and business,<br><span style="color:#FFB25E;">live every Tuesday</span></h2>
      <p class="lede rv" style="color:#C4D3E2;">Rafael hosts <b style="color:#fff;">Kingdom Business Live</b> — a weekly show about running a business on Kingdom principles, stewardship and serving people well — live on Facebook every Tuesday at 6&nbsp;PM.</p>
      <div class="rv" style="font-family:'Fraunces',serif;font-style:italic;font-weight:500;font-size:17px;color:#F4E9DB;margin:22px 0 4px;line-height:1.5;">&ldquo;Whoever can be trusted with very little can also be trusted with much.&rdquo;</div>
      <div class="rv" style="font-size:12.5px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);">Luke 16:10</div>
      <div class="rv" style="margin-top:26px;"><a class="btn btn-flame" href="https://www.facebook.com/juan.colon.9883739/videos/2240320903383618/" target="_blank" rel="noopener">Watch on Facebook</a></div>
    </div>
    <div class="rv" style="border-radius:var(--r-lg);overflow:hidden;box-shadow:0 30px 70px -20px rgba(0,0,0,.5);"><img src="assets/rafaelcordero.jpg" alt="Rafael, founder of American Appliance Repair and host of Kingdom Business Live"></div>
  </div>
</section>

{cta_band("Whether it's a repair, a part, or a whole new appliance — the same family takes care of you.")}
'''))

# ---------------- WARRANTY ----------------
PAGES.append(dict(file="warranty.html",
 title="Our Warranty | American Appliance Repair, Corpus Christi TX",
 meta="Every American Appliance Repair job is backed by a 6-month warranty on parts replaced and labor. Plus: approve the repair and your trip & diagnostic fee is on us.",
 noindex=False,
 hero_img="AAR_Appliance_Service_IMG-5.jpg",
 crumb="Our Warranty",
 h1="Our warranty:<br><span style=\"color:#FFB25E;\">we stand behind the work</span>",
 lede="Every repair is backed by a 6-month warranty on parts replaced and labor. Here's exactly what that means — in plain English.",
 body=f'''
<section style="background:var(--paper);">
  <div class="wrap" style="max-width:860px;">
    <div class="sec-head rv">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> The Promise</span>
      <h2 class="sec">6 months. Parts &amp; labor.</h2>
      <p class="lede">If a part we replaced fails, or the repair we made doesn't hold, within 6 months — we make it right. That's the promise on every invoice.</p>
    </div>
    <div class="sympt-grid" style="grid-template-columns:1fr 1fr;">
      <div class="sy rv"><span class="ck">✓</span><span><b>6-month warranty</b> on every part we replace</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>6-month warranty</b> on the labor for that repair</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Approve the repair, and your trip &amp; diagnostic fee is on us</b></span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Honest answers</b> — if it's not worth fixing, we'll tell you</span></div>
    </div>
    <div class="sec-head rv" style="margin-top:52px;">
      <h2 class="sec" style="font-size:clamp(22px,2.6vw,30px);">The fine print, honestly stated</h2>
      <p class="lede">No surprises — here's what the warranty does and doesn't cover:</p>
    </div>
    <div class="faq" style="background:none;">
      <details class="rv" open><summary>What if a different part fails later?<span class="pm">+</span></summary><div class="ans">The warranty covers the part we replaced and the labor for that repair. If a warranty call turns out to be a different part or a separate problem not covered under the original repair, a trip fee applies — and we'll quote the new repair up front, as always.</div></details>
      <details class="rv"><summary>Does maintenance count as labor?<span class="pm">+</span></summary><div class="ans">Corrective maintenance is not covered under the labor warranty — the warranty covers the repair work itself.</div></details>
      <details class="rv"><summary>What voids the warranty?<span class="pm">+</span></summary><div class="ans">Labor, diagnostics, or any attempt to repair the appliance by anyone other than American Appliance Repair voids the labor warranty. Damage to replaced parts caused by the customer or a third party voids the parts warranty. In short: let us stand behind our own work, and we will.</div></details>
      <details class="rv"><summary>What about appliances I buy from you?<span class="pm">+</span></summary><div class="ans">Units from our Appliances 4U showroom carry their own coverage: <b>new (manufactured) units — 12 months; pre-owned units — 30 days.</b> Details at the time of sale and on your receipt.</div></details>
    </div>
  </div>
</section>

{cta_band("Up-front quotes, a 6-month warranty, and the diagnostic fee on us when you approve the repair.")}
'''))

# ---------------- FINANCING ----------------
PAGES.append(dict(file="financing.html",
 title="Financing | American Appliances 4U, Corpus Christi TX",
 meta="Financing available on appliances at the Appliances 4U showroom in Corpus Christi — new, scratch-&-dent and quality used units. We also buy appliances and accept trade-ins.",
 noindex=False,
 hero_img="warehouse.jpg",
 crumb="Financing",
 h1="Get the appliance now.<br><span style=\"color:#FFB25E;\">Pay on your terms.</span>",
 lede="Financing is available on appliance purchases at our Appliances 4U showroom — new, scratch-&-dent, and quality used units.",
 body=f'''
<section style="background:var(--paper);">
  <div class="wrap" style="max-width:860px;">
    <div class="sec-head rv">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> Appliances 4U Showroom</span>
      <h2 class="sec">How it works</h2>
      <p class="lede">Come see the showroom at 3701 Apollo Rd — new, scratch-&amp;-dent and pre-owned units, with options to fit your budget.</p>
    </div>
    <div class="steps">
      <div class="step rv"><div class="n">1</div><h3>Pick your appliance</h3><p>New, scratch-&amp;-dent, or quality used — every unit backed by a warranty (12 months on new, 30 days on pre-owned).</p></div>
      <div class="step rv"><div class="n">2</div><h3>Ask about financing</h3><p>Financing is available on appliance purchases — ask at the showroom or call (361) 400-9513 and we'll walk you through it.</p></div>
      <div class="step rv"><div class="n">3</div><h3>Delivery &amp; installation</h3><p>Delivery and professional installation are available for a fee — we'll quote it with your purchase, and we haul away the old unit too.</p></div>
    </div>
    <div class="sympt-grid" style="grid-template-columns:1fr 1fr;margin-top:40px;">
      <div class="sy rv"><span class="ck">✓</span><span><b>We buy appliances</b> — turn your old unit into cash</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Trade-ins accepted</b> — put your old unit toward the new one</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Installation &amp; haul-away</b> available with delivery</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Repair-first honesty</b> — if fixing yours is smarter, we'll say so</span></div>
    </div>
  </div>
</section>

{cta_band("Visit the showroom at 3701 Apollo Rd, or call Parts & Sales at (361) 400-9513 to ask about financing.")}
'''))

# ---------------- EMERGENCY ----------------
PAGES.append(dict(file="emergency-appliance-repair.html",
 title="Emergency & After-Hours Appliance Repair | Corpus Christi TX",
 meta="Appliance emergency in Corpus Christi? After-hours and emergency service available — refrigerators, freezers, commercial ice machines and more. Call (361) 673-0937.",
 noindex=False,
 hero_img="AAR_Appliance_Service_IMG-1.jpg",
 crumb="Emergency Service",
 h1="Appliance emergency?<br><span style=\"color:#FFB25E;\">We answer after hours.</span>",
 lede="Some appliance problems can't wait for business hours. After-hours and emergency service is available — call and we'll get you taken care of.",
 body=f'''
<section class="sympt">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> Can't-Wait Problems</span>
      <h2 class="sec">When it's an emergency, call — don't wait</h2>
      <p class="lede">These are the calls we treat as urgent:</p>
    </div>
    <div class="sympt-grid">
      <div class="sy rv"><span class="ck">✓</span><span><b>Refrigerator or freezer down</b> — hundreds of dollars of food on the line</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Commercial ice machine out</b> — your restaurant or bar can't serve</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Washer flooding</b> — water on the floor and spreading</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Gas smell at the stove</b> — leave, call your gas provider or 911 FIRST, then us for the repair</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Dryer burning smell</b> — stop the dryer and call; lint and heat are a fire risk</span></div>
      <div class="sy rv"><span class="ck">✓</span><span><b>Commercial kitchen equipment down</b> — every hour is money</span></div>
    </div>
    <div class="svc-cta rv">
      <a href="tel:+13616730937" class="btn btn-navy">Emergency? Call (361) 673-0937 now</a>
      <div class="note">Open Mon–Fri 8–8 · Sat 9–4 · After-hours &amp; emergency service available by phone</div>
    </div>
  </div>
</section>

<section class="steps-band">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> What To Expect</span>
      <h2 class="sec">Fast help, honest priorities</h2>
    </div>
    <div class="steps">
      <div class="step rv"><div class="n">1</div><h3>Call — day or night</h3><p>Talk to us, tell us what's happening, and we'll tell you honestly how fast we can be there.</p></div>
      <div class="step rv"><div class="n">2</div><h3>Protect what matters</h3><p>We'll walk you through what to do right now — keep the fridge closed, shut the water valve, kill the breaker.</p></div>
      <div class="step rv"><div class="n">3</div><h3>Fixed with parts on hand</h3><p>Our own parts store means emergency repairs finish in one visit more often — with a 6-month warranty.</p></div>
    </div>
  </div>
</section>

{cta_band("Refrigerators, freezers, ice machines, washers — when it can't wait, call us first.")}
'''))

# ---------------- AMERICAN POWER ----------------
PAGES.append(dict(file="american-power.html",
 title="American Power — Solar, Battery Backup & EV Charging | Corpus Christi, TX",
 meta="American Power is the renewable energy division of American Appliance Repair — residential & commercial solar, battery backup and EV charging across the Coastal Bend, in partnership with Powur. $0 down. Free energy analysis: (361) 673-0937.",
 noindex=False,
 hero_img="solar-home.jpg",
 crumb="American Power",
 h1="Stop renting your electricity.<br><span style=\"color:#FFB25E;\">Own your power.</span>",
 lede="Solar solutions designed to save you money and protect your future — from the same veteran-owned family you already trust with your appliances.",
 ctas=f'''      <a href="tel:+13616730937" class="btn btn-flame">{PHONE_SVG}Free Energy Analysis — (361) 673-0937</a>''',
 body='''
<!-- intro -->
<section style="background:var(--paper);">
  <div class="wrap about-grid">
    <div>
      <span class="eyebrow rv"><img src="assets/insignia.png" alt=""> Renewable Energy Division</span>
      <h2 class="sec rv">The newest member<br>of the family</h2>
      <p class="lede rv" style="margin-bottom:18px;">American Power brings the same veteran-owned, faith-led standard you know from our repair trucks to your energy bill — solar, battery backup and EV charging for homes and businesses across the Coastal Bend.</p>
      <p class="rv" style="margin-bottom:14px;">We work in partnership with <b>Powur</b>, one of the nation's leading solar platforms — so you get proven equipment and professional installation, with a local, familiar face handling it from first conversation to switch-on.</p>
      <p class="rv">It starts with a <b>free custom energy analysis</b> built around your home and your actual usage — no pressure, no obligation, just the honest math on what your roof could be doing for you.</p>
    </div>
    <div class="rv" style="border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow-lg);"><img src="assets/solar-home.jpg" alt="Home with rooftop solar panels — American Power solar installation"></div>
  </div>
</section>

<!-- value props -->
<section class="solar-band">
  <div class="wrap" style="display:block;">
    <img class="ap-logo rv" src="assets/american-power-logo.png?v=4" alt="American Power — Own Your Power">
    <h2 class="sec rv" style="color:#fff;">Why go solar with <span class="fl">American Power</span></h2>
    <div class="solar-list" style="max-width:900px;">
      <div class="si rv"><span class="ck">✓</span><span><b>$0 down</b> — go solar and start saving immediately</span></div>
      <div class="si rv"><span class="ck">✓</span><span><b>No upfront cost</b> — no large payments, no hidden fees</span></div>
      <div class="si rv"><span class="ck">✓</span><span><b>Protection from rising energy costs</b> — lock in predictable rates</span></div>
      <div class="si rv"><span class="ck">✓</span><span><b>Free custom energy analysis</b> — built around your home &amp; usage</span></div>
      <div class="si rv"><span class="ck">✓</span><span><b>Start saving immediately</b> — lower bills from the moment it's on</span></div>
      <div class="si rv"><span class="ck">✓</span><span><b>Residential &amp; commercial</b> — plus battery backup &amp; EV charging</span></div>
    </div>
    <div class="pw rv">In partnership with Powur · A division of American Appliance Repair, LLC</div>
  </div>
</section>

<!-- what we offer -->
<section class="steps-band">
  <div class="wrap">
    <div class="sec-head rv" style="text-align:center;margin-left:auto;margin-right:auto;">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> What We Offer</span>
      <h2 class="sec">Power for every part of your life</h2>
    </div>
    <div class="steps">
      <div class="step rv"><div class="n">☀</div><h3>Solar Systems</h3><p>Residential &amp; commercial rooftop solar — designed around your usage so the numbers actually work.</p></div>
      <div class="step rv"><div class="n">🔋</div><h3>Battery Backup</h3><p>Keep the lights on when the grid goes down — store your own power for outages and peak hours.</p></div>
      <div class="step rv"><div class="n">⚡</div><h3>EV Charging</h3><p>Home charging solutions for your electric vehicle — fueled by your own roof.</p></div>
    </div>
  </div>
</section>

<!-- how it works -->
<section style="background:var(--cool);border-top:1px solid var(--line-cool);">
  <div class="wrap">
    <div class="sec-head rv" style="text-align:center;margin-left:auto;margin-right:auto;">
      <span class="eyebrow"><img src="assets/insignia.png" alt=""> How It Works</span>
      <h2 class="sec">Three steps to owning your power</h2>
    </div>
    <div class="steps">
      <div class="step rv"><div class="n">1</div><h3>Free Energy Analysis</h3><p>We look at your bill and your usage and give you the honest math — no pressure, no obligation.</p></div>
      <div class="step rv"><div class="n">2</div><h3>Custom Proposal</h3><p>A system designed around your home — $0 down, no upfront cost, no hidden fees.</p></div>
      <div class="step rv"><div class="n">3</div><h3>Install &amp; Switch On</h3><p>Professional installation through our Powur partnership — and your savings start the moment it's live.</p></div>
    </div>
  </div>
</section>

<!-- cta -->
<section class="cta-band">
  <div class="wrap">
    <span class="eyebrow rv" style="color:var(--gold);"><img src="assets/insignia.png" alt=""> Own Your Power</span>
    <h2 class="rv">Find out what your roof could be saving you</h2>
    <p class="lede rv" style="max-width:52ch;">One call gets you a free custom energy analysis — built around your home, your usage and your bill.</p>
    <div class="ctas rv">
      <a href="tel:+13616730937" class="btn btn-flame">''' + PHONE_SVG + '''Call (361) 673-0937</a>
      <a href="index.html#contact" class="btn btn-white">Send a Request</a>
    </div>
    <div class="fine rv">Free energy analysis · $0 down · Residential &amp; commercial · A division of American Appliance Repair, LLC</div>
  </div>
</section>'''))

# ---------------- template ----------------
def build(p):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
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
  <div class="bg" style="background-image:url('assets/{p["hero_img"]}');"></div>
  <div class="shade"></div>
  <div class="wrap">
    <div class="crumb h-in"><a href="index.html">Home</a><span class="sep">›</span><span>{p["crumb"]}</span></div>
    <h1 class="h-in d1">{p["h1"]}</h1>
    <p class="lede h-in d2">{p["lede"]}</p>
    <div class="ctas h-in d3">
{p.get("ctas") or f'''      <a href="tel:+13616730937" class="btn btn-flame">{PHONE_SVG}Call (361) 673-0937</a>
      <button class="btn btn-white hcp-button" onClick="HCPWidget.openModal()">Book Online</button>'''}
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
