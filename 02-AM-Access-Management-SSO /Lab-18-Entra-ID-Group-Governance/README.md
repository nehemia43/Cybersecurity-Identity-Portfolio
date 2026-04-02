# Lab 18: Entra ID Group Governance & Dynamic Membership

## 🎯 Objective
To establish a scalable and automated group management architecture, utilizing dynamic membership rules to enforce 'Zero-Touch' provisioning and lifecycle policies to maintain directory hygiene.

## 🛠 Technical Implementation
* **Group Archetyping:** Provisioned Security Groups for resource authorization and Microsoft 365 Groups for cross-functional collaboration.
* **Dynamic Orchestration:** Implemented attribute-based membership rules (e.g., Job Title/Manager) to automate user onboarding into departmental resources.
* **Administrative Delegation:** Assigned 'Group Owners' to empower decentralized management, reducing help-desk ticket volume for simple membership changes.
* **Governance Framework:** Enforced global naming conventions (Prefix/Suffix) and 'Blocked Word' lists to prevent namespace confusion and shadow-IT proliferation.
* **Lifecycle Automation:** Configured a group expiration policy to automatically prune inactive resources, satisfying long-term directory audit requirements.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates automated group membership management and lifecycle controls.
* **Standardization:** Naming policies ensure that all identities are searchable and audit-ready, preventing "Identity Debt" in the tenant.

## 📸 Proof of Work

### 1. Group Creation & Ownership
Evidence of the Security and M365 groups with delegated ownership assigned to a non-admin identity.
![Group Setup](./group_setup.png)

### 2. Dynamic Membership Rules
Showing the attribute-based logic that automates user assignments.
![Dynamic Rules](./dynamic_rules.png)

### 3. Governance & Naming Policies
The configuration screen for blocked words and forced prefixes/suffixes.
![Naming Policy](./naming_policy.png)

### 4. Expiration & Lifecycle
Evidence of the automated expiration policy to manage unused groups.
![Group Expiration](./group_expiration.png)
