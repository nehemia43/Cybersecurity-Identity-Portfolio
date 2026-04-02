# Lab 20: Per-User Multi-Factor Authentication (MFA) Implementation

## 🎯 Objective
To enforce a "Something You Know" (Password) + "Something You Have" (Mobile Device) security model by implementing per-user MFA and verifying the enrollment lifecycle for delegated identities.

## 🛠 Technical Implementation
* **Granular Enforcement:** Targeted the 'Alex' identity for MFA enablement via the legacy Per-User MFA portal to simulate high-priority account protection.
* **Enrollment Orchestration:** Navigated the user-facing registration flow (FRX) to bind a secondary authentication factor to the identity.
* **Attribute Mapping:** Evaluated the difference between user-provided 'Authentication Phone' and admin-defined 'Office Phone' attributes sourced from the directory.
* **Authentication Validation:** Successfully performed a "Dirty Login" session in an incognito environment to confirm MFA interception and successful 2FA verification.

## ⚖️ GRC & Security Connection
* **NIST 800-63B:** Digital Identity Guidelines. This lab satisfies requirements for Multi-Factor Authenticators (AAL2).
* **Anti-Phishing Baseline:** Directly mitigates credential-stuffing attacks by ensuring that a compromised password alone is insufficient for unauthorized resource access.

## 📸 Proof of Work

### 1. MFA Administrative Dashboard
Showing the 'Enabled' status for the Alex identity in the per-user management screen.
![MFA Enablement](./mfa_enable.png)

### 2. User Enrollment Flow
The registration screen showing the phone verification process during the first login.
![MFA Registration](./mfa_register.png)

### 3. Successful MFA Challenge
An incognito window showing the SMS code challenge following the initial password entry.
![MFA Challenge](./mfa_challenge.png)

### 4. Admin Audit Verification
The Azure Portal 'Authentication Methods' screen confirming the user's registered MFA devices.
![Audit Verification](./mfa_audit.png)
