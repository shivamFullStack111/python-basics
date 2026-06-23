# =====================================================
# PYTHON LOOPS CHEATSHEET
# =====================================================

# What is a Loop?
# A loop is used to execute a block of code multiple times.

# Types of Loops:
# 1. for loop
# 2. while loop

# =====================================================
# FOR LOOP
# =====================================================

# Loop through a sequence

for i in [1, 2, 3, 4, 5]:
    print(i)

# Output:
# 1 2 3 4 5


# =====================================================
# RANGE FUNCTION
# =====================================================

# range(stop)

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4


# range(start, stop)

for i in range(1, 6):
    print(i)

# Output:
# 1 2 3 4 5


# range(start, stop, step)

for i in range(0, 11, 2):
    print(i)

# Output:
# 0 2 4 6 8 10


# Reverse Loop

for i in range(10, 0, -1):
    print(i)

# Output:
# 10 9 8 7 6 5 4 3 2 1


# =====================================================
# LOOPING THROUGH STRING
# =====================================================

name = "Shivam"

for char in name:
    print(char)


# =====================================================
# LOOPING THROUGH LIST
# =====================================================

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# =====================================================
# ENUMERATE
# =====================================================

fruits = ["Apple", "Banana", "Mango"]

for index, value in enumerate(fruits):
    print(index, value)

# Output:
# 0 Apple
# 1 Banana
# 2 Mango


# =====================================================
# WHILE LOOP
# =====================================================

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1 2 3 4 5


# Infinite Loop

# while True:
#     print("Running Forever")


# =====================================================
# BREAK
# =====================================================

for i in range(10):

    if i == 5:
        break

    print(i)

# Output:
# 0 1 2 3 4


# =====================================================
# CONTINUE
# =====================================================

for i in range(5):

    if i == 2:
        continue

    print(i)

# Output:
# 0 1 3 4


# =====================================================
# PASS
# =====================================================

for i in range(5):
    pass

print("Program Continues")


# =====================================================
# FOR ELSE
# =====================================================

for i in range(5):
    print(i)
else:
    print("Loop Completed")

# else runs when loop finishes normally


# =====================================================
# NESTED LOOPS
# =====================================================

for i in range(3):

    for j in range(3):
        print(i, j)

# Output:
# 0 0
# 0 1
# 0 2
# 1 0
# ...


# =====================================================
# LIST COMPREHENSION
# =====================================================

squares = [x * x for x in range(5)]

print(squares)

# Output:
# [0, 1, 4, 9, 16]


# With Condition

evens = [x for x in range(10) if x % 2 == 0]

print(evens)

# Output:
# [0, 2, 4, 6, 8]


# =====================================================
# COMMON INTERVIEW QUESTIONS
# =====================================================

# Difference Between for and while?

# for:
# Used when number of iterations is known

for i in range(5):
    print(i)

# while:
# Used when number of iterations is unknown

count = 0

while count < 5:
    print(count)
    count += 1


# =====================================================
# LOOP CONTROL STATEMENTS
# =====================================================

# break
# Stops loop immediately

# continue
# Skips current iteration

# pass
# Does nothing


# =====================================================
# TIME COMPLEXITY
# =====================================================

# Single Loop       -> O(n)

# Nested Loop       -> O(n²)

# Triple Loop       -> O(n³)


# =====================================================
# SUMMARY
# =====================================================

# for loop
# while loop
# range()
# enumerate()
# break
# continue
# pass
# for-else
# nested loops
# list comprehension

# =====================================================
# END OF LOOPS CHEATSHEET
# =====================================================