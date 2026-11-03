# Identity & privileged access

Status: In progress.

## Requirement
Separate employee, administrator, application, and deployment identities around the smallest required access.

## Design decision
Use workload identity for service access and scoped, temporary administration. Separate authentication from authorization.

## Current evidence
Key Vault allow → deny → restore is recorded. Bastion SSH and a login during a one-hour JIT window were demonstrated. JIT expiry and audit closure remain pending.

## Next implementation
Verify fresh access is blocked after JIT expiry while the VM is running; complete the human/application access matrix. Okta and CyberArk extensions need separate product-specific evidence.

## Acceptance test
An approved action succeeds, an unassigned action fails, and a new administration connection fails after the approved window.

## Interview discussion
Explain the requirement, trust boundary, alternatives, rejected option, expected failure, observed evidence, limitations, cost and rollback. Separate work already tested from proposed improvements.
