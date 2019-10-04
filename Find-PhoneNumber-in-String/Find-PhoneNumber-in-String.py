def check_phone_number(string):
    if len(string) != 12:
        return False
    for i in range(0, 3):
        if not string[i].isdecimal():
            return False
    if string[3] != '-':
        return False
    for i in range(4, 7):
        if not string[i].isdecimal():
            return False
    if string[7] != '-':
        return False
    for i in range(8, 12):
        if not string[i].isdecimal():
            return False
        return True

string = input("Enter a Sentence: ")

for i in range(len(string)):
    split = string[i:i+12]
    if check_phone_number(split):
        print('Phone number has been found! : ' + split)