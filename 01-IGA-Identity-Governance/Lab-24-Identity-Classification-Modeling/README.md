# Lab 24: Identity Classification & Attribute Modeling

## 🎯 Objective
To implement a differentiated identity model in SailPoint IdentityIQ, ensuring that identity attributes are provisioned and governed based on the authoritative source and the legal relationship (Employee vs. Contractor) with the organization.

## 🛠 Technical Implementation
* **Classification Logic:** Utilized the Identity Warehouse to categorize 230+ identities into distinct 'Employee' and 'Contractor' types.
* **Authoritative Source Mapping:** Evaluated the correlation between secondary data sources (HR vs. Vendor Management) and the resultant identity type attribute.
* **Attribute Schema Customization:** Analyzed the 'Job Title' and 'Pay Grade' attributes, confirming their presence for employees and their absence for contractors as a matter of data privacy and minimization.
* **Identity Warehouse Navigation:** Demonstrated the ability to perform bulk identity audits and filter identities based on organizational relationship types.

## ⚖️ GRC & Security Connection
* **NIST 800-53 (IA-4):** Identifier Management. Demonstrates the management of specific identity attributes and types to ensure clear accountability.
* **Data Minimization (GDPR/Privacy):** By explicitly choosing NOT to store 'Job Title' for contractors, the organization reduces the amount of Personal Identifiable Information (PII) held on non-employees, lowering the risk in the event of a data breach.

## 📸 Proof of Work

### 1. Identity Type Classification
A view of the Identity Warehouse showing the 'Employee' and 'Contractor' labels.
![Identity Types](./identity_types.png)

### 2. Employee Profile (Full Attribute Schema)
Evidence of an employee record showing the Job Title and Manager attributes.
![Employee Schema](./employee_schema.png)

### 3. Contractor Profile (Minimized Schema)
Showing a contractor profile where the 'Job Title' field is intentionally left blank.
![Contractor Schema](./contractor_schema.png)
