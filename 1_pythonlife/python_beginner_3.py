'''
                                            Data Types
Datatype means type of value we are assigning to a variable

Datatypes in Python:
- Int, float, Boolean, String, Complex
- List [], Tuple (), Set {}, Dictionary {}
- Frozenset, None

'''

# Integers

# a = 1
# b = -2
# print(type(a), type(b))     # Output: <class 'int'> <class 'int'>

# Float

c = 3.12

# Boolean
passed_10th = True # True is 1
passed_12th = False # False is 0
print(type(passed_10th), type(passed_12th))     # Output: <class 'bool'> <class 'bool'>


print(passed_10th)

# String
subject = 'Python' 
school = "BVK"

# Complex
vector = 1+3j   # 1 is real number where as 3j is imaginary number
print(type(vector))       # Output: <class 'complex'>


'''
Type conversion - changing the data type of a value from one type to another
int()
float()
str()
bool()
Types - Implicit and Explicit Type Conversions
'''

k = 2
print(float(k))   # Output: 2.0

h = 5.4
print(int(h))    # output: 5

# Implicit Type Conversion 

'''
Implicit conversion, Python automatically converts one data type to another when it’s required during expression evaluation — without any action from the programmer.

Key points:

Done automatically by the Python interpreter.

No data loss or risk of errors.

Usually happens when mixing different numeric types (e.g., int with float).

'''

a = 5       # int
b = 2.0     # float

result = a + b  # int + float
print(result)   # Output: 7.0
print(type(result))  # Output: <class 'float'>


# Explicit Type Conversion

'''
In explicit conversion, the programmer manually converts the data type using Python’s built-in functions.

Common conversion functions:

int() → converts to integer

float() → converts to float

str() → converts to string

list(), tuple(), set(), etc. → convert between collections
'''

x = "10"
y = int(x)   # convert string to int
z = float(y) # convert int to float

print(y, type(y))  # Output: 10 <class 'int'>
print(z, type(z))  # Output: 10.0 <class 'float'>
