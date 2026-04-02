# Lab 21: Cross-Platform Federation & SAML SSO (Entra ID to G Suite)

## 🎯 Objective
To implement an enterprise-grade Federated Identity solution using SAML 2.0, establishing Microsoft Entra ID as the authoritative Identity Provider (IdP) for Google Workspace (Service Provider).

## 🛠 Technical Implementation
* **SAML 2.0 Configuration:** Established a bidirectional trust relationship by exchanging metadata, Entity IDs, and X.509 certificates between Azure and Google Cloud.
* **Automated Provisioning (SCIM):** Configured the Entra ID Provisioning Service to automate the user lifecycle (Create, Update, Delete) in G Suite based on Azure group assignments.
* **Just-In-Time (JIT) Logic:** Evaluated the attribute mapping requirements to ensure consistent UPN-to-Email synchronization across disparate cloud platforms.
* **Federated Authentication Testing:** Validated the IDP-Initiated SSO flow, confirming successful token exchange and seamless user redirection without redundant credential prompts.

## ⚖️ GRC & Security Connection
* **NIST 800-63C:** Federation and Assertions. This lab demonstrates the secure communication of authentication and attribute assertions between an IdP and an RP (Relying Party).
* **Identity Consolidation:** Reduces the "Attack Surface" by centralizing all authentication and MFA policies in a single location, simplifying termination (Offboarding) and auditing.

## 📸 Proof of Work

### 1. SAML Configuration Details
Showing the shared URLs and Identifiers between the Azure Enterprise App and the Google Admin console.
![SAML Config](./saml_handshake.png)

### 2. Automated Provisioning Authorization
Evidence of the successful API connection and "Test Connection" status for user syncing.
![Provisioning Setup](./scim_provision.png)

### 3. SSO Verification (The Redirect)
A capture of the login flow successfully landing on the Google dashboard via Azure authentication.
![SSO Success](./sso_redirect.png)
