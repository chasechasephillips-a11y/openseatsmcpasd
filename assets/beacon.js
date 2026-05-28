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

    // ─── 3) Engagement: scroll depth + key-section reach + CTA clicks ───
    // Answers "did they read it / try to convert" — which raw pageviews on a
    // single-page site can't. Each event fires at most once per page load.
    var path = location.pathname;
    function ev(kind, label) {
      var body = JSON.stringify({ path: path, kind: kind, label: label });
      if (navigator.sendBeacon) {
        navigator.sendBeacon('/api/event', new Blob([body], { type: 'application/json' }));
      } else {
        fetch('/api/event', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: body, keepalive: true
        }).catch(function () {});
      }
    }

    // 3a) Scroll depth — fire 25/50/75/100 once each.
    var marks = [25, 50, 75, 100], fired = {};
    function onScroll() {
      var doc = document.documentElement;
      var scrollable = doc.scrollHeight - window.innerHeight;
      if (scrollable <= 0) return;
      var pct = (window.scrollY || doc.scrollTop) / scrollable * 100;
      for (var i = 0; i < marks.length; i++) {
        var m = marks[i];
        if (pct >= m && !fired[m]) { fired[m] = 1; ev('scroll', String(m)); }
      }
      if (fired[100]) window.removeEventListener('scroll', onScroll);
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    setTimeout(onScroll, 0); // catch short pages already fully visible

    // 3b) Key-section reach — only the conversion-critical sections.
    var KEY_SECTIONS = ['sign', 'download', 'volunteer', 'events', 'faq'];
    if ('IntersectionObserver' in window) {
      var seen = {};
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting && !seen[e.target.id]) {
            seen[e.target.id] = 1;
            ev('section', e.target.id);
            io.unobserve(e.target);
          }
        });
      }, { threshold: 0.4 });
      KEY_SECTIONS.forEach(function (id) {
        var el = document.getElementById(id);
        if (el) io.observe(el);
      });
    }

    // 3c) CTA clicks — hero buttons, downloads, form submits.
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a, button');
      if (!a) return;
      var href = (a.getAttribute('href') || '');
      var txt = (a.textContent || '').trim().toLowerCase().slice(0, 40);
      if (href.indexOf('#sign') !== -1)            ev('cta', 'click-sign-nav');
      else if (href.indexOf('#meeting') !== -1)    ev('cta', 'click-show-up');
      else if (/\.pdf($|\?)/i.test(href))          ev('cta', 'download-pdf');
      else if (href.indexOf('/circulators') !== -1) ev('cta', 'open-circulators');
      else if (href.indexOf('/toolkit') !== -1)     ev('cta', 'open-toolkit');
      else if (txt.indexOf('sign') !== -1 && a.tagName === 'BUTTON') ev('cta', 'click-sign-btn');
    }, true);

    // Form submits = the real conversion intent.
    ['signForm', 'volForm', 'suggestForm'].forEach(function (id) {
      var f = document.getElementById(id);
      if (f) f.addEventListener('submit', function () { ev('cta', 'submit-' + id); }, true);
    });

  } catch (e) { /* never let stats break the page */ }
})();
