# Deploy Open Seats MCPASD on Cloudflare Pages

The site is a static HTML file plus a small D1-backed API. Hosting, database, and forms all live in your Cloudflare account. No monthly cost at this scale.

**What's in this folder:**

| File / folder | What it is |
|---------------|-----------|
| `index.html` | The website |
| `functions/api/sign.js` | Records petition supporters into D1 |
| `functions/api/volunteer.js` | Records volunteer signups into D1 |
| `functions/api/stats.js` | Public counts for the homepage counter + dashboard |
| `functions/api/export.js` | Token-gated CSV export of all signups |
| `schema.sql` | D1 database tables |
| `wrangler.toml` | Cloudflare config (binding names, etc.) |

---

## One-time setup (~15 min)

### 1. Put this folder in a GitHub repo
Create a repo (e.g. `openseatsmcpasd`) and push the contents of `04_Website_v2/` to it.

### 2. Create the D1 database
From the repo folder, with Wrangler installed (`npm i -g wrangler`, then `wrangler login`):

```
wrangler d1 create openseats
```

It prints a `database_id`. Paste that value into `wrangler.toml` where it says `PASTE_YOUR_D1_DATABASE_ID_HERE`, then commit.

### 3. Create the tables
```
wrangler d1 execute openseats --file=./schema.sql --remote
```

### 4. Create the Pages project
In the Cloudflare dashboard: **Workers & Pages → Create → Pages → Connect to Git** → pick your repo.
- Build command: leave blank (it's static)
- Build output directory: `/`
- Deploy

### 5. Bind the database to Pages
Pages project → **Settings → Functions → D1 database bindings → Add binding**:
- Variable name: `DB`
- D1 database: `openseats`

Then **Settings → Environment variables → Add**:
- `EXPORT_TOKEN` = a long random string (this gates the CSV export)

Redeploy once so the bindings take effect (Deployments → Retry deployment).

### 6. Custom domain
Pages project → **Custom domains → Set up a domain** → `openseatsmcpasd.org`.
Since your DNS is already in Cloudflare, it wires up automatically and issues HTTPS. If the domain isn't registered yet, Cloudflare Registrar sells `.org` at cost (~$10/yr).

---

## How the pieces work

- **Sign-up form** → `POST /api/sign` → row in the `signatures` table. Duplicate emails update the existing row instead of inflating the count.
- **Volunteer form** → `POST /api/volunteer` → row in `volunteers`.
- **Homepage counter** → `GET /api/stats` → live supporter count, meeting commitments, per-Area breakdown. Cached 60s.
- **CSV export** → `GET /api/export?token=YOUR_TOKEN&type=signatures` (or `type=volunteers`) → downloads everything. Keep the token private.

---

## Automation this unlocks

Because the data is in D1 and `/api/stats` + `/api/export` are real endpoints, you can layer automation on top:

- **Live campaign dashboard** — see `10_Campaign_Dashboard_Live.html` in the project folder. Open it any time; it fetches `/api/stats` and shows current numbers, per-Area progress, and meeting commitments.
- **Weekly check-in** — a scheduled task can pull `/api/stats` every Monday and summarize the week (set up separately in Cowork).
- **Bulk follow-up** — export the CSV before each event to text/email everyone who hasn't gotten a paper sheet yet.

---

## Update the placeholders before launch

Search `index.html` for these and replace:

| Placeholder | Replace with |
|-------------|--------------|
| `[Host address 1]` / `[Host address 2]` | Drop-off addresses for signed sheets |
| `[PO Box or host address]` | Mailing address for signed sheets |
| `petition@openseatsmcpasd.org` | Your real petition email |

---

## QA checklist before going live

- [ ] Submit the sign-up form yourself — confirm the row lands in D1 (`wrangler d1 execute openseats --command "SELECT * FROM signatures" --remote`)
- [ ] Confirm the homepage counter ticks up after you submit
- [ ] Test the volunteer form the same way
- [ ] Hit `/api/export?token=...&type=signatures` and confirm the CSV downloads
- [ ] Open the site on your phone
- [ ] Confirm the countdown shows days to Sept 22
- [ ] Check all share buttons

The counter shows online supporters, not verified paper signatures — those are two different things. The legal threshold is 500 paper signatures with circulator certifications; the online number is your momentum/turnout proxy.
