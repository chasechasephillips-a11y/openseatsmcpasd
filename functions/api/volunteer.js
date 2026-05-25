// POST /api/volunteer — records a volunteer signup into D1.
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();

    const name = (d.name || '').toString().trim();
    const email = (d.email || '').toString().trim().toLowerCase();
    const phone = (d.phone || '').toString().trim();   // optional now

    if (!name || !email) {
      return json({ error: 'Name and email are required.' }, 400);
    }

    // "how" arrives as a string or an array of checkbox values.
    let help = d.how;
    if (Array.isArray(help)) help = help.join(', ');
    help = (help || '').toString().trim();

    await context.env.DB.prepare(
      `INSERT INTO volunteers (name, email, phone, help) VALUES (?, ?, ?, ?)`
    ).bind(name, email, phone, help).run();

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
