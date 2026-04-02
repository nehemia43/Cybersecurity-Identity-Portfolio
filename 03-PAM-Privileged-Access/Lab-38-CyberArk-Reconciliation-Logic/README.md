# Lab 38: Automated Password Policy & Reconciliation Logic

## 🎯 Objective
To implement a self-healing credential management framework in CyberArk by configuring automated rotation, verification, and reconciliation tasks, including a Master Policy exception for high-frequency rotation.

## 🛠 Technical Implementation
* **Lifecycle Automation:** Activated `PerformPeriodicChange` and `PerformPeriodicVerification` to establish a continuous credential health-check within the Windows server environment.
* **Self-Healing Reconciliation:** Configured `AutomaticReconcileWhenUnsynced` to trigger automated password resets via a designated domain-level reconciliation account.
* **Operational Guardrails:** Defined execution windows (`FromHour`/`ToHour`) and `ExecutionDays` to ensure that automated password rotations align with corporate maintenance schedules.
* **Reconciliation Mapping:** Linked the reconciliation identity by mapping the technical account name and safe location (`CyberArk Service Accounts`) within the platform properties.
* **Policy Override:** Implemented a Master Policy Exception to override the global 90-day rotation baseline, enforcing a strict 45-day lifecycle for the target platform.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (IA-5):** Authenticator Management. Demonstrates the automated rotation of authenticators and the ability to remediate out-of-sync credentials without manual intervention.
* **Continuous Compliance:** Automated verification ensures that the "Password in the Vault" is always the "Password on the Server," providing 100% audit accuracy for privileged sessions.

## 📸 Proof of Work

### 1. Password Management Toggles
A view of the platform properties tree showing 'Periodic Change' and 'Verification' set to 'Yes'.
![Management Toggles](./mgmt_toggles.png)

### 2. Reconciliation Account Linkage
Evidence of the reconciliation safe and technical account name being configured in the platform settings.
![Reconciliation Link](./reconcile_link.png)

### 3. Master Policy Exception
Showing the 45-day rotation exception specifically applied to the `win-SLV-lock-45` platform.
![Policy Exception](./rotation_exception.png)
