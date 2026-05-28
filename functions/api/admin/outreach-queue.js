// GET /api/admin/outreach-queue?token=...
// One-shot payload for the local outreach sender. Returns everything it
// needs to decide what to send: online signers (with days-since-signup,
// whether a paper signature with the same name exists, and which nurture
// stages already went out), committed attendees (+ phone + stages sent),
// the momentum recipient list, opt-outs, and live campaign stats.
export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const token = url.searchParams.get('token');
  if (!context.env.EXPORT_TOKEN || token !== context.env.EXPORT_TOKEN) {
    return json({ error: 'Unauthorized' }, 401);
  }

  const db = context.env.DB;
  try {
    // ─── Live stats (mirror /api/stats math) ───
    const onlineCount = (await db.prepare('SELECT COUNT(*) c FROM signatures').first()).c;
    const paperTracked = (await db.prepare(
      "SELECT COUNT(*) c FROM paper_signatures WHERE validity != 'invalid'"
    ).first()).c;
    const paperLegacy = parseInt(context.env.PAPER_SIGNATURES || '0', 10) || 0;
    const total = paperLegacy + paperTracked + onlineCount;
    const last7 = (await db.prepare(
      "SELECT COUNT(*) c FROM signatures WHERE created_at >= datetime('now','-7 days')"
    ).first()).c;

    // ─── Opt-outs ───
    const optRows = await db.prepare('SELECT email FROM outreach_optout').all();
    const optouts = (optRows.results || []).map(r => r.email);

    // ─── Sent log → map email|campaign|stage ───
    const logRows = await db.prepare(
      'SELECT email, campaign, stage FROM outreach_log'
    ).all();
    const sent = {};
    for (const r of (logRows.results || [])) sent[`${r.email}|${r.campaign}|${r.stage}`] = 1;

    // ─── Paper-signature name set (to detect "already mailed") ───
    const paperNames = await db.prepare(
      "SELECT DISTINCT lower(first_name) f, lower(last_name) l FROM paper_signatures WHERE validity != 'invalid'"
    ).all();
    const paperNameSet = new Set((paperNames.results || []).map(r => `${r.f}|${r.l}`));

    // ─── Online signers ───
    const sigRows = await db.prepare(
      `SELECT first_name, last_name, email, phone, area,
              will_attend_meeting, will_circulate, created_at,
              CAST((julianday('now') - julianday(created_at)) AS INTEGER) AS days_since
         FROM signatures
        ORDER BY created_at ASC`
    ).all();
    const signers = (sigRows.results || []).map(r => ({
      first_name: r.first_name,
      last_name: r.last_name,
      email: r.email,
      phone: r.phone || '',
      area: r.area || '',
      will_attend_meeting: r.will_attend_meeting,
      will_circulate: r.will_circulate,
      days_since: r.days_since,
      has_paper_match: paperNameSet.has(`${(r.first_name || '').toLowerCase()}|${(r.last_name || '').toLowerCase()}`),
      nurture_sent: {
        A: !!sent[`${r.email}|nurture|A`],
        B: !!sent[`${r.email}|nurture|B`],
        C: !!sent[`${r.email}|nurture|C`]
      }
    }));

    // ─── Committed attendees (will_attend_meeting=1) ───
    const attendees = signers
      .filter(s => s.will_attend_meeting)
      .map(s => ({
        first_name: s.first_name, email: s.email, phone: s.phone,
        meeting_sent: {
          t14: !!sent[`${s.email}|meeting|t14`],
          t3: !!sent[`${s.email}|meeting|t3`],
          dayof_email: !!sent[`${s.email}|meeting|dayof`],
          dayof_text: !!sent[`${s.email}|meeting|dayof|imessage`]
        }
      }));

    // ─── Momentum recipients: circulators + volunteers ───
    const volRows = await db.prepare(
      "SELECT name, email FROM volunteers WHERE help NOT LIKE 'EVENT_SUGGESTION:%'"
    ).all();
    const momentum = [];
    const seenEmail = new Set();
    for (const s of signers) {
      if (s.will_circulate && !seenEmail.has(s.email)) {
        momentum.push({ first_name: s.first_name, email: s.email });
        seenEmail.add(s.email);
      }
    }
    for (const v of (volRows.results || [])) {
      if (v.email && !seenEmail.has(v.email)) {
        momentum.push({ first_name: (v.name || '').split(' ')[0] || 'there', email: v.email });
        seenEmail.add(v.email);
      }
    }

    return json({
      ok: true,
      stats: {
        total, goal: 550, legal_minimum: 500, last7,
        online: onlineCount, paper: paperLegacy + paperTracked
      },
      optouts,
      signers,
      attendees,
      momentum
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
