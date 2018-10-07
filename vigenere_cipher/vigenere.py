alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#actuall stuff
def decryption(key, text):
    key_len = len(key)
    count = 0
    #adjusting the key
    real_key = ''
    #fixing spaces
    for i in text:
        if i != ' ':
            if count == len(key):
                count = 0
            real_key += key[count]
            count += 1
        else:
            real_key += ' '
    #print(real_key)
    encr = ''
    #decrypting
    for c in range(0,len(text)):
        if text[c] == ' ':
            encr += ' '
        elif ((ord(text[c]) >= 48) and (ord(text[c]) <= 57)):
            encr += text[c]
        else:
            encr += (alph[(ord(text[c]) - ord(real_key[c])) % 26])
    return encr

def encryption(key, text):
    key_len = len(key)
    count = 0
    #adjusting the key
    real_key = ''
    #fixing spaces
    for i in text:
        if i != ' ':
            if count == len(key):
                count = 0
            real_key += key[count]
            count += 1
            
        else:
            real_key += ' '
    #print(real_key)
    encr = ''
    #encrypting
    for c in range(0,len(text)):
        if text[c] == ' ':
            encr += ' '
        elif ((ord(text[c]) >= 48) and (ord(text[c]) <= 57)):
            encr += text[c]
        else:
            encr += (alph[(ord(real_key[c]) + ord(text[c])) % 26])
    return encr

#user input
def main():
    boolean = True
    while(boolean):
        try:
            mode = input('Do you want to encrypt or to decrypt [e/d]? ')
            if mode.upper().startswith('E'):
                text = input('Please enter the text: ').upper()
                key = input('Please enter the key: ').upper()
                print(encryption(key, text))
                boolean = False
            elif mode.upper().startswith('D'):
                text = input('Please enter the text: ').upper()
                key = input('Please enter the key: ').upper()
                print(decryption(key, text))
                boolean = False
            else:
                print('Please enter a valid choice')
        except KeyboardInterrupt:
            exit()
    
if __name__ == '__main__':
    main()
