# Lab 34: Automated Credential Hygiene & Session Retention

## 🎯 Objective
To automate the privileged credential lifecycle and establish a video-based audit trail for administrative sessions, ensuring continuous synchronization and compliance between CyberArk and target infrastructure.

## 🛠 Technical Implementation
* **Automated Rotation (CPM):** Configured a 90-day password rotation cycle to mitigate the risk of long-term credential exposure.
* **Verification & Reconciliation:** Established a 7-day heartbeat verification to detect 'out-of-sync' accounts and trigger automated remediation.
* **Session Proxying (PSM):** Re-enabled 'Click to Connect' functionality to enforce credential isolation and eliminate the need for administrators to handle raw passwords.
* **Visual Auditing:** Activated video-based session recording to satisfy forensic accountability and regulatory monitoring requirements.
* **Retention Governance:** Set a 90-day audit log retention period to align with standard corporate compliance baselines.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (IA-5):** Authenticator Management. Demonstrates automated password changes and the enforcement of complex, dynamic authenticators.
* **SOX/HIPAA Compliance:** Session recording provides non-repudiable evidence of administrative activity, essential for protecting sensitive financial or medical data systems.

## 📸 Proof of Work

### 1. Password Management Parameters
A view of the CPM settings showing the 90-day rotation and 7-day verification frequency.
![CPM Settings](./cpm_config.png)

### 2. Session Monitoring Activation
Evidence of the 'Privileged Session Monitoring' parameter being enabled in the Master Policy.
![Session Monitoring](./session_mon_active.png)

### 3. Policy Inheritance (By Platform)
A screenshot showing a specific platform inheriting the Master Policy settings or maintaining an exception.
![Platform Policy](./platform_inheritance.png)
