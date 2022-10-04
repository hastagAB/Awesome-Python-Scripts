import csv
from email.message import EmailMessage
import os
import subprocess
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import shutil
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.2fG" % (G)
        else:
            return "%.2fM" % (M)
    else:
        return "%.2fkb" % (kb)
def disk_usage(disk):
    usage = shutil.disk_usage(disk+":\\")
    return(usage)
sum = 0
top15 = []
def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return(completed)
comandPS="Add-PSsnapin Microsoft.Exchange.Management.PowerShell.E2010; Get-Mailbox -ResultSize unlimited | Get-MailboxStatistics | Select DisplayName,TotalItemSize | Sort-Object -Property TotalItemSize -Descending | export-csv -path sizes.csv -Encoding default"
print(run(comandPS))
with open('sizes.csv', newline='') as csvfile:
    statscount = csv.reader(csvfile, delimiter=',', quotechar='"')
    statscount2 = statscount
    for row in statscount:
        spl = ''.join(row[-1]).split('(')
        spl[-1] = spl[-1].replace(' bytes)', "")
        spl[-1] = spl[-1].replace(',', "")
        if spl[-1].isdecimal() == 1:
            sum=sum+int(spl[-1])
with open('sizes.csv', newline='') as csvfile:
    statscount = csv.reader(csvfile, delimiter=',', quotechar='"')
    text = '<table style="border-collapse: collapse">\n'
    i = 0
    for ind in statscount:
        if i >= 2:
            tete = '<tr><td style="border: 1px solid; padding: 2px;">'+'</td><td style="border: 1px solid; padding: 2px;">'.join(ind)+'</td></tr>\n'
            text = text + tete
        i = i+1
        if i >= 17:
            text = text + "</table>"
            break
    print(text)
sum = sum/1024/1024/1024
print("Сумма = "+str(sum)+" GB")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
stringdate = dt_string.replace("/", "-")
stringdate = stringdate.replace(" ", "-")
stringdate = stringdate.replace(":", "-")
os.rename("sizes.csv", "sizes_"+stringdate+".csv")
f = open("data.log", "a")
f.write(str(dt_string)+" - "+str(sum)+" GB\n")
f.close()
f = open("data.log", "r")
content = f.readlines()
if len(content) >= 2:
    past = content[-2].split(" ")
    difference = float(sum) - float(past[3])
    usage = disk_usage("D")
    usedsp = formatSize(usage[1])
    freesp = formatSize(usage[2])
    fullsp = formatSize(usage[0])
    res_txt = "<html><head></head><body>Space used = "+str(sum)+"\n<br>Increased from past check for "+str(difference)+" GB<br><br>\n"+"Top15 mails \n"+text+"\n Used space on disk ="+usedsp+" of "+fullsp+"</body></html>"
else:
    res_txt = "<html><head></head><body>Space used = "+str(sum)+"\n"+"Top15 mails \n"+text+"</body></html>"
print(res_txt)
res_t = MIMEText(res_txt, "html")
msg = MIMEMultipart('alternative')
msg.attach(res_t)
msg['Subject'] = 'Exchange summary'
msg['From'] = ''
msg['To'] = ''
post_user = ''
system_pass = ''
try:
    smtp_server = smtplib.SMTP('')
    smtp_server.ehlo()
    smtp_server.login(post_user, system_pass)
    smtp_server.send_message(msg)
    smtp_server.close()
    print ("Email sent successfully to "+msg['to']+"!")
except Exception as ex:
    print ("Something went wrong….",ex)
