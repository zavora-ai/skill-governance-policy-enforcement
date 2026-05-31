# Governance Policy Enforcement Examples

## Example 1: "Can I deploy to production right now?"
```
evaluate_policy(action: "deploy", resource: "production/api", actor: "dev-james") → {allowed: false, reason: "Production deploys require platform-team approval. Change freeze active until Monday.", policies: ["prod-deploy-gate", "change-freeze-weekends"]}
```
Response: "❌ Deploy blocked by 2 policies:\n1. **prod-deploy-gate** — requires platform-team approval\n2. **change-freeze-weekends** — active until Monday\n\nOptions: request an exception with justification, or wait until Monday."

## Example 2: "What if we limit staging to 3 replicas max?"
```
simulate_policy(policy_change: {rule: "max-replicas", new_value: 3, scope: "staging"}) → {impact: {affected_services: 8, currently_over_limit: 2, services_affected: ["batch-worker (5 replicas)", "event-processor (4 replicas)"]}}
evaluate_policy(action: "apply_policy_change", resource: "staging/policy", actor: "admin") → {allowed: true, note: "Admin has policy-management permission"}
```
Response: "📊 Simulation results for max-replicas=3 in staging:\n• 8 services evaluated, 2 currently exceed limit\n• **batch-worker** would scale down from 5 → 3\n• **event-processor** would scale down from 4 → 3\n\nYou have permission to apply this change. Want me to proceed?"

## Example 3: "Generate the Q1 compliance report for the auditors"
```
audit_log(filter: {date_range: "2026-Q1", policies: ["data-retention", "access-control", "encryption-at-rest"]}) → {total_evaluations: 3420, allowed: 3385, denied: 32, exceptions: 3}
list_approvals(status: "resolved", date_range: "2026-Q1") → [{total: 45, approved: 41, rejected: 4}]
export_evidence(scope: "2026-Q1", policies: ["data-retention", "access-control", "encryption-at-rest"], format: "pdf") → {url: "/evidence/Q1-2026-full-audit.pdf", pages: 34, generated: "2026-05-30T09:00:00Z"}
```
Response: "📋 Q1 2026 Compliance Report generated:\n• 3,420 policy evaluations (99.1% pass rate)\n• 32 denials, 3 approved exceptions\n• 45 approval requests (41 approved, 4 rejected)\n• Full evidence: /evidence/Q1-2026-full-audit.pdf (34 pages)"
