// GET /api/stats — public counts that power the homepage counter, the
// per-Area gauge, and the live campaign dashboard. Cached 60s at the edge.
//
// Total signature count = LEGACY_PAPER (env var, lump-sum count of paper
// signatures Chase received before the admin tool existed) + tracked paper
// rows from D1 (excluding 'invalid') + online signups (D1 signatures table).
export async function onRequestGet(context) {
  try {
    const db = context.env.DB;

    // Online signups
    const total = await db.prepare('SELECT COUNT(*) AS c FROM signatures').first();
    const meeting = await db.prepare(
      'SELECT COUNT(*) AS c FROM signatures WHERE will_attend_meeting = 1'
    ).first();
    const circulators = await db.prepare(
      'SELECT COUNT(*) AS c FROM signatures WHERE will_circulate = 1'
    ).first();
    const onlineByArea = await db.prepare(
      "SELECT area, COUNT(*) AS c FROM signatures WHERE area != '' GROUP BY area"
    ).all();
    const last7 = await db.prepare(
      "SELECT COUNT(*) AS c FROM signatures WHERE created_at >= datetime('now','-7 days')"
    ).first();

    // Tracked paper signatures
    const paperRow = await db.prepare(
      "SELECT COUNT(*) AS c FROM paper_signatures WHERE validity != 'invalid'"
    ).first();
    const paperValid = await db.prepare(
      "SELECT COUNT(*) AS c FROM paper_signatures WHERE validity = 'valid'"
    ).first();
    const paperByArea = await db.prepare(
      "SELECT area, COUNT(*) AS c FROM paper_signatures " +
      "WHERE area != '' AND validity != 'invalid' GROUP BY area"
    ).all();

    // Lump-sum legacy paper count (env var)
    const paperLegacy = parseInt(context.env.PAPER_SIGNATURES || '0', 10) || 0;
    const paperTracked = paperRow ? paperRow.c : 0;
    const onlineSigs = total ? total.c : 0;

    // Merge paper + online byArea into a single map
    const areaMap = {};
    for (const r of (paperByArea.results || [])) {
      const a = r.area || 'Unspecified';
      if (!areaMap[a]) areaMap[a] = { area: a, paper: 0, online: 0, total: 0 };
      areaMap[a].paper += r.c;
      areaMap[a].total += r.c;
    }
    for (const r of (onlineByArea.results || [])) {
      const a = r.area || 'Unspecified';
      if (!areaMap[a]) areaMap[a] = { area: a, paper: 0, online: 0, total: 0 };
      areaMap[a].online += r.c;
      areaMap[a].total += r.c;
    }
    const byArea = Object.values(areaMap).sort((a, b) => b.total - a.total);

    return new Response(JSON.stringify({
      signatures: paperLegacy + paperTracked + onlineSigs,
      paperSignatures: paperLegacy + paperTracked,
      paperLegacy: paperLegacy,
      paperTracked: paperTracked,
      paperValid: paperValid ? paperValid.c : 0,
      onlineSignups: onlineSigs,
      goal: 550,
      legalMinimum: 500,
      meetingCommits: meeting ? meeting.c : 0,
      circulators: circulators ? circulators.c : 0,
      last7Days: last7 ? last7.c : 0,
      byArea: byArea
    }), {
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=60',
        'Access-Control-Allow-Origin': '*'
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({ signatures: 0, goal: 550, error: err.message }), {
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
