# Lab 08: Administrative Hardening & Privilege Auditing

## 🎯 Objective
To reduce the attack surface of a Windows endpoint by obfuscating the default privileged account name and enabling granular audit logs for all privileged activities.

## 🛠 Technical Implementation
* **Account Obfuscation:** Leveraged Local Group Policy (`gpedit.msc`) to rename the default `Administrator` account to `iamadmin`. This mitigates automated brute-force attacks targeting the well-known SID for the root account.
* **Security Baseline Enforcement:** Executed `gpupdate /force` to ensure the rename was committed to the local SAM database.
* **Privilege Auditing:** Configured the `Audit privilege use` policy to track Success and Failure events, providing a definitive audit trail for administrative actions.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Renaming default accounts is a core hardening requirement to prevent unauthorized access and "Low-Hanging Fruit" exploits.
* **Compliance (Audit Logs):** Enabling privilege use auditing is essential for meeting **PCI-DSS** and **HIPAA** logging requirements, ensuring accountability for every administrative change.

## 📸 Proof of Work

### 1. Group Policy Configuration
Proving the technical enforcement of the account rename.
![GPO Rename](./rename_policy.png)

### 2. Account Verification
Validating that the local SAM database reflects the obfuscated name.
![Renamed Account](./account_verify.png)

### 3. Audit Log Validation
Showing the Windows Event Viewer successfully capturing privileged activity logs.
![Security Logs](./audit_logs.png)
