# Adaptation Notes

`decision-design` is a DEDAL-native adaptation influenced by Matt Pocock's public `grilling` / `grill-me` skill pattern.

Source repository: `mattpocock/skills`
Inspected source commit/tree: `3cca18b368ae95cdbdebbff572ccafa662551015`
Source license: MIT (Copyright 2026 Matt Pocock)
Adapted: 2026-09-14

Retained ideas: dependency-aware decision tree/frontier, separating retrievable facts from owner decisions, iterative rounds, and a shared-understanding gate for deliberate design work.

Changed for DEDAL: provider-specific Skill/subagent mechanics removed; heavy questioning is opt-in/contextual rather than globally triggered; DEDAL may proceed with stated uncertainty when the Creator chooses; project/runtime/system authority remains higher priority.

This package is a rewritten DEDAL contract, not a verbatim copy of the upstream skill.
