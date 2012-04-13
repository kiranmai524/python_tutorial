def cheese_and_crackers(cheese_count, boxes_of_crackers): #defining a block of code with name cheese_and_crackers
    print "You have %d cheeses!" % cheese_count    #statement of the method
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
#end of method

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)#numbers as arguments
# prints 20, 30

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # variables as arguments
# the values 20,30 are overridden by 10,50

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) 


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)# combination of variable ,numbers and math

