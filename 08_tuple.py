# =====================================================
# PYTHON TUPLE CHEATSHEET
# =====================================================

# What is a Tuple?
# - Ordered collection
# - Immutable (cannot be changed)
# - Allows duplicate values
# - Faster than lists
# - Uses parentheses ()

my_tuple = (10, 20, 30, 40)

# =====================================================
# CREATING TUPLES
# =====================================================

numbers = (1, 2, 3, 4)

mixed = (1, "Shivam", True, 99.5)

single = (10,)      # Comma is required

empty = ()


# =====================================================
# ACCESSING ELEMENTS
# =====================================================

numbers = (10, 20, 30, 40)

print(numbers[0])     # First element

print(numbers[1])     # Second element

print(numbers[-1])    # Last element

print(numbers[-2])    # Second last element


# =====================================================
# SLICING
# =====================================================

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

print(numbers[:3])

print(numbers[2:])

print(numbers[::-1])   # Reverse tuple


# =====================================================
# LOOPING THROUGH TUPLE
# =====================================================

numbers = (10, 20, 30)

for item in numbers:
    print(item)


# =====================================================
# CHECKING MEMBERSHIP
# =====================================================

numbers = (10, 20, 30)

print(20 in numbers)

print(50 not in numbers)


# =====================================================
# TUPLE METHODS
# =====================================================

numbers = (10, 20, 30, 20, 40)

numbers.count(20)
# Count occurrences

numbers.index(30)
# Find index


# =====================================================
# TUPLE UNPACKING
# =====================================================

person = ("Shivam", 22, "Jalandhar")

name, age, city = person

print(name)
print(age)
print(city)


# =====================================================
# PACKING
# =====================================================

data = "Shivam", 22, "India"

print(type(data))


# =====================================================
# CONCATENATION
# =====================================================

a = (1, 2)

b = (3, 4)

c = a + b

print(c)

# Output:
# (1, 2, 3, 4)


# =====================================================
# REPETITION
# =====================================================

numbers = (1, 2)

print(numbers * 3)

# Output:
# (1, 2, 1, 2, 1, 2)


# =====================================================
# CONVERTING TUPLE
# =====================================================

# Tuple -> List

my_tuple = (1, 2, 3)

my_list = list(my_tuple)

print(my_list)


# List -> Tuple

my_list = [1, 2, 3]

my_tuple = tuple(my_list)

print(my_tuple)


# =====================================================
# USEFUL BUILT-IN FUNCTIONS
# =====================================================

numbers = (10, 20, 30, 40)

len(numbers)
# Length

max(numbers)
# Largest value

min(numbers)
# Smallest value

sum(numbers)
# Sum of values

sorted(numbers)
# Returns sorted list


# =====================================================
# IMMUTABILITY
# =====================================================

numbers = (10, 20, 30)

# numbers[0] = 100
# ERROR:
# TypeError: 'tuple' object does not support item assignment


# =====================================================
# NESTED TUPLE
# =====================================================

data = (
    (1, 2),
    (3, 4),
    (5, 6)
)

print(data[0])

print(data[1][1])


# =====================================================
# TUPLE VS LIST
# =====================================================

# Tuple
# Immutable
# Faster
# Uses ()

# List
# Mutable
# Slower
# Uses []


# =====================================================
# COMMON METHODS SUMMARY
# =====================================================

# count() -> Count occurrences
# index() -> Find index


# =====================================================
# TIME COMPLEXITY
# =====================================================

# Access      -> O(1)
# Search      -> O(n)
# index()     -> O(n)
# count()     -> O(n)

# =====================================================
# END OF TUPLE CHEATSHEET
# =====================================================