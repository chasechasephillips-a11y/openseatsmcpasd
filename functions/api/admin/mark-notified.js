// POST /api/admin/mark-notified
// Body: { token, items: [{ type: 'signature'|'volunteer'|'suggestion', id: 123 }, ...] }
// Flips notified=1 for each row. (suggestion rows live in `volunteers`.)
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();
    if (!context.env.EXPORT_TOKEN || d.token !== context.env.EXPORT_TOKEN) {
      return json({ error: 'Unauthorized' }, 401);
    }
    const items = Array.isArray(d.items) ? d.items : [];
    if (items.length === 0) return json({ ok: true, marked: 0 });

    const sigIds = items.filter(x => x.type === 'signature').map(x => Number(x.id)).filter(n => Number.isFinite(n));
    const volIds = items.filter(x => x.type === 'volunteer' || x.type === 'suggestion').map(x => Number(x.id)).filter(n => Number.isFinite(n));

    let marked = 0;
    if (sigIds.length) {
      const placeholders = sigIds.map(() => '?').join(',');
      const r = await context.env.DB.prepare(
        `UPDATE signatures SET notified = 1 WHERE id IN (${placeholders})`
      ).bind(...sigIds).run();
      marked += r.meta?.changes || 0;
    }
    if (volIds.length) {
      const placeholders = volIds.map(() => '?').join(',');
      const r = await context.env.DB.prepare(
        `UPDATE volunteers SET notified = 1 WHERE id IN (${placeholders})`
      ).bind(...volIds).run();
      marked += r.meta?.changes || 0;
    }

    return json({ ok: true, marked });
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
