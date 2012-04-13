formatter ="%r%r%r%r"
print formatter %(1,2,3,4) # repr being used to be replaced by numbers
print formatter %("one","two","three","four") # strings being replaced by repr
print formatter %(True,False,False,True) # boolean values 
print formatter %(formatter,formatter,formatter,formatter) # expression 
print formatter %("I had this thing.","that you could type up right.","But it didn't sing.","so I said goodnight.")
# strings being printed .
# all these strings are printed in single quotes except for "But it didn't sing." because it contains "  '  "
which is an escape sequence hence to make the difference the interpreter interprets the code in the following way.
