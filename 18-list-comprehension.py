# ==========================================================
# List Comprehension Examples
# ==========================================================

# ----------------------------------------------------------
# Example 1 : Create a List
# ----------------------------------------------------------

numbers = [i for i in range(1, 6)]
print("Example 1:", numbers)

# Output:
# [1, 2, 3, 4, 5]


# ----------------------------------------------------------
# Example 2 : Square of Numbers
# ----------------------------------------------------------

square = [i * i for i in range(1, 6)]
print("Example 2:", square)

# Output:
# [1, 4, 9, 16, 25]


# ----------------------------------------------------------
# Example 3 : Cube of Numbers
# ----------------------------------------------------------

cube = [i ** 3 for i in range(1, 6)]
print("Example 3:", cube)

# Output:
# [1, 8, 27, 64, 125]


# ----------------------------------------------------------
# Example 4 : Convert Strings to Uppercase
# ----------------------------------------------------------

names = ["shivam", "rahul", "aman"]

upper_names = [name.upper() for name in names]

print("Example 4:", upper_names)

# Output:
# ['SHIVAM', 'RAHUL', 'AMAN']


# ----------------------------------------------------------
# Example 5 : Even Numbers
# ----------------------------------------------------------

even = [i for i in range(11) if i % 2 == 0]

print("Example 5:", even)

# Output:
# [0, 2, 4, 6, 8, 10]


# ----------------------------------------------------------
# Example 6 : Odd Numbers
# ----------------------------------------------------------

odd = [i for i in range(11) if i % 2 != 0]

print("Example 6:", odd)

# Output:
# [1, 3, 5, 7, 9]


# ----------------------------------------------------------
# Example 7 : Numbers Greater Than 5
# ----------------------------------------------------------

numbers = [2, 5, 8, 10, 1, 15]

greater = [num for num in numbers if num > 5]

print("Example 7:", greater)

# Output:
# [8, 10, 15]


# ----------------------------------------------------------
# Example 8 : If Else in List Comprehension
# ----------------------------------------------------------

result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]

print("Example 8:", result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ----------------------------------------------------------
# Example 9 : First Letter of Each Word
# ----------------------------------------------------------

names = ["Shivam", "Rahul", "Aman"]

first_letters = [name[0] for name in names]

print("Example 9:", first_letters)

# Output:
# ['S', 'R', 'A']


# ----------------------------------------------------------
# Example 10 : Length of Each Word
# ----------------------------------------------------------

words = ["Python", "Java", "JavaScript"]

length = [len(word) for word in words]

print("Example 10:", length)

# Output:
# [6, 4, 10]