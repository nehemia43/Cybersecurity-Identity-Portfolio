# Lab 31: CyberArk PAM Fundamentals & Session Isolation

## 🎯 Objective
To demonstrate the secure management and execution of privileged administrative tasks using CyberArk PAM, utilizing session isolation and real-time audit recording to secure high-value targets.

## 🛠 Technical Implementation
* **LDAP-Integrated Authentication:** Established a secure administrative session using LDAP-sourced identities, ensuring centralized credential governance.
* **Vault Architecture:** Navigated the CyberArk 'Safe' and 'Platform' hierarchy to identify authorized privileged accounts for Linux environment management.
* **Just-In-Time Justification:** Implemented a mandatory 'Reason for Access' prompt, establishing a granular audit trail for compliance and traceability.
* **Session Isolation (PSM):** Executed a proxied SSH connection to a target Linux server via the Privileged Session Manager (PSM), ensuring the administrative workstation remains isolated from the target resource.
* **Comprehensive Auditing:** Validated the automatic session recording feature, providing a full video and keystroke log for forensic and regulatory review.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-17):** Remote Access. This lab demonstrates the implementation of managed access control points for administrative sessions.
* **Accountability:** The use of session recording and access justification satisfies 'Strict Liability' audit requirements, ensuring that every privileged action can be attributed and reviewed.

## 📸 Proof of Work

### 1. CyberArk Web Portal (Account View)
Showing the Mike identity authenticated via LDAP with access to the Linux Admin safes.
![Account View](./cyberark_dashboard.png)

### 2. Access Justification
Evidence of the 'Reason for Access' prompt required before the RDP/PSM file is issued.
![Justification](./access_reason.png)

### 3. Isolated Session (The Recording)
A screenshot of the Linux CLI showing the 'You are being recorded' notification and active session proxying.
![Session Recording](./session_active.png)
