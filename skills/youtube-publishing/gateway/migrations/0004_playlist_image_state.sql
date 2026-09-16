CREATE TABLE IF NOT EXISTS playlist_image_state (
  playlist_id TEXT PRIMARY KEY,
  profile_alias TEXT NOT NULL,
  image_id TEXT,
  source_url TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_playlist_image_state_profile_alias
  ON playlist_image_state(profile_alias);
