import requests
import csv
from datetime import datetime, timedelta

# 1. SETUP: Double-check these!
OKTA_URL = "https://dev-XXXXXX.okta.com" # Make sure this is your dev URL
API_TOKEN = "008wQfimNcQxufl_L9S2r5pk_Ko4KIQqzzeAlOn-LE"            # Make sure this is your active token

def generate_evidence():
    print(f"--- 🤖 Security Robot: Starting Audit ({datetime.now().strftime('%Y-%m-%d')}) ---")
    headers = {
        "Authorization": f"SSWS {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # 2. THE REQUEST
    response = requests.get(f"{OKTA_URL}/api/v1/users", headers=headers)
    
    # Check if the connection worked
    if response.status_code != 200:
        print(f"❌ Error: Could not connect to Okta. (Status: {response.status_code})")
        print(f"Message from Okta: {response.text}")
        return

    users = response.json()
    
    # 3. THE AUDIT LOGIC
    ninety_days_ago = datetime.now() - timedelta(days=90)
    evidence_list = []
    
    print(f"Found {len(users)} users. Checking for risks...")

    for user in users:
        # We use .get() to avoid crashing if a field is missing
        profile = user.get('profile', {})
        email = profile.get('login', 'Unknown') # Or profile.get('email')
        last_login_str = user.get('lastLogin')
        
        if not last_login_str:
            status = "FAIL: Never Logged In"
        else:
            # Okta sends dates with a 'Z' at the end; we strip it to read it
            clean_date = last_login_str.replace("Z", "")
            login_date = datetime.fromisoformat(clean_date.split(".")[0])
            status = "PASS" if login_date > ninety_days_ago else "FAIL: Inactive > 90 Days"
        
        evidence_list.append({"User": email, "Last_Login": last_login_str, "Audit_Status": status})

    # 4. CREATE THE RECEIPT
    filename = f"Evidence_Audit_{datetime.now().strftime('%Y-%m-%d')}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["User", "Last_Login", "Audit_Status"])
        writer.writeheader()
        writer.writerows(evidence_list)
    
    print(f"✅ Success! Evidence created: {filename}")

if __name__ == "__main__":
    generate_evidence()
