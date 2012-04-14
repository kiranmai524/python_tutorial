var = 100;prod=1
for i in range(2,var+1,1):
		prod*=i
sum=0
while prod>0:
			sum+=(prod%10)
			prod/=10
print sum