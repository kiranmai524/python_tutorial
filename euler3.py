var=input("enter a composite number")
for i in range(var,1,-1):
		count=0
		for j in range(1,i+1,1):
				if i%j==0: count+=1
		if count==2: 
					if var%i==0 and var!=i:
							print "the highest prime factor is ",i
							break
		
# another condition is like
#if var%i==0:
#if var==i: print "the number is a prime number
#else: print "the number is 