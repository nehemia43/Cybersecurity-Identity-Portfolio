# Secure delivery & operations

Status: Design only.

## Requirement
Make the proven configuration reproducible, reviewable, and resistant to unsafe changes.

## Design decision
Use Terraform and scoped OIDC federation; plan private runner connectivity and identity permissions before deployment.

## Current evidence
This platform’s Terraform modules and deployment pipeline are not implemented yet. Existing manual labs define the acceptance requirements.

## Next implementation
Codify a bounded environment, secure state access, add security checks, constrain deployment trust, and test cleanup.

## Acceptance test
An intentionally unsafe change fails a check; a corrected change passes and deploys into the authorized lab scope.

## Interview discussion
Explain the requirement, trust boundary, alternatives, rejected option, expected failure, observed evidence, limitations, cost and rollback. Separate work already tested from proposed improvements.
