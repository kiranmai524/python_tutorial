def is_prime(digit):
		now=3
		while (now*now)<=digit:
				if digit%now==0: return False
				else: now+=2
		return True
numprime=1 #considering 2 as only even prime we only check the odd numbers
num=1;sum=2
while num<2000000:
		num+=2
		if is_prime(num):
				sum+=num
				numprime+=1
print "the sum of prime numbers below 2000000 is%r and number of primes is %r"%(sum,numprime)