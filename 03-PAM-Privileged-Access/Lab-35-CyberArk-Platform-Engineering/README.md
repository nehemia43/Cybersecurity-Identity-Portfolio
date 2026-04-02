# Lab 35: Platform Engineering & Granular Policy Overrides

## 🎯 Objective
To engineer a custom CyberArk Platform using standardized nomenclature and advanced workflow configurations, establishing the technical foundation for automated credential rotation and reconciliation.

## 🛠 Technical Implementation
* **Platform Prototyping:** Duplicated the 'Windows Server Local' template to create a specialized target platform: `win-SLV-lock-45`.
* **Nomenclature Discipline:** Applied an enterprise-naming convention to define OS, Asset Type, Scope, and Rotation Frequency within the Platform ID.
* **Credential Seeding:** Configured 'Auto Change on Add' to enforce immediate password randomization upon account onboarding, mitigating 'Time-of-Check to Time-of-Use' vulnerabilities.
* **Schema Definition:** Audited mandatory and optional onboarding attributes (Address, Username, Domain) to ensure data integrity for automated CPM tasks.
* **Reconciliation Architecture:** Linked a secondary reconciliation identity to the platform to facilitate automated 'Out-of-Sync' remediation.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates the capability to define specific security parameters for different classes of privileged accounts.
* **Configuration Consistency:** Using platforms ensures that every Windows server in the organization follows the exact same rotation and verification policy, eliminating "Security Silos."

## 📸 Proof of Work

### 1. Platform Management Dashboard
Showing the newly created `win-SLV-lock-45` platform in the Windows category.
![Platform List](./platform_list.png)

### 2. UI & Workflow Configuration
Evidence of the 'Auto Change on Add' parameter being set to 'Yes' in the tree-view editor.
![Workflow Settings](./workflow_config.png)

### 3. Required Onboarding Attributes
The schema view showing the mandatory fields (Address, Username) required for account integration.
![Onboarding Schema](./onboarding_schema.png)
