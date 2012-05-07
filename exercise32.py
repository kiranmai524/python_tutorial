the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges','pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#the first kind of for loop goes through a list
for number in the_count:
	print "This is count %d" %number
	
#same as above
for fruit in fruits:
	print "A fruit of type %s" %fruit
	
#also we can go through mixed lists too
#notice we have to use %r since we don't know  what's in it
for i in change:
	print "I got %r" %i
#we can also build lists, first start with an empty one
elements= []

# then use range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." %i
	#append is a function that  lists understand
	elements.append(i)
	
#now we can  print them too

for i in elements:
	print "The elements was %d" %i
	
#extra credit
for i in range(1,3):
	print "The elements are: %d" %i

for i in range(2,4):
	print "The element: %d" %i
	
a = ['kiran', 'sri', 'friends']
for j in a:
	print "The names are %s " %j
	print "Lengths are %d " %(len(j))
	print "Names and its length: %s %d " %(j, len(j))

for j in range(len(a)):
	print j,a[j]