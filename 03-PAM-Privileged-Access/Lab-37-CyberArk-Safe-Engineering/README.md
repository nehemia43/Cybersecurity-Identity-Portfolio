# Lab 37: Safe Architecture & Delegated Permissions

## 🎯 Objective
To engineer a secure storage container (Safe) within the CyberArk Vault, enforcing a regional nomenclature and implementing a multi-tiered RBAC model via Active Directory integration.

## 🛠 Technical Implementation
* **Safe Provisioning:** Created the `win-SV-FR` safe, ensuring compliance with the platform-level 'AllowedSafes' regex established in previous governance labs.
* **CPM Load Balancing:** Assigned the safe to the primary Central Policy Manager to facilitate automated rotation and verification tasks.
* **Directory Integration:** Integrated 'Acme Corp' Active Directory groups (`Cyberark Users`, `Cyberark Security`) to drive delegated access control.
* **Permission Templating:** Applied granular 'Connect Only' presets for technical administrators and 'View Audit' rights for the security oversight team.
* **Lifecycle Retention:** Configured password versioning and retention periods to support forensic recovery and operational continuity.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-6):** Least Privilege. This lab demonstrates the 'Need-to-Know' principle by separating those who can *use* an account from those who can *audit* its usage.
* **Separation of Duties (SoD):** By assigning different AD groups to the same safe with different presets, the organization ensures that no single group has total control over the credential lifecycle.

## 📸 Proof of Work

### 1. Safe Creation & Nomenclature
A view of the Safe creation form showing the `win-SV-FR` name and CPM assignment.
![Safe Creation](./safe_creation.png)

### 2. AD Group Integration
Evidence of the search and selection of Active Directory groups for safe membership.
![AD Integration](./ad_group_search.png)

### 3. Permission Preset Configuration
Showing the 'Connect Only' and 'View Audit' checkboxes being assigned to their respective groups.
![Permission Mapping](./permission_presets.png)
