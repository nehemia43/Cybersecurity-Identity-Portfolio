# Lab 36: PSM Governance, Notifications, and Password Complexity

## 🎯 Objective
To implement advanced platform-level governance in CyberArk, focusing on the management of session recording evidence, notification logic, and granular password complexity requirements.

## 🛠 Technical Implementation
* **Recording Lifecycle Management:** Configured the `SessionRecordSafe` and retention periods to align with corporate audit and storage policies.
* **UI Deterrence Controls:** Customized the duration and visibility of PSM recording notifications to ensure compliance with privacy laws and internal security awareness.
* **Safe Pattern Enforcement:** Utilized the `AllowedSafes` attribute with Regex/Wildcard logic (`win-SV-*`) to restrict the platform's blast radius to authorized Windows Server safes.
* **Notification Optimization:** Engineered a notification schedule to prioritize critical alerts (Expiration/Deactivation) while minimizing noise during non-business hours.
* **Technical Password Policy:** Defined a strict generation schema (Length, Char-mix) including a 'Forbidden Characters' list to ensure compatibility with legacy target system interpreters.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AU-12):** Audit Generation. This lab demonstrates the configuration of automated audit events and the secure retention of privileged session evidence.
* **Operational Resilience:** By excluding incompatible characters from the password generator, the organization prevents automated rotation tasks from causing accidental service outages on legacy infrastructure.

## 📸 Proof of Work

### 1. PSM Recording & UI Settings
A view of the tree-editor showing the retention days and notification popup duration.
![PSM Settings](./psm_governance.png)

### 2. AllowedSafes Pattern
Evidence of the `win-SV-*` restriction to ensure proper safe-to-platform mapping.
![Safe Pattern](./allowed_safes.png)

### 3. Password Generation Schema
The configuration screen showing the complexity requirements (Min/Max length and forbidden characters).
![Password Policy](./password_complexity.png)
