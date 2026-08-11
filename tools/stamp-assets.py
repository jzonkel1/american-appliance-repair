# -*- coding: utf-8 -*-
"""Stamps site.css / site.js links in every root page with a content hash.

Browsers (iOS Safari especially) hold a cached stylesheet long past GitHub's
10-minute max-age, so an unchanged URL means an unchanged page on the phone.
Hashing the file into the query string gives every edit a brand-new URL that
no cache can satisfy — and an unchanged file keeps its stamp, so cached copies
stay valid when nothing moved.

Run after any generator. Idempotent.
"""
import io, os, re, glob, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def digest(rel):
    # normalise line endings before hashing: git checks these files out with CRLF
    # on Windows and LF on the Linux Actions runner, and a platform-dependent
    # stamp would make every drip run rewrite all 37 pages (and collide with
    # local edits) even though nothing actually changed.
    with io.open(os.path.join(ROOT, rel), "rb") as f:
        data = f.read().replace(b"\r\n", b"\n")
    return hashlib.md5(data).hexdigest()[:8]

STAMPS = {"assets/site.css": digest("assets/site.css"),
          "assets/site.js": digest("assets/site.js")}

changed = 0
for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
    src = io.open(path, encoding="utf-8").read()
    out = src
    for rel, h in STAMPS.items():
        # match the asset with or without an existing ?v= stamp
        out = re.sub(re.escape(rel) + r"(\?v=[0-9a-f]+)?", rel + "?v=" + h, out)
    if out != src:
        io.open(path, "w", encoding="utf-8").write(out)
        changed += 1

print("stamped", ", ".join(f"{k} -> {v}" for k, v in STAMPS.items()))
print(changed, "of", len(glob.glob(os.path.join(ROOT, '*.html'))), "pages updated")
