file = raw_input("enter the file name")
file1 = open(file,'w')
formatter ="%r\n%r"
file1.write(formatter %(raw_input("line1"),raw_input("line2")))
#file1.write(check)
file1.close()
