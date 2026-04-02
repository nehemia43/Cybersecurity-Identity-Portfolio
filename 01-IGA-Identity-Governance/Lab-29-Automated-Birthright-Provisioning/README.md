# Lab 29: Automated Role Provisioning & Birthright Governance

## 🎯 Objective
To implement a "Zero-Touch" provisioning model in SailPoint IdentityIQ, using attribute-based assignment rules to automate the lifecycle of high-privilege roles for executive leadership.

## 🛠 Technical Implementation
* **RBAC Role Engineering:** Developed the 'Time Tracking Reporting' role, abstracting granular application entitlements into a business-friendly container.
* **Attribute-Based Assignment (ABAC):** Configured a 'Match List' assignment rule targeting the 'Executive Management' department attribute to trigger automated grants.
* **Joiner Workflow Simulation:** Processed the onboarding of a new executive identity via authoritative source aggregation, validating that the required access was provisioned without manual intervention.
* **Lifecycle Event Processing:** Executed 'Identity Refresh' tasks to synchronize the identity warehouse with the new role-engine logic.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates automated mechanisms to support the management of information system accounts based on organizational position.
* **Access Creep Mitigation:** By tying access to current identity attributes, the solution ensures 'Automatic Revocation' when a user changes departments, preventing the accumulation of unnecessary privileges over time.

## 📸 Proof of Work

### 1. Role Assignment Logic
A view of the SailPoint role editor showing the 'Department = Executive Management' matching rule.
![Role Rule](./role_logic.png)

### 2. Automated Grant Verification
Evidence of the 'Time Tracking Reporting' role appearing on the new user's (Will Smith) identity cube immediately following aggregation.
![Automated Grant](./birthright_success.png)

### 3. Entitlement Consolidation
Showing the underlying 'Reporting' capability being successfully inherited through the business role.
![Inherited Access](./entitlement_inheritance.png)
