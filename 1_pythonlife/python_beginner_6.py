'''
Strings: Collection of characters

String Declaration:
- Single Quotes ('') e.g: a='py'
- Double Quotes ('') e.g: b="py"
- Triple Quotes ('') e.g: c="""py"""

String Methods:
- lower()
- upper()
- endswith() -  returns boolean
- startswith() - returns boolean
- replace(old, new)
- split() - Splits string to list
- count() - count number of chars/words
- rstrip() - trim space on Right side of string
- lstrip() - trim space on Left side of string
- strip() - trim space in a string
- removeprefix() - removing set of chars from prefix
- removesuffix() - removing set of chars from suffix
- find() - Used to search for a word or letter in a string - If found → it gives the position number (index) where it starts - If not found → it gives -1 (no error).
- Index() - Works the same way as find(), but with one difference - If not found → it gives an error, not -1.
'''

subject = "Maths"
print(subject.lower())
print(subject.upper())

city = 'Hyderabad City'
print(city.endswith("city")) # false due to case sensitivity

print(city.replace("Hyderabad", "Visakhapatnam")) #Visakhapatnam City

print(city.index("City")) # 10 or Value Error  not -1
print(city.find("Vizag")) # -1
print(city.count("a")) # 2
print(len(city)) #14

# Converting string to list

print(city.split()) # ['Hyderabad', 'City']