// POST /api/admin/update — change validity, edit fields, etc.
// Body: { token, id, ...any-field-to-update }
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();
    if (!context.env.EXPORT_TOKEN || d.token !== context.env.EXPORT_TOKEN) {
      return json({ error: 'Unauthorized' }, 401);
    }
    const id = parseInt(d.id, 10);
    if (!id) return json({ error: 'id is required' }, 400);

    const allowed = ['first_name', 'last_name', 'street_address', 'city', 'area',
                     'source', 'circulator_name', 'date_received', 'validity', 'notes'];
    const sets = [];
    const vals = [];
    for (const k of allowed) {
      if (k in d) {
        let v = d[k];
        if (k === 'validity' && !['valid', 'invalid', 'unverified'].includes(v)) continue;
        sets.push(`${k} = ?`);
        vals.push((v ?? '').toString());
      }
    }
    if (sets.length === 0) return json({ error: 'No fields to update' }, 400);

    vals.push(id);
    await context.env.DB.prepare(
      `UPDATE paper_signatures SET ${sets.join(', ')} WHERE id = ?`
    ).bind(...vals).run();

    return json({ ok: true });
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
