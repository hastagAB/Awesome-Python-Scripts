#a simple RSA public key and private key pair generator
#using gcd from math module for coprimes
#and random for random numbers
import math
import random
p = random.randint(1,100)
q = random.randint(100,200)
if (math.gcd(p,q) == 1):
	n = p * q
	phi = (p-1)*(q-1)
	k = 0
	e = random.randint(1,20000)
	if (math.gcd(phi,e)==1):
		for i in range(1,20000):
			d = (((phi * i) + 1)/e)
			if d.is_integer():
				k = d
				break
		print('Public key is: (',e,',',n,')')
		print('Private key is: (',int(k),',',n,')')
