# =====================================================
# PYTHON IF, ELIF, ELSE CHEATSHEET
# =====================================================

# What is if-else?
# Used to make decisions in a program.

# =====================================================
# SIMPLE IF
# =====================================================

age = 18

if age >= 18:
    print("You can vote")


# =====================================================
# IF ELSE
# =====================================================

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# =====================================================
# IF ELIF ELSE
# =====================================================

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# =====================================================
# MULTIPLE CONDITIONS
# =====================================================

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")


# =====================================================
# OR OPERATOR
# =====================================================

is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access Granted")


# =====================================================
# NOT OPERATOR
# =====================================================

is_banned = False

if not is_banned:
    print("User Allowed")


# =====================================================
# NESTED IF
# =====================================================

age = 20

if age >= 18:
    print("Adult")

    if age >= 60:
        print("Senior Citizen")
    else:
        print("Not Senior Citizen")


# =====================================================
# SHORT HAND IF
# =====================================================

age = 20

if age >= 18: print("Adult")


# =====================================================
# SHORT HAND IF ELSE (Ternary Operator)
# =====================================================

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)


# =====================================================
# COMPARISON OPERATORS
# =====================================================

# ==   Equal
# !=   Not Equal
# >    Greater Than
# <    Less Than
# >=   Greater Than Equal To
# <=   Less Than Equal To

x = 10
y = 20

if x < y:
    print("y is greater")


# =====================================================
# TRUTHY AND FALSY VALUES
# =====================================================

# False Values:
# False
# None
# 0
# 0.0
# ""
# []
# {}
# set()

if "":
    print("Runs")
else:
    print("Empty String is False")


# =====================================================
# PASS STATEMENT
# =====================================================

age = 20

if age > 18:
    pass

print("Program continues")


# =====================================================
# MATCH CASE (Python 3.10+)
# Similar to Switch in JavaScript
# =====================================================

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")


# =====================================================
# INTERVIEW QUESTIONS
# =====================================================

# Difference between if and elif?

# if:
# Creates a new condition check

# elif:
# Checked only if previous condition is False

# Example

num = 10

if num > 20:
    print("Greater than 20")
elif num > 5:
    print("Greater than 5")

# Output:
# Greater than 5


# =====================================================
# SUMMARY
# =====================================================

# if      -> First condition
# elif    -> Additional condition
# else    -> Runs when all conditions fail

# and     -> All conditions must be True
# or      -> Any one condition True
# not     -> Reverse condition

# pass    -> Empty block

# =====================================================
# END OF IF ELSE CHEATSHEET
# =====================================================