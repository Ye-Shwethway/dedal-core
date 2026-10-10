#!/usr/bin/env python3
"""Check routing and document contracts beyond YAML syntax and file existence."""
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate_selection(routing):
    errors = []
    select = next((s for s in routing.get("steps", []) if s.get("id") == "select"), {})
    if (select.get("max_primary") != 1 or select.get("max_supporting") != 3
            or select.get("multiple_profiles") != "require_semantic_resolution"
            or select.get("no_forced_match") is not True
            or select.get("lexical_matches") != "candidates_only"
            or select.get("semantic_decision") != "required_before_profile_activation"
            or select.get("semantic_decision_schema") != "state/routing-decision.schema.json"):
        errors.append("routing_selection_policy")
    return errors


def validate(profiles, routing, registry, document, inventory):
    errors = validate_selection(routing)
    active = {name for name, skill in registry.get("skills", {}).items() if skill.get("status") == "active"}
    if profiles.get("schema_version") != 4 or routing.get("schema_version") != 2:
        errors.append("routing_schema_version")
    if set(profiles) != {"schema_version", "profiles"} or not isinstance(profiles.get("profiles"), list):
        errors.append("profile_root_shape")
    known = {"id", "match", "primary", "supporting", "required_core", "required_private", "conditional_private", "execution_gates", "operations", "phase_gates", "required_machine", "media_workflow"}
    ids = set()
    for p in profiles.get("profiles", []):
        if not isinstance(p, dict) or set(p) - known or not isinstance(p.get("id"), str) or p["id"] in ids:
            errors.append("profile_shape_or_duplicate_id")
            continue
        ids.add(p["id"])
        match = p.get("match")
        if (not isinstance(match, dict) or set(match) - {"all", "any"}
                or not any(match.get(k) for k in ("all", "any"))
                or any(not isinstance(match.get(k, []), list) or any(not isinstance(t, str) or not t.strip() for t in match.get(k, [])) for k in ("all", "any"))):
            errors.append(f"invalid_match:{p['id']}")
        primary, supporting = p.get("primary"), p.get("supporting", [])
        if (not isinstance(primary, str) or primary not in active
                or not isinstance(supporting, list) or len(supporting) > 3
                or any(not isinstance(s, str) for s in supporting)
                or len(supporting) != len(set(s for s in supporting if isinstance(s, str)))
                or primary in supporting or any(s not in active for s in supporting if isinstance(s, str))):
            errors.append(f"invalid_skill_composition:{p['id']}")
        required = p.get("required_core", [])
        if (not isinstance(required, list) or len(required) != len(set(required))
                or any(not isinstance(x, str) or x.startswith("/") or ".." in Path(x).parts or x not in inventory for x in required)):
            errors.append(f"invalid_required_core:{p['id']}")
        if any(registry["skills"][s]["entrypoint"] not in required for s in [primary, *supporting] if isinstance(s, str) and s in active):
            errors.append(f"missing_skill_entrypoint_dependency:{p['id']}")
        machine = p.get("required_machine", [])
        if (not isinstance(machine, list) or any(not isinstance(x, str) or x not in inventory or x in required for x in machine)
                or len(machine) != len(set(machine)) or any(x.startswith("skills/") for x in machine)):
            errors.append(f"invalid_machine_dependency:{p['id']}")
        private = p.get("required_private", [])
        if not isinstance(private, list) or any(not isinstance(x, str) or not x.startswith("/DEDAL/private-overlay/") for x in private):
            errors.append(f"invalid_private_boundary:{p['id']}")
        branches = p.get("conditional_private", [])
        if not isinstance(branches, list) or any(not isinstance(b, dict) or set(b) != {"when", "sources"} or not isinstance(b.get("when"), str) or not isinstance(b.get("sources"), list) or any(not isinstance(x, str) or not x.startswith("/DEDAL/private-overlay/") for x in b["sources"]) for b in branches):
            errors.append(f"invalid_conditional_private:{p['id']}")
        elif len({b["when"] for b in branches}) != len(branches):
            errors.append(f"duplicate_condition:{p['id']}")
        gates = p.get("execution_gates", [])
        if not isinstance(gates, list) or not gates or len(gates) != len(set(gates)) or any(not isinstance(x, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", x) for x in gates):
            errors.append(f"invalid_gates:{p['id']}")
        phases = p.get("phase_gates")
        operations = p.get("operations")
        phase_names = {"inspect", "execute", "close"}
        if (not isinstance(phases, dict) or set(phases) != phase_names
                or any(not isinstance(v, list) or any(not isinstance(g, str) or g not in gates for g in v)
                       or len(v) != len(set(v)) for v in phases.values())
                or set(gates) != {g for v in phases.values() for g in v}):
            errors.append(f"invalid_phase_gates:{p['id']}")
        if (not isinstance(operations, dict) or not operations
                or any(not isinstance(k, str) or not re.fullmatch(r"[a-z][a-z0-9_]*", k)
                       or not isinstance(v, list) or not v or any(s not in phase_names for s in v)
                       or len(v) != len(set(v)) for k, v in operations.items())):
            errors.append(f"invalid_operations:{p['id']}")
        media = p.get("media_workflow")
        if media is not None:
            from media_workflow import ACTIONS
            if (not isinstance(media, dict) or set(media) - {"execute", "close"}
                    or any(not isinstance(v, dict) or any(op not in operations or phase not in operations[op]
                           or action not in ACTIONS for op, action in v.items()) for phase, v in media.items())
                    or any("media_workflow_ready" not in phases[phase] for phase in media)):
                errors.append(f"invalid_media_workflow:{p['id']}")
    if document.get("schema_version") != 1 or document.get("default") != "reject" or document.get("classification") != "first_matching_rule":
        errors.append("document_policy")
    roles, rules = document.get("roles", {}), document.get("rules", [])
    if not isinstance(roles, dict) or not isinstance(rules, list):
        errors.append("document_shape")
    else:
        patterns = set()
        for rule in rules:
            if (not isinstance(rule, dict) or set(rule) != {"pattern", "role"}
                    or not isinstance(rule.get("pattern"), str) or rule.get("role") not in roles
                    or rule["pattern"] in patterns):
                errors.append("invalid_or_duplicate_document_rule")
            else:
                patterns.add(rule["pattern"])
        for name, role in roles.items():
            if set(role) != {"authority", "formats"} or not isinstance(role["authority"], str) or not isinstance(role["formats"], list) or not role["formats"]:
                errors.append(f"invalid_document_role:{name}")
    for path in ("state/hydration-receipt.schema.json", "state/routing-decision.schema.json", "state/checkpoint.schema.json"):
        schema = json.loads((ROOT / path).read_text())
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema" or schema.get("type") != "object":
            errors.append(f"invalid_json_schema_header:{path}")
    return errors


if __name__ == "__main__":
    load = lambda path: yaml.safe_load((ROOT / path).read_text())
    errors = validate(load("index/task-profiles.yaml"), load("index/routing.yaml"),
                      load("index/SKILL_REGISTRY.yaml"), load("index/document-schema.yaml"),
                      set(json.loads((ROOT / "core-files.json").read_text())["files"]))
    from build_skill_catalog import build
    if load("index/skill-catalog.yaml") != build(ROOT):
        errors.append("skill_catalog_source_drift")
    if errors:
        print("CORE CONTRACTS: FAIL", *errors, sep="\n- ")
        sys.exit(1)
    print("CORE CONTRACTS: PASS routing composition, references, schema roles")
