# Lab 28: Entitlement Engineering & Request Fulfillment (SailPoint IIQ)

## 🎯 Objective
To demonstrate the end-to-end lifecycle of access fulfillment, from the programmatic creation of new application entitlements to the execution of manager-led approval workflows and automated JDBC provisioning.

## 🛠 Technical Implementation
* **Entitlement Catalog Management:** Provisioned a new 'Reporting' capability within the Time Tracking application schema, defining it as a 'Requestable' business resource.
* **Workflow Orchestration:** Navigated a multi-persona request flow involving a Requester (Admin), an Approver (Manager), and a Target Subject (End User).
* **Automated Provisioning (JDBC):** Leveraged a direct database connector to facilitate the write-back of permissions, ensuring that the 'reporting' entitlement was successfully committed to the target application's database.
* **Self-Service Portal Navigation:** Utilized the 'Manage User Access' portal to perform attribute-based searches and aggregate access requests for delegated identities.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates the formal request and approval process required before granting additional system privileges.
* **Least Privilege Enforcement:** By requiring manager approval, the organization ensures that high-value entitlements like 'Reporting' are only granted to users with a legitimate business "Need to Know."

## 📸 Proof of Work

### 1. Entitlement Creation & Approval
Showing the administrator approving the creation of the new 'Reporting' entitlement in the catalog.
![Entitlement Creation](./entitlement_approval.png)

### 2. The Request Portal
A view of the 'Manage User Access' screen where the reporting access is selected for Alan Burton.
![Access Request](./request_portal.png)

### 3. Manager Approval Workflow
Evidence of the manager (Sara Barry) reviewing and approving the pending request.
![Manager Approval](./manager_action.png)

### 4. Provisioning Verification
The final identity profile for Alan Burton showing the successfully assigned 'Reporting' capability.
![Final Assignment](./access_verified.png)
