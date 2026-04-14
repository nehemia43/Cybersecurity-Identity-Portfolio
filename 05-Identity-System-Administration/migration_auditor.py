import os
import requests
from dotenv import load_dotenv

# 1. Load your secure keys from the .env file
load_dotenv()
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
    response = requests.post(url, data=data)
    
    # Debugging logic to catch the exact Microsoft error
    if response.status_code != 200:
        error_info = response.json()
        print(f"--- 🛠️ MICROSOFT DEBUG INFO ---")
        print(f"Status Code: {response.status_code}")
        print(f"Error: {error_info.get('error')}")
        print(f"Description: {error_info.get('error_description')}")
        print(f"-------------------------------")
        return None
        
    return response.json().get('access_token')

def audit_identity_risks(token):
    print("--- 🔍 Starting Domain Migration Impact Analysis ---")
    headers = {'Authorization': f'Bearer {token}'}
    
    # FETCH USERS: Pulling UPN and ID attributes
    user_url = "https://graph.microsoft.com/v1.0/users?$select=displayName,userPrincipalName,id"
    users = requests.get(user_url, headers=headers).json().get('value', [])
    
    print(f"Found {len(users)} users. Mapping UPN to Object ID...")
    for user in users:
        print(f"Checking: {user['userPrincipalName']} | ID: {user['id']}")

    # FETCH APPS: Scanning for SAML/SSO dependencies
    app_url = "https://graph.microsoft.com/v1.0/servicePrincipals?$select=displayName,preferredSingleSignOnMode"
    apps = requests.get(app_url, headers=headers).json().get('value', [])
    
    print(f"\nScanning {len(apps)} Applications for SSO Dependencies...")
    for app in apps:
        sso_mode = app.get('preferredSingleSignOnMode', 'None/Other')
        risk = "⚠️ HIGH RISK" if sso_mode == "saml" else "✅ LOW RISK"
        print(f"App: {app['displayName']} | SSO: {sso_mode} | STATUS: {risk}")

if __name__ == "__main__":
    access_token = get_token()
    if access_token:
        audit_identity_risks(access_token)
    else:
        print("❌ Error: Could not authenticate. Check your .env file!")
