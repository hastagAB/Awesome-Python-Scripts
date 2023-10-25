import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+`~[]{]\|;:,<.>/?'

welcomeMessage = "Welcome to the Password Generator!"
detailsMessage = "This program will generate a secure password using a random arrangement of letters (CAPS ON & caps off), numbers, and punctuations."
creatorMessage = "Created by Professor Renderer on October 3rd, 2018."

print(welcomeMessage + '\n' + detailsMessage + '\n' + creatorMessage + '\n')

exitMessage = 0
passwordGeneratorUsage = 1
passwordGeneratorPrompt = 1


while exitMessage != 1:

    while passwordGeneratorUsage == 1:

        passwordGeneratorPrompt = 1
       
        passwordNum = input('How many passwords would you like to generate? ')
        passwordNum = int(passwordNum)


        passwordLength = input('How long will the password(s) be? ')
        passwordLength = int(passwordLength)

        print('\n')
        print('Here are your password(s): \n')

        passwordFile = open('Passwords.txt', 'w')
        for p in range(passwordNum):
            password = ''
            for c in range(passwordLength):
                password += random.choice(chars)
            print(password)
            passwordFile.write(password + '\n')
        passwordFile.close()
        print('\n')

        while passwordGeneratorPrompt == 1:

            getContinue = input('Do you want to use the Password Generator again? (Y/N)')
            print('\n')
            
            if getContinue == "Y" or getContinue == "y":
                passwordGeneratorPrompt = 0
                print('\n')
            elif getContinue == "N" or getContinue == "n":
                exitMessage = 1
                passwordGeneratorUsage = 0
                passwordGeneratorPrompt = 0
            else:
                print("Please enter 'Y' or 'N.'\n")


print('\n')
print('Thank you for using the Password Generator. Have a nice day!')

