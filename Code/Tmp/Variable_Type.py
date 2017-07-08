
## Assigning Values to Varuables
counter = 100   # An integer assignment
miles = 1000.0  # A floating point
name = "Kenny"  # A string

print counter
print miles
print name


## Multiple Assignment
a = b = c = 1
a, b, c = 1, 2, "Kenny"
print a, b, c


## Standard Data Types
# Python has five standard data types:
# 1. Numbers
# 2. String
# 3. List
# 4. Tuples
# 5. Dictionary

## Python Numbers
print "===== Number Type ====="
var1 = 1
var2 = 10
del var1

var_a = var_b = 1
del var_a, var_b

print var2

var_int1 = 10
var_int2 = -100
var_int3 = 0x69
var_int4 = -0x50

var_long1 = 234234234L
var_long2 = -2134242L
var_long3 = 0xDAEDAEL

var_float1 = 10.0
var_float2 = -15.23
#var_float3 = 32.2+e12 #error
#var_float4 = 30-E10 #error


## Python Strings
var_str = "Hello word!"

print "===== String Type ====="
print var_str # Prints complete string
print var_str[0] # Prints first character of the string
print var_str[2: 8] # Prints characters starting from 3rd to 7th
print var_str[2: ]  # Prints string starting from 3 character
print var_str * 2   # Prints string two times
print var_str + " Test!" # Prints concatenated string


## Python Lists
# using square brakets ([]) and accessed ([] and [:])
list = ['abcd', 100, 2.33, 'asdf', 23.3]
tinyList = [1234, 'asdf']

print "===== Lists Type ====="
print list # Prints complete list
print list[0] # Prints first element of the list
print list[1: 3] # Prints elements starting from 2nd to 4th
print list[2: ] # Prints elements starting from 3rd element
print tinyList * 2 # Prints list two times
print list + tinyList # Prints concatenated lists


## Python tuples
# using parentheses (()) and CANNOT be updated.
tuple = ('abcd', 100, 2.33, 'asdf', 23.3)
tinyTuple = (1234, 'asdf')

print "===== Tuples Type ====="
print tuple # Prints complete list
print tuple[0] # Prints first element of the list
print tuple[1: 3] # Prints elements starting from 2nd to 4th
print tuple[2: ] # Prints elemets starting from 3rd element
print tuple * 2 # Prints list two times
print tuple + tinyTuple # Prints concatenated lists


## Python Dictionary
# using curly braces ({}) and accessed ([])
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinyDict = {
    'name': 'john',
    'code': '6745',
    'dept': 'sales'
}

print "===== Dictionary Type ====="
print dict['one'] # Prints value
print dict[2] # Prints value
print tinyDict # Prints complete dictionary
print dict.keys() # Prints all the keys
print tinyDict.keys() # Prints all the keys
print tinyDict.values() # Prints all the values


## Data type conversion
print "===== Type conversion Type ====="

# converts to (int) integer int(x)
print "=== Converts to int ==="
con_int = '12'
con_int = int(con_int);
print con_int + 4

# converts to (long) integer long(x)
print "=== Converts to long ==="
con_long = '123L'
con_long = long(con_long)
print con_long + 122

# converts to (float) float float(x)
print "=== Converts to float ==="
con_float = '123.2'
con_float = float(con_float)
print con_float + 123

# Create a complex number complex(real, imag)
print "=== Create a complex number ==="
con_complex = complex(2 , 3)
print con_complex

# converts to string
print "=== Converts to string ==="
con_string = str(1234.0)
print con_string + '233'

# converts to list
print "=== Converts to list === [error]"
# aTuple = ('asdsdf', 'sdf');
# con_list = list(aTuple)
# print con_list