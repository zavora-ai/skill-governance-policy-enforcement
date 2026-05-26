#!/usr/bin/env python3
"""Evaluate if an action is allowed by policy rules."""
import json, sys

POLICIES = {
    "payment_over_1000": {"action": "payment", "condition": "amount > 100000", "decision": "requires_approval"},
    "deploy_production": {"action": "deploy", "condition": "env == production", "decision": "requires_approval"},
    "delete_data": {"action": "delete", "condition": "any", "decision": "requires_approval"},
}

def evaluate(data):
    action = data.get("action", "")
    matching = [p for p in POLICIES.values() if p["action"] == action]
    if not matching:
        return {"decision": "allowed", "policy": "none", "reason": "No policy covers this action"}
    return {"decision": matching[0]["decision"], "policy": matching[0]["condition"], "reason": f"Policy requires approval for {action}"}

if __name__ == "__main__":
    print(json.dumps(evaluate(json.loads(sys.argv[1])), indent=2))
