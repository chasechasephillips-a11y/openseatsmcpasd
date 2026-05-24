// POST /api/admin/add
// Body: { token, first_name, last_name, street_address, city, area, source,
//         circulator_name, date_received, validity, notes }
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();
    if (!context.env.EXPORT_TOKEN || d.token !== context.env.EXPORT_TOKEN) {
      return json({ error: 'Unauthorized' }, 401);
    }
    const first = (d.first_name || '').toString().trim();
    const last  = (d.last_name  || '').toString().trim();
    if (!first || !last) return json({ error: 'first_name and last_name are required' }, 400);

    const validity = ['valid', 'invalid', 'unverified'].includes(d.validity) ? d.validity : 'unverified';

    const result = await context.env.DB.prepare(
      `INSERT INTO paper_signatures
         (first_name, last_name, street_address, city, area, source,
          circulator_name, date_received, validity, notes)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
    ).bind(
      first, last,
      (d.street_address || '').toString().trim(),
      (d.city || '').toString().trim(),
      (d.area || '').toString().trim(),
      (d.source || '').toString().trim(),
      (d.circulator_name || '').toString().trim(),
      (d.date_received || new Date().toISOString().slice(0, 10)).toString().trim(),
      validity,
      (d.notes || '').toString().trim()
    ).run();

    return json({ ok: true, id: result.meta?.last_row_id });
  } catch (err) {
    return json({ error: 'Server error: ' + err.message }, 500);
  }
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}
