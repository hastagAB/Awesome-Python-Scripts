# Website Blocker using Python
This is a program which blocks certain distracting website like Facebook, Youtube etc during your work hours.

## Libraby Used
time (datetime is imported from python)

## Host Files
Host is an operating system file which maps hostnames to IP addresses.
Using python file handling manipulation I have changed hostnames on the hosts files for a certain interval of day when I'm working and need no distraction and deleted it then after when the time is over.

## Location of host file
### Host file on Mac and Linux :
    $ /etc/hosts

### Host file on windows :
    $ C:\Windows\System32\drivers\etc

## Note
* Windows user need to create a duplicate of OS’s host file. Now provide the path of the duplicate file in hosts_path mentioned in the script.
* For scheduling above script in Linux you have to open crontab in your terminal as a root.(use sudo command)
