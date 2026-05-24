-- Paper-signature ledger.
-- Each row = one signature line on a physical petition sheet that Chase has
-- received (mail / drop-off / event). Powers the per-Area public gauge AND
-- the legal audit trail when sheets are filed.
CREATE TABLE IF NOT EXISTS paper_signatures (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name      TEXT NOT NULL,
  last_name       TEXT NOT NULL,
  street_address  TEXT,
  city            TEXT,
  area            TEXT,                       -- 'I'|'II'|'III'|'IV'|'V' or ''
  source          TEXT,                       -- 'mail' | 'dropoff' | 'event' | 'other'
  circulator_name TEXT,                       -- who collected this sig
  date_received   TEXT,                       -- ISO date string, e.g. '2026-05-24'
  validity        TEXT DEFAULT 'unverified',  -- 'valid' | 'invalid' | 'unverified'
  notes           TEXT,
  created_at      TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_paper_sigs_validity ON paper_signatures (validity);
CREATE INDEX IF NOT EXISTS idx_paper_sigs_area     ON paper_signatures (area);
CREATE INDEX IF NOT EXISTS idx_paper_sigs_created  ON paper_signatures (created_at);
