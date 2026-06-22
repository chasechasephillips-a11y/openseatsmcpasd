-- Canvassing / door-knock log for circulators (esp. kids walking routes).
-- One row per stop. client_id is a localStorage-generated UUID so the offline-
-- first app can retry syncs without creating duplicates.
CREATE TABLE IF NOT EXISTS canvass_log (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  circulator    TEXT NOT NULL,            -- name the circulator set on their device
  client_id     TEXT,                     -- UUID from the device, for idempotent sync
  address       TEXT,                     -- where they went (free text)
  lat           REAL,                     -- optional captured location
  lon           REAL,
  talked_to     TEXT,                     -- names of anyone they spoke with
  actions       TEXT,                     -- comma-joined quick actions (hanger, dropped, signed, ...)
  comments      TEXT,
  stop_time     TEXT,                     -- ISO timestamp from the device (when they were there)
  created_at    TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_canvass_created     ON canvass_log(created_at);
CREATE INDEX IF NOT EXISTS idx_canvass_circulator  ON canvass_log(circulator);
CREATE UNIQUE INDEX IF NOT EXISTS idx_canvass_client ON canvass_log(client_id);
