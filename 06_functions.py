# =====================================================
# PYTHON FUNCTIONS CHEATSHEET
# =====================================================

# What is a Function?
# A function is a block of code that performs a specific task.
# Functions help avoid code repetition and improve readability.

# Syntax

def greet():
    print("Hello World")

greet()


# =====================================================
# FUNCTION WITH PARAMETERS
# =====================================================

def greet(name):
    print("Hello", name)

greet("Shivam")


# =====================================================
# FUNCTION WITH MULTIPLE PARAMETERS
# =====================================================

def add(a, b):
    print(a + b)

add(10, 20)


# =====================================================
# RETURN STATEMENT
# =====================================================

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# =====================================================
# DEFAULT PARAMETERS
# =====================================================

def greet(name="Guest"):
    print("Hello", name)

greet()          # Guest
greet("Shivam")  # Shivam


# =====================================================
# POSITIONAL ARGUMENTS
# =====================================================

def info(name, age):
    print(name, age)

info("Shivam", 22)


# =====================================================
# KEYWORD ARGUMENTS
# =====================================================

def info(name, age):
    print(name, age)

info(age=22, name="Shivam")


# =====================================================
# ARBITRARY ARGUMENTS (*args)
# =====================================================

# Accepts multiple positional arguments

def total(*args):
    print(args)
    print(sum(args))

total(10, 20, 30, 40)


# =====================================================
# KEYWORD ARBITRARY ARGUMENTS (**kwargs)
# =====================================================

# Accepts multiple keyword arguments

def info(**kwargs):
    print(kwargs)

info(name="Shivam", age=22, city="Jalandhar")


# =====================================================
# LOCAL VARIABLE
# =====================================================

def test():
    x = 100
    print(x)

test()

# x cannot be accessed outside function


# =====================================================
# GLOBAL VARIABLE
# =====================================================

x = 100

def test():
    print(x)

test()


# =====================================================
# GLOBAL KEYWORD
# =====================================================

x = 10

def change():
    global x
    x = 50

change()

print(x)


# =====================================================
# RECURSION
# =====================================================

# Function calling itself

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)


# =====================================================
# LAMBDA FUNCTION
# =====================================================

# Anonymous one-line function

square = lambda x: x * x

print(square(5))


# Multiple Parameters

add = lambda a, b: a + b

print(add(10, 20))


# =====================================================
# NESTED FUNCTION
# =====================================================

def outer():

    def inner():
        print("Inner Function")

    inner()

outer()


# =====================================================
# FUNCTION AS VARIABLE
# =====================================================

def greet():
    print("Hello")

my_function = greet

my_function()


# =====================================================
# BUILT-IN FUNCTIONS
# =====================================================

print("Hello")

len([1, 2, 3])

type(100)

max([1, 2, 3])

min([1, 2, 3])

sum([1, 2, 3])

sorted([3, 1, 2])

round(10.567, 2)

abs(-10)


# =====================================================
# DOCSTRING
# =====================================================

def add(a, b):
    """
    Returns sum of two numbers
    """
    return a + b

print(add.__doc__)


# =====================================================
# FUNCTION SUMMARY
# =====================================================

# def           -> Create function
# return        -> Return value
# parameter     -> Variable in function definition
# argument      -> Value passed to function

# *args         -> Multiple positional arguments
# **kwargs      -> Multiple keyword arguments

# lambda        -> Anonymous function

# global        -> Access global variable

# recursion     -> Function calls itself

# =====================================================
# INTERVIEW QUESTIONS
# =====================================================

# Q. Difference between parameter and argument?

# Parameter:
# Variable defined in function

# Argument:
# Actual value passed to function

# Example:

def add(a, b):   # a and b are parameters
    return a + b

add(10, 20)      # 10 and 20 are arguments

# =====================================================
# END OF FUNCTIONS CHEATSHEET
# =====================================================