var1 = input("enter the number1")
var2 = input("enter the number2")
print ((var1+var2)**2)-(var1**2+var2**2)
# it can be extended as
sum=0;sum1=0
var = input("get the number for finding the difference")
for i in range(1,var+1,1):
		c= i**2
		sum+=c
		sum1+=i
print "the difference is ",(sum1**2)-sum

		