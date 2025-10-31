'''
List: []
- Mutable data type - Can be modified even after assigning data to list variable
- stores different types of elements
- allows duplicates
- allow indexing

Methods:
append - Add object into the list
extend - Extends list with multiple objects
count - count objects inside list
insert
pop
remove - remove element from list
index
'''

v=[1, 22, 8.6, 5, 'Kiran']
print(v)
print(v[4])
print(v[-1])
# Output:
# [1, 22, 8.6, 5, 'Kiran']
# Kiran
# Kiran

print(v[0:4:2]) # Output: [Start, Stop, Skip] - Output: [1, 8.6]
'''
start = 0 → start from index 0 (the first element)

stop = 4 → stop before index 4 (so, up to index 3)

step = 2 → take out every 2nd element
'''
v.append("Python")
print(v) # [1, 22, 8.6, 5, 'Kiran', 'Python']

v.extend([5, 25,7.9,'Raj'])
print(v) # [1, 22, 8.6, 5, 'Kiran', 'Python', 5, 25, 7.9, 'Raj']

print(v.count(5)) # 2

v.remove(22)
print(v) # [1, 8.6, 5, 'Kiran', 'Python', 5, 25, 7.9, 'Raj']