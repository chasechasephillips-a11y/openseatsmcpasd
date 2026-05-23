-- Open Seats MCPASD — Cloudflare D1 schema
-- Run once after creating the D1 database:
--   wrangler d1 execute openseats --file=./schema.sql --remote

CREATE TABLE IF NOT EXISTS signatures (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name          TEXT NOT NULL,
  last_name           TEXT NOT NULL,
  email               TEXT NOT NULL,
  phone               TEXT,
  area                TEXT,
  address             TEXT NOT NULL,
  will_attend_meeting INTEGER DEFAULT 0,
  will_circulate      INTEGER DEFAULT 0,
  source              TEXT DEFAULT 'website',
  created_at          TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS volunteers (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT NOT NULL,
  email       TEXT NOT NULL,
  phone       TEXT,
  help        TEXT,
  created_at  TEXT DEFAULT (datetime('now'))
);

-- Prevents the same email from inflating the supporter count.
CREATE UNIQUE INDEX IF NOT EXISTS idx_signatures_email ON signatures(email);
CREATE INDEX IF NOT EXISTS idx_signatures_created ON signatures(created_at);
CREATE INDEX IF NOT EXISTS idx_signatures_area ON signatures(area);
