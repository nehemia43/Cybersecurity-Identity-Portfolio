# Lab 41: Native SSH Proxying & Terminal Integration (PSM for SSH)

## 🎯 Objective
To implement a high-productivity administrative workflow using CyberArk PSM for SSH, enabling secure terminal access via Putty while maintaining strict credential isolation and session auditing.

## 🛠 Technical Implementation
* **Native Terminal Integration:** Configured Putty to utilize the CyberArk PSM for SSH proxy, bypassing the web interface for direct command-line access.
* **String Nomenclature Mastery:** Developed and validated the multi-parameter connection string (`VaultUser@TargetUser@TargetAddress@ProxyAddress`) required for proxy routing.
* **MFA-Ready Authentication:** Successfully performed a Vault-level authentication handshake within the terminal environment.
* **CLI Justification Workflow:** Verified the enforcement of 'Reason for Access' prompts within the SSH proxy stream, ensuring 100% audit compliance.
* **Isolated Session Execution:** Validated the transparent injection of vaulted credentials into the target Linux environment (`targetLin`) without exposing sensitive data to the administrative endpoint.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-17):** Remote Access. Demonstrates the ability to proxy and monitor administrative remote access sessions using native protocols.
* **Frictionless Governance:** Promotes PAM adoption by allowing administrators to retain familiar toolsets (Putty, MobaXterm) while still enforcing session recording and password isolation.

## 📸 Proof of Work

### 1. Putty Connection Configuration
A view of the Putty configuration screen showing the formatted connection string in the 'Host Name' field.
![Putty Config](./putty_config.png)

### 2. The Terminal Handshake
Evidence of the Vault password prompt and the subsequent 'Reason for Access' request within the CLI.
![Terminal Handshake](./cli_justification.png)

### 3. Active Proxied Session
A screenshot showing the successful login to the Linux target, including the 'Session is being recorded' notification.
![Active Session](./proxied_ssh.png)
