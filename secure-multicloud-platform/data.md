# Application & data protection

Status: In progress.

## Requirement
Protect document and reporting data with private service access and explicit read-versus-write permissions.

## Design decision
Combine private DNS and endpoints with service permissions; network reachability alone does not authorize a data operation.

## Current evidence
Private Blob read: HTTP 200; write denied: 403. SQL managed-identity SELECT passed; INSERT denied: error 229. SQL explicitly rejected public-network access.

## Next implementation
Build the small application, test its user authorization, and add a bounded recovery exercise. GCP implementation is planned.

## Acceptance test
The application reads approved data privately; disallowed changes fail. Test transport, network, identity, and permissions separately.

## Interview discussion
Explain the requirement, trust boundary, alternatives, rejected option, expected failure, observed evidence, limitations, cost and rollback. Separate work already tested from proposed improvements.
