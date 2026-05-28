// POST /api/admin/outreach-log
// Body: { token, email, campaign, stage, channel }
// Records that a message was sent so the sender never double-sends.
// Bound params (safe against quotes in addresses).
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();
    if (!context.env.EXPORT_TOKEN || d.token !== context.env.EXPORT_TOKEN) {
      return json({ error: 'Unauthorized' }, 401);
    }
    const email = (d.email || '').toString().trim().toLowerCase();
    const campaign = (d.campaign || '').toString().trim();
    const stage = (d.stage || '').toString().trim();
    const channel = (d.channel || 'email').toString().trim();
    if (!email || !campaign || !stage) return json({ error: 'Missing fields' }, 400);

    await context.env.DB.prepare(
      `INSERT OR IGNORE INTO outreach_log (email, campaign, stage, channel)
       VALUES (?, ?, ?, ?)`
    ).bind(email, campaign, stage, channel).run();

    return json({ ok: true });
  } catch (err) {
    return json({ error: 'Server error: ' + err.message }, 500);
  }
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }
  });
}
