# Lab 19: Scalable Group Management via PowerShell

## 🎯 Objective
To implement automated group management workflows in Microsoft Entra ID, focusing on the programmatic creation of security groups and the bulk assignment of user identities via PowerShell.

## 🛠 Technical Implementation
* **Session Management:** Demonstrated the ability to troubleshoot and re-establish expired cloud API connections using MFA-aware authentication handshakes.
* **Security Group Provisioning:** Utilized the `New-AzureADGroup` cmdlet to create a "Zero-Touch" security container for the Application Development team.
* **API-Driven Membership:** Programmatically assigned user identities (Alex@rainingcloudy.com) to the target group using delegated PowerShell parameters.
* **Membership Auditing:** Leveraged `Get-AzureADGroupMember` to perform a real-time audit of the group's security perimeter, verifying that only authorized identities were successfully nested.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (AC-3):** Access Enforcement. Demonstrates the technical ability to manage the groups that enforce access control decisions.
* **Auditability:** Scripting group memberships creates a repeatable process that can be logged and reviewed by auditors to ensure no "Permission Creep" has occurred.

## 📸 Proof of Work

### 1. Programmatic Group Creation
Evidence of the PowerShell script successfully creating the 'App Developers' security group.
![Group Creation](./ps_group_create.png)

### 2. Scripted Membership Assignment
Showing the successful execution of the member assignment command.
![Member Add](./ps_member_add.png)

### 3. Forensic Verification
| CLI Audit (Get-AzureADGroupMember) | Portal Confirmation (UI) |
| :--- | :--- |
| ![CLI Verify](./ps_group_audit.png) | ![Portal Verify](./portal_group_check.png) |
