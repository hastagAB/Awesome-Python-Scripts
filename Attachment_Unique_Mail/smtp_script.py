import pandas as pd
import os
import smtplib
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders

# Load the CSV file
csv_file = 'file_path'  # CSV Path
df = pd.read_csv(csv_file)

# Path to the folder containing the PDFs
pdf_folder_path = 'Attachment_folder_path'  # Add the attachment folder you wish to send (name them as per the CSV file)

# Email server configuration
smtp_server = ''  # Replace with your SMTP server 
smtp_port = 587  # Replace with your SMTP port (commonly 587 for TLS)
smtp_user = ''  # Replace with your email address
smtp_password = ''  # Replace with your unique access password (typically 16 letter generated through your email provider's settings)

# Sending each mail
for index, row in df.iterrows():
    # Create a new email message
    msg = EmailMessage()
    msg['Subject'] = 'enter_subject_here'
    msg['From'] = smtp_user
    msg['To'] = row['email']  # Assuming your CSV has a column named 'email' for the address
    msg['CC'] = '' # CC; optional
    msg.set_content('') # The text contents of the mail

    # PDF file name and path
    pdf_file_name = row['name'] + '.pdf'  # Assuming your CSV has a column named 'name' for the person you are sending to
    pdf_file_path = os.path.join(pdf_folder_path, pdf_file_name)

    # Check if the PDF file exists and attach it
    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, 'rb') as f:
            file_data = f.read()
            file_type = 'application/pdf'
            file_name = pdf_file_name

        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)
    else:
        print(f"PDF file not found for {row['name']}")

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

# This script will send emails as soon as it's run. Be careful!