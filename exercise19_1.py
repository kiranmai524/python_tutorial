def method(arg1,arg2,arg3):
    print arg1+arg2+arg3
def method1():
  print "dead block"
 
method(1,2,3) # numbers

a=2;b=3;c=5 # numbers to variables 
method(a,b,c)
#math as arguments
method(1+2,2+3,3+4)
# math and variables combined
method(a+3,b+1,c-2)
#strings as input
method('hai','world','welcome')
#strings assigned to variables
str='hai';str1='world';str2='welcome'
method(str,str1,str2)
#strings and variables
method('this','is',str1)
#float
method(2.0,a,3)
#variables
method1()
