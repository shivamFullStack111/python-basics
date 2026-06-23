# =====================================================
# PYTHON DICTIONARY CHEATSHEET
# =====================================================

# What is a Dictionary?
# - Stores data in Key : Value pairs
# - Mutable (can be changed)
# - Ordered (Python 3.7+)
# - Keys must be unique

student = {
    "name": "Shivam",
    "age": 22,
    "city": "Jalandhar"
}

# =====================================================
# ACCESSING VALUES
# =====================================================

student["name"]

student.get("name")

student.get("salary", "Not Found")


# =====================================================
# ADDING ITEMS
# =====================================================

student["course"] = "BCA"

student["salary"] = 50000


# =====================================================
# UPDATING ITEMS
# =====================================================

student["age"] = 23

student.update({"city": "Punjab"})


# =====================================================
# REMOVING ITEMS
# =====================================================

student.pop("age")
# Remove specific key

student.popitem()
# Remove last item

del student["name"]
# Delete key

student.clear()
# Remove all items


# =====================================================
# COMMON METHODS
# =====================================================

student.keys()
# Returns all keys

student.values()
# Returns all values

student.items()
# Returns key-value pairs

student.get("name")
# Safe access

student.update({"age": 22})
# Update dictionary

student.copy()
# Copy dictionary

student.clear()
# Remove all items


# =====================================================
# LOOPING THROUGH DICTIONARY
# =====================================================

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)


# =====================================================
# CHECKING KEYS
# =====================================================

print("name" in student)

print("salary" not in student)


# =====================================================
# NESTED DICTIONARY
# =====================================================

users = {
    "user1": {
        "name": "Shivam",
        "age": 22
    },
    "user2": {
        "name": "Rahul",
        "age": 25
    }
}

print(users["user1"]["name"])


# =====================================================
# DICTIONARY COMPREHENSION
# =====================================================

squares = {x: x*x for x in range(5)}

print(squares)

# Output:
# {0:0, 1:1, 2:4, 3:9, 4:16}


# =====================================================
# CONVERTING DICTIONARY
# =====================================================

student = {
    "name": "Shivam",
    "age": 22
}

list(student.keys())

list(student.values())

list(student.items())


# =====================================================
# USEFUL BUILT-IN FUNCTIONS
# =====================================================

len(student)
# Number of key-value pairs

type(student)

dict()
# Create dictionary


# =====================================================
# MERGING DICTIONARIES
# =====================================================

a = {"x": 1}
b = {"y": 2}

c = a | b

print(c)

# Output:
# {'x': 1, 'y': 2}


# =====================================================
# DICTIONARY VS LIST
# =====================================================

# Dictionary
# Key-Value Pairs
# Fast Lookup
# Uses {}

# List
# Indexed Values
# Uses []


# =====================================================
# COMMON METHODS SUMMARY
# =====================================================

# get()       -> Get value safely
# keys()      -> Get all keys
# values()    -> Get all values
# items()     -> Get key-value pairs
# update()    -> Update dictionary
# pop()       -> Remove key
# popitem()   -> Remove last item
# copy()      -> Copy dictionary
# clear()     -> Remove all items


# =====================================================
# TIME COMPLEXITY
# =====================================================

# Access      -> O(1)
# Insert      -> O(1)
# Update      -> O(1)
# Delete      -> O(1)
# Search Key  -> O(1)

# =====================================================
# END OF DICTIONARY CHEATSHEET
# =====================================================