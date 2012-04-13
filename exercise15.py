from sys import argv # importing arguments from the command prompt

script, filename = argv # unpacking of the variables

txt = open(filename) # opening a file syntax open(name[,mode

print "Here's your file %r:" % filename # printing the file name
print txt.read()      # printing the contents of the file using  read() method for files

txt.close()  # to close the file opened

print "Type the filename again:" #request the input
file_again = raw_input(" ")   #input from console 

txt_again = open(file_again) # open file

print txt_again.read()  # again read the file

txt.close()

#close() is used for closing a file opened with the open method. it is a good practise to close a file so that it is not locked for the further access.
