people = 50
cars = 20
buses = 15

if cars > people:
	print " We should take the cars"
elif cars < people:
	print "We should not take the cars"
elif cars != people:
	print "No.of cars not equal to no.of people"
else:
	print "We can't decide"
	
if buses > cars:
	print "Too many buses"
elif buses < cars:
	print "Too many cars"
elif buses == cars:
	print " buses = cars"
else:
	print "We still can\'t find"
	
if people > buses:
	print "Alright, let\'s just take the buses"
else:
	print "Fine,let\'s stay home then."
	
