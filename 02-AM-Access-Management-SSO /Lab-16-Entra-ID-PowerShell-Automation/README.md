# Lab 16: Programmatic Identity Management via PowerShell

## 🎯 Objective
To transition from manual UI-based administration to automated cloud identity management using PowerShell, focusing on module integration, RBAC role assignment, and scripted user provisioning.

## 🛠 Technical Implementation
* **API Integration:** Installed and configured the `AzureAD` PowerShell module to establish a secure administrative session with the Entra ID tenant.
* **Privileged Identity Management:** Assigned the 'Global Administrator' role to a delegated identity to facilitate remote management capabilities.
* **Identity Orchestration:** Developed a PowerShell script to provision a new cloud identity (`Steve@rainingcloudy.com`) using complex objects for secure password handling.
* **Data Auditing:** Leveraged `Get-AzureADUser` with advanced server-side filtering to perform an identity audit and verify successful provisioning.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-2):** Account Management. Demonstrates the use of automated mechanisms to support the management of information system accounts.
* **Standardization:** Scripted provisioning ensures that every user is created with the exact same security attributes, eliminating the risk of "Configuration Drift" caused by manual entry errors.

## 📸 Proof of Work

### 1. PowerShell Environment Setup
Showing the successful installation of the AzureAD module and the connection handshake.
![PowerShell Connection](./ps_connect.png)

### 2. Scripted User Provisioning
Evidence of the PowerShell script used to create the 'Steve' identity with secure password objects.
![Provisioning Script](./ps_provision.png)

### 3. Verification (Cloud & CLI)
| CLI Verification (Get-AzureADUser) | Portal Verification (UI) |
| :--- | :--- |
| ![CLI Verify](./cli_verify.png) | ![Portal Verify](./portal_verify.png) |
