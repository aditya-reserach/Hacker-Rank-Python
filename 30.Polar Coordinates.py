"""
==========================================================
Problem Statement
==========================================================
Polar coordinates are an alternative way of representing 
Cartesian coordinates or Complex Numbers.

A complex number 'z' is determined by:
    z = x + yj
    where x = real part, y = imaginary part, j = sqrt(-1)

A polar coordinate (r, φ) is determined by:
    r = modulus (distance from origin to point)
    φ = phase angle (counter-clockwise angle from +x axis)

Your task:
------------
Given a complex number 'z' as input, convert it into 
polar coordinates and print:
    1. Modulus (r)
    2. Phase angle (φ in radians)

Input Format:
    A single line containing the complex number, e.g., 1+2j

Constraints:
    The given number is a valid complex number.

Output Format:
    First line → modulus
    Second line → phase angle

Example:
----------
Input:
    1+2j

Output:
    2.23606797749979
    1.1071487177940904
==========================================================
"""

# ==========================================================
# Solution 1: Using Prebuilt Functions
# ==========================================================

# Import the `phase` function from Python's `cmath` module.
# `cmath` is a library for complex number mathematics.
from cmath import phase

# Take input from user.
# Example: "1+2j"
# input() takes the raw string, strip() removes spaces (like " 1+2j " → "1+2j").
z = input().strip()

# Convert the string into a complex number.
# complex("1+2j") → (1+2j) where real=1, imag=2.
c = complex(z)

# abs(complex) → returns modulus of complex number.
# Mathematically: r = sqrt(x^2 + y^2).
print(abs(c))

# phase(complex) → returns the angle φ (in radians).
# It calculates angle = atan2(y, x).
print(phase(c))


"""
Time Complexity (Solution 1):
    - Conversion to complex → O(1)
    - abs(c) → O(1) (direct formula sqrt(x^2+y^2))
    - phase(c) → O(1) (uses atan2 internally)
    Total = O(1)

Space Complexity (Solution 1):
    - Only variables `z` and `c` stored → O(1)
    Total = O(1)
"""


# ==========================================================
# Solution 2: Without Using Prebuilt Functions
# ==========================================================

# Import `math` module (basic math library).
# We only use sqrt() for modulus and atan2() for angle.
import math

# Again, take input from user and remove spaces.
z = input().strip()

# Convert the string into complex manually.
# complex() still used for conversion from string to separate real & imag,
# because Hackerrank input is in complex format like "1+2j".
# But we DO NOT use prebuilt `abs()` or `phase()`.
c = complex(z)

# Extract real and imaginary parts.
x = c.real   # real part
y = c.imag   # imaginary part

# Calculate modulus manually.
# Formula: r = sqrt(x^2 + y^2).
r = math.sqrt(x**2 + y**2)

# Calculate phase angle manually.
# Formula: φ = atan2(y, x)
# atan2 handles all 4 quadrants correctly.
phi = math.atan2(y, x)

# Print results.
print(r)
print(phi)


"""
Time Complexity (Solution 2):
    - Extracting real/imag → O(1)
    - sqrt(x^2 + y^2) → O(1)
    - atan2(y, x) → O(1)
    Total = O(1)

Space Complexity (Solution 2):
    - Variables x, y, r, phi stored → O(1)
    Total = O(1)
"""
