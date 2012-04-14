var=1000
for a in range(1,var/3,1):
		for b in range(1,var/2,1):
				c=var-a-b
				if (a*a+b*b)==c*c : 
						print "the triplet is ",a,b,c
						break 