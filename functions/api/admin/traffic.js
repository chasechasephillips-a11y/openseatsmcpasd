// GET /api/admin/traffic?token=...&days=14
// Aggregated traffic stats for the /admin dashboard. Token-gated.
export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const token = url.searchParams.get('token');
  if (!context.env.EXPORT_TOKEN || token !== context.env.EXPORT_TOKEN) {
    return json({ error: 'Unauthorized' }, 401);
  }

  const days = Math.min(60, Math.max(1, parseInt(url.searchParams.get('days') || '14', 10)));
  const db = context.env.DB;

  try {
    const totals = await db.prepare(
      `SELECT
         COUNT(*)                                                            AS all_time,
         SUM(CASE WHEN date(ts) = date('now')                THEN 1 ELSE 0 END) AS today,
         SUM(CASE WHEN ts >= datetime('now','-7 days')       THEN 1 ELSE 0 END) AS last7,
         SUM(CASE WHEN ts >= datetime('now','-30 days')      THEN 1 ELSE 0 END) AS last30
       FROM pageviews`
    ).first();

    const uniques = await db.prepare(
      `SELECT
         COUNT(DISTINCT ip_hash)                                                                       AS uniq_all,
         COUNT(DISTINCT CASE WHEN date(ts) = date('now')          THEN ip_hash END)                    AS uniq_today,
         COUNT(DISTINCT CASE WHEN ts >= datetime('now','-7 days') THEN ip_hash END)                    AS uniq_last7
       FROM pageviews`
    ).first();

    const byPath = await db.prepare(
      `SELECT path, COUNT(*) AS views, COUNT(DISTINCT ip_hash) AS uniques
         FROM pageviews
        WHERE ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY path
        ORDER BY views DESC
        LIMIT 20`
    ).bind(days).all();

    const byDay = await db.prepare(
      `SELECT date(ts) AS day,
              COUNT(*) AS views,
              COUNT(DISTINCT ip_hash) AS uniques
         FROM pageviews
        WHERE ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY day
        ORDER BY day ASC`
    ).bind(days).all();

    const byReferrer = await db.prepare(
      `SELECT referrer, COUNT(*) AS c
         FROM pageviews
        WHERE referrer IS NOT NULL
          AND referrer != ''
          AND referrer NOT LIKE '%openseatsmcpasd.%'
          AND ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY referrer
        ORDER BY c DESC
        LIMIT 15`
    ).bind(days).all();

    const byCountry = await db.prepare(
      `SELECT country, COUNT(*) AS c
         FROM pageviews
        WHERE country IS NOT NULL AND country != ''
          AND ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY country
        ORDER BY c DESC
        LIMIT 10`
    ).bind(days).all();

    // Attribution by source/circulator (?ref=).
    const byRef = await db.prepare(
      `SELECT ref, COUNT(*) AS views, COUNT(DISTINCT ip_hash) AS uniques
         FROM pageviews
        WHERE ref IS NOT NULL AND ref != ''
          AND ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY ref
        ORDER BY views DESC
        LIMIT 25`
    ).bind(days).all();

    // City-level geo (cookieless, from Cloudflare edge).
    const byCity = await db.prepare(
      `SELECT city, COUNT(*) AS views, COUNT(DISTINCT ip_hash) AS uniques
         FROM pageviews
        WHERE city IS NOT NULL AND city != ''
          AND ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY city
        ORDER BY views DESC
        LIMIT 15`
    ).bind(days).all();

    // Today, hour-by-hour (UTC). Pads missing hours to 0 in the UI.
    const byHour = await db.prepare(
      `SELECT strftime('%H', ts) AS hour, COUNT(*) AS views, COUNT(DISTINCT ip_hash) AS uniques
         FROM pageviews
        WHERE ts >= datetime('now','start of day')
        GROUP BY hour
        ORDER BY hour`
    ).all();

    // Most recent 25 visits — for the live feed
    const recent = await db.prepare(
      `SELECT ts, path, country, referrer
         FROM pageviews
        ORDER BY ts DESC
        LIMIT 25`
    ).all();

    // ─── Engagement (homepage funnel) ───
    // Denominator: unique homepage visitors in the window.
    const homeVisitors = await db.prepare(
      `SELECT COUNT(DISTINCT ip_hash) AS c
         FROM pageviews
        WHERE path = '/' AND ts >= datetime('now','-' || ?1 || ' days')`
    ).bind(days).first();

    // Scroll depth: unique visitors reaching each milestone.
    const scroll = await db.prepare(
      `SELECT label, COUNT(DISTINCT ip_hash) AS uniques
         FROM events
        WHERE kind = 'scroll' AND ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY label`
    ).bind(days).all();

    // Section reach: unique visitors who saw each conversion-critical section.
    const sections = await db.prepare(
      `SELECT label, COUNT(DISTINCT ip_hash) AS uniques
         FROM events
        WHERE kind = 'section' AND ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY label
        ORDER BY uniques DESC`
    ).bind(days).all();

    // CTA clicks: total + unique per action.
    const ctas = await db.prepare(
      `SELECT label, COUNT(*) AS clicks, COUNT(DISTINCT ip_hash) AS uniques
         FROM events
        WHERE kind = 'cta' AND ts >= datetime('now','-' || ?1 || ' days')
        GROUP BY label
        ORDER BY clicks DESC`
    ).bind(days).all();

    return json({
      ok: true,
      window_days: days,
      totals: totals || { all_time: 0, today: 0, last7: 0, last30: 0 },
      uniques: uniques || { uniq_all: 0, uniq_today: 0, uniq_last7: 0 },
      by_path: byPath.results || [],
      by_day: byDay.results || [],
      by_referrer: byReferrer.results || [],
      by_country: byCountry.results || [],
      by_ref: byRef.results || [],
      by_city: byCity.results || [],
      by_hour: byHour.results || [],
      recent: recent.results || [],
      engagement: {
        home_visitors: homeVisitors ? homeVisitors.c : 0,
        scroll: scroll.results || [],
        sections: sections.results || [],
        ctas: ctas.results || []
      }
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
