-- Outreach automation: send-log + opt-out.
-- The local sender (~/scripts/openseats-outreach.py) reads /api/admin/outreach-queue,
-- sends stage-appropriate messages, then logs each via /api/admin/outreach-log so
-- it never double-sends. Opt-outs come from the public /api/unsubscribe link.

CREATE TABLE IF NOT EXISTS outreach_log (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  email     TEXT NOT NULL,
  campaign  TEXT NOT NULL,   -- 'momentum' | 'nurture' | 'meeting'
  stage     TEXT NOT NULL,   -- nurture: 'A'|'B'|'C'; meeting: 't14'|'t3'|'dayof'; momentum: 'YYYY-WW'
  channel   TEXT DEFAULT 'email',  -- 'email' | 'imessage'
  sent_at   TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_outreach_once
  ON outreach_log(email, campaign, stage, channel);

CREATE TABLE IF NOT EXISTS outreach_optout (
  email        TEXT PRIMARY KEY,
  opted_out_at TEXT DEFAULT CURRENT_TIMESTAMP
);
