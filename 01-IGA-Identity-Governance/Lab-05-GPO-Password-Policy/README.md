# Lab 05: Password Policy Enforcement via GPO

## 🎯 Objective
To implement automated security governance by enforcing password complexity and length requirements across a domain using Group Policy Objects (GPOs).

## 🛠 Technical Implementation
* **Object Migration:** Realigned the workstation asset into the managed `Computers` Organizational Unit to ensure proper policy inheritance.
* **GPO Architecture:** Designed and linked a custom Group Policy Object (GPO) to the IAM container, targeting the `Account Policies` node.
* **Control Baseline:** * Minimum Length: 6 Characters.
    * History: 0 (Disabled for lab environment).
    * Complexity: Disabled (to validate length-only enforcement).
* **Validation:** Verified policy application via `gpupdate /force` and performed a negative test by attempting to set a non-compliant 4-character password.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (IA-5):** Specifically addresses Authenticator Management. This lab demonstrates the technical enforcement of "Password Quality" requirements defined in a corporate security policy.
* **Governance Automation:** Moves the organization from "Manual Compliance" (asking users to be secure) to "Technical Enforcement" (forcing the system to be secure).

## 📸 Proof of Work
![GPO Configuration Dashboard](./ou_policy_config.png)
![Password Rejection Message](./password_failure.png)
