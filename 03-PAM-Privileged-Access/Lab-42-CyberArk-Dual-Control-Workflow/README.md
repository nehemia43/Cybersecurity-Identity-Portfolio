# Lab 42: Dual Control & Multi-Tiered Approval Workflows

## 🎯 Objective
To implement a strict "Four-Eyes" authorization model in CyberArk, ensuring that privileged sessions on sensitive infrastructure require a secondary human approval before execution.

## 🛠 Technical Implementation
* **Global Policy Enforcement:** Activated Dual Control within the Master Policy to mandate access requests for the entire vault.
* **Delegated Approval Authority:** Designated an 'Approver' identity (Dexter) at the Safe level, utilizing the Level 1 Approver preset to separate authorization from execution.
* **Just-In-Time (JIT) Workflow:** Navigated the end-user request flow as a standard identity (Carlos), defining access reasons and temporal windows (One-time vs. Timeframe).
* **Multi-Persona Validation:** Executed the approval process from the Security Manager's perspective, providing documented justification for the grant.
* **Audit Transparency:** Verified the transition of the request status from 'Pending' (Yellow) to 'Confirmed' (Green), culminating in an isolated, recorded RDP session.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-3):** Access Enforcement. Demonstrates the implementation of the 'Dual Authorization' principle for high-risk administrative tasks.
* **Insider Threat Mitigation:** Prevents a single compromised administrative identity from accessing sensitive data by requiring a secondary, independent verification step.

## 📸 Proof of Work

### 1. Master Policy Activation
A screenshot of the CyberArk Master Policy showing Dual Control set to 'Active.'
![Policy Setup](./dual_control_active.png)

### 2. The Pending Request (User View)
The account dashboard for Carlos showing the 'Request Connection' button and a pending status.
![Pending Request](./request_pending.png)

### 3. Incoming Request (Approver View)
The dashboard for Dexter showing the details of Carlos's request and the 'Confirm' action.
![Approval Interface](./incoming_request.png)

### 4. Successful Session Fulfillment
The final state where the connection is authorized and the 'Connect' button is available for the user.
![Session Authorized](./access_granted.png)
