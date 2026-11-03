# Cloud foundations & governance

Status: Design only.

## Requirement
Define the business requirements, trust boundaries, resource structure, policies, and cost controls.

## Design decision
Start with the existing Azure environment. Add GCP counterparts for selected requirements before considering direct cross-cloud connectivity.

## Current evidence
Architecture scope and implementation plan are documented. No integrated landing zone or policy-remediation result is claimed.

## Next implementation
Inventory current resources and costs; document threats and alternatives; test one scoped Azure Policy and a GCP baseline.

## Acceptance test
An unsafe configuration is rejected by the selected policy; a compliant configuration succeeds. Record actual outcomes.

## Interview discussion
Explain the requirement, trust boundary, alternatives, rejected option, expected failure, observed evidence, limitations, cost and rollback. Separate work already tested from proposed improvements.
