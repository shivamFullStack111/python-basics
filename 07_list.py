# =====================================================
# PYTHON LIST CHEATSHEET
# =====================================================

# What is a List?
# - Ordered collection
# - Mutable (can be changed)
# - Allows duplicate values
# - Can store different data types

my_list = [10, 20, 30, 40]

# =====================================================
# ACCESSING ELEMENTS
# =====================================================

my_list[0]      # First element
my_list[1]      # Second element
my_list[-1]     # Last element
my_list[-2]     # Second last element

# Slicing

my_list[0:2]    # [10, 20]
my_list[:3]     # [10, 20, 30]
my_list[1:]     # [20, 30, 40]
my_list[::-1]   # Reverse list


# =====================================================
# ADDING ELEMENTS
# =====================================================

my_list.append(50)
# Adds one item at end

my_list.insert(1, 15)
# Insert at specific index

my_list.extend([60, 70, 80])
# Add multiple items


# =====================================================
# REMOVING ELEMENTS
# =====================================================

my_list.remove(20)
# Remove first occurrence of value

my_list.pop()
# Remove last element

my_list.pop(0)
# Remove element at index

del my_list[1]
# Delete by index

my_list.clear()
# Remove all elements


# =====================================================
# SEARCHING
# =====================================================

my_list.index(30)
# Returns index of value

my_list.count(20)
# Counts occurrences


# =====================================================
# SORTING
# =====================================================

numbers = [5, 1, 8, 3]

numbers.sort()
# Ascending order

numbers.sort(reverse=True)
# Descending order

sorted(numbers)
# Returns new sorted list


# =====================================================
# REVERSING
# =====================================================

numbers.reverse()
# Reverse original list

numbers[::-1]
# Returns reversed copy


# =====================================================
# COPYING
# =====================================================

copy_list = numbers.copy()

copy_list = numbers[:]

copy_list = list(numbers)


# =====================================================
# LIST OPERATORS
# =====================================================

a = [1, 2]
b = [3, 4]

a + b
# [1, 2, 3, 4]

a * 3
# [1, 2, 1, 2, 1, 2]


# =====================================================
# CHECKING MEMBERSHIP
# =====================================================

10 in my_list
# True if exists

10 not in my_list
# True if does not exist


# =====================================================
# USEFUL BUILT-IN FUNCTIONS
# =====================================================

len(my_list)
# Number of elements

max(my_list)
# Largest value

min(my_list)
# Smallest value

sum(my_list)
# Total sum

sorted(my_list)
# Sorted copy


# =====================================================
# ITERATING THROUGH LIST
# =====================================================

for item in my_list:
    print(item)

for index, value in enumerate(my_list):
    print(index, value)


# =====================================================
# LIST COMPREHENSION
# =====================================================

squares = [x*x for x in range(5)]
# [0, 1, 4, 9, 16]

even_numbers = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]


# =====================================================
# NESTED LIST
# =====================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix[0]
# [1, 2, 3]

matrix[1][2]
# 6


# =====================================================
# COMMON LIST METHODS SUMMARY
# =====================================================

# append()      -> Add one item
# insert()      -> Insert at index
# extend()      -> Add multiple items
# remove()      -> Remove by value
# pop()         -> Remove by index
# clear()       -> Remove all items
# index()       -> Find index
# count()       -> Count occurrences
# sort()        -> Sort list
# reverse()     -> Reverse list
# copy()        -> Copy list

# =====================================================
# TIME COMPLEXITY (INTERVIEW)
# =====================================================

# append()      -> O(1)
# pop()         -> O(1) (last element)
# insert()      -> O(n)
# remove()      -> O(n)
# search (in)   -> O(n)
# index()       -> O(n)
# sort()        -> O(n log n)

# =====================================================
# END OF LIST CHEATSHEET
# =====================================================