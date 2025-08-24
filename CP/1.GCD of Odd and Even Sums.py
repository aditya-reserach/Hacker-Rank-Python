# ======================================================
# Problem: GCD of sums of first n odd and even numbers
# ======================================================
# You are given an integer n. Your task is to compute the 
# Greatest Common Divisor (GCD) of:
# 1. sumOdd: the sum of the first n odd numbers
# 2. sumEven: the sum of the first n even numbers
# Return the GCD of sumOdd and sumEven.
#
# Example:
# Input: n = 4
# Sum of first 4 odd numbers: 1+3+5+7 = 16
# Sum of first 4 even numbers: 2+4+6+8 = 20
# GCD(16, 20) = 4
#
# Constraints: 1 <= n <= 1000

# ======================================================
# Code 1: Using prebuilt function math.gcd
# ======================================================

import math  # Import math module to use gcd function

# Step 1: Read input
n = int(input().strip())  # Read integer n from user

# Step 2: Compute sum of first n odd numbers using formula n^2
sum_odd = n * n

# Step 3: Compute sum of first n even numbers using formula n*(n+1)
sum_even = n * (n + 1)

# Step 4: Compute GCD using built-in math.gcd() function
result_builtin = math.gcd(sum_odd, sum_even)

# Step 5: Print the result
print("Using math.gcd():", result_builtin)

# ------------------------------------------------------
# Time Complexity:
# - Calculating sums: O(1) (using formulas)
# - math.gcd(a, b): O(log(min(sum_odd, sum_even)))
# Space Complexity: O(1) (only integers stored)
# ------------------------------------------------------

# ======================================================
# Code 2: Without using prebuilt function (manual GCD)
# ======================================================

# Step 1: Read input (can reuse n if running together)
# n = int(input().strip())  # Already read above

# Step 2: Define a function to compute GCD manually using Euclidean algorithm
def gcd_manual(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two numbers a and b
    using the Euclidean algorithm (without using any prebuilt function).
    """
    while b != 0:         # Repeat until remainder becomes 0
        a, b = b, a % b   # Swap: b becomes a, remainder becomes b
    return a              # When b = 0, a is the GCD

# Step 3: Compute GCD using manual function
result_manual = gcd_manual(sum_odd, sum_even)

# Step 4: Print the result
print("Using manual GCD:", result_manual)

# ------------------------------------------------------
# Time Complexity:
# - Calculating sums: O(1)
# - gcd_manual(a, b): O(log(min(sum_odd, sum_even)))
# Space Complexity: O(1)
# ------------------------------------------------------
