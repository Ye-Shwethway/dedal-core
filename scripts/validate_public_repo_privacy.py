#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".json", ".yaml", ".yml", ".toml", ".js", ".mjs", ".cjs", ".py", ".sql", ".txt", ".sh"}
SKIP_DIRS = {".git", "node_modules", "dist", "build", "coverage", ".venv", "venv"}

patterns = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "bearer token": re.compile(r"Bearer\s+[A-Za-z0-9._~+/=-]{24,}"),
    "google oauth token": re.compile(r"\bya29\.[A-Za-z0-9._-]{20,}"),
    "google api key": re.compile(r"\bAIza[0-9A-Za-z_-]{25,}"),
    "jwt-like value": re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"),
    "live yt3 asset": re.compile(r"https://yt3\.googleusercontent\.com/[A-Za-z0-9_?=&%./:-]+"),
    "cloudflare account/database id assignment": re.compile(r"(?im)^\s*(?:account_id|database_id)\s*=\s*[\"\'][0-9a-f-]{16,}[\"\']\s*$"),
}

# Public source may document regexes and obvious synthetic fixtures. Real YouTube channel IDs are
# disallowed unless they carry the explicit TEST marker used by contract fixtures.
channel_id = re.compile(r"\bUC[A-Za-z0-9_-]{20,30}\b")
playlist_id = re.compile(r"\bPL[A-Za-z0-9_-]{20,50}\b")
video_id = re.compile(r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{11}(?![A-Za-z0-9_-])")
long_base64 = re.compile(r"(?<![A-Za-z0-9+/=])[A-Za-z0-9+/]{400,}={0,2}(?![A-Za-z0-9+/=])")

findings = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS or any(part in SKIP_DIRS for part in path.parts):
        continue
    text = path.read_text(errors="ignore")
    rel = path.relative_to(ROOT)
    for label, rx in patterns.items():
        for m in rx.finditer(text):
            # Source-code examples that literally contain the scanner's regex should not self-trigger.
            line = text.count("\n", 0, m.start()) + 1
            if rel == Path("scripts/validate_public_repo_privacy.py"):
                continue
            findings.append((str(rel), line, label, m.group(0)[:100]))
    if rel != Path("scripts/validate_public_repo_privacy.py"):
        for m in channel_id.finditer(text):
            value = m.group(0)
            if "TEST" not in value and "EXAMPLE" not in value:
                findings.append((str(rel), text.count("\n", 0, m.start()) + 1, "live-looking YouTube channel id", value))
        for m in playlist_id.finditer(text):
            value = m.group(0)
            if "TEST" not in value and "EXAMPLE" not in value:
                findings.append((str(rel), text.count("\n", 0, m.start()) + 1, "live-looking YouTube playlist id", value))
        # Video IDs are only actionable when attached to an explicit video-id key/parameter in public source.
        for m in re.finditer(r"(?i)(?:video[_-]?id|videoId)\s*[:=]\s*[\"\']([A-Za-z0-9_-]{11})[\"\']", text):
            value = m.group(1)
            if "TEST" not in value and "EXAMPLE" not in value:
                findings.append((str(rel), text.count("\n", 0, m.start()) + 1, "live-looking YouTube video id", value))
        for m in long_base64.finditer(text):
            findings.append((str(rel), text.count("\n", 0, m.start()) + 1, "suspicious long base64 blob", m.group(0)[:80]))

if findings:
    lines = ["public repo privacy scan: FAIL"]
    lines += [f"{p}:{line}: {label}: {sample}" for p, line, label, sample in findings[:50]]
    raise SystemExit("\n".join(lines))

print("public repo privacy scan: PASS")
