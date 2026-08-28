#!/usr/bin/env python3
"""Refresh the Kingdom Business LIVE facade poster.

The homepage player is a click-to-load facade, so it needs a still image. That
image should be the newest episode's own thumbnail, not a fixed photo, or it
drifts out of sync with the player (which always plays the newest upload).

Reads the channel ID straight out of index.html so there is only ever one place
to change it. Uses the uploads playlist page rather than the Data API: no key,
no quota. Writes assets/kbl-poster.jpg only when the bytes actually change, so
a no-op run leaves the tree clean.

Non-fatal by design: YouTube markup shifts around, and a missing poster should
never break a deploy. On any failure it warns and exits 0, leaving the previous
poster in place.

    python tools/fetch-kbl-poster.py
"""

import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
POSTER = ROOT / "assets" / "kbl-poster.jpg"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def warn(msg):
    print(f"[kbl-poster] {msg} — keeping the existing poster")
    sys.exit(0)


def main():
    html = INDEX.read_text(encoding="utf-8")
    m = re.search(r'data-yt-channel="(UC[A-Za-z0-9_-]{22})"', html)
    if not m:
        warn("no configured channel id in index.html")
    channel = m.group(1)

    # The uploads playlist is newest-first, so the first videoId on the page is
    # the latest episode.
    playlist = "UU" + channel[2:]
    try:
        page = get(f"https://www.youtube.com/playlist?list={playlist}").decode(
            "utf-8", "replace")
    except Exception as e:
        warn(f"could not load the uploads playlist ({e})")

    vid = re.search(r'"videoId":"([A-Za-z0-9_-]{11})"', page)
    if not vid:
        warn("no video found in the uploads playlist")
    vid = vid.group(1)

    # maxres only exists once YouTube has generated it; hq always does.
    data = None
    for quality in ("maxresdefault", "hqdefault"):
        try:
            data = get(f"https://i.ytimg.com/vi/{vid}/{quality}.jpg")
            break
        except Exception:
            continue
    if not data:
        warn(f"no thumbnail available for {vid}")

    if POSTER.exists() and POSTER.read_bytes() == data:
        print(f"[kbl-poster] already current ({vid}, {len(data) // 1024} KB)")
        return

    POSTER.parent.mkdir(parents=True, exist_ok=True)
    POSTER.write_bytes(data)
    print(f"[kbl-poster] updated to {vid} ({len(data) // 1024} KB)")


if __name__ == "__main__":
    main()
