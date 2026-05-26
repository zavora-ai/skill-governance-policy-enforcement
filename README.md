# Governance Policy Enforcement Skill

> Policy evaluation engine — check actions against rules, manage approvals, simulate policy changes, request exceptions, and export audit evidence for compliance.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Evaluate | 1 | Check if action is allowed |
| Approve | 2 | List pending → resolve |
| Simulate | 1 | Test policy change impact |
| Export | 1 | Compliance evidence |

### Without this skill:
- Actions executed without policy check
- Policy changes deployed without impact analysis
- No audit evidence for compliance reviews

### With this skill:
- Every governed action evaluated before execution
- Policy changes simulated before applying
- Full audit evidence exportable for any period

## Installation

```bash
git clone https://github.com/zavora-ai/skill-governance-policy-enforcement.git \
  ~/.skills/skills/governance-policy-enforcement
```

## Requirements

**Required:** `mcp-governance-policy` (8 tools)
**Cross-MCP:** mcp-payments (payment gates), mcp-environment (deploy gates)

## Example

**User:** "Can we deploy to production right now?"

**Result:**
```
Policy evaluation: deploy_production
Decision: REQUIRES APPROVAL
Conditions: CI must pass + staging healthy + eng_lead approval
Status: 2/3 conditions met. Waiting on approval.
```

## Scripts

### `evaluate_action.py`
```bash
python scripts/evaluate_action.py '{"action": "payment", "amount": 500000}'
# → {"decision": "requires_approval", "policy": "payments_over_1000"}
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

## Success Criteria

| Metric | Target |
|--------|--------|
| Trigger rate | 90% on relevant queries |
| Compliance | 100% governed actions evaluated |
| Audit trail | Every action logged with actor + reason |

## Related Skills

See the full [ADK-Rust Enterprise Skills Registry](https://github.com/zavora-ai) for all 35 skills.

