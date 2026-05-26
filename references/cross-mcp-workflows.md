# Governance Cross-MCP Workflows

## Governance + Payments: Policy-Gated Payments
```
GOVERNANCE: evaluate_policy(action: "payment", amount: 500000, actor: "agent_1")
  → {decision: "requires_approval", policy: "payments_over_1000"}
PAYMENTS: request_payment_approval(id: "pi_big")
GOVERNANCE: open_approval(action: "payment_500000", approver: "finance_mgr")
→ Human approves
GOVERNANCE: resolve_approval(id, decision: "approved")
PAYMENTS: execute_approved_intent(id: "pi_big")
```

## Governance + Environment: Deploy Gate
```
GOVERNANCE: evaluate_policy(action: "deploy_production", actor: "agent_1")
  → {decision: "allowed", conditions: ["ci_passes", "staging_healthy"]}
ENVIRONMENT: run_checks(env: "staging") → healthy ✅
ENVIRONMENT: promote_release(from: "staging", to: "production")
GOVERNANCE: audit_log(action: "deploy_production", result: "success")
```
