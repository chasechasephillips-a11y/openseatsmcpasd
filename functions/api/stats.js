// GET /api/stats — public counts that power the homepage counter
// and the live campaign dashboard. Cached 60s at the edge.
export async function onRequestGet(context) {
  try {
    const db = context.env.DB;

    const total = await db.prepare('SELECT COUNT(*) AS c FROM signatures').first();
    const meeting = await db.prepare(
      'SELECT COUNT(*) AS c FROM signatures WHERE will_attend_meeting = 1'
    ).first();
    const circulators = await db.prepare(
      'SELECT COUNT(*) AS c FROM signatures WHERE will_circulate = 1'
    ).first();
    const byArea = await db.prepare(
      "SELECT area, COUNT(*) AS c FROM signatures WHERE area != '' GROUP BY area"
    ).all();
    const last7 = await db.prepare(
      "SELECT COUNT(*) AS c FROM signatures WHERE created_at >= datetime('now','-7 days')"
    ).first();

    // PAPER_SIGNATURES is a wrangler.toml [vars] entry — paper signatures
    // Chase has physically received. The public counter shows paper +
    // online interest signups so it reflects real campaign momentum.
    const paper = parseInt(context.env.PAPER_SIGNATURES || '0', 10) || 0;
    const onlineSigs = total ? total.c : 0;

    return new Response(JSON.stringify({
      signatures: paper + onlineSigs,
      paperSignatures: paper,
      onlineSignups: onlineSigs,
      goal: 550,
      legalMinimum: 500,
      meetingCommits: meeting ? meeting.c : 0,
      circulators: circulators ? circulators.c : 0,
      last7Days: last7 ? last7.c : 0,
      byArea: (byArea && byArea.results) ? byArea.results : []
    }), {
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=60',
        'Access-Control-Allow-Origin': '*'
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({ signatures: 0, goal: 550 }), {
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
