'''
Control Statements

Conditional Statements / Decision Making Statements: if, else, elif, nested if
Looping Statements / Iterative statements: for, while, nested loops
Jumping Statements: pass, break, continue

'''

'''
Decision Making Statements:

Conditional statements are used when you want your program to make a choice or decide which block of code to execute based on a condition.

When to Use:

Use conditional statements when:

You want to execute different code depending on some condition.

You need your program to take decisions.

Syntax:

if condition:
    statements
else:
    statements
'''

age = 38

# If Else

if age>18 or age==18:
    print("Eligible to Vote")
else:
    print("Not eligible to vote")

# Nested If Else

if age<35:
    print("Eligible for government exam")
    if age==35:
        print("This is your attempt")
else:
    print("Not eligible for appearing the exam")


'''
Iterative statements: 

Iterative statements (loops) are used when you want to repeat a block of code multiple times — either a fixed number of times or until a condition is met.

When to Use:

Use iterative statements when:

You want to perform repetitive tasks (e.g., processing items in a list).

You don't want to write the same code many times manually.

'''

a = [1,2,3,4,5]

for i in a:
    print(i) # prints 1 to 5 in output

for i in range(5):
    print("Hello, world!") # prints "Hello, world!" five times

for i in range(0,10,2):   # since we gave 2 in the range function it skips one value, if you gave 3 - it skips 2 values - Output: (0,3,6,9)
    print(i)  # Output: 0,2,4,6,8

b = "python language"
for k in b:
    print(k) # Prints all the characters in b including space

m = 10
while m<20:
    print("m value is less than 20", m)
    m+=1       # Prints until m value is less than 20
# Output: 
'''
m value is less than 20 10
m value is less than 20 11
m value is less than 20 12
m value is less than 20 13
m value is less than 20 14
m value is less than 20 15
m value is less than 20 16
m value is less than 20 17
m value is less than 20 18
m value is less than 20 19
'''

# Nested For loop: So, the inner loop executes fully for every single iteration of the outer loop.

for i in range(3):          # Outer loop
    for j in range(2):      # Inner loop
        print(f"i = {i}, j = {j}")

'''
Explanation:
The outer loop runs 3 times (i = 0, 1, 2).
For each iteration of the outer loop, the inner loop runs 2 times (j = 0, 1).
Output:

i = 0, j = 0
i = 0, j = 1
i = 1, j = 0
i = 1, j = 1
i = 2, j = 0
i = 2, j = 1
'''

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # move to the next line

'''
Explanation:

The outer loop controls the number of rows.

The inner loop controls how many * are printed in each row.
Output: 
* 
* * 
* * * 
* * * * 
* * * * * 

'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

'''
Explanation:

The outer loop iterates over each row (list).

The inner loop iterates over each element in that row.
Output:
1 2 3 
4 5 6 
7 8 9

'''