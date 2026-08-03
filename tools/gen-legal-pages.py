# -*- coding: utf-8 -*-
"""Generates privacy-policy.html and terms-of-service.html using the shared
nav/footer from gen-service-pages.py. Edit the body strings, re-run."""
import io, os, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("gsp", os.path.join(HERE, "gen-service-pages.py"))
gsp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gsp)  # note: also regenerates service pages (harmless)

UPDATED = "July 2026"

PRIVACY = ("Privacy Policy", "privacy-policy.html", """
<h2>Who we are</h2>
<p>American Appliance Repair, LLC ("we," "us") is a veteran-owned appliance repair, parts, and sales company located at 3701 Apollo Rd, Corpus Christi, TX 78413. This policy explains what information we collect through this website and how we use it.</p>

<h2>Information we collect</h2>
<ul>
<li><b>Information you send us</b> — when you submit a service request or contact form, we receive the details you provide: your name, phone number, email address, and a description of your appliance issue.</li>
<li><b>Calls and texts</b> — when you call or text our service or parts lines, we keep normal business records of that communication so we can schedule and complete your service.</li>
<li><b>Basic site data</b> — like most websites, our hosting and analytics tools may record standard technical information such as pages visited, browser type, and approximate location, used only to understand how the site is performing.</li>
</ul>

<h2>How we use it</h2>
<ul>
<li>To respond to your request, schedule appointments, and perform the services you ask for</li>
<li>To follow up about work we've done for you — including asking how we did</li>
<li>To keep required business and warranty records</li>
</ul>
<p>If you provide your phone number with a service request, we may call or text you about that request. Message and data rates may apply; reply STOP to any text to opt out of further messages.</p>

<h2>What we don't do</h2>
<p>We do not sell, rent, or trade your personal information. We share it only with the service providers that make our business run (such as website hosting, form processing, and scheduling software), with payment processors when you make a purchase, or when the law requires it.</p>

<h2>Third-party content</h2>
<p>This site embeds content from third parties — Google Maps, Google Fonts, and Facebook video. Those services may set their own cookies or collect usage data under their own privacy policies when the embedded content loads.</p>

<h2>Data retention &amp; your choices</h2>
<p>We keep customer records as long as needed for warranty coverage, bookkeeping, and legal requirements. You can ask us at any time what information we have about you, ask us to correct it, or ask us to delete what we're not legally required to keep — just call or email us using the details below.</p>

<h2>Children</h2>
<p>Our website and services are intended for adults. We do not knowingly collect information from children under 13.</p>

<h2>Changes to this policy</h2>
<p>If we update this policy, the new version will be posted on this page with a new "last updated" date.</p>

<h2>Contact us</h2>
<p>Questions about this policy or your information:<br>
American Appliance Repair, LLC · 3701 Apollo Rd, Corpus Christi, TX 78413<br>
Service: <a href="tel:+13616730937">(361) 673-0937</a> · Parts &amp; Sales: <a href="tel:+13614009513">(361) 400-9513</a></p>
""")

TERMS = ("Terms of Service", "terms-of-service.html", """
<h2>Agreement</h2>
<p>By using this website or scheduling service with American Appliance Repair, LLC ("we," "us"), you agree to these terms. If you don't agree, please don't use the site.</p>

<h2>Our services</h2>
<ul>
<li><b>Estimates &amp; pricing</b> — repair work is quoted up front after diagnosis, before work begins. The price you approve is the price you pay unless additional problems are discovered and approved by you first.</li>
<li><b>Repair warranty</b> — our repairs are backed by a warranty on parts and labor as stated on your service invoice. The invoice is the controlling document for warranty terms on any specific job.</li>
<li><b>Appliance &amp; parts sales</b> — warranty coverage for appliances and parts we sell (including new, scratch-&amp;-dent, and used units) is stated at the time of sale and on your receipt.</li>
<li><b>Scheduling</b> — same-day service depends on availability. Appointment times are our best good-faith estimate, and we'll keep you informed if the schedule changes.</li>
</ul>

<h2>Website content</h2>
<p>The content on this site is provided for general information about our business. We work to keep it accurate, but hours, service offerings, and availability can change without notice — when in doubt, call us. Content on this site (text, images, and branding) belongs to American Appliance Repair, LLC or its licensors and may not be copied for commercial use without permission.</p>

<h2>Reviews and customer content</h2>
<p>Customer reviews shown on this site are real reviews from our Google Business Profile, reproduced as written by their authors.</p>

<h2>Third-party links &amp; embeds</h2>
<p>This site links to and embeds third-party services (such as Google Maps and Facebook). We're not responsible for the content or practices of those services.</p>

<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, American Appliance Repair, LLC is not liable for indirect, incidental, or consequential damages arising from use of this website. Nothing in these terms limits the warranties expressly provided on your service invoice or sales receipt, or any rights you have under Texas law that cannot be waived.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of Texas. Any disputes will be handled in the courts of Nueces County, Texas.</p>

<h2>Changes</h2>
<p>We may update these terms from time to time; the current version will always be posted on this page.</p>

<h2>Contact us</h2>
<p>American Appliance Repair, LLC · 3701 Apollo Rd, Corpus Christi, TX 78413<br>
Service: <a href="tel:+13616730937">(361) 673-0937</a> · Parts &amp; Sales: <a href="tel:+13614009513">(361) 400-9513</a></p>
""")

def build(title, fname, body):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>document.documentElement.className += ' js';</script>
<title>{title} | American Appliance Repair</title>
<meta name="description" content="{title} for American Appliance Repair, LLC — veteran-owned appliance repair, parts and sales in Corpus Christi, TX.">
<meta name="robots" content="noindex,follow">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..900&family=Fraunces:ital,opsz,wght@1,9..144,500;1,9..144,600&family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>

{gsp.nav_html(fname)}

<section class="doc-hero">
  <div class="wrap">
    <h1>{title}</h1>
    <div class="k">American Appliance Repair, LLC · Last updated {UPDATED}</div>
  </div>
</section>

<div class="doc">
{body.strip()}
</div>

{gsp.FOOTER}

<script src="assets/site.js"></script>
</body>
</html>
'''

for title, fname, body in (PRIVACY, TERMS):
    io.open(os.path.join(ROOT, fname), "w", encoding="utf-8").write(build(title, fname, body))
    print("wrote", fname)
