tabby_cat = "\tI'm tabbed in." # horizontal tab
persian_cat = "I'm split\non a line." # a new line 
backslash_cat = "I'm \\ a \\ cat."# first in the double back-slash is escape sequence and the other retains its meaning


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

sample = 'I\'d say that it works' # here single quotes is used to represent the string which has an ' qoute before the completion of the string to mark the difference an escape sequence (back slash \)
                                  # is used
sample1=" 2\b3" # used as a backspace sequence
sample2="hi word\rld" # replace sequence
print sample
print sample1
print sample2								  
print 'I am 6\'2" tall.' # here a back slash before ' implies the escape sequence
print "I am 6'2\" tall."  # here a back slash before " implies the escape sequence