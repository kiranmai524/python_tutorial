import math
var =int( math.pow(2,1000))
sum=0
while var>0:
		sum+=(var%10)
		var/=10
print "the sum is",sum