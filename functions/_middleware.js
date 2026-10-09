// Serves the Yes MCPASD site (the /yes/ folder) at its own domain.
//
// Inert until yesmcpasd.org is added as a custom domain on this Pages
// project: requests for any other host pass straight through, except that
// once YES_DOMAIN_LIVE = "1" is set, openseatsmcpasd.org/yes/... redirects
// to yesmcpasd.org so search engines consolidate on one address.
//
//   yesmcpasd.org/            -> /yes/
//   yesmcpasd.org/faq/        -> /yes/faq/
//   yesmcpasd.org/robots.txt  -> /yes/robots.txt (and sitemap.xml)
//   yesmcpasd.org/yes/faq/    -> 301 yesmcpasd.org/faq/
//   yesmcpasd.org/api/...     -> the shared API, untouched
const YES_HOST = 'yesmcpasd.org';

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const host = url.hostname;

  if (host === 'www.' + YES_HOST) {
    url.hostname = YES_HOST;
    return Response.redirect(url.toString(), 301);
  }

  if (host !== YES_HOST) {
    const live = context.env && context.env.YES_DOMAIN_LIVE === '1';
    if (live && (url.pathname === '/yes' || url.pathname.startsWith('/yes/'))) {
      const to = new URL(url.pathname.replace(/^\/yes/, '') || '/', 'https://' + YES_HOST);
      to.search = url.search;
      return Response.redirect(to.toString(), 301);
    }
    return context.next();
  }

  if (url.pathname.startsWith('/api/')) return context.next();

  if (url.pathname === '/yes' || url.pathname.startsWith('/yes/')) {
    url.pathname = url.pathname.replace(/^\/yes/, '') || '/';
    return Response.redirect(url.toString(), 301);
  }

  const inner = new URL(url);
  inner.pathname = '/yes' + url.pathname;
  const res = await context.env.ASSETS.fetch(new Request(inner.toString(), context.request));

  // Pages adds trailing slashes with a redirect to the /yes/ path; strip it.
  const loc = res.headers.get('Location');
  if (loc && res.status >= 300 && res.status < 400) {
    const target = new URL(loc, inner);
    target.hostname = YES_HOST;
    target.pathname = target.pathname.replace(/^\/yes/, '') || '/';
    return Response.redirect(target.toString(), res.status === 308 ? 301 : res.status);
  }
  return res;
}
