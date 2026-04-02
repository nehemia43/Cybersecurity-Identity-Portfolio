# Lab 27: Granular Offboarding & Identity Disabling (Suspension)

## 🎯 Objective
To implement and validate a non-destructive offboarding workflow in SailPoint IdentityIQ, focusing on attribute-driven account suspension for long-term leave scenarios.

## 🛠 Technical Implementation
* **Attribute-Driven Logic:** Modified the authoritative CSV source to toggle the `inactive` status, simulating a state-change in a primary HR system (e.g., Workday).
* **Task Orchestration:** Executed a two-stage lifecycle process:
    1. **Aggregation:** To synchronize the identity's state with the warehouse.
    2. **Refresh with Process Events:** To trigger the business rules required to cascade the 'Disable' command to downstream applications.
* **Visual Validation:** Verified the 'Red' status of linked accounts (Corporate Chat, Time Tracking), confirming that access has been successfully revoked at the target system level without deleting the identity object.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates the capability to temporarily disable accounts for users on extended leave or during investigative periods.
* **Security Best Practice:** Prevents 'Stale' or 'Ghost' accounts from being exploited by malicious actors during periods of legitimate user absence.

## 📸 Proof of Work

### 1. Authoritative Source Update
Showing the `inactive` attribute set to `True` for the target identity.
![CSV Update](./csv_inactive.png)

### 2. Identity Refresh (Process Events)
Evidence of the task execution that triggers the disabling logic.
![Task Execution](./refresh_task.png)

### 3. Downstream Revocation (Red Status)
A screenshot of the identity's application accounts showing the disabled status (Red indicators).
![Disabled Accounts](./disabled_indicators.png)
