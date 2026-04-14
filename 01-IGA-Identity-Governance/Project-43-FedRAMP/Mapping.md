To automate the continuous monitoring of identity-related controls to ensure "Audit Readiness" for SOC 2 and FedRAMP environments using the Secure Controls Framework (SCF).

Technical Action (What you do),SCF Control (The Standard),SOC 2 (SaaS Rule),FedRAMP (Gov Rule)

User Access Review: Running a script to see who has an account.,IAC-01,CC6.1,AC-2

Inactivity Check: Flagging users who haven't logged in for 90 days.,IAC-06,CC6.3,AC-2 (3)

MFA Verification: Checking if admins have Multi-Factor enabled.,IAC-02,CC6.2,IA-2



Evidence Type: Automated CSV Export.



Frequency: Daily (via GitHub Actions).



Storage: Secure GitHub "Evidence" Folder.



Control Owner: Identity Architect (That's you!).
