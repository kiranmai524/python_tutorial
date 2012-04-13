x= "there are %d types of people. " % 10 # d is the specifier used for integer values
binary = 'binary' # string declaration
do_not = "don't" # here don't is declared using double quotes as a single quote is am escape sequence and throws an error
y = "Those who know %s and those %s." %(binary,do_not) # used the strings in another string with specifiers
  # here for 'y' strings binary and do_not are given as inputs which are priorly represented by specifiers
print x; print y;
print " I said: %r." %x # regular expression is replaced by string 
print " I also said: '%s'." %y

hilarious = False # binary variable declaration
joke_evalution = "Isn't that joke so funny?! %r" 
  # %s %d %f and others can be used for a single data type whereas , when we give a %r it can be replaced by any data variable
  
print joke_evalution %hilarious # %r replaced by a string
w = " This is the left side of .. "
e= " a string with right side."
print w+e # concatenation of two strings


# in the above program a a string is put in a string in 5 places. as in x the value is replaced by a number and other specifiers are either %r or %s
# %s is definitely for a string and %r is a global specifier and in all the instances above it is replaced by a string only
# the last statement is concatenation of two strings . over ridding of the + operator is common feature.