"""One-time refactor: pull the homepage's inline CSS/JS into shared files
(assets/site.css + assets/site.js) and relink index.html, then append the
service-page styles used by the generated service pages."""
import re, io

ROOT = r"C:\Users\George\Desktop\Zonkel Media\Websites\American Appliance Repair"
idx = io.open(ROOT + r"\index.html", encoding="utf-8").read()

# ---- extract <style> ----
m = re.search(r"<style>(.*?)</style>", idx, re.S)
css = m.group(1)

SERVICE_CSS = """
  /* ---------- service pages ---------- */
  .page-hero{position:relative;min-height:440px;display:flex;align-items:flex-end;padding:170px 0 58px;overflow:hidden;background:var(--ink);}
  .page-hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;}
  .page-hero .shade{position:absolute;inset:0;background:linear-gradient(100deg,rgba(0,4,34,.93) 0%,rgba(0,4,34,.74) 46%,rgba(0,4,34,.32) 100%),linear-gradient(0deg,rgba(0,4,34,.6) 0%,transparent 42%);}
  .page-hero .wrap{position:relative;z-index:2;width:100%;}
  .crumb{display:flex;gap:8px;align-items:center;font-size:12.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#9FB4C9;margin-bottom:16px;flex-wrap:wrap;}
  .crumb a:hover{color:#fff;}
  .crumb .sep{color:var(--flame);}
  .page-hero h1{color:#fff;font-size:clamp(34px,4.8vw,58px);max-width:16em;margin:0 0 14px;text-shadow:0 4px 26px rgba(0,4,34,.5);}
  .page-hero .lede{color:#D9E2EC;max-width:58ch;text-shadow:0 1px 10px rgba(0,4,34,.5);}
  .page-hero .ctas{display:flex;gap:14px;flex-wrap:wrap;margin-top:26px;}
  .sympt{background:var(--paper);padding-top:70px;}
  .sympt-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:38px;}
  .sy{background:#fff;border:1px solid var(--line);border-radius:var(--r-md);padding:18px 20px;display:flex;gap:13px;align-items:flex-start;font-size:15px;color:var(--body);line-height:1.5;}
  .sy .ck{color:var(--flame);font-weight:800;flex:none;font-size:17px;}
  .sy b{color:var(--ink);}
  .steps-band{background:#fff;border-top:1px solid var(--line);border-bottom:1px solid var(--line);}
  .steps{display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px;margin-top:40px;}
  .step{position:relative;padding:26px 24px 24px;background:var(--paper);border:1px solid var(--line);border-radius:var(--r-lg);}
  .step .n{font-family:'Archivo',sans-serif;font-stretch:125%;font-weight:800;font-size:34px;color:var(--flame);line-height:1;margin-bottom:10px;}
  .step h3{font-size:17px;margin-bottom:7px;}
  .step p{font-size:14px;color:var(--soft);line-height:1.55;}
  .parts-adv{background:var(--navy);color:#fff;position:relative;overflow:hidden;}
  .parts-adv:before{content:"";position:absolute;top:-200px;right:-120px;width:480px;height:480px;border-radius:50%;background:radial-gradient(circle,rgba(232,115,12,.15),transparent 65%);}
  .parts-adv .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:50px;align-items:center;position:relative;}
  .parts-adv h2{color:#fff;}
  .parts-adv .lede{color:#C4D3E2;}
  .parts-adv ul{list-style:none;margin-top:22px;}
  .parts-adv li{display:flex;gap:12px;padding:7px 0;font-size:15.5px;color:#DCE6EF;}
  .parts-adv li .ck{color:var(--gold);font-weight:800;flex:none;}
  .parts-adv li b{color:#fff;}
  .parts-adv .rev-card{flex:none;transform:rotate(1.2deg);}
  .more-svcs{background:var(--cool);border-top:1px solid var(--line-cool);padding:54px 0;}
  .more-svcs h3{font-size:20px;margin-bottom:20px;}
  .cta-band{background:linear-gradient(165deg,var(--ink),var(--navy));color:#fff;text-align:center;}
  .cta-band h2{color:#fff;font-size:clamp(28px,3.4vw,42px);}
  .cta-band .lede{color:#B9C9D9;margin:14px auto 30px;}
  .cta-band .ctas{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
  .cta-band .fine{margin-top:18px;font-size:13.5px;color:#8AA2BA;font-weight:600;}
  @media(max-width:1020px){
    .sympt-grid,.steps{grid-template-columns:1fr 1fr;}
    .parts-adv .wrap{grid-template-columns:1fr;}
  }
  @media(max-width:640px){
    .sympt-grid,.steps{grid-template-columns:1fr;}
    .page-hero{text-align:center;padding-top:150px;}
    .page-hero h1,.page-hero .lede{margin-left:auto;margin-right:auto;}
    .page-hero .ctas{justify-content:center;}
    .crumb{justify-content:center;}
  }
"""

io.open(ROOT + r"\assets\site.css", "w", encoding="utf-8").write(css.strip() + "\n" + SERVICE_CSS)
idx = idx.replace(m.group(0), '<link rel="stylesheet" href="assets/site.css">')

# ---- extract bottom <script> (the one after footer) ----
m2 = re.search(r"<script>\n// nav: transparent(.*?)</script>", idx, re.S)
js = "// nav: transparent" + m2.group(1)
# guard the marquee clone for pages without #revTrack
js = js.replace(
    "const track = document.getElementById('revTrack');\nconst clone = track.cloneNode(true);\nclone.setAttribute('aria-hidden','true');\ntrack.parentNode.appendChild(clone);",
    "const track = document.getElementById('revTrack');\nif (track) {\n  const clone = track.cloneNode(true);\n  clone.setAttribute('aria-hidden','true');\n  track.parentNode.appendChild(clone);\n}"
)
io.open(ROOT + r"\assets\site.js", "w", encoding="utf-8").write(js.strip() + "\n")
idx = idx.replace(m2.group(0), '<script src="assets/site.js"></script>')

io.open(ROOT + r"\index.html", "w", encoding="utf-8").write(idx)
print("site.css:", len(css), "chars + service styles")
print("site.js:", len(js), "chars")
print("index.html relinked")
