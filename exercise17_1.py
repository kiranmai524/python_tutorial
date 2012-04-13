from sys import argv
from os.path import exists
import keyword 

script, from_file, to_file = argv

print keyword.kwlist
print "Copying from %s to %s" % (from_file, to_file)

print  we could do these two on one line too, how?
input = open(from_file)
#indata = input.read()

output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()

#output.close() is necessary where input.close() is an option . when we open a file in write mode we need to close it to mark that 
# the file will be listening which needs to be closed so as to save the changes and let it open for further use
# 3 open(to_file,'w').write(open(from_file).read())
#5 type is an alternative for cat 