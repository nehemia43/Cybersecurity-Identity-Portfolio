# Lab 33: CyberArk Master Policy & Governance Baselines

## 🎯 Objective
To establish a global privileged access governance framework by configuring the CyberArk Master Policy, enforcing session-level security controls, and managing platform-specific exceptions.

## 🛠 Technical Implementation
* **Global Workflow Configuration:** Implemented a standardized security baseline, enforcing 'Exclusive Access' (Checkin/Checkout) and 'One-Time Password' (OTP) rotation across the enterprise vault.
* **Dual Control Orchestration:** Evaluated the multi-level approval process and configured 'Four-Eyes' authorization for high-sensitivity platforms.
* **Exception Management:** Developed platform-specific overrides to the Master Policy, allowing for tailored workflows that balance high-security requirements with operational efficiency.
* **Session Accountability:** Enforced mandatory 'Reason for Access' prompts to ensure all privileged sessions are mapped to documented business justifications.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-3):** Access Enforcement. Demonstrates the centralized management of access control policies and the ability to enforce strict authorization workflows.
* **SOX Compliance:** Exclusive access and OTP rotation provide the "Absolute Accountability" required for financial systems, ensuring that administrative actions are tied to a single, verified identity.

## 📸 Proof of Work

### 1. Master Policy Configuration
A view of the Master Policy interface showing the activated security parameters for the organization.
![Master Policy](./master_policy_baselines.png)

### 2. Platform Exceptions
Evidence of a specific platform (e.g., Windows Server) having a customized exception for Dual Control.
![Policy Exception](./policy_exception.png)

### 3. Applied Governance (Account View)
Showing the badges on the account list that confirm Exclusive Access and OTP are being enforced by the policy.
![Applied Governance](./applied_policy.png)
