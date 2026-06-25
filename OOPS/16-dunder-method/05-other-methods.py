# ==========================================
# MOST COMMON PYTHON DUNDER (MAGIC) METHODS
# ==========================================


# ------------------------------------------
# 1. __init__() -> Constructor
# Called automatically when an object is created.
# ------------------------------------------

class User:
    def __init__(self, name):
        self.name = name

u = User("Shivam")


# ------------------------------------------
# 2. __str__() -> Human-readable string
# Called by print(obj)
# ------------------------------------------

class User:
    def __str__(self):
        return "User Object"

print(User())   # User Object


# ------------------------------------------
# 3. __repr__() -> Developer representation
# Used for debugging.
# ------------------------------------------

class User:
    def __repr__(self):
        return "User('Shivam')"

print(User())   # User('Shivam')


# ------------------------------------------
# 4. __len__() -> len(obj)
# ------------------------------------------

class Team:
    def __len__(self):
        return 5

print(len(Team()))   # 5


# ------------------------------------------
# 5. __add__() -> +
# ------------------------------------------

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)   # 30


# ------------------------------------------
# 6. __sub__() -> -
# ------------------------------------------

class Number:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


# ------------------------------------------
# 7. __mul__() -> *
# ------------------------------------------

class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value


# ------------------------------------------
# 8. __truediv__() -> /
# ------------------------------------------

class Number:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return self.value / other.value


# ------------------------------------------
# 9. __eq__() -> ==
# ------------------------------------------

class User:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


# ------------------------------------------
# 10. __lt__() -> <
# ------------------------------------------

class User:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age


# ------------------------------------------
# 11. __gt__() -> >
# ------------------------------------------

class User:
    def __init__(self, age):
        self.age = age

    def __gt__(self, other):
        return self.age > other.age


# ------------------------------------------
# 12. __contains__() -> in operator
# ------------------------------------------

class Team:
    def __contains__(self, item):
        return item == "Shivam"

team = Team()

print("Shivam" in team)   # True


# ------------------------------------------
# 13. __getitem__() -> obj[key]
# ------------------------------------------

class Data:
    def __getitem__(self, key):
        return f"Value of {key}"

d = Data()

print(d["name"])   # Value of name


# ------------------------------------------
# 14. __setitem__() -> obj[key] = value
# ------------------------------------------

class Data:
    def __setitem__(self, key, value):
        print(f"{key} = {value}")


# ------------------------------------------
# 15. __call__() -> obj()
# Makes object behave like a function
# ------------------------------------------

class Greeting:
    def __call__(self):
        print("Hello")

g = Greeting()

g()   # Hello


# ------------------------------------------
# 16. __iter__() -> iteration support
# ------------------------------------------

class Numbers:
    def __iter__(self):
        return iter([1, 2, 3])

for i in Numbers():
    print(i)


# ------------------------------------------
# 17. __next__() -> next(iterator)
# ------------------------------------------

class Counter:
    def __init__(self):
        self.count = 0

    def __next__(self):
        self.count += 1
        return self.count


# ------------------------------------------
# 18. __del__() -> Destructor
# Called before object destruction
# ------------------------------------------

class User:
    def __del__(self):
        print("Object Deleted")


# ------------------------------------------
# 19. __bool__() -> bool(obj)
# ------------------------------------------

class User:
    def __bool__(self):
        return True

print(bool(User()))


# ------------------------------------------
# 20. __hash__() -> hash(obj)
# ------------------------------------------

class User:
    def __hash__(self):
        return 12345

print(hash(User()))


# ==========================================
# MOST ASKED IN INTERVIEWS
# ==========================================
#
# __init__()
# __str__()
# __repr__()
# __len__()
# __add__()
# __eq__()
# __lt__()
# __getitem__()
# __setitem__()
# __call__()
# __iter__()
# __next__()
#
# Learn these first.
# ==========================================