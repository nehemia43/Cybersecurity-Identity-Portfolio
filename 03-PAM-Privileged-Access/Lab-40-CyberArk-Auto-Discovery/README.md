# Lab 40: Automatic Account Discovery & Onboarding Rules

## 🎯 Objective
To implement an automated "Shadow IT" detection framework in CyberArk, utilizing Discovery Scans and Onboarding Rules to ensure 100% visibility and governance of privileged accounts across the enterprise.

## 🛠 Technical Implementation
* **Onboarding Rule Engineering:** Created a standardized rule for the 'Windows Server' perimeter, enforcing automated safe assignment (`win-SV-FR`) and platform mapping.
* **Discovery Scan Orchestration:** Configured and executed an LDAP-integrated scan targeting specific Organizational Units (OUs) in the Acme Corp domain.
* **Privileged Scanning:** Leveraged a dedicated CPM-led scanning identity to query local SAM databases on target servers.
* **Automated Integration:** Successfully identified and automatically onboarded 15 "Shadow Admin" accounts into the Vault without manual intervention.
* **Pending Account Triage:** Performed an audit of discovered accounts using metadata (Age/Activity) to determine the appropriate governance action (Onboard vs. Decommission).

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates the capability to detect and manage unauthorized or "Orphaned" accounts in a dynamic infrastructure.
* **Attack Surface Reduction:** Directly mitigates the risk of 'Credential Dumping' by finding and securing unmanaged administrative accounts that are primary targets for lateral movement.

## 📸 Proof of Work

### 1. Onboarding Rule Configuration
A view of the 'Discovery' rule showing the server-type filters and target safe mapping.
![Onboarding Rule](./onboarding_rule.png)

### 2. Discovery Scan Management
Evidence of the 'In Progress' and 'Completed' scan status for the Acme Corp domain.
![Scan Status](./scan_results.png)

### 3. Automated Onboarding Verification
The Account View showing the 15 newly discovered accounts successfully integrated into the safe.
![Discovered Accounts](./discovered_success.png)
