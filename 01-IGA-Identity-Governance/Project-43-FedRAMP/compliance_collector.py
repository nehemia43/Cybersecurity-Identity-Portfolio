import requests
import csv
from datetime import datetime, timedelta

# Settings
OKTA_ORG = "https://your-dev-id.okta.com"
API_KEY = "008wQfimNcQxufl_L9S2r5pk_Ko4KIQqzzeAlOn-LE" # Use GitHub Secrets in a real job!

def generate_evidence():
    print(f"--- Evidence Collection Started: {datetime.now()} ---")
    headers = {"Authorization": f"SSWS {API_KEY}"}
    
    # 1. Pull the data
    response = requests.get(f"{OKTA_ORG}/api/v1/users", headers=headers)
    users = response.json()
    
    # 2. Define our "Audit Rule" (FedRAMP requires 90-day checks)
    ninety_days_ago = datetime.now() - timedelta(days=90)
    
    evidence_list = []
    
    for user in users:
        email = user['profile']['email']
        last_login = user.get('lastLogin')
        
        # Logic: Is this account a "Risk"?
        if not last_login:
            status = "FAIL: Never Logged In (Orphaned Account)"
        else:
            login_date = datetime.strptime(last_login, "%Y-%m-%dT%H:%M:%S.%fZ")
            status = "PASS" if login_date > ninety_days_ago else "FAIL: Inactive > 90 Days"
        
        evidence_list.append({"User": email, "Last_Login": last_login, "Audit_Status": status})

    # 3. Create the "Evidence Artifact" for the Auditor
    filename = f"Evidence_AC2_{datetime.now().strftime('%Y-%m-%d')}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["User", "Last_Login", "Audit_Status"])
        writer.writeheader()
        writer.writerows(evidence_list)
    
    print(f"Success! Artifact created: {filename}")

if __name__ == "__main__":
    generate_evidence()
