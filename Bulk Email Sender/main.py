import pandas as pd
import smtplib

# Initialise Credentials
SenderAddress = "abc@gmail.com"
password = "Enter Your Password"
''' example
password="123456"
'''

# Read the email addresses from excel sheet
e = pd.read_excel("test.xlsx")

# Converting Emails in list format
emails = e['Emails'].values

# Creating instance of subclass SMTP inside smtplib class
server = smtplib.SMTP("smtp.gmail.com", 587)

# Setup
server.starttls()
server.login(SenderAddress, password)

# Initialise the content
greeting = "Dear Receiver,"
msg="Main Content"
link="Any URLS"
end="Ending Greets"
regards="With Regards"
name="Sender's name"
subject = "Subject"
body = "Subject: {}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n{}".format(subject,greeting,msg,link,end,regards,name)

# Loop to send mail to all email ids
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()