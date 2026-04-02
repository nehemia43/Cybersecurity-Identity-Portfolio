# Lab 39: Account Onboarding & Lifecycle Verification

## 🎯 Objective
To perform manual onboarding of a privileged local administrator account and validate the end-to-end lifecycle of automated credential rotation, exclusive access governance, and isolated session recording.

## 🛠 Technical Implementation
* **Manual Onboarding:** Integrated the `localAdmin01` account into the `win-SV-FR` safe, leveraging platform-level regex filtering to ensure correct safe-to-platform mapping.
* **Immediate Credential Hardening:** Validated the 'Auto-Change on Add' policy, witnessing the CPM intercept the initial weak password and perform an automated rotation/reconciliation.
* **Exclusive Access Enforcement:** Verified the 'Check-in/Check-out' lock mechanism, ensuring non-repudiation by preventing concurrent administrative sessions on the same account.
* **Isolated Session Verification:** Executed a proxied RDP session via the PSM, confirming the 'Recording Active' notification and the successful injection of vault-managed credentials.
* **Audit Trail Analysis:** Audited the 'Activity' tab to verify the chronological log of account creation, CPM rotation, and successful user connection.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (IA-5):** Authenticator Management. This lab provides evidence of removing human knowledge of passwords by rotating credentials immediately upon system entry.
* **Zero Trust Architecture:** Demonstrates the 'Proxy' model where the administrator never handles the raw password, and the workstation is isolated from the target server.

## 📸 Proof of Work

### 1. Onboarding Metadata
A view of the account creation screen showing the specific Windows platform and safe mapping.
![Onboarding](./account_add.png)

### 2. CPM Activity & Rotation Success
Evidence of the 'Lightning Bolt' transitioning to a successful 'Reconciled' status in the activity logs.
![CPM Activity](./cpm_rotation_log.png)

### 3. Active Session & Lock Status
Showing the isolated RDP session running while the CyberArk UI indicates the account is 'Checked out' by the current user.
![Exclusive Access](./session_checkout.png)
