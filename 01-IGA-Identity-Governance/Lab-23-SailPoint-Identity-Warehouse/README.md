# Lab 23: Enterprise IAG Strategy & Identity Warehousing (SailPoint IIQ)

## 🎯 Objective
To explore the architecture of a market-leading Identity Governance and Administration (IGA) solution, focusing on identity warehousing, attribute synchronization from authoritative sources, and the abstraction of entitlements into business roles.

## 🛠 Technical Implementation
* **Identity Warehouse Analysis:** Navigated a centralized repository of 239 managed identities, analyzing the correlation between HR-sourced attributes and system-level accounts.
* **Authoritative Source Integration:** Evaluated the "Employee" application as the primary identity source, demonstrating an understanding of how HR data drives downstream access.
* **Role/Entitlement Hierarchy:** Deconstructed the identity of a 'Manager' profile to differentiate between packaged Business Roles and granular Application Entitlements (e.g., Approve/Reject permissions).
* **Governance Interface Mapping:** Identified the core functional pillars of the SailPoint platform: Lifecycle Management, Application Governance, and Intelligence/Reporting.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (IA-4):** Identifier Management. Demonstrates the management of unique organizational identifiers and their associated attributes across disparate systems.
* **Separation of Duties (SoD):** Using a centralized IAG tool allows for the automated detection of "Toxic Combinations" of entitlements that could lead to fraud or data breaches.

## 📸 Proof of Work

### 1. The Identity Warehouse
A view of the centralized identity repository showing managed users and their HR-aligned attributes.
![Identity Warehouse](./identity_warehouse.png)

### 2. Entitlement Breakdown
Evidence of the granular rights assigned to a user, showcasing the difference between Role-based and Direct assignments.
![Entitlements](./entitlement_view.png)

### 3. Application Accounts & Sources
Showing the linkage between a single identity and multiple target application accounts (Time Tracking, Chat, etc.).
![App Accounts](./account_links.png)
