# =====================================================
# PYTHON SET OPERATIONS
# Union, Intersection, Difference, Symmetric Difference
# =====================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# =====================================================
# UNION
# =====================================================

# Combines all unique elements

print(a.union(b))

# OR

print(a | b)

# Output:
# {1, 2, 3, 4, 5, 6}


# =====================================================
# INTERSECTION
# =====================================================

# Common elements

print(a.intersection(b))

# OR

print(a & b)

# Output:
# {3, 4}


# =====================================================
# DIFFERENCE
# =====================================================

# Elements present in first set but not second

print(a.difference(b))

# OR

print(a - b)

# Output:
# {1, 2}


print(b.difference(a))

# Output:
# {5, 6}


# =====================================================
# SYMMETRIC DIFFERENCE
# =====================================================

# Elements present in either set but not both

print(a.symmetric_difference(b))

# OR

print(a ^ b)

# Output:
# {1, 2, 5, 6}


# =====================================================
# SUBSET
# =====================================================

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))

# Output:
# True


# =====================================================
# SUPERSET
# =====================================================

a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))

# Output:
# True


# =====================================================
# DISJOINT
# =====================================================

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))

# Output:
# True
# No common elements


# =====================================================
# UPDATE METHODS
# =====================================================

a = {1, 2, 3}
b = {3, 4, 5}

a.update(b)

print(a)

# Output:
# {1, 2, 3, 4, 5}


# =====================================================
# SUMMARY
# =====================================================

# union()                  -> Combine sets
# intersection()           -> Common values
# difference()             -> Values in first set only
# symmetric_difference()   -> Non-common values
# issubset()               -> Check subset
# issuperset()             -> Check superset
# isdisjoint()             -> No common values

# |   -> Union
# &   -> Intersection
# -   -> Difference
# ^   -> Symmetric Difference

# =====================================================
# END
# =====================================================