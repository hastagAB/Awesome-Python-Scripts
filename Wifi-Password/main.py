import subprocess
systemInfo=''
try:
    systemInfo = subprocess.check_output(['uname']).decode('utf-8', errors="backslashreplace").split('\n')
    systemInfo = systemInfo[0]
except :
    pass
if systemInfo == "Linux":
    wifiData = subprocess.check_output(['ls', '/etc/NetworkManager/system-connections']).decode('utf-8', errors="backslashreplace").split('\n')
    print ("Wifiname                       Password")
    print ("----------------------------------------")

    for wifiname in wifiData:
        if wifiname != '':
            wifiPass = subprocess.check_output(['sudo','cat', f"/etc/NetworkManager/system-connections/{wifiname}"]).decode('utf-8', errors="backslashreplace").split('\n')
            password=wifiPass[15].strip("psk=");
            print ("{:<30} {:<}".format(wifiname, password))
else:
    wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except :
                print ("{:<30}|  {:<}".format(i, ""))
        except :
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
