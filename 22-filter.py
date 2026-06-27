# ==========================================================
# Example 1 : Even Numbers
# ==========================================================

numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# Output:
# [2, 4, 6]


# ==========================================================
# Example 2 : Odd Numbers
# ==========================================================

numbers = [1, 2, 3, 4, 5, 6]

odd = list(filter(lambda x: x % 2 != 0, numbers))

print(odd)

# Output:
# [1, 3, 5]


# ==========================================================
# Example 3 : Numbers Greater Than 10
# ==========================================================

numbers = [5, 10, 15, 20, 25]

greater = list(filter(lambda x: x > 10, numbers))

print(greater)

# Output:
# [15, 20, 25]
