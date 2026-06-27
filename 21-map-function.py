# ==========================================================
# Example 1 : Normal Function 
# ==========================================================



lst = [6,4,2,7,9,1,2,0]


def square(a):
    return a*a

result = map( square,lst )

print(list(result))













# ==========================================================
# Example 2 : Square of Numbers
# ==========================================================

numbers = [1, 2, 3, 4, 5]

square = list(map(lambda x: x * x, numbers))

print(square)

# Output:
# [1, 4, 9, 16, 25]










# ==========================================================
# Example 3 : Convert to Uppercase
# ==========================================================

names = ["shivam", "rahul", "aman"]

upper = list(map(lambda name: name.upper(), names))

print(upper)

# Output:
# ['SHIVAM', 'RAHUL', 'AMAN']












# ==========================================================
# Example 4 : Multiple Lists
# ==========================================================

list1 = [1, 2, 3]
list2 = [10, 20, 30]

result = list(map(lambda x, y: x + y, list1, list2))

print(result)

# Output:
# [11, 22, 33]












"""
==========================================================
Map Function
==========================================================

map() ka use kisi function ko iterable (List, Tuple, etc.)
ke har element par apply karne ke liye hota hai.

Syntax:
map(function, iterable)

Ye ek map object return karta hai, isliye output dekhne ke liye
usually list() use karte hain.

Example:

numbers = [1,2,3]

result = list(map(lambda x: x*x, numbers))

Python Internally Yehi Karta Hai:

result = []

for x in numbers:
    result.append(x*x)

Output:
[1,4,9]

Multiple Lists:

list(map(lambda x,y: x+y, list1, list2))

Yaha map() dono lists ke same index wale elements
ko function me pass karta hai.

Use Cases:
✔ Har element par same operation perform karna.
✔ Lambda functions ke saath.
✔ Data conversion (int, str, float).
✔ Strings ko uppercase/lowercase banana.

Shortcut:
for loop -> Jab logic bada ho.
map() -> Jab har element par same operation lagana ho.
==========================================================
"""