
"""
==========================================================
Dictionary Comprehension (Beginner Friendly)
==========================================================

Dictionary Comprehension ka use ek dictionary ko short aur clean
way me banane ke liye hota hai. Ye bilkul List Comprehension ki
tarah hi hota hai, bas isme key:value pair bante hain.

Syntax:
{key: value for item in iterable}

==========================================================
Example 1 : Number -> Square
==========================================================
"""

square = {i: i * i for i in range(1, 6)}
print("Example 1:", square)

"""
Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}









==========================================================
Example 2 : Number -> Cube
==========================================================
"""

cube = {i: i ** 3 for i in range(1, 6)}
print("Example 2:", cube)

"""
Output:
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}










==========================================================
Example 3 : String Length
==========================================================
"""

names = ["Shivam", "Rahul", "Aman"]

length = {name: len(name) for name in names}

print("Example 3:", length)

"""
Output:
{
'Shivam':6,
'Rahul':5,
'Aman':4
}











==========================================================
Example 4 : Uppercase Values
==========================================================
"""

names = ["shivam", "rahul", "aman"]

upper = {name: name.upper() for name in names}

print("Example 4:", upper)

"""
Output:
{
'shivam':'SHIVAM',
'rahul':'RAHUL',
'aman':'AMAN'
}









==========================================================
Example 5 : Even Numbers
==========================================================
"""

even = {i: i * i for i in range(1, 11) if i % 2 == 0}

print("Example 5:", even)













"""
==========================================================
Example 6 : Odd Numbers
==========================================================
"""

odd = {i: i * i for i in range(1, 11) if i % 2 != 0}

print("Example 6:", odd)









"""
==========================================================
Example 7 : If Else
==========================================================
"""

result = {
    i: "Even" if i % 2 == 0 else "Odd"
    for i in range(1, 6)
}

print("Example 7:", result)

"""
Output:
{
1:'Odd',
2:'Even',
3:'Odd',
4:'Even',
5:'Odd'
}










==========================================================
Example 8 : Character Frequency
==========================================================
"""

word = "python"

frequency = {char: word.count(char) for char in word}

print("Example 8:", frequency)









"""
==========================================================
Example 9 : Swap Key & Value
==========================================================
"""

student = {
    "name": "Shivam",
    "age": 21
}

swap = {value: key for key, value in student.items()}

print("Example 9:", swap)

"""
Output:
{
'Shivam':'name',
21:'age'
}









==========================================================
Example 10 : Celsius to Fahrenheit
==========================================================
"""

temperature = {
    "Delhi": 30,
    "Mumbai": 35,
    "Punjab": 28
}

fahrenheit = {
    city: (temp * 9/5) + 32
    for city, temp in temperature.items()
}

print("Example 10:", fahrenheit)










"""
==========================================================
Dry Run
==========================================================

Code:

square = {i:i*i for i in range(1,4)}

Python Internally:

square = {}

i = 1
square[1] = 1

i = 2
square[2] = 4

i = 3
square[3] = 9

Final Output:
{
1:1,
2:4,
3:9
}

==========================================================
Formula
==========================================================

Normal Way

result = {}

for item in iterable:
    result[key] = value

↓

Dictionary Comprehension

result = {
    key:value
    for item in iterable
}

With Condition

result = {
    key:value
    for item in iterable
    if condition
}

With If Else

result = {
    key: value1 if condition else value2
    for item in iterable
}

==========================================================
Difference

List Comprehension
------------------
[expression for item in iterable]

Dictionary Comprehension
------------------------
{key:value for item in iterable}

List -> Stores only values
Dictionary -> Stores key:value pairs

==========================================================
Shortcut Rule

Simple:
{key:value for item in iterable}

With if:
{key:value for item in iterable if condition}

With if-else:
{key:value1 if condition else value2 for item in iterable}

==========================================================
"""