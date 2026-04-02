# Lab 26: Attribute Synchronization & Source of Truth Governance

## 🎯 Objective
To demonstrate the "Mover" lifecycle phase by synchronizing attribute changes from authoritative sources and configuring data persistence policies to maintain identity integrity.

## 🛠 Technical Implementation
* **Authoritative Synchronization:** Simulated a location transfer by modifying flat-file source data and executing an aggregation task to update the Identity Warehouse.
* **Identity Mapping Configuration:** Configured attribute-level governance by toggling 'Edit Modes' (Read-Only vs. Temporary) within the Global Settings.
* **Conflict Resolution Testing:** Performed a manual attribute override ('Madrid') and validated that the authoritative source correctly synchronized and overwrote the manual entry during the next task cycle.
* **Schema Mapping:** Analyzed the technical link between CSV headers and SailPoint Identity Attributes to ensure seamless data flow.

## ⚖️ GRC & Security Connection
* **Data Integrity:** Ensures that the IGA solution remains a faithful reflection of the HR 'Source of Truth,' preventing unauthorized manual changes to identity data.
* **Audit Readiness:** By forcing changes through the authoritative source, the organization maintains a centralized audit trail of all identity transfers and status changes.

## 📸 Proof of Work

### 1. Source Data Modification
A capture of the CSV file showing the attribute update from 'London' to 'Paris.'
![Source Update](./source_update.png)

### 2. Identity Mapping Configuration
Evidence of the 'Region' attribute being set to 'Temporary' edit mode for governance testing.
![Attribute Mapping](./attribute_mapping.png)

### 3. Manual Override Verification
The SailPoint UI showing the manual entry before the next aggregation cycle.
![Manual Override](./manual_override.png)

### 4. Automated Persistence (Post-Aggregation)
Showing the attribute reverting to the authoritative value, proving successful governance enforcement.
![Persistence Check](./persistence_check.png)
