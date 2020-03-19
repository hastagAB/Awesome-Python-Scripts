from smtplib import SMTP as smtp
import json

def sendmail(sender_add, reciever_add, msg, password):
    server = smtp('smtp.gmail.com:587')
    server.starttls()
    server.login(sender_add, password)
    server.sendmail(sender_add, reciever_add, msg)
    print("Mail sent succesfully....!")


group = {}
print('\t\t ......LOGIN.....')
your_add = input('Enter your email address :')
password = input('Enter your email password for login:')
print('\n\n\n\n')
choice = 'y'
while(choice != '3' or choice != 'no'):
    print("\n 1.Create a group\n2.Message a group\n3.Exit")
    choice = input()
    if choice == '1':
        ch = 'y'
        while(ch != 'n'):
            gname = input('Enter name of group :')
            group[gname] = input('Enter contact emails separated by a single space :').rstrip()
            ch = input('Add another....y/n? :').rstrip()
        with open('groups.json', 'a') as f:
            json.dump(group, f)
    elif choice == '2':
        gname = input('Enter name of group :')
        try:
            f = open('groups.json', 'r')
            members = json.load(f)
            f.close()
        except:
            print('Invalid group name. Please Create group first')
            exit
        members = members[gname].split()
        msg = input('Enter message :')
        for i in members:
            try:
                sendmail(your_add, i, msg, password)
            except:
                print("An unexpected error occured. Please try again later...")
                continue
    else:
        break
