def is_prime(digit):
		now=3
		while (now*now)<=digit:
				if digit%now==0: return False
				else: now+=2
		return True
numprime=1 #considering 2 as only even prime we only check the odd numbers
num=1;sum=2
while numprime<10001:
		num+=2
		if is_prime(num):
				numprime+=1
print "the 10001'st prime is ",num