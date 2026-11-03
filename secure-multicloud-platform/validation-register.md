# Validation register

| Control | Observed result | Scope / limits |
|---|---|---|
| Key Vault workload identity | Retrieval succeeds; removing read role denies; restoring role succeeds | Disposable secret; public path denial not separately verified |
| Blob private read | HTTP 200 and content verification pass | Container-scoped Reader |
| Blob write | HTTP 403 AuthorizationPermissionMismatch | Service authorization test |
| Blob HTTP transport | HTTP 400 AccountRequiresHttps | Separate from identity and network tests |
| SQL private read/write | Managed-identity SELECT pass; INSERT denied with error 229 | One demonstration table |
| SQL public path | Explicit Deny Public Network Access rejection | Cloud Shell request |
| Bastion and JIT | Login during approved window; hostname/user verified October 16, 2026 at 11:42:03 UTC | Expiry and audit closure pending; generic pre-window timeout is inconclusive alone |
| GCP / integrated app / detection / Terraform | Not yet implemented | Design only; do not interpret roadmap as successful deployment |

Historical captures do not establish current live resource state. Verify current compute and paid-plan settings before resuming. Full resource cleanup remains unverified.
