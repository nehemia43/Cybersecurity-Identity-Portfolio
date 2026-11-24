# SC-500 Lab 500-03 — Time-limited SSH through Azure Bastion

**Status:** Fresh run planned. Results below from the earlier run are historical.

## Architecture decision

Use Azure Bastion as the SSH administration path and just-in-time (JIT) access to limit the time an administrator can initiate a new connection. The lab checks the login and the temporary network rule separately.

## Earlier run

SSH through Bastion succeeded during the approved access window. After expiry, a fresh connection failed while the VM was running and the temporary network security group allow rule was absent. Activity Log correlation, direct public SSH testing, and full cleanup verification remained pending. This test covered a fresh connection attempt.

## Fresh run checklist

| Checkpoint | Evidence to record | Result |
| --- | --- | --- |
| Read-only inventory | VM power state, Bastion availability, SSH rule baseline, and Defender plan | Pending |
| Approved window | Request and expiry times, temporary rule scope, and fresh SSH outcome | Pending |
| After expiry | VM power state, temporary rule status, and fresh SSH outcome | Pending |
| Audit correlation | Activity Log record or documented evidence gap | Pending |
| Cleanup | Intended final state and actual resource and plan settings | Pending |

Record the expected result, observed result, timestamp, and sanitized evidence for each checkpoint. Add troubleshooting notes and design trade-offs as the run progresses.

## After lab completion

Summarize what was built, how the access path was tested, what issues came up, and what to keep or change next time. Use the recorded results for interview practice.

[Portfolio architecture and earlier evidence](https://aesthetic-pudding-79f963.netlify.app/architecture#identity)
