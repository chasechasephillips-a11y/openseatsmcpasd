// GET /api/admin/pending?token=...
// Returns submissions (signatures + volunteers + event suggestions) where
// notified=0. The local notifier polls this, sends Chase an email per row,
// then POSTs /api/admin/mark-notified to flip the flag.
export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const token = url.searchParams.get('token');
  if (!context.env.EXPORT_TOKEN || token !== context.env.EXPORT_TOKEN) {
    return json({ error: 'Unauthorized' }, 401);
  }

  try {
    const sigs = await context.env.DB.prepare(
      `SELECT id, first_name, last_name, email, phone, area, address,
              will_attend_meeting, will_circulate, created_at
         FROM signatures
        WHERE notified = 0
        ORDER BY created_at ASC`
    ).all();

    const vols = await context.env.DB.prepare(
      `SELECT id, name, email, phone, help, created_at
         FROM volunteers
        WHERE notified = 0
        ORDER BY created_at ASC`
    ).all();

    const sigRows = (sigs.results || []).map(r => ({ type: 'signature', ...r }));
    const volRows = (vols.results || []).map(r => {
      const isSuggest = (r.help || '').startsWith('EVENT_SUGGESTION:');
      return { type: isSuggest ? 'suggestion' : 'volunteer', ...r };
    });

    return json({ ok: true, rows: [...sigRows, ...volRows] });
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
