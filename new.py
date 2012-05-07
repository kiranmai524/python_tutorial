a,b,i=1,1,2;prod=1
n=input("enter:")
while i<n:
		c=a+b
		i+=1
		prod*=c
		a=b
		b=c
print "fifact(%d) is %d"%(n,prod)

