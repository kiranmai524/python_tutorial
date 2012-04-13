# for opening a file from directory by reading command line argument.

print "Type the filename again:" #request the input
file_again = raw_input(" ")   #input from console 

txt_again = open(file_again) # open file

print txt_again.read()  # again read the file

txt.close()
