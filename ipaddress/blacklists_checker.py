import pydnsbl
import sys
from IPy import IP
import smtplib
from email.message import EmailMessage

def test_ip(ip):
    ip_checker = pydnsbl.DNSBLIpChecker()
    result = ip_checker.check(ip)
    if result.blacklisted == True:
        detected = result.detected_by
        return(result, detected)
    else:
        return()

res_txt = 'IP blacklists check returned next results:\n'
send_param = 0
if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        if x in '-y-Y':
            send_param = 1
        else:
            try:
                IP(x)
            except:
                print('Argument isn`t a valid ip('+x+")\n Skipping argument")
            else:
                if test_ip(x):
                    res, detec = test_ip(x)
                    res_txt = res_txt + str(res) +'\n'+ str(detec) +'\n'+'\n'
else:   
    print('Type in ip to check')
    x = input()
    try:
        IP(x)
    except:
        print('Argument isn`t a valid ip('+x+")")
        sys.exit()
    else:
        if test_ip(x):
                res, detec = test_ip(x)
                res_txt = res_txt + str(res) +'\n'+ str(detec) +'\n'
if len(res_txt) <= 43:
    print("IPs not blacklisted!")
else:
    if send_param == 1:
        mailed = "Y"
    else:
        print('Send mail (default No)')
        mailed = input()
    if mailed in 'Yy' and mailed != "":
        msg = EmailMessage()
        msg.set_content(res_txt)
        msg['Subject'] = 'Delist IPs from blacklists'
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
    print('Blacklist result is: \n' + res_txt)
