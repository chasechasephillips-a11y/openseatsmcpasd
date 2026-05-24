// POST /api/admin/delete
// Body: { token, id }
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();
    if (!context.env.EXPORT_TOKEN || d.token !== context.env.EXPORT_TOKEN) {
      return json({ error: 'Unauthorized' }, 401);
    }
    const id = parseInt(d.id, 10);
    if (!id) return json({ error: 'id is required' }, 400);

    await context.env.DB.prepare(`DELETE FROM paper_signatures WHERE id = ?`).bind(id).run();
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
