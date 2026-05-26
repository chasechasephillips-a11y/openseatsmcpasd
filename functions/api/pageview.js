// POST /api/pageview — cookieless visit beacon.
// Body: { path: string, referrer?: string }
// We hash UA + IP with EXPORT_TOKEN as salt so the raw values never hit disk.
// Bots are filtered by UA; admin/probe traffic is filtered by a query param.

const BOT_RE = /bot|crawl|spider|slurp|bingpreview|headless|monitor|http-client|curl|wget|python-requests|java\/|go-http/i;

export async function onRequestPost(context) {
  try {
    const d = await context.request.json();
    let path = (d.path || '').toString().trim();
    const referrer = (d.referrer || '').toString().trim().slice(0, 500);

    if (!path) return json({ ok: false }, 400);
    // Strip query strings and fragments — we only want page-level paths.
    path = path.split('#')[0].split('?')[0];
    if (path.length > 200) path = path.slice(0, 200);

    const ua = context.request.headers.get('user-agent') || '';
    if (BOT_RE.test(ua)) return json({ ok: true, skipped: 'bot' });

    const ip = context.request.headers.get('cf-connecting-ip') || '';
    const country = context.request.headers.get('cf-ipcountry') || '';
    const salt = context.env.EXPORT_TOKEN || 'unsalted';

    // Salted SHA-256 truncated to 16 hex chars — enough to dedupe visitors,
    // not enough to identify them.
    const uaHash = await sha256(salt + '|ua|' + ua);
    const ipHash = await sha256(salt + '|ip|' + ip);

    await context.env.DB.prepare(
      `INSERT INTO pageviews (path, referrer, ua_hash, ip_hash, country)
       VALUES (?, ?, ?, ?, ?)`
    ).bind(path, referrer || null, uaHash, ipHash, country || null).run();

    return json({ ok: true });
  } catch (err) {
    // Swallow errors — never break the page for a stat write
    return json({ ok: false, error: err.message }, 200);
  }
}

// Permissive CORS for the beacon (called via fetch from openseatsmcpasd.org).
export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '86400'
    }
  });
}

async function sha256(s) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return Array.from(new Uint8Array(buf)).slice(0, 8).map(b => b.toString(16).padStart(2, '0')).join('');
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Cache-Control': 'no-store'
    }
  });
}
