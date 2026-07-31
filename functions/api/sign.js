// POST /api/sign — records an online petition supporter into D1.
export async function onRequestPost(context) {
  try {
    const d = await context.request.json();

    const firstName = (d.firstName || '').toString().trim();
    const lastName = (d.lastName || '').toString().trim();
    const email = (d.email || '').toString().trim().toLowerCase();
    const address = (d.address || '').toString().trim();

    if (!firstName || !lastName || !email || !address) {
      return json({ error: 'Missing required fields.' }, 400);
    }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      return json({ error: 'Invalid email.' }, 400);
    }

    const phone = (d.phone || '').toString().trim();
    const area = (d.area || '').toString().trim();
    const meeting = d.meeting ? 1 : 0;
    const circulate = d.circulator ? 1 : 0;
    // "Needs a sheet delivered" and "come pick up my signed sheet" both put this
    // person in the pickup queue — either way I'm driving to their address.
    // (Form sends delivery=pickup|mail and status=need-sheet|have-sheet; older
    //  clients may still send a boolean `pickup`.)
    const pickup = (d.pickup || d.delivery === 'pickup' || d.status === 'need-sheet') ? 1 : 0;
    const heard = (d.heard || '').toString().trim().slice(0, 60) || 'website';

    await context.env.DB.prepare(
      `INSERT INTO signatures
         (first_name, last_name, email, phone, area, address, will_attend_meeting, will_circulate, prefers_pickup, source)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
       ON CONFLICT(email) DO UPDATE SET
         first_name = excluded.first_name,
         last_name = excluded.last_name,
         phone = excluded.phone,
         area = excluded.area,
         address = excluded.address,
         will_attend_meeting = excluded.will_attend_meeting,
         will_circulate = excluded.will_circulate,
         prefers_pickup = excluded.prefers_pickup,
         source = excluded.source`
    ).bind(firstName, lastName, email, phone, area, address, meeting, circulate, pickup, heard).run();

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
