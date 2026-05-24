// GET /api/admin/list?token=...
// Returns all paper signatures (token-gated). Used by /admin/ UI.
export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const token = url.searchParams.get('token');
  if (!context.env.EXPORT_TOKEN || token !== context.env.EXPORT_TOKEN) {
    return json({ error: 'Unauthorized' }, 401);
  }
  try {
    const rows = await context.env.DB.prepare(
      `SELECT id, first_name, last_name, street_address, city, area, source,
              circulator_name, date_received, validity, notes, created_at
         FROM paper_signatures
        ORDER BY created_at DESC, id DESC`
    ).all();

    // Per-Area counts (treats unverified as still-counting; only excludes invalid)
    const byArea = await context.env.DB.prepare(
      `SELECT area, COUNT(*) AS c
         FROM paper_signatures
        WHERE validity != 'invalid' AND area != ''
        GROUP BY area`
    ).all();

    const totals = await context.env.DB.prepare(
      `SELECT
         COUNT(*) AS total,
         SUM(CASE WHEN validity = 'valid'      THEN 1 ELSE 0 END) AS valid,
         SUM(CASE WHEN validity = 'invalid'    THEN 1 ELSE 0 END) AS invalid,
         SUM(CASE WHEN validity = 'unverified' THEN 1 ELSE 0 END) AS unverified
       FROM paper_signatures`
    ).first();

    return json({
      ok: true,
      rows: rows.results || [],
      byArea: byArea.results || [],
      totals: totals || { total: 0, valid: 0, invalid: 0, unverified: 0 }
    });
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
