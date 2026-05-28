// POST /api/event — engagement beacon (scroll depth, section reach, CTA clicks).
// Body: { path, kind: 'scroll'|'section'|'cta', label }
// Same salted IP hashing as /api/pageview. Bots filtered by UA.

const BOT_RE = /bot|crawl|spider|slurp|bingpreview|headless|monitor|http-client|curl|wget|python-requests|java\/|go-http/i;
const VALID_KINDS = ['scroll', 'section', 'cta'];

export async function onRequestPost(context) {
  try {
    const d = await context.request.json();
    let path = (d.path || '').toString().trim().split('#')[0].split('?')[0].slice(0, 200);
    const kind = (d.kind || '').toString().trim();
    const label = (d.label || '').toString().trim().slice(0, 60);

    if (!path || !VALID_KINDS.includes(kind) || !label) return json({ ok: false }, 400);

    const ua = context.request.headers.get('user-agent') || '';
    if (BOT_RE.test(ua)) return json({ ok: true, skipped: 'bot' });

    const ip = context.request.headers.get('cf-connecting-ip') || '';
    const salt = context.env.EXPORT_TOKEN || 'unsalted';
    const ipHash = await sha256(salt + '|ip|' + ip);

    await context.env.DB.prepare(
      `INSERT INTO events (path, kind, label, ip_hash) VALUES (?, ?, ?, ?)`
    ).bind(path, kind, label, ipHash).run();

    return json({ ok: true });
  } catch (err) {
    return json({ ok: false, error: err.message }, 200);
  }
}

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
