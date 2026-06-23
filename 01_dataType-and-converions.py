# =====================================================
# PYTHON DATA TYPES & TYPE CONVERSION
# =====================================================

# =====================================================
# DATA TYPES
# =====================================================

# 1. INTEGER (int)
age = 22
print(type(age))  # <class 'int'>


# 2. FLOAT (float)
price = 99.99
print(type(price))  # <class 'float'>


# 3. STRING (str)
name = "Shivam"
print(type(name))  # <class 'str'>


# 4. BOOLEAN (bool)
is_active = True
print(type(is_active))  # <class 'bool'>


# 5. LIST (list)
numbers = [1, 2, 3, 4]
print(type(numbers))  # <class 'list'>


# 6. TUPLE (tuple)
coordinates = (10, 20)
print(type(coordinates))  # <class 'tuple'>


# 7. SET (set)
unique_numbers = {1, 2, 3, 4}
print(type(unique_numbers))  # <class 'set'>


# 8. DICTIONARY (dict)
student = {
    "name": "Shivam",
    "age": 22
}
print(type(student))  # <class 'dict'>


# 9. NONE TYPE
data = None
print(type(data))  # <class 'NoneType'>


# =====================================================
# TYPE CHECKING
# =====================================================

x = 100

print(type(x))

print(isinstance(x, int))     # True
print(isinstance(x, float))   # False


# =====================================================
# TYPE CONVERSION (TYPE CASTING)
# =====================================================

# String -> Integer

num = "100"
converted = int(num)

print(converted)
print(type(converted))


# Integer -> String

age = 22
converted = str(age)

print(converted)
print(type(converted))


# Integer -> Float

num = 10
converted = float(num)

print(converted)
print(type(converted))


# Float -> Integer

price = 99.99
converted = int(price)

print(converted)   # 99
print(type(converted))


# Integer -> Boolean

print(bool(1))     # True
print(bool(0))     # False


# String -> Boolean

print(bool("Hello"))   # True
print(bool(""))        # False


# List -> Tuple

my_list = [1, 2, 3]

my_tuple = tuple(my_list)

print(my_tuple)


# Tuple -> List

my_tuple = (1, 2, 3)

my_list = list(my_tuple)

print(my_list)


# List -> Set

my_list = [1, 2, 2, 3, 3]

my_set = set(my_list)

print(my_set)   # duplicates removed


# Set -> List

my_set = {1, 2, 3}

my_list = list(my_set)

print(my_list)


# Dictionary Keys -> List

student = {
    "name": "Shivam",
    "age": 22
}

keys = list(student.keys())

print(keys)


# =====================================================
# USER INPUT TYPE CONVERSION
# =====================================================

# input() always returns string

age = int(input("Enter age: "))

salary = float(input("Enter salary: "))

name = str(input("Enter name: "))

# Boolean Input

is_student = input("Are you student? (True/False): ")

is_student = is_student.lower() == "true"

print(is_student)


# =====================================================
# COMMON TYPE CONVERSION FUNCTIONS
# =====================================================

int()      # Convert to integer

float()    # Convert to float

str()      # Convert to string

bool()     # Convert to boolean

list()     # Convert to list

tuple()    # Convert to tuple

set()      # Convert to set

dict()     # Convert to dictionary


# =====================================================
# QUICK SUMMARY
# =====================================================

# int     -> Whole Numbers
# float   -> Decimal Numbers
# str     -> Text
# bool    -> True / False
# list    -> Ordered, Mutable
# tuple   -> Ordered, Immutable
# set     -> Unique Values
# dict    -> Key-Value Pairs
# None    -> No Value

# =====================================================
# END
# =====================================================