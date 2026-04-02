# Lab 32: Advanced PAM Workflows & Credential Governance

## 🎯 Objective
To demonstrate advanced privileged access use cases, including multi-protocol session proxying (WinSCP) and secure credential management for legacy system support.

## 🛠 Technical Implementation
* **Multi-Protocol Session Isolation:** Configured and executed a PSM-WinSCP session to facilitate secure file transfers between an isolated administrative workstation and a target Linux server.
* **Storage Hierarchy Navigation:** Utilized WinSCP through the CyberArk proxy to manage remote tree structures while maintaining local disk isolation.
* **Secure Credential Retrieval:** Demonstrated the 'Show' and 'Copy' password workflow, highlighting the requirement for just-in-time access justification.
* **Ephemeral Security Controls:** Analyzed the automated clipboard clearing and session-timeout mechanisms designed to prevent credential persistence on the endpoint.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates the auditability of privileged credential access and the enforcement of 'Need-to-Know' through justification prompts.
* **Data Exfiltration Prevention:** By using the PSM to proxy WinSCP, the organization maintains control over which files enter and exit the production environment.

## 📸 Proof of Work

### 1. Multi-Protocol Selection
A view of the 'Connect' dropdown showing the choice between SSH and WinSCP protocols.
![Protocol Options](./protocol_choice.png)

### 2. PSM-WinSCP Interface
Showing the split-pane view: the CyberArk intermediate server/local disk (left) and the target server (right).
![WinSCP Proxy](./winscp_session.png)

### 3. Audited Credential Exposure
Evidence of the 'Reason' prompt for password display and the subsequent secure viewing window.
![Password Retrieval](./password_show.png)
