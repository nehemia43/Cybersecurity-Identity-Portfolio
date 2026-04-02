# Lab 30: Intelligent Role Mining & Access Profile Consolidation

## 🎯 Objective
To leverage Identity Intelligence via SailPoint Role Mining to discover common access patterns across the enterprise and consolidate granular entitlements into manageable IT Roles (Access Profiles).

## 🛠 Technical Implementation
* **Role Mining Orchestration:** Initiated a targeted discovery campaign across four production applications to identify "Permission Clusters" within the identity warehouse.
* **Pattern Recognition:** Analyzed 'Group 1' results to identify 77 identities sharing a common baseline of `Input` and `Europe Read` entitlements.
* **Role Promotion:** Engineered a new 'Basic Role' IT Role, encapsulating discovered entitlements and assigning formal administrative ownership.
* **Retroactive Identity Detection:** Executed a Refresh Identity Cube task to trigger the "Magic" detection of the new role across existing identities, successfully mapping the role to users who already possessed the underlying rights.

## ⚖️ GRC & Security Connection
* **Complexity Reduction:** Moves the organization from 'Entitlement Fatigue' to a streamlined Role-Based Access Control (RBAC) model, making Access Certifications 50% faster for managers.
* **Identity Hygiene:** Identifies "foundational" roles that were previously undocumented, ensuring that birthright access is based on actual usage data rather than outdated HR job descriptions.

## 📸 Proof of Work

### 1. Role Mining Analysis
The SailPoint 'Group Analysis' table showing the identified clusters and the number of matching identities.
![Mining Results](./role_mining_results.png)

### 2. Access Profile Configuration
Evidence of the 'Basic Role' being created and the underlying entitlements being mapped.
![Access Profile](./access_profile_config.png)

### 3. Identity Verification (The "Magic" Stamp)
A screenshot of Adam Kennedy's profile showing the role was 'Detected' automatically by the system.
![Role Detected](./role_detected.png)
