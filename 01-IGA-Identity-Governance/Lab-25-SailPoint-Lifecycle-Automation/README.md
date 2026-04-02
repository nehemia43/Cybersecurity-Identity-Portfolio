# Lab 25: Authoritative Source Aggregation & Lifecycle Automation

## 🎯 Objective
To implement automated Identity Lifecycle Management (ILM) using flat-file authoritative sources, demonstrating the Joiner/Leaver process through SailPoint IdentityIQ tasks.

## 🛠 Technical Implementation
* **Authoritative Source Integration:** Configured flat-file connectors to simulate HR (Workday/SAP) and Vendor Management systems.
* **Joiner Orchestration:** Successfully provisioned new Identity Cubes for 'Lionel Messi' and 'Cristiano Ronaldo' by executing scheduled Aggregation Tasks.
* **Manager Correlation (Identity Refresh):** Implemented a 'Manager Discovery' process to resolve Manager IDs into clickable identity links, establishing a searchable organizational hierarchy.
* **Automated Deprovisioning (Leaver):** Validated the 'Leaver' workflow by removing records from the authoritative source, resulting in the automated deletion of the associated Identity Cubes.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates automated mechanisms to support the management of information system accounts throughout their lifecycle.
* **Orphaned Account Mitigation:** By syncing with the HR "Source of Truth," the organization ensures that terminated employees (Leavers) do not retain "Ghost Access" to sensitive systems.

## 📸 Proof of Work

### 1. Authoritative Source Flat-Files
Showing the raw identity data for employees and contractors before and after activation.
![Source Files](./source_data.png)

### 2. Task Execution & Results
Evidence of the Aggregation and Identity Refresh tasks completing successfully.
![Task Results](./task_execution.png)

### 3. Identity Warehouse Verification
| New Joiner (Messi) | Manager Link (Correlation) |
| :--- | :--- |
| ![Joiner Success](./joiner_created.png) | ![Manager Correlation](./manager_linked.png) |

### 4. Leaver Verification
Showing the Identity Warehouse after the record is removed from the source, confirming the deletion.
![Leaver Success](./leaver_deleted.png)
