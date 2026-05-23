// GET /api/export?token=YOUR_TOKEN&type=signatures|volunteers
// Token-gated CSV export so Chase (or an automated task) can pull
// the full list any time. Set EXPORT_TOKEN in the Cloudflare dashboard.
export async function onRequestGet(context) {
  const url = new URL(context.request.url);
  const token = url.searchParams.get('token');
  const type = url.searchParams.get('type') || 'signatures';

  if (!context.env.EXPORT_TOKEN || token !== context.env.EXPORT_TOKEN) {
    return new Response('Unauthorized', { status: 401 });
  }

  try {
    let rows, headers;
    if (type === 'volunteers') {
      const res = await context.env.DB.prepare(
        'SELECT id, name, email, phone, help, created_at FROM volunteers ORDER BY created_at DESC'
      ).all();
      rows = res.results || [];
      headers = ['id', 'name', 'email', 'phone', 'help', 'created_at'];
    } else {
      const res = await context.env.DB.prepare(
        `SELECT id, first_name, last_name, email, phone, area, address,
                will_attend_meeting, will_circulate, created_at
         FROM signatures ORDER BY created_at DESC`
      ).all();
      rows = res.results || [];
      headers = ['id', 'first_name', 'last_name', 'email', 'phone', 'area',
                 'address', 'will_attend_meeting', 'will_circulate', 'created_at'];
    }

    const esc = (v) => {
      const s = (v === null || v === undefined) ? '' : String(v);
      return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
    };
    const csv = [headers.join(',')]
      .concat(rows.map((r) => headers.map((h) => esc(r[h])).join(',')))
      .join('\n');

    return new Response(csv, {
      headers: {
        'Content-Type': 'text/csv',
        'Content-Disposition': `attachment; filename="${type}.csv"`
      }
    });
  } catch (err) {
    return new Response('Server error', { status: 500 });
  }
}
