import win32com.client
import pandas as pd
import os

# Load the CSV file
csv_file = 'your_file_path_here'  # Replace with the path to your CSV file, make sure to have \\ instead of \
df = pd.read_csv(csv_file)

# Path to the folder containing the PDFs
pdf_folder_path = 'your_folder_here'  # Add the attachment folder you wish to send (name them as per the CSV file)

# Outlook setup
ol = win32com.client.Dispatch("outlook.application")
olmailitem = 0x0

# Sending each mail
for index, row in df.iterrows():

    newmail = ol.CreateItem(olmailitem)
    newmail.Subject = 'enter_subject_here'
    newmail.To = row['email']  # Assuming your CSV has a column named 'email' with the mail address
    newmail.CC = '' # cc; optional
    newmail.Body = '' # text contents of your mail

    # PDF file name and path
    pdf_file_name = row['name'] + '.pdf'  # Assuming your CSV has a column named 'name'
    pdf_file_path = os.path.join(pdf_folder_path, pdf_file_name)


    if os.path.exists(pdf_file_path):
        newmail.Attachments.Add(pdf_file_path)
    else:
        print(f"PDF file not found for {row['name']}")

    newmail.Send()

# Note: This script will send emails as soon as it's run. Be careful!