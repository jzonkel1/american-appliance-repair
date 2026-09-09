// americanpowerstx.com -> American Power page.
//
// Why this exists instead of only the _redirects rule: link-preview scrapers
// (Facebook/Instagram/Messenger, iMessage, LinkedIn, Slack, WhatsApp...) fetch
// with a Range header, and Netlify answers a ranged request on a redirect with
// a 206 + "Redirecting to ..." body instead of a 301. The scraper takes the 206
// as the page and shows a bare "americanpowerstx.com" card. So: scrapers get a
// 200 page carrying the American Power Open Graph tags; everyone else gets a
// body-less 301 that nothing can turn into a 206. Only runs for the alias host;
// the main site falls straight through. The _redirects rule still covers every
// other path on the alias.
const TARGET = "https://americanappliancerepaircc.com/american-power.html";
const IMG = "https://americanappliancerepaircc.com/assets/og-american-power.jpg?v=1bdfdfd6";
const TITLE = "American Power \u2014 Solar, Battery Backup & EV Charging | Corpus Christi, TX";
const DESC = "American Power is the renewable energy division of American Appliance Repair \u2014 residential solar, battery backup and EV charging across the Coastal Bend. $0 down. Free energy analysis: (361) 425-7797.";
const BOT = /facebookexternalhit|facebot|twitterbot|linkedinbot|slackbot|slack-imgproxy|whatsapp|discordbot|telegrambot|pinterest|skypeuripreview|embedly|quora link preview|outbrain|vkshare|redditbot|applebot|snapchat|iframely|bingpreview/i;

export default async (request, context) => {
  const host = new URL(request.url).hostname.toLowerCase();
  if (!host.endsWith("americanpowerstx.com")) return context.next();

  const ua = request.headers.get("user-agent") || "";
  if (BOT.test(ua)) {
    const html = `<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>${TITLE}</title>
<meta name="description" content="${DESC}">
<link rel="canonical" href="${TARGET}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="American Power">
<meta property="og:url" content="https://americanpowerstx.com/">
<meta property="og:title" content="${TITLE}">
<meta property="og:description" content="${DESC}">
<meta property="og:image" content="${IMG}">
<meta property="og:image:secure_url" content="${IMG}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="American Power \u2014 solar, battery backup &amp; EV charging in Corpus Christi, TX. (361) 425-7797">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${TITLE}">
<meta name="twitter:description" content="${DESC}">
<meta name="twitter:image" content="${IMG}">
<meta http-equiv="refresh" content="0;url=${TARGET}">
</head><body><p>American Power \u2014 <a href="${TARGET}">continue to the site</a>.</p></body></html>`;
    return new Response(html, { status: 200, headers: { "content-type": "text/html; charset=utf-8", "cache-control": "public, max-age=300" } });
  }

  return new Response(null, { status: 301, headers: { location: TARGET, "cache-control": "public, max-age=3600" } });
};

export const config = { path: "/" };
