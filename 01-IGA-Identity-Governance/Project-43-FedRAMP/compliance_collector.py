import requests
import csv
from datetime import datetime, timedelta

# --- 1. CONFIGURATION ---
# IMPORTANT: Make sure these are correct!
OKTA_URL = "https://dev-XXXXXX.okta.com" 
API_TOKEN = "008wQfimNcQxufl_L9S2r5pk_Ko4KIQqzzeAlOn-LE" 

def generate_evidence():
    print(f"--- 🤖 Security Robot: Starting Audit ({datetime.now().strftime('%Y-%m-%d %H:%M')}) ---")
    
    headers = {
        "Authorization": f"SSWS {API_TOKEN}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # --- 2. THE API CALL ---
    try:
        response = requests.get(f"{OKTA_URL}/api/v1/users", headers=headers)
        
        # If Okta says "No" (e.g., 401 Unauthorized), this will tell us
        if response.status_code != 200:
            print(f"❌ OKTA ERROR: {response.status_code}")
            print(f"Reason: {response.text}")
            return

        users = response.json()
        
        # --- 3. THE AUDIT LOGIC ---
        ninety_days_ago = datetime.now() - timedelta(days=90)
        evidence_list = []
        
        print(f"Found {len(users)} users. Checking for risks...")

        for user in users:
            # Safely get the profile data
            profile = user.get('profile', {})
            # Okta users usually use 'login' as their primary ID
            email = profile.get('login') or profile.get('email') or "Unknown_User"
            
            last_login_str = user.get('lastLogin')
            
            if not last_login_str:
                status = "FAIL: Never Logged In"
            else:
                # Clean up the timestamp to make it readable for Python
                clean_date = last_login_str.split(".")[0].replace("Z", "")
                login_date = datetime.fromisoformat(clean_date)
                
                if login_date > ninety_days_ago:
                    status = "PASS"
                else:
                    status = "FAIL: Inactive > 90 Days"
            
            evidence_list.append({
                "User": email,
                "Last_Login": last_login_str,
                "Audit_Status": status
            })

        # --- 4. CREATE THE EVIDENCE RECEIPT ---
        filename = f"Evidence_Audit_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["User", "Last_Login", "Audit_Status"])
            writer.writeheader()
            writer.writerows(evidence_list)
        
        print(f"✅ SUCCESS! Evidence artifact created: {filename}")

    except Exception as e:
        print(f"❌ SCRIPT ERROR: {e}")

if __name__ == "__main__":
    generate_evidence()
