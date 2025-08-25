# ==========================================================
# Problem Statement:
# ==========================================================
# Given two sets of integers, A and B, print their symmetric difference in ascending order.
# Symmetric difference means all elements which exist in either set A or set B but not in both.
#
# Input Format:
# Line 1: Integer M, size of set A
# Line 2: M space-separated integers, elements of set A
# Line 3: Integer N, size of set B
# Line 4: N space-separated integers, elements of set B
#
# Output Format:
# Print the symmetric difference integers in ascending order, one per line.
#
# Sample Input:
# 4
# 2 4 5 9
# 4
# 2 4 11 12
#
# Sample Output:
# 5
# 9
# 11
# ==========================================================


# ==========================================================
# Code 1: Using prebuilt symmetric_difference() method
# ==========================================================

# Read size of first set
m = int(input())  # Example: 4

# Read elements of first set and convert to Python set
a = set(map(int, input().split()))  # Example: {2,4,5,9}

# Read size of second set
n = int(input())  # Example: 4

# Read elements of second set and convert to Python set
b = set(map(int, input().split()))  # Example: {2,4,11,12}

# Compute symmetric difference using prebuilt function
a_b = sorted(a.symmetric_difference(b))  # Example: [5, 9, 11]

# Print each element of the symmetric difference in ascending order
for num in a_b:
    print(num)

# ==========================================================
# Time Complexity Analysis for Code 1:
# - Converting input to sets: O(M + N)
# - symmetric_difference(): O(M + N)
# - sorted(): O(k log k) where k = size of symmetric difference
# Overall: O(M + N + k log k)
# 
# Space Complexity:
# - Sets a, b, and a_b: O(M + N)
# - Sorted list: O(k)
# Overall: O(M + N)
# ==========================================================


# ==========================================================
# Code 2: Without using prebuilt symmetric_difference()
# ==========================================================

# Step 1: Read size of first set
m = int(input())

# Step 2: Read elements of first set and convert to set
a = set(map(int, input().split()))

# Step 3: Read size of second set
n = int(input())

# Step 4: Read elements of second set and convert to set
b = set(map(int, input().split()))

# Step 5: Compute elements in a but not in b
a_minus_b = a - b  # set difference: elements only in a

# Step 6: Compute elements in b but not in a
b_minus_a = b - a  # set difference: elements only in b

# Step 7: Union of both differences gives symmetric difference
sym_diff = a_minus_b | b_minus_a  # union operator '|'

# Step 8: Sort the symmetric difference in ascending order
sorted_diff = sorted(sym_diff)

# Step 9: Print each element
for num in sorted_diff:
    print(num)

# ==========================================================
# Time Complexity Analysis for Code 2:
# - Converting input to sets: O(M + N)
# - a - b and b - a: O(M + N) each
# - Union (|): O(M + N)
# - sorted(): O(k log k), k = size of symmetric difference
# Overall: O(M + N + k log k)
# 
# Space Complexity:
# - Sets a, b, a_minus_b, b_minus_a, sym_diff: O(M + N)
# - Sorted list: O(k)
# Overall: O(M + N)
# ==========================================================
