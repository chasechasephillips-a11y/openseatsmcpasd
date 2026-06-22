// /api/canvass
//  POST  — log one canvassing stop (open; used by /circulate app). Idempotent on client_id.
//  GET    — token-gated review feed + summary (used by /admin and the daily email).

export async function onRequestPost(context) {
  try {
    const d = await context.request.json();

    const circulator = (d.circulator || '').toString().trim().slice(0, 80);
    if (!circulator) return json({ error: 'Missing circulator name.' }, 400);

    const clientId = (d.client_id || d.clientId || '').toString().trim().slice(0, 60) || null;
    const address  = (d.address || '').toString().trim().slice(0, 300);
    const talkedTo = (d.talked_to || d.talkedTo || '').toString().trim().slice(0, 300);
    const comments = (d.comments || '').toString().trim().slice(0, 1000);
    const stopTime = (d.stop_time || d.stopTime || '').toString().trim().slice(0, 40);

    let actions = d.actions;
    if (Array.isArray(actions)) actions = actions.join(', ');
    actions = (actions || '').toString().trim().slice(0, 300);

    const lat = numOrNull(d.lat);
    const lon = numOrNull(d.lon);

    // Need at least something meaningful beyond a name.
    if (!address && !actions && !talkedTo && !comments) {
      return json({ error: 'Nothing to log.' }, 400);
    }

    await context.env.DB.prepare(
      `INSERT INTO canvass_log
         (circulator, client_id, address, lat, lon, talked_to, actions, comments, stop_time)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
       ON CONFLICT(client_id) DO NOTHING`
    ).bind(circulator, clientId, address, lat, lon, talkedTo, actions, comments, stopTime).run();

    return json({ ok: true });
  } catch (err) {
    return json({ error: 'Server error.' }, 500);
  }
}

export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const token = url.searchParams.get('token');
  if (!context.env.EXPORT_TOKEN || token !== context.env.EXPORT_TOKEN) {
    return json({ error: 'Unauthorized' }, 401);
  }
  try {
    const rows = await context.env.DB.prepare(
      `SELECT id, circulator, address, lat, lon, talked_to, actions, comments, stop_time, created_at
         FROM canvass_log
        ORDER BY created_at DESC, id DESC
        LIMIT 300`
    ).all();

    const totals = await context.env.DB.prepare(
      `SELECT
         COUNT(*) AS stops,
         SUM(CASE WHEN created_at >= datetime('now','-7 days')  THEN 1 ELSE 0 END) AS stops_7d,
         SUM(CASE WHEN created_at >= datetime('now','-1 days')  THEN 1 ELSE 0 END) AS stops_24h,
         SUM(CASE WHEN actions LIKE '%hanger%'  THEN 1 ELSE 0 END) AS hangers,
         SUM(CASE WHEN actions LIKE '%signed%'  THEN 1 ELSE 0 END) AS signed,
         SUM(CASE WHEN actions LIKE '%dropped%' THEN 1 ELSE 0 END) AS dropped,
         COUNT(DISTINCT circulator) AS circulators
       FROM canvass_log`
    ).first();

    const byCirc = await context.env.DB.prepare(
      `SELECT circulator, COUNT(*) AS stops,
              SUM(CASE WHEN actions LIKE '%hanger%' THEN 1 ELSE 0 END) AS hangers,
              SUM(CASE WHEN actions LIKE '%signed%' THEN 1 ELSE 0 END) AS signed,
              MAX(created_at) AS last_active
         FROM canvass_log
        GROUP BY circulator
        ORDER BY stops DESC`
    ).all();

    return json({
      ok: true,
      rows: rows.results || [],
      totals: totals || {},
      byCirculator: byCirc.results || []
    });
  } catch (err) {
    return json({ error: 'Server error: ' + err.message }, 500);
  }
}

function numOrNull(v) {
  const n = parseFloat(v);
  return Number.isFinite(n) ? n : null;
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' }
  });
}
