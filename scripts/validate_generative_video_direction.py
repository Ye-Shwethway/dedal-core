#!/usr/bin/env python3
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
skill=(root/'skills/generative-video-direction/SKILL.md').read_text()
notes=(root/'skills/generative-video-direction/ADAPTATION_NOTES.md').read_text()
post=(root/'skills/video-post-production/SKILL.md').read_text()
story=(root/'skills/story-weaver/SKILL.md').read_text()
visual=(root/'skills/visual-narrative-production/SKILL.md').read_text()
registry=(root/'index/SKILL_REGISTRY.yaml').read_text()
routing=json.loads((root/'state/routing-boundaries.json').read_text())
for p in [
 'references/motion-shot-design.md','references/temporal-continuity-ledger.md','references/reference-role-and-provider-capability.md',
 'references/prompt-compilation-and-provider-adaptation.md','references/generated-take-qa-and-repair.md','references/bridge-contracts.md','references/adaptive-keyframe-density-and-transition-bridges.md','references/file-mediated-agent-handoff.md',
 'schemas/motion-shot-spec.schema.json','schemas/temporal-continuity-ledger.schema.json','schemas/generation-contract.schema.json']:
    assert (root/'skills/generative-video-direction'/p).exists(), p
assert 'name: generative-video-direction' in skill
assert 'Motion Shot Spec' in skill and 'Generated clips are takes' in skill
assert 'unknown' in (root/'skills/generative-video-direction/references/reference-role-and-provider-capability.md').read_text()
assert 'video-post-production' in post and 'backward-compatible routing aliases' in post
assert 'generative-video-direction' in story and 'generative-video-direction' in visual
assert 'generative-video-direction:' in registry and 'video-post-production:' in registry
assert 'aliases: ["video-post-production", "video-production", "video-editing"]' in registry
blob=json.dumps(routing)
assert 'generative-video-direction' in blob and 'video-post-production' in blob
assert 'provider-neutral' in notes.lower() or 'dedal-native' in notes.lower()
contract=(root/'evals/generative-video-direction/contract-v1.md').read_text()
for n in ['GVD-01','GVD-04','GVD-06','GVD-09','GVD-12','GVD-13','GVD-14','GVD-15','GVD-16','GVD-17']:
    assert n in contract
assert (root/'skills/generative-video-direction/providers/luma.md').exists()
assert 'adaptive' in (root/'skills/generative-video-direction/references/adaptive-keyframe-density-and-transition-bridges.md').read_text().lower()
print('generative video direction: valid')

assert 'manifest version' in (root/'skills/generative-video-direction/references/file-mediated-agent-handoff.md').read_text().lower()

assert 'production_started' in (root/'docs/architecture/FILE_MEDIATED_CREATIVE_AGENT_BRIDGE.md').read_text()
assert 'scope=set' in (root/'skills/generative-video-direction/SKILL.md').read_text()
