// Cookieless pageview beacon for openseatsmcpasd.org.
// No cookies, no localStorage, no consent banner needed.
// Fires two things on load:
//   1) POST /api/pageview → our own D1 table, surfaced in /admin traffic panel.
//   2) Cloudflare Web Analytics beacon (if CF_TOKEN is set) → CF dashboard.
// Skip with ?notrack=1 (e.g. Chase testing his own links).

// Paste your CF Web Analytics site token here once you've enabled it at
// dash.cloudflare.com → Analytics → Web Analytics → Add a site.
// Leave blank to skip — the D1 tracker still works.
var CF_TOKEN = '';

(function () {
  try {
    if (location.search.indexOf('notrack=1') !== -1) return;

    // ─── 1) D1 pageview beacon ───
    var payload = JSON.stringify({
      path: location.pathname,
      referrer: document.referrer || ''
    });
    var url = '/api/pageview';
    if (navigator.sendBeacon) {
      var blob = new Blob([payload], { type: 'application/json' });
      navigator.sendBeacon(url, blob);
    } else {
      fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload,
        keepalive: true
      }).catch(function () {});
    }

    // ─── 2) Cloudflare Web Analytics ───
    if (CF_TOKEN) {
      var s = document.createElement('script');
      s.defer = true;
      s.src = 'https://static.cloudflareinsights.com/beacon.min.js';
      s.setAttribute('data-cf-beacon', JSON.stringify({ token: CF_TOKEN }));
      document.head.appendChild(s);
    }
  } catch (e) { /* never let stats break the page */ }
})();
