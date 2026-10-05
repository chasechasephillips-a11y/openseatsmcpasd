-- MCPASD Yes Committee volunteer sign-ups (the /yes/ site).
-- Kept in its own table so Yes Committee data never mixes with Open Seats data.
-- wrangler d1 execute openseats --file=./schema-yes.sql --remote
CREATE TABLE IF NOT EXISTS yes_volunteers (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT NOT NULL,
  email       TEXT NOT NULL,
  phone       TEXT,
  area        TEXT,
  help        TEXT,
  note        TEXT,
  created_at  TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_yes_volunteers_created ON yes_volunteers(created_at);
