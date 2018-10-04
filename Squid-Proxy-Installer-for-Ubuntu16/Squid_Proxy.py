import subprocess, os
import platform


def squid():
    if platform.platform().find("Ubuntu-16.04"):
        squid = "squid"
    else:
        squid = "squid3"
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "install", "squid"])
    path = "/etc/{}/squid.conf".format(squid)
    file = open(path).read()

    s1 = file.replace("http_access allow localhost manager", "#http_access allow localhost manager")
    s2 = s1.replace("http_access deny manager", "#http_access deny manager")
    s3 = s2.replace("http_access allow localhost\n", "http_access allow all\n")

    file_port = file.split("\nhttp_port ")[1].split("\n")[0]
    print("Default Port: ", file_port)
    port = input("Change to: ")
    c_port = s3.replace("\nhttp_port " + file_port + "\n", "\nhttp_port " + port + "\n")
    open("/etc/{}/squid.conf".format(squid), "w").write(c_port)
    subprocess.call(["sudo", "service", squid, "restart"])
    print("Squid Proxy installed")


def add_pw():
    if platform.platform().find("Ubuntu-16.04"):
        squid = "squid"
    else:
        squid = "squid3"
    subprocess.call(["sudo", "apt-get", "install", "apache2-utils"])
    subprocess.call(["sudo", "touch", "/etc/{}/squid_passwd".format(squid)])
    subprocess.call(["sudo", "chown", "proxy", "/etc/{}/squid_passwd".format(squid)])
    user = input("Username: ")
    subprocess.call(["sudo", "htpasswd", "/etc/{}/squid_passwd".format(squid), user])
    path = "/etc/squid/squid.conf"
    file = open(path).read()
    sq = file.replace("http_access allow all\n",
                    "auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/squid_passwd\n"
                    "acl ncsa_users proxy_auth REQUIRED\n"
                    "http_access allow ncsa_users\n")
    open("/etc/squid/squid.conf", "w").write(sq)
    subprocess.call(["sudo", "service", squid, "restart"])
    print("Succesfully")


def change_pw():
    if platform.platform().find("Ubuntu-16.04"):
        squid = "squid"
    else:
        squid = "squid3"
    user = input("Username: ")
    subprocess.call(["sudo", "htpasswd", "/etc/{}/squid_passwd".format(squid), user])
    subprocess.call(["sudo", "service", squid, "restart"])
    print("Succesfully")


def remove_pw():
    if platform.platform().find("Ubuntu-16.04"):
        squid = "squid"
    else:
        squid = "squid3"
    os.remove("/etc/{}/squid_passwd".format(squid))
    path = "/etc/{}/squid.conf".format(squid)
    file = open(path).read()
    sq = file.replace("auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/squid_passwd\n"
                          "acl ncsa_users proxy_auth REQUIRED\n"
                          "http_access allow ncsa_users\n", "http_access allow all\n")
    open("/etc/{}/squid.conf".format(squid), "w").write(sq)
    subprocess.call(["sudo", "service", squid, "restart"])
    print("Succesfully")


def uninstall_squid():
    if platform.platform().find("Ubuntu-16.04"):
        squid = "squid"
    else:
        squid = "squid3"
    del_sq = input("Are you sure? (y/n): ")
    if del_sq == "y" or del_sq == "Y":
        subprocess.call(["sudo", "apt-get", "purge", "--auto-remove", squid])
        print("Succesfully")
    else:
        pass

while True:
    squid_select = input("""
    1 - Install Squid Proxy
    2 - Add Password
    3 - Change Password
    4 - Remove Password
    5 - Uninstall Squid Proxy
    6 - Exit\n""")

    if squid_select == "1":
        squid()
    elif squid_select == "2":
        add_pw()
    elif squid_select == "3":
        change_pw()
    elif squid_select == "4":
        remove_pw()
    elif squid_select == "5":
        uninstall_squid()
    elif squid_select == "6":
        break
    else:
        pass
