# Secure Multi-Cloud Business Platform

Enterprise-style lab architecture by Nehemia F. Shury. This is a fictional internal document/reporting platform using disposable data, not a production deployment.

Status: integrated platform in progress. Existing Azure identity and private-data lab components have recorded tests. GCP implementation, application integration, detection and Terraform remain planned. Google Cloud Professional Cloud Security Engineer is a study track, not an earned certification.

## Shared design
Employee identity → application authorization → workload identity → private data services → audit and detection. Administrators use a separate Bastion/JIT path. Reviewed infrastructure delivery defines the environment. Azure is the first implementation; GCP will implement selected matching requirements without assuming identical services or requiring a cross-cloud tunnel.

- [Cloud foundations & governance](foundations.md) — Design only
- [Identity & privileged access](identity.md) — In progress
- [Application & data protection](data.md) — In progress
- [Detection & incident response](detection.md) — Design only
- [Secure delivery & operations](delivery.md) — Design only

Existing portfolio repository: https://github.com/nehemia43/Cybersecurity-Identity-Portfolio
