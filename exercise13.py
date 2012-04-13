from sys import argv

script, first, second, third, four = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "your fourth variable is:",four
print first,;print second,;print third,;print four

name=raw_input( "enter %s"%first)
clas =raw_input("enter %r"%second)
rol =raw_input("enter %r"%third)
row =raw_input("enter %s"%four)

print """ hi %s , you are of %s with roll number %s and you sit in row %s """%(name,clas,rol,row)
