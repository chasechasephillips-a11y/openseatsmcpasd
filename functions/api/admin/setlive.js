// GET/POST /api/admin/setlive?token=...&sigCount=&circulators=&goal=
// Update the public live momentum numbers from anywhere (phone-friendly URL).
// Token-gated by EXPORT_TOKEN. Any omitted param keeps its current value.
export async function onRequest(context) {
  const url = new URL(context.request.url);
  const token = url.searchParams.get('token');
  if (!token || token !== context.env.EXPORT_TOKEN) {
    return json({ ok: false, error: 'Unauthorized' }, 401);
  }
  try {
    const cur = (await context.env.DB.prepare(
      `SELECT sig_count, circulators, goal FROM live_stats WHERE id = 1`
    ).first()) || {};
    const num = (v, d) => { const n = parseInt(v, 10); return Number.isFinite(n) && n >= 0 ? n : d; };
    const sigCount = num(url.searchParams.get('sigCount'), cur.sig_count != null ? cur.sig_count : 0);
    const circulators = num(url.searchParams.get('circulators'), cur.circulators != null ? cur.circulators : 0);
    const goal = num(url.searchParams.get('goal'), cur.goal != null ? cur.goal : 550);

    await context.env.DB.prepare(
      `INSERT INTO live_stats (id, sig_count, circulators, goal, updated_at)
       VALUES (1, ?, ?, ?, datetime('now'))
       ON CONFLICT(id) DO UPDATE SET
         sig_count = excluded.sig_count,
         circulators = excluded.circulators,
         goal = excluded.goal,
         updated_at = excluded.updated_at`
    ).bind(sigCount, circulators, goal).run();

    return json({ ok: true, sigCount, circulators, goal });
  } catch (e) {
    return json({ ok: false, error: e.message }, 500);
  }
}

function json(b, s = 200) {
  return new Response(JSON.stringify(b), {
    status: s,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }
  });
}
