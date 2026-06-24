// GET /api/live — public live momentum numbers (phone-updatable via /api/admin/setlive).
// Replaces the static /data.json as the source for the homepage counters, so Chase can
// bump the count/circulators from his phone without editing a file or redeploying.
export async function onRequestGet(context) {
  try {
    const row = await context.env.DB.prepare(
      `SELECT sig_count AS sigCount, circulators, goal FROM live_stats WHERE id = 1`
    ).first();
    const body = row || { sigCount: 0, circulators: 0, goal: 550 };
    return new Response(JSON.stringify(body), {
      headers: {
        'Content-Type': 'application/json',
        'Cache-Control': 'public, max-age=30',
        'Access-Control-Allow-Origin': '*'
      }
    });
  } catch (e) {
    return new Response(JSON.stringify({ sigCount: 0, circulators: 0, goal: 550 }), {
      status: 200,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
    });
  }
}
