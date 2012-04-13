cars = 100 # declaration of number variable
space_in_car = 4.0 # floating point variable declaration
drivers = 30 
passengers = 90
cars_not_driven = cars - drivers # no. of cars vacant
cars_driven = drivers # those can taken out
carpool_capacity = cars_driven *space_in_car
average_passengers_per_car = passengers/cars_driven

print "There are ",cars,"cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."