'''
Jumping Statements: Pass, Break, Continue

Pass: If you want to write the statements inside the if condition later at some point of time, you can use pass to avoid the indentation errors
Break: It breaks the iteration when a condition is met and execution exists form loop
Continue: It skips the current iteration of the loop when a condition is met and continues the rest of the iterations.
'''

if True:
    pass

for i in "pythonlife":
    if i=='l':
        break
    print(i)

# Output:
'''
p
y
t
h
o
n
'''

for i in "pythonlife":
    if i=='l':
        continue
    print(i)

# Output: skips iteration of for loop when i value is l. No l in the output
'''
p
y
t
h
o
n
i
f
e
'''
