from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()    			# for deleting the contents of the file

print "Now I'm going to ask you for three lines."

# take input contents for the above file

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

# reopening the file to see whether we have inserted correctly or not.

tar = open(filename,'r')

print "the above file is modified as: "

print tar.read()

tar.close()
# even without truncate the file is being replaced.
# w is for write mode modes - r for read , w for write ,a for append