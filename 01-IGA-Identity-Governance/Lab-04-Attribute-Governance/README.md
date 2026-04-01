# Lab 04: Identity Attribute Management & Access Governance

## 🎯 Objective
To implement granular Identity Attribute management and establish time-bound access controls to satisfy security and compliance requirements.

## 🛠 Technical Implementation
* **Identity Enrichment:** Populated high-fidelity metadata (Department, Office, Manager) to support future Attribute-Based Access Control (ABAC).
* **Time-Based Access:** Configured **Logon Hours** to restrict interactive logins to authorized business shifts, reducing the attack surface during off-hours.
* **Lifecycle Governance:** Implemented **Account Expiration** dates to mitigate the risk of "Orphaned Accounts" for temporary or contract-based identities.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Directly addresses Account Management by ensuring accounts have a defined lifecycle and specific operational periods.
* **Audit Trail:** Rich attribute data ensures that security logs provide clear context (Who, What, Where) during an incident response investigation.

## 📸 Proof of Work
![User Attributes Dashboard](./images/User_Attributes.png)
![Logon Hours Config](./images/Logon_Hours.png)
