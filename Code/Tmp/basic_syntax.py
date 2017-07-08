import sys

## Comment: a hash sign (#)
print "Hello, Basic syntax!"


## Lines and Identation
if True:
    print "Answer";
    print "True"
else:
    print "Answer"
    print "Fasle"


## Multi-Line Statements
# Using line continuation character '\'
total = "iten_one " + \
        "item_two " + \
        "item_three "
print 'string =', total

# Contained [], {}, () do not need '\'
days = [
    'Monday' ,
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday'
]
print "Array =", days


## Quotation
# Accepts single ('), double (") and triple (''' or """)
word = 'word'
sentence = "This is a sentence"
paragraph = """This is a paragraph. It is made up of multiple lines and sentence."""
print word
print sentence
print paragraph


## Waiting for the User
#raw_input("\n\nPress the enter key to exit")


## Multiple statments on a Single Line
print "\nUsing lib: "
x = 'foo'; sys.stdout.write(x + '\n')


## Multiple Statement Groups as Suites
# using a colon (:)
a = 4
if a > 8:
    suite = 10
elif a >5:
    suite = 6
else:
    suite = 0;
print '\nsuite:', suite

##