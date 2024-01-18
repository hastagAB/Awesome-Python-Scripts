# Mass_Email_Unique_Attachments
Sends mails to a list of addresses, with different attachments. 
Useful for mailing personalized certificates, layoff letters and wedding invitations. 
Reads data from a CSV file with email addresses and the names of the files which are to be sent as attachments.
# Setup
- Create a folder containing all attachments which are to be sent
- Create a CSV file with two columns, the name of the attachment file, and the mail address of the receiver
- Add the path of the folder and CSV file in your script
# Usage
There are two scripts, the native script will use the Outlook or Windows Mail to send the mails. The mails will be sent from your currently logged-in mail id. This script is suitable for Windows.
The SMTP script allows you to setup a SMTP server to send mails. Follow the comment instructions in the script to setup an SMTP server. This requires you to allow alternative sign-in from your email provider. 
The `smtp_server` depends on which mail provider you are using. Common servers for major providers are:
- Yahoo!
  - smtp.mail.yahoo.com
- Gmail
  - smtp.gmail.com
- Outlook
  - smtp.office365.com	/ smtp-mail.outlook.com

The password to be entered in `smtp_password` is generated from your email provider settings.
- https://hotter.io/docs/email-accounts/secure-app-gmail/
- https://superuser.com/questions/1521236/how-to-allow-less-secure-app-access-in-microsoft-email
- https://help.inspectionsupport.com/en/articles/392427-enable-less-secure-apps-for-smtp-use-isn-yahoo-mail
      
The first script is suitable for users who don't wish to setup an SMTP server, or don't want to generate a less secure key.

# Alteration
You can modify the code to change the type of attachments being sent, for example instead of PDFs, you can send Word documents by changing the `pdf_file_name = row['name'] + '.pdf'` to `pdf_file_name = row['name'] + '.docx'`. For images, use .png, .jpg, etc.

You can also comment out the CC option if you don't wish to CC the mail to anyone.
