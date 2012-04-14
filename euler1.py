var = 0
sum=0
while True:
		if var%3==0 or var%5==0: sum +=var
		var+=1
		if var>1000: break
	  
print "the sum of multiples of 3 and 5 is ",sum	