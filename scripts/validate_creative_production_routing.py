#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
contract = json.loads((root / 'evals/creative-production-routing/contract-v1.json').read_text())
video = (root / 'skills/video-production/SKILL.md').read_text()
pres = (root / 'skills/presentation-engineering/SKILL.md').read_text()
routing = json.loads((root / 'state/routing-boundaries.json').read_text())

assert len(contract['cases']) >= 10
assert 'Video Production' in video
assert 'Presentation Engineering' in pres
assert 'render success is not playback' in video.lower()
assert 'rendered visual qa is mandatory' in pres.lower()
assert 'video-production' in json.dumps(routing)
assert 'presentation-engineering' in json.dumps(routing)
assert 'ffmpeg' in video.lower()
assert 'native slide' in pres.lower() or 'slide/pptx execution tool' in pres.lower()

print(f"creative production routing: valid ({len(contract['cases'])} cases)")
