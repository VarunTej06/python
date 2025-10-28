'''
Variable: Which Stores a value or address of a value

Syntax: variable_name = Value_of_variable

math_score = 98
variable: math_score
value: 98

use id() to know the memory address of variable e.g: 213001 (memory location of variable)

Rules:
 - Don't start with digit or symbols
 - Starting letter could be either an alphabet or underscore
 - variables are case sensitive unlike HTML

'''

a = 10
print(a)

b,c,d = 1,3,4
print(b,c,d)  # Output: 1 3 4

e = 1,2,3
print(e)      # Output: (1, 2, 3) Will pack the values and show as a tuple

f=g=h=22
print(f,g,h)  # Output: 22 22 22

_total = 38
print(_total) # Output: 38
print(id(_total))  # Output: 140735874926664


# Case Sensitive variables
pythonversion = 3.12
PYTHONVERSION = 3.9

print(pythonversion)  # Output: 3.12
print(PYTHONVERSION)  # Output: 3.9