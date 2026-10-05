// POST /api/yes-volunteer — records a /yes/ volunteer sign-up into D1.
// Separate from /api/volunteer: Yes Committee sign-ups live in yes_volunteers.
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();

    const name = clip(d.name, 120);
    const email = clip(d.email, 200).toLowerCase();
    const phone = clip(d.phone, 40);
    const area = clip(d.area, 80);
    const note = clip(d.note, 1000);

    if (!name || !email || !email.includes('@')) {
      return json({ error: 'Name and a valid email are required.' }, 400);
    }

    let help = d.how;
    if (Array.isArray(help)) help = help.join(', ');
    help = clip(help, 500);

    await context.env.DB.prepare(
      `INSERT INTO yes_volunteers (name, email, phone, area, help, note) VALUES (?, ?, ?, ?, ?, ?)`
    ).bind(name, email, phone, area, help, note).run();

    return json({ ok: true });
  } catch (err) {
    return json({ error: 'Server error.' }, 500);
  }
}

function clip(v, n) {
  return (v || '').toString().trim().slice(0, n);
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' }
  });
}
