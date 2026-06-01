// GET /api/admin/pickups?token=...
// Returns the queue of online signups who asked Elizabeth to pick up
// their signed petition sheet (prefers_pickup = 1). Token-gated.
export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const token = url.searchParams.get('token');
  if (!context.env.EXPORT_TOKEN || token !== context.env.EXPORT_TOKEN) {
    return json({ error: 'Unauthorized' }, 401);
  }
  try {
    const rows = await context.env.DB.prepare(
      `SELECT id, first_name, last_name, email, phone, area, address,
              will_attend_meeting, will_circulate, created_at
         FROM signatures
        WHERE prefers_pickup = 1
        ORDER BY created_at DESC, id DESC`
    ).all();
    const total = await context.env.DB.prepare(
      `SELECT COUNT(*) AS c FROM signatures WHERE prefers_pickup = 1`
    ).first();
    return json({
      ok: true,
      rows: rows.results || [],
      total: total ? total.c : 0
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
