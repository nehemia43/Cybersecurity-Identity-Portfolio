# Lab 06: Password Hardening & Brute Force Protection

## 🎯 Objective
To mitigate credential-based attacks (Brute Force/Dictionary) by enforcing advanced password complexity and implementing automated account lockout thresholds.

## 🛠 Technical Implementation
* **Password Hardening:** Increased minimum length to **8 characters** and enabled **Password History (5)** to prevent credential reuse.
* **Brute Force Protection:** Configured **Account Lockout Policy** to trigger after **3 failed attempts**, with a 30-minute cooling-off period.
* **Identity Recovery:** Demonstrated the administrative "Unlock" procedure within Active Directory Users and Computers (ADUC) to restore user access after a lockout event.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-7):** Unsuccessful Logon Attempts. This lab satisfies the requirement to limit the number of consecutive failed logon attempts.
* **SOC2 / ISO 27001:** These frameworks require proof that an organization has automated mechanisms to prevent unauthorized access via password guessing.

## 📸 Proof of Work

### 1. Security Policy Configuration
![Policy Settings](./policy_hardened.png)

### 2. Lockout Enforcement (The Negative Test)
Validating that the system blocks access after the 3rd failed attempt.
![Account Locked Message](./account_locked.png)

### 3. Administrative Unlock
Showing the manual intervention required by an IAM Admin to restore the identity.
![ADUC Unlock View](./admin_unlock.png)
