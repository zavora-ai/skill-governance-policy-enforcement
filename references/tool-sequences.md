# Governance Policy Enforcement Tool Sequences (8 tools)

## Evaluation (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `evaluate_policy` | Check if action is allowed by policy | read |
| `simulate_policy` | Simulate policy change impact | read |

## Approvals (3)
| Tool | Purpose | Risk |
|------|---------|------|
| `open_approval` | Create approval request | write |
| `list_approvals` | List pending/resolved approvals | read |
| `resolve_approval` | Approve or reject a request | **production** |

## Exceptions (1)
| Tool | Purpose | Risk |
|------|---------|------|
| `request_exception` | Request policy exception with justification | write |

## Audit (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `audit_log` | View policy decision history | read |
| `export_evidence` | Export compliance evidence package | read |

## Sequence: Pre-Action Policy Check (3 calls)
```
1. evaluate_policy(action: "deploy", resource: "production/api", actor: "ci-bot") → {allowed: false, reason: "requires approval from platform-team", policy: "prod-deploy-gate"}
2. open_approval(action: "deploy", resource: "production/api", justification: "Critical bugfix for payment timeout", approvers: ["platform-team"]) → {approval_id: "apr-101", status: "pending"}
3. resolve_approval(approval_id: "apr-101", decision: "approved", actor: "alice@company.com", reason: "Verified fix is safe") → {resolved: true, action_unblocked: true}
```

## Sequence: Simulate Before Applying (3 calls)
```
1. simulate_policy(policy_change: {rule: "max-replicas", new_value: 3, scope: "staging"}) → {impact: {affected_services: 5, currently_over_limit: 2, services: ["worker", "batch-processor"]}}
2. evaluate_policy(action: "apply_policy_change", resource: "staging", actor: "admin") → {allowed: true}
3. audit_log(filter: {action: "policy_change", last: "24h"}) → [{action: "max-replicas changed", actor: "admin", time: "now"}]
```

## Sequence: Compliance Export (3 calls)
```
1. audit_log(filter: {date_range: "2026-Q1", policy: "data-retention"}) → {entries: 142, denials: 3, exceptions: 1}
2. list_approvals(status: "resolved", date_range: "2026-Q1") → [{id: "apr-045", action: "delete-user-data", decision: "approved"}, ...]
3. export_evidence(scope: "2026-Q1", policies: ["data-retention", "access-control"], format: "pdf") → {url: "/evidence/Q1-2026-compliance.pdf", pages: 28}
```
