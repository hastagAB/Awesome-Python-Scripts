"""
For more information on the algorithm, refer the following links:

https://www.di-mgt.com.au/rsa_alg.html
https://people.csail.mit.edu/rivest/Rsapaper.pdf
https://www.youtube.com/watch?v=wXB-V_Keiu8

"""


def isPrime(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p*p<=n:
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1

    return prime[n]


def gcd(a,b):
    while b!=0:
        r = a%b
        a=b
        b=r
    return a

def Multiplicative_inverse(a,b):
    s1 = 1
    s2 = 0
    m = b
    while b!=0:
        q=a//b
        r=a%b
        a=b
        b=r
        s=s1-q*s2
        s1=s2
        s2=s
        
    if s1<0:
        s1+=m
        
    return s1

def powermod(x,y,p):
    res = 1
    
    x = x%p 
    while (y>0):
        
        if (y%2) == 1:
            res = (res*x)%p
            
        y = y//2
        x = (x*x)%p
        
    return res

if __name__ == '__main__':
    while (True):
        res = input('Do you want to enter prime numbers (y) or let the algorithm do it for you (n) or exit (e)? (y/n/e): ')
        if res == 'y':
            while True:
                p = 13
                p = int(input('Enter a prime number: '))
                if isPrime(p):
                    break
                else:
                    print(p,'is not a prime number')
                    continue

            while True:
                q = 17
                q = int(input('Enter a different prime number: '))
                if isPrime(q) and (p*q>26):
                    break
                else:
                    print('Both the prime numbers are same!! or product of both the prime numbers is less than 26!!')
                    continue

            n = p*q
            phi_n = (p-1)*(q-1)
            a = 19
            while True:
                a = int(input('Enter a number such that Greatest Common Divisor of that number with '+ str(phi_n) + ' is 1: '))
                if gcd(a,phi_n)!=1:
                    continue
                else:
                    break

            b = Multiplicative_inverse(a,phi_n)
            message = input('Enter the message to be encrypted (lower case): ')
            message = message.lower()

            encrypted_string = ""
            encrypted_num = []

            for i in range(len(message)):
                ch = message[i]
                if ch!=' ':
                    m = ord(ch) - 97
                    e = powermod(m,a,n)
                    encrypted_num.append(e)
                    encrypted_string += chr(e%26 + 97)
                else:
                    encrypted_string +=' '

            print('Encrypted message is:', encrypted_string)
            print(encrypted_num)
            res = input("Do you want to decrypt it too? (y/n): ")
            if res == 'y':
                decrypted = ''
                j=0
                for i in range(len(encrypted_string)):
                    ch = message[i]
                    if ch != ' ':
                        e = encrypted_num[j]
                        m = powermod(e,b,n)
                        ch = chr(m+97)
                        decrypted+=ch
                        j+=1
                    else:
                        decrypted+=' '
                    
                print("Decrypted message is:",decrypted)
            else:
                ans = input("Do you want to continue? (y/n): ")
                if ans == 'y':
                    continue
                else:
                    break

        elif res == 'n':
            p = 13
            q = 17
            n = p*q
            a = 5
            b = 77
            message = input('Enter the message to be encrypted (lower case): ')
            message = message.lower()

            encrypted_string = ""
            encrypted_num = []

            for i in range(len(message)):
                ch = message[i]
                if ch!=' ':
                    m = ord(ch) - 97
                    e = powermod(m,a,n)
                    encrypted_num.append(e)
                    encrypted_string += chr(e%26 + 97)
                else:
                    encrypted_string +=' '

            print('Encrypted message is:', encrypted_string)
            res = input("Do you want to decrypt it too? (y/n): ")
            if res == 'y':
                decrypted = ''
                j=0
                for i in range(len(encrypted_string)):
                    ch = encrypted_string[i]
                    if ch != ' ':
                        e = encrypted_num[j]
                        m = powermod(e,b,n)
                        ch = chr(m+97)
                        decrypted+=ch
                        j+=1
                    else:
                        decrypted+=' '
                    
                print("Decrypted message is:",decrypted)
            else:
                ans = input("Do you want to continue? (y/n): ")
                if ans == 'y':
                    continue
                else:
                    break
        elif res == 'e':
            break
        else:
            print('Invalid command!')
            continue
