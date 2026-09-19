#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
contract = json.loads((root / 'evals/creative-production-routing/contract-v1.json').read_text())
video = (root / 'skills/video-production/SKILL.md').read_text()
editing_modes = (root / 'skills/video-production/references/editing-modes.md').read_text()
pres = (root / 'skills/presentation-engineering/SKILL.md').read_text()
routing = json.loads((root / 'state/routing-boundaries.json').read_text())

assert len(contract['cases']) >= 14
assert 'Video Production' in video
assert 'Presentation Engineering' in pres
assert 'render success is not playback' in video.lower()
assert 'rendered visual qa is mandatory' in pres.lower()
assert 'video-production' in json.dumps(routing)
assert 'presentation-engineering' in json.dumps(routing)
assert 'ffmpeg' in video.lower()
assert 'simple / narrative edit' in video.lower()
assert 'fan / visual-montage edit' in video.lower()
assert 'structure acceptance' in video.lower()
assert 'full-frame white flashes' in video.lower()
assert 'fan-edit build sequence' in editing_modes.lower()
assert 'end intentionally' in editing_modes.lower()
assert 'crop through motion' in editing_modes.lower()
assert 'native slide' in pres.lower() or 'slide/pptx execution tool' in pres.lower()

print(f"creative production routing: valid ({len(contract['cases'])} cases)")
