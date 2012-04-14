import math
def numdiv(num):
		count=0
		sqroot=math.trunc(math.sqrt(num))
		for i in range(1,sqroot+1,1):
				if num%i==0: count+=2 # that means squareroot of the number and the value i multiplied gives the number so number of factors =2
		if sqroot*sqroot == num : count-1#if a perfect square then squareroot is added twice so removw one factor
		return count
number = 1
while numdiv(number)<500:
		number+=1
print "the first triangle number to have more than 500 divisors is", number

		