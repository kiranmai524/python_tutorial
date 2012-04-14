var=20;product=1
for i in range(var,1,-1):
		count=0
		for j in range(1,i+1,1):
				if i%j==0: count+=1
		if count==2: product*=i
#the produt so obtained is a multiple of all d prime numbers now multiplying this prime numbers and check divisibility with composites
for j in range(1,var+1,1):
		if product%j!=0:
				for k in range(1,var+1,1):
						count=0
						for r in range(1,var+1,1):
								if k%r==0: count+=1
						if count==2: 
								product*=k
								if product%j!=0:product/=k
								else: break
		
		
print product