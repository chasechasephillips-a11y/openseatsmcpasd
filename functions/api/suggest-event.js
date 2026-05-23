// POST /api/suggest-event — low-friction event location suggestions.
// Piggy-backs on the volunteers table; rows are tagged
// help="EVENT_SUGGESTION: <where>" so they're easy to filter on export.
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();
    const where = (d.where || '').toString().trim();
    const name  = (d.name  || '').toString().trim() || 'Anonymous';
    const email = (d.email || '').toString().trim().toLowerCase() || 'noreply@suggest.local';

    if (!where) return json({ error: 'Tell us where to host.' }, 400);
    if (where.length > 500) return json({ error: 'Keep it under 500 characters.' }, 400);

    await context.env.DB.prepare(
      `INSERT INTO volunteers (name, email, phone, help) VALUES (?, ?, ?, ?)`
    ).bind(`SUGGEST: ${name}`, email, '', `EVENT_SUGGESTION: ${where}`).run();

    return json({ ok: true });
  } catch (err) {
    return json({ error: 'Server error.' }, 500);
  }
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}
