-- Notification ledger.
-- `notified=1` means an alert email has been sent to Chase about this row.
-- A local launchd poller (~/scripts/openseats-notify.py) flips these.
ALTER TABLE signatures ADD COLUMN notified INTEGER DEFAULT 0;
ALTER TABLE volunteers ADD COLUMN notified INTEGER DEFAULT 0;
