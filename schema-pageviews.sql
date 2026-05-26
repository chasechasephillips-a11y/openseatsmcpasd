-- Cookieless pageview tracker.
-- One row per page load. UA + IP are hashed with EXPORT_TOKEN as salt
-- (never stored in plaintext) so we can count unique visitors per day
-- without setting cookies or storing identifiers.
CREATE TABLE IF NOT EXISTS pageviews (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  ts        TEXT DEFAULT CURRENT_TIMESTAMP,
  path      TEXT NOT NULL,
  referrer  TEXT,
  ua_hash   TEXT,
  ip_hash   TEXT,
  country   TEXT
);
CREATE INDEX IF NOT EXISTS idx_pageviews_ts ON pageviews(ts);
CREATE INDEX IF NOT EXISTS idx_pageviews_path ON pageviews(path);
CREATE INDEX IF NOT EXISTS idx_pageviews_ip_day ON pageviews(ip_hash, ts);
