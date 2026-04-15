import os
import csv
import requests
from dotenv import load_dotenv

# Reusing your existing lab keys
load_dotenv('05-Identity-System-Administration/.env')
TENANT_ID = os.getenv('TENANT_ID')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        'client_id': CLIENT_ID,
        'scope': 'https://graph.microsoft.com/.default',
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    return requests.post(url, data=data).json().get('access_token')

def run_offboarding_workflow(token):
    print("--- 🚀 Initializing Ensemble Health JML Workflow ---")
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    
    with open('hr_terminations.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['status'] == 'terminated':
                print(f"⚠️ Security Event: Termination detected for {row['name']}")
                
                # Logic to disable account in Entra ID
                user_url = f"https://graph.microsoft.com/v1.0/users/{row['upn']}"
                response = requests.patch(user_url, json={"accountEnabled": False}, headers=headers)
                
                if response.status_code == 204:
                    print(f"✅ COMPLIANCE REACHED: {row['upn']} disabled.")
                else:
                    print(f"❌ LOG ALERT: Failed to disable {row['upn']}.")

if __name__ == "__main__":
    token = get_token()
    if token:
        run_offboarding_workflow(token)