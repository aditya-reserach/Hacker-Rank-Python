"""
Problem Statement:
You are given three integers: a, b, and m.
You need to:
1. Print pow(a, b)   → result of a raised to the power b
2. Print pow(a, b, m) → result of (a^b) % m

Input Format:
- The first line contains integer a.
- The second line contains integer b.
- The third line contains integer m.

Constraints:
- a, b, m are integers
- If m is provided, it cannot be negative.

Output Format:
- Line 1: a^b
- Line 2: (a^b) % m

Example:
Input:
3
4
5

Output:
81
1
"""

# ------------------------------
# Approach 1: Using Python's built-in pow()
# ------------------------------

# Read inputs
a = int(input())
b = int(input())
m = int(input())

# First result: normal power
print(pow(a, b))  

# Second result: modular power
print(pow(a, b, m))  


# ------------------------------
# Approach 2: Without using pow() or ** operator
# Using Fast Exponentiation (Exponentiation by Squaring)
# ------------------------------

def fast_power(base, exp):
    """
    Function to compute base^exp without using pow() or **.
    Uses fast exponentiation with O(log exp) time complexity.
    """
    result = 1
    while exp > 0:
        # If exponent is odd, multiply result with current base
        if exp % 2 == 1:
            result *= base
        # Square the base
        base *= base
        # Divide exponent by 2 (floor division)
        exp //= 2
    return result


def fast_power_mod(base, exp, mod):
    """
    Function to compute (base^exp) % mod efficiently.
    Uses modular exponentiation with O(log exp) time complexity.
    """
    result = 1
    base %= mod  # reduce base mod m initially
    while exp > 0:
        # If exponent is odd, multiply result with base % mod
        if exp % 2 == 1:
            result = (result * base) % mod
        # Square the base under modulo
        base = (base * base) % mod
        # Divide exponent by 2
        exp //= 2
    return result


# Verify using custom implementation
print(fast_power(a, b))        # same as a^b
print(fast_power_mod(a, b, m)) # same as (a^b) % m
