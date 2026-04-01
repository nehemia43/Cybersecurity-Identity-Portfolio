# Lab 01: Windows Server Domain Controller Promotion

## 🎯 Objective
The focus of this lab is to configure a baseline Windows Server environment and promote it to a Primary Domain Controller (DC) to handle identity services.

## 🛠 Technical Configuration
* **Operating System:** Windows Server (Standard Edition)
* **Server Name:** `WindowsServer`
* **Domain Name:** `cyber.local` (New Forest)
* **NetBIOS Name:** `CYBER`
* **Static IP Address:** `192.168.44.200`
* **DNS Server:** `127.0.0.1` (Loopback address for local resolution)

## 🚀 Implementation Steps
1.  **Identity & Network Prep:** Renamed the server to `WindowsServer` and assigned a static IPv4 address within the virtual network range.
2.  **Role Installation:** Used Server Manager to add the **Active Directory Domain Services (AD DS)** and **DNS Server** roles.
3.  **Domain Promotion:** Promoted the server to a Domain Controller for a new forest (`cyber.local`) and configured the DSRM password.
4.  **Verification:** Validated that the `cyber.local` DNS zone was created and initialized the `IAM Class` Organizational Unit (OU) in **Active Directory Users and Computers**.

## 📸 Proof of Work
![AD Promotion Dashboard](./AD_Dashboard.png)
