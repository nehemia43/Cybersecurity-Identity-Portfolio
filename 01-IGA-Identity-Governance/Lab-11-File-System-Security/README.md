# Lab 11: File System Security & Data Governance (NTFS)

## 🎯 Objective
To implement granular data-at-rest security by enforcing NTFS Access Control Lists (ACLs) based on departmental roles, ensuring strict data isolation within a shared file environment.

## 🛠 Technical Implementation
* **Directory Architecture:** Constructed a hierarchical data structure (`C:\IAM`) to simulate a corporate file server environment.
* **Access Control Mapping:** Applied the Principle of Least Privilege (PoLP) by mapping Active Directory Security Groups to specific folder permissions.
* **Deny-Override Logic:** Utilized explicit NTFS "Deny" permissions to ensure that departmental data (Finance/HR/IT) remains siloed, even if users share common secondary group memberships.
* **Public Collaboration Space:** Provisioned a "Public" directory with 'Modify' permissions, allowing cross-functional data sharing while preventing unauthorized permission changes.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-6):** Least Privilege. This lab demonstrates technical enforcement of data access boundaries.
* **Data Sovereignty:** Proves the ability to maintain data integrity and confidentiality at the file-system level, a core requirement for **HIPAA** and **GDPR** compliance.

## 📸 Proof of Work

### 3. Verification (Cross-Departmental Testing)
Validating the "Deny-Override" logic. The system successfully authorizes the departmental owner while hard-blocking unauthorized identities.

| Authorized Access (Finance User) | Unauthorized Access (Blocked) |
| :--- | :--- |
| ![Finance Success](./finance_access.png) | ![Access Denied](./blocked_access.png) |

---
## 🏁 Pillar 01: Foundation Complete
This concludes the foundational Identity Governance section. All core infrastructure (AD, GPO, IIS, and NTFS) is now secured and audited.