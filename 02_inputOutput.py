# =====================================================
# PYTHON INPUT & OUTPUT CHEATSHEET
# =====================================================

# INPUT
# =====================================================

# input() always returns STRING

name = input("Enter your name: ")

print(name)
print(type(name))


# Integer Input

age = int(input("Enter age: "))

print(age)
print(type(age))


# Float Input

salary = float(input("Enter salary: "))

print(salary)
print(type(salary))


# Boolean Input

is_student = input("Are you student? (True/False): ")

is_student = is_student.lower() == "true"

print(is_student)
print(type(is_student))


# Multiple Inputs

a, b = input("Enter two numbers: ").split()

print(a)
print(b)


# Multiple Integer Inputs

a, b = map(int, input("Enter two numbers: ").split())

print(a)
print(b)


# Multiple Float Inputs

x, y = map(float, input("Enter two decimal values: ").split())

print(x)
print(y)


# =====================================================
# OUTPUT
# =====================================================

print("Hello World")


# Print Variables

name = "Shivam"
age = 22

print(name)
print(age)


# Print Multiple Values

print(name, age)


# Separator

print("Python", "Java", "JavaScript", sep=" | ")

# Output:
# Python | Java | JavaScript


# End Parameter

print("Hello", end=" ")
print("World")

# Output:
# Hello World


# =====================================================
# STRING FORMATTING
# =====================================================

name = "Shivam"
age = 22

# f-string (Recommended)

print(f"My name is {name} and I am {age} years old")


# format()

print("My name is {} and I am {} years old".format(name, age))


# Percentage Formatting

print("My name is %s and I am %d years old" % (name, age))


# =====================================================
# ESCAPE CHARACTERS
# =====================================================

print("Hello\nWorld")
# New Line

print("Hello\tWorld")
# Tab Space

print("He said \"Hello\"")
# Double Quotes

print("C:\\Users\\Shivam")
# Backslash


# =====================================================
# TYPE CONVERSION WITH INPUT
# =====================================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)


# =====================================================
# COMMON INTERVIEW QUESTION
# =====================================================

# Q: What does input() return?

# Answer:
# input() always returns STRING data type.

x = input("Enter number: ")

print(type(x))
# <class 'str'>


# =====================================================
# SUMMARY
# =====================================================

# input()       -> Take input from user
# print()       -> Display output

# int()         -> Convert to integer
# float()       -> Convert to float
# str()         -> Convert to string
# bool()        -> Convert to boolean

# sep=""        -> Separator in print()
# end=""        -> Ending character in print()

# f""           -> Modern string formatting

# =====================================================
# END OF INPUT & OUTPUT CHEATSHEET
# =====================================================