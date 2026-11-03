# Detection & incident response

Status: Design only.

## Requirement
Turn access decisions and configuration changes into useful detection and investigation evidence.

## Design decision
Choose a small set of diagnostic sources and a specific detection before expanding collection or automation.

## Current evidence
Earlier lab failures and role changes provide candidate test scenarios. No integrated log-ingestion, KQL alert, or automated response is claimed.

## Next implementation
Configure scoped diagnostics, confirm ingestion, write a query, generate a safe test event, trigger one alert, and investigate it.

## Acceptance test
A timestamped test event is found in logs and triggers the configured detection; the runbook identifies actor, resource, time, and response.

## Interview discussion
Explain the requirement, trust boundary, alternatives, rejected option, expected failure, observed evidence, limitations, cost and rollback. Separate work already tested from proposed improvements.
