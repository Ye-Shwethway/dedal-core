PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS channel_profiles (
 alias TEXT PRIMARY KEY, channel_id TEXT NOT NULL UNIQUE, display_name TEXT,
 default_privacy TEXT NOT NULL DEFAULT 'private' CHECK(default_privacy IN ('private','unlisted','public')),
 enabled INTEGER NOT NULL DEFAULT 0 CHECK(enabled IN (0,1)), credential_ref TEXT,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS oauth_credentials (
 credential_ref TEXT PRIMARY KEY, profile_alias TEXT NOT NULL UNIQUE REFERENCES channel_profiles(alias) ON DELETE CASCADE,
 channel_id TEXT NOT NULL, ciphertext TEXT NOT NULL, iv TEXT NOT NULL, scopes TEXT NOT NULL,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS oauth_states (
 state_hash TEXT PRIMARY KEY, profile_alias TEXT NOT NULL REFERENCES channel_profiles(alias) ON DELETE CASCADE,
 browser_hash TEXT NOT NULL, pkce_ciphertext TEXT NOT NULL, pkce_iv TEXT NOT NULL,
 expires_at TEXT NOT NULL, consumed_at TEXT, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS connect_tickets (
 ticket_hash TEXT PRIMARY KEY, profile_alias TEXT NOT NULL REFERENCES channel_profiles(alias) ON DELETE CASCADE,
 expires_at TEXT NOT NULL, consumed_at TEXT, created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS upload_jobs (
 id TEXT PRIMARY KEY, idempotency_key TEXT NOT NULL UNIQUE,
 profile_alias TEXT NOT NULL REFERENCES channel_profiles(alias), channel_id TEXT NOT NULL,
 source_type TEXT NOT NULL CHECK(source_type IN ('direct_url','local_file')), source_locator TEXT NOT NULL,
 source_fingerprint TEXT, title TEXT NOT NULL, description TEXT NOT NULL DEFAULT '',
 tags_json TEXT NOT NULL DEFAULT '[]', category_id TEXT NOT NULL DEFAULT '22',
 made_for_kids INTEGER NOT NULL DEFAULT 0 CHECK(made_for_kids IN (0,1)),
 playlist_id TEXT, thumbnail_locator TEXT,
 requested_privacy TEXT NOT NULL DEFAULT 'private' CHECK(requested_privacy IN ('private','unlisted','public')),
 publish_at TEXT, status TEXT NOT NULL CHECK(status IN ('queued','claimed','uploading','verifying','verified','failed','cancelled')),
 claimed_at TEXT, lease_expires_at TEXT, bytes_total INTEGER, bytes_uploaded INTEGER NOT NULL DEFAULT 0,
 youtube_video_id TEXT, error_summary TEXT, result_summary TEXT,
 created_at TEXT NOT NULL, updated_at TEXT NOT NULL, completed_at TEXT);
CREATE INDEX IF NOT EXISTS idx_upload_jobs_claim ON upload_jobs(status,created_at);
CREATE INDEX IF NOT EXISTS idx_upload_jobs_profile ON upload_jobs(profile_alias,created_at);
CREATE INDEX IF NOT EXISTS idx_upload_jobs_fingerprint ON upload_jobs(profile_alias,source_fingerprint);
CREATE TABLE IF NOT EXISTS upload_sessions (
 job_id TEXT PRIMARY KEY REFERENCES upload_jobs(id) ON DELETE CASCADE,
 session_ciphertext TEXT NOT NULL, session_iv TEXT NOT NULL,
 content_type TEXT NOT NULL, content_length INTEGER NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS mutation_audit (
 id TEXT PRIMARY KEY, actor_type TEXT NOT NULL, action TEXT NOT NULL, profile_alias TEXT,
 channel_id TEXT, job_id TEXT, outcome TEXT NOT NULL, details_json TEXT NOT NULL DEFAULT '{}', created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS schema_migrations (version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL);
INSERT OR IGNORE INTO schema_migrations(version,applied_at) VALUES(1,datetime('now'));
