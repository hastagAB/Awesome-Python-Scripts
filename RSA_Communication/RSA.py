#Modulus (N) bit length, k.
#OUTPUT: An RSA key pair ((N,e),d) where N is the modulus, the product of two primes (N=pq) not exceeding k bits in length;
# e is the public exponent, a number less than and coprime to (p−1)(q−1);
# and d is the private exponent such that e*d ≡ 1 mod (p−1)*(q−1).
##############################################################
#Select a value of e from 3,5,17,257,65537 (easy operations)
# while p mod e = 1
#   p = genprime(k/2)
#
# while q mode e = 1:
#   q = genprime(k - k/2)
#
#N = p*q
#L = (p-1)(q-1)
#d = modinv(e, L)
#return (N,e,d)

from random import randrange, getrandbits
import base64

class rsa():

    def __init__(self, e=4, k=5):
        self.e = [3, 5, 17, 257, 65537][e]
        self.k = [128, 256, 1024, 2048, 3072, 4096][k]

    def is_prime(self, n, tests=128):
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        for _ in range(tests):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    def genprime(self, length=1024):
        p = 1
        while len(bin(p))-2 != length:
            p = list(bin(getrandbits(length)))
            p = int(''.join(p[0:2] + ['1', '1'] + p[4:]), 2)
        p += 1 if p % 2 == 0 else 0

        ip = self.is_prime(p)
        while not ip:
            p += 2
            ip = self.is_prime(p)

        return p

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def get_creds(self, e, k):
        N = 0
        while len(bin(int(N)))-2 != k:
            p = self.genprime(int(k/2))
            while pow(p, 1, e) == 1:
                p = self.genprime(int(k/2))
            q = self.genprime(k - int(k/2))
            while pow(q, 1, e) == 1 and q == p:
                q = self.genprime(k - int(k/2))
            N = p*q
            L = (p-1)*(q-1)
            d = self.modinv(e, L)
        return p, q, (d, e, N)

    def get_keys(self):
        p, q, creds = self.get_creds(self.e, self.k)
        return creds

    def save_keys(self, filename="keys.k"):
        keys = self.get_keys()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(keys[0]) + "\n" + str(keys[1]) + "\n" + str(keys[2]))

    def load_keys(self, filename="keys.k"):
        with open(filename, "r", encoding="utf-8") as file:
            f = file.read().split("\n")
            d = int(f[0])
            e = int(f[1])
            n = int(f[2])
        return (d, e, n)

    def encrypt(self, ke, plaintext):
        key, n = ke
        b64_string = base64.b64encode(plaintext.encode("utf-8")).decode("utf-8")
        ready_code = []
        for char in list(b64_string):
            ready_code.append('0' * (3 - len(str(ord(char)))) + str(ord(char)))
        ready_code = int("1" + "".join(ready_code))
        cipher = pow(ready_code, key, n)
        return cipher

    def decrypt(self, kd, ciphertext):
        key, n = kd
        plain_list = list(str(pow(ciphertext, key, n)))[1:]
        plain = []
        count = 1
        temp = ""
        for i in plain_list:
            if count != 4:
                temp += i
                count += 1
            else:
                plain.append(temp)
                temp = i
                count = 2
        plain.append(temp)
        plain_list = plain
        plain = base64.b64decode(''.join([chr(int(char)) for char in plain_list])).decode("utf-8")
        return plain

encryption = rsa()
keys = encryption.get_keys()

d = keys[0]
e = keys[1]
n = keys[2]

print("key: \n" + str(e) + "/" + str(n))

while True:
    choose =  input("Encrypt (e)/ Decrypt (d) > ")
    if choose == "e":
        e, n = input("insert key > ").split("/")
        to_encrypt = input("message to encrypt > ")
        a = encryption.encrypt((int(e), int(n)), to_encrypt)
        print(a)
    elif choose == "d":
        to_decrypt = input("message to decrypt > ")
        a = encryption.decrypt((d, n), to_decrypt)
        print(a)
