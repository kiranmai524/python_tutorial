for i in range(1000,1,-1):
		check=i*(i-1)
		check1=check
		recheck=0
		while check>0:
				r=check%10
				recheck=recheck*10+r
				check/=10
		if(recheck==check1):
				print "it is a palindrome",check1,"product of",i,i-1
				break
		
		
		