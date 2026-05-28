// GET /api/unsubscribe?e=<email>&s=<sig>
// Public one-click opt-out. sig = HMAC-SHA256(email, EXPORT_TOKEN) truncated.
// The sender embeds this link in every automated email.
export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const email = (url.searchParams.get('e') || '').trim().toLowerCase();
  const sig = (url.searchParams.get('s') || '').trim();

  if (!email || !sig) return page('Invalid unsubscribe link.', false);

  const expected = await hmac(email, context.env.EXPORT_TOKEN || '');
  if (sig !== expected) return page('This unsubscribe link is invalid or expired.', false);

  try {
    await context.env.DB.prepare(
      'INSERT OR IGNORE INTO outreach_optout (email) VALUES (?)'
    ).bind(email).run();
  } catch (err) {
    return page('Something went wrong. Email chase.chasephillips@gmail.com to opt out.', false);
  }

  return page("You're unsubscribed from Open Seats updates. You won't get any more automated emails. (You can still sign the petition any time.)", true);
}

async function hmac(message, key) {
  const enc = new TextEncoder();
  const cryptoKey = await crypto.subtle.importKey(
    'raw', enc.encode(key), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']
  );
  const sigBuf = await crypto.subtle.sign('HMAC', cryptoKey, enc.encode(message));
  return Array.from(new Uint8Array(sigBuf)).slice(0, 12).map(b => b.toString(16).padStart(2, '0')).join('');
}

function page(msg, ok) {
  const html = `<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Unsubscribe — Open Seats MCPASD</title>
<style>
  body{font-family:Georgia,serif;background:#F5EFE0;color:#1A1614;display:flex;
       align-items:center;justify-content:center;min-height:100vh;margin:0;padding:24px}
  .card{max-width:480px;background:#FCF9F0;border:1px solid #9C8B73;
        box-shadow:5px 5px 0 #9C8B73;padding:36px 32px;text-align:center}
  h1{font-size:22px;color:${ok ? '#355E3B' : '#9A3B2C'};margin:0 0 12px}
  p{font-size:15px;color:#3D332B;line-height:1.6;margin:0}
  a{color:#6F2A1F}
</style></head><body><div class="card">
<h1>${ok ? 'Done.' : 'Hmm.'}</h1><p>${msg}</p>
<p style="margin-top:16px;font-size:13px"><a href="https://openseatsmcpasd.org">openseatsmcpasd.org</a></p>
</div></body></html>`;
  return new Response(html, {
    status: ok ? 200 : 400,
    headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' }
  });
}
