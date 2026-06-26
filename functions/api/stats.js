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
    const onlineLast30 = await db.prepare(
      "SELECT COUNT(*) AS c FROM signatures WHERE created_at >= datetime('now','-30 days')"
    ).first();
    const onlineLast = await db.prepare(
      'SELECT MAX(created_at) AS d FROM signatures'
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

    // Momentum on tracked paper sheets. Use date_received (the real collection
    // date) when present, else fall back to created_at. Excludes 'invalid'.
    const paperDateExpr =
      "COALESCE(NULLIF(date_received,''), date(created_at))";
    const paperLast7 = await db.prepare(
      "SELECT COUNT(*) AS c FROM paper_signatures " +
      "WHERE validity != 'invalid' AND " + paperDateExpr + " >= date('now','-7 days')"
    ).first();
    const paperLast30 = await db.prepare(
      "SELECT COUNT(*) AS c FROM paper_signatures " +
      "WHERE validity != 'invalid' AND " + paperDateExpr + " >= date('now','-30 days')"
    ).first();
    const paperLast = await db.prepare(
      "SELECT MAX(" + paperDateExpr + ") AS d FROM paper_signatures WHERE validity != 'invalid'"
    ).first();

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

    // ── Momentum / velocity (tracked signups + tracked paper; legacy lump-sum
    //    has no dates so it can't contribute to a rate). Drives the digest's
    //    projection, the stall detector, and the pace alert. ──
    const oL7 = last7 ? last7.c : 0;
    const oL30 = onlineLast30 ? onlineLast30.c : 0;
    const pL7 = paperLast7 ? paperLast7.c : 0;
    const pL30 = paperLast30 ? paperLast30.c : 0;
    const addedLast7 = oL7 + pL7;
    const addedLast30 = oL30 + pL30;
    const dailyRate30 = Math.round((addedLast30 / 30) * 100) / 100;

    // Most recent tracked signature (online or paper), and days since.
    const lastDates = [];
    if (onlineLast && onlineLast.d) lastDates.push(String(onlineLast.d).slice(0, 10));
    if (paperLast && paperLast.d) lastDates.push(String(paperLast.d).slice(0, 10));
    const lastSigDate = lastDates.sort().pop() || null;
    let daysSinceLastSig = null;
    if (lastSigDate) {
      const ms = Date.now() - Date.parse(lastSigDate + 'T00:00:00Z');
      daysSinceLastSig = Math.max(0, Math.floor(ms / 86400000));
    }

    // Project where the count lands at the current 30-day rate. Sign-by is
    // Aug 20, 2026 (last day to collect). Cap the contribution at >=0.
    const SIGN_BY_MS = Date.parse('2026-08-20T00:00:00Z');
    const daysToSignBy = Math.max(0, Math.ceil((SIGN_BY_MS - Date.now()) / 86400000));
    const currentTotal = paperLegacy + paperTracked + onlineSigs;
    const projectedFinal = Math.round(currentTotal + dailyRate30 * daysToSignBy);

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
      byArea: byArea,
      momentum: {
        addedLast7: addedLast7,
        addedLast30: addedLast30,
        onlineLast7: oL7,
        onlineLast30: oL30,
        paperLast7: pL7,
        paperLast30: pL30,
        dailyRate30: dailyRate30,
        daysSinceLastSig: daysSinceLastSig,
        lastSigDate: lastSigDate,
        daysToSignBy: daysToSignBy,
        projectedFinal: projectedFinal
      }
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
