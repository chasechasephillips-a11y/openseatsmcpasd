# Renew MCPASD: site + deploy

A one-page static site for the Nov. 3, 2026 MCPASD operating referendum. It has no build step, no database and no forms, and the page works with JavaScript off (JS only powers the tax calculator and the copy-link button).

```
renew/
  ACTION_PLAN.md   ← the campaign plan (NOT deployed)
  README.md        ← this file (NOT deployed)
  site/            ← the only folder that gets deployed
    index.html  og-image.png  favicon.svg  robots.txt  sitemap.xml  _headers  _redirects
```

**Status: DRAFT, not published.** `index.html` carries a `noindex` tag, and the Open Seats `_redirects` sends `/renew/*` home, so nothing here leaks onto openseatsmcpasd.org.

## Preview locally

Open `site/index.html` in a browser, or run:

```
npx wrangler pages dev renew/site
```

## Deploy as its own Cloudflare Pages project

Keep it separate from Open Seats: a different project and a different domain.

```
wrangler pages project create renewmcpasd --production-branch=main
wrangler pages deploy renew/site --project-name=renewmcpasd --branch=main
```

Then go to **Pages → renewmcpasd → Custom domains** and add the domain.

## Launch checklist

- [ ] **Delete the `noindex` line** near the top of `site/index.html`. It's marked `DRAFT`. If you skip this, Google will never show the page.
- [ ] Find and replace the placeholders if you change them:
  - `renewmcpasd.org` → your domain (in `index.html`, `robots.txt`, `sitemap.xml`)
  - `Renew MCPASD` → the committee's exact registered name (the "Paid for by" line in the footer)
  - `hello@renewmcpasd.org` → your real inbox
- [ ] Work through **§8 "Verify before you print"** in `ACTION_PLAN.md`
- [ ] Pages → **Web Analytics** → enable (free, cookieless)
- [ ] Google Search Console: add the domain, submit `/sitemap.xml`, and use **Request indexing** on `/`
- [ ] Bing Webmaster Tools: import from Search Console
- [ ] Paste the URL into the Facebook Sharing Debugger to confirm the preview image shows
- [ ] On your phone, test the Text / Facebook / Email share buttons and the calculator

## Short links (in `site/_redirects`)

| Link | Goes to | Use on |
|------|---------|--------|
| `/yard` | home, tagged `yardsign` | yard signs |
| `/door` | home, tagged `doorhanger` | door hangers |
| `/card` | home, tagged `card` | palm cards |
| `/ad` | home, tagged `google-ad` | Google ads final URL |
| `/fb` · `/nd` | home, tagged | Facebook · Nextdoor posts |
| `/myths` · `/cost` · `/vote` · `/sign` | that section | replies in comment threads |

## Updating a number

Every figure appears in plain HTML in `site/index.html`. Search for it, change it, and redeploy. If the $64 estimate changes, search for `64`, `$0.64` and `$288` and update each hit, including `PER_100K_YEAR4` in the calculator script at the bottom.
