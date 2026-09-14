PRAGMA foreign_keys = OFF;
BEGIN TRANSACTION;

CREATE TABLE upload_jobs_v2 (
 id TEXT PRIMARY KEY, idempotency_key TEXT NOT NULL UNIQUE,
 profile_alias TEXT NOT NULL REFERENCES channel_profiles(alias), channel_id TEXT NOT NULL,
 source_type TEXT NOT NULL CHECK(source_type IN ('direct_url','local_file','google_drive')), source_locator TEXT NOT NULL,
 source_fingerprint TEXT, title TEXT NOT NULL, description TEXT NOT NULL DEFAULT '',
 tags_json TEXT NOT NULL DEFAULT '[]', category_id TEXT NOT NULL DEFAULT '22',
 made_for_kids INTEGER NOT NULL DEFAULT 0 CHECK(made_for_kids IN (0,1)),
 playlist_id TEXT, thumbnail_locator TEXT,
 requested_privacy TEXT NOT NULL DEFAULT 'private' CHECK(requested_privacy IN ('private','unlisted','public')),
 publish_at TEXT, status TEXT NOT NULL CHECK(status IN ('queued','claimed','uploading','verifying','verified','failed','cancelled')),
 claimed_at TEXT, lease_expires_at TEXT, bytes_total INTEGER, bytes_uploaded INTEGER NOT NULL DEFAULT 0,
 youtube_video_id TEXT, error_summary TEXT, result_summary TEXT,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL, completed_at TEXT
);

INSERT INTO upload_jobs_v2 SELECT * FROM upload_jobs;
DROP TABLE upload_jobs;
ALTER TABLE upload_jobs_v2 RENAME TO upload_jobs;

CREATE INDEX idx_upload_jobs_claim ON upload_jobs(status,created_at);
CREATE INDEX idx_upload_jobs_profile ON upload_jobs(profile_alias,created_at);
CREATE INDEX idx_upload_jobs_fingerprint ON upload_jobs(profile_alias,source_fingerprint);

INSERT OR IGNORE INTO schema_migrations(version,applied_at) VALUES(2,datetime('now'));
COMMIT;
PRAGMA foreign_keys = ON;
