from sys import exit
def meet():
	print " Fix appointment"
	next =raw_input("> ")
	if next == "True":
		print "your appointment is fixed"
	elif next == "False":
		print " Appointment is not fixed"
	else:
		print "Try again"
	intr()
	exit(0)
def intr():
	print "Will you attend Interview?"
	next = raw_input("> ")
	if '1' in next:
		print " GoodLuck"
	elif '0' in next:
		print "Betterluck"
	else:
		print "you can\'t take decisions"
		
		
	
	
def apply():
	print "Applied for any company?"
	next = raw_input("> ")
	if "applied" in next:
		meet()
	elif "neverapply" in next:
		intr()
	else:
		print " You are idiot"

apply()	
	
	