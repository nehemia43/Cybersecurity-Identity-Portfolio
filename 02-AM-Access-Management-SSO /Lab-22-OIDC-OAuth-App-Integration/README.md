# Lab 22: Modern App Registration & OIDC/OAuth 2.0 Integration

## 🎯 Objective
To demonstrate the integration of custom-built applications with Microsoft Entra ID using OpenID Connect (OIDC) for authentication and OAuth 2.0 for authorization.

## 🛠 Technical Implementation
* **Application Provisioning:** Registered a custom ASP.NET Core web application within the Entra ID 'App Registrations' blade, defining a single-tenant access boundary.
* **Protocol Handshake:** Configured secure Redirect URIs and Front-channel logout URLs to manage the OIDC callback lifecycle.
* **Code-Level Identity Mapping:** Integrated the Application (Client) ID and Directory (Tenant) ID into the local `appsettings.json` to facilitate the cryptographic handshake with the Microsoft Identity Platform.
* **Functional Validation:** Successfully executed a local runtime environment, verifying the automated redirect to the corporate IdP and the subsequent token issuance to the application.

## ⚖️ GRC & Security Connection
* **NIST 800-63C:** Federated Identity. This lab provides hands-on evidence of implementing modern assertion-based authentication protocols.
* **Security by Design:** Demonstrates the 'Least Privilege' principle by ensuring the application only requests the specific user claims (scopes) required for basic identity verification.

## 📸 Proof of Work

### 1. App Registration Metadata
Evidence of the registered application, showing the Client and Tenant IDs.
![App Registration](./app_reg_details.png)

### 2. Redirect URI Configuration
The 'Authentication' blade showing the secured localhost callback paths.
![Redirect Config](./redirect_uris.png)

### 3. Localhost Authentication Success
A capture of the custom application successfully displaying the authenticated user's UPN.
![App Login Success](./app_success.png)
