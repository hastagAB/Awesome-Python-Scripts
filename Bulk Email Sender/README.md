## Bulk Email Sender

If you want to send same mail to a large number of emails ids, this script is perfect for you.

### We are using smtplib module for email sending

Requirements: 
- pip install smtplib
- pip install pandas

#### Flow

smtplib(Simple Mail Transfer Protocol)

1. Initialise the credentials for your sending emails ("SenderAddress" and "password" line 5 in main.py)
2. Read the excel file for emails ("e" line 12 in main.py)
3. Converting excel formatted column into python list. ("emails" line 15 in main.py)
4. Create an instance of smtplib.SMTP class ("server" line 18 in main.py)
5. Basic setup : starting the instance and logging in process (line 21 in main.py)
6. Initialise the content to various string variables which constitute the main content of your email. (line 25 in main.py)
7. Loop through all emails in the list and send the emails. (line 35 in main.py)

#### NOTE
If you make any changes main.py, please mention it in README.md (this file). A better documentation makes the process of development faster.

---
Author - Saumitra Jagdale
 




