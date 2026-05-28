-- Engagement events: scroll depth, section reach, CTA clicks.
-- Complements `pageviews` — answers "how far did they read / did they try
-- to convert" which raw pageviews on a single-page site can't show.
-- ip_hash uses the same salted scheme as pageviews (dedupe, not identify).
CREATE TABLE IF NOT EXISTS events (
  id       INTEGER PRIMARY KEY AUTOINCREMENT,
  ts       TEXT DEFAULT CURRENT_TIMESTAMP,
  path     TEXT,
  kind     TEXT,    -- 'scroll' | 'section' | 'cta'
  label    TEXT,    -- scroll: '25'|'50'|'75'|'100'; section: id; cta: name
  ip_hash  TEXT
);
CREATE INDEX IF NOT EXISTS idx_events_ts ON events(ts);
CREATE INDEX IF NOT EXISTS idx_events_kind ON events(kind, label);
CREATE INDEX IF NOT EXISTS idx_events_ip_day ON events(ip_hash, ts);
