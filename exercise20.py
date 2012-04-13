from sys import argv #import of system statement

script, input_file = argv # unpacking 

def print_all(f): #definition
    print f.read() # read the content of the file and print d same

def rewind(f): # redefining seek function
    f.seek(0) # set the cursor position to the starting of the file


def print_a_line(line_count, f): 
    print line_count, f.readline()#  prints the line number and the line  

current_file = open(input_file) #opening a file to read the contents

print "First let's print the whole file:\n"

print_all(current_file) # f=current_file , print_All(f) prints the content of the file

print "Now let's rewind, kind of like a tape."

rewind(current_file) # move to the starting of the file

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) # prints the current line number and the contents of the line

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)