"""
Problem Statement:
------------------
You are given a right triangle ABC, where angle ABC = 90°.
Point M is the midpoint of the hypotenuse AC.
You are given two natural numbers as input:
    - Side AB (integer)
    - Side BC (integer)

Task:
-----
Find angle MBC (angle between MB and BC) in degrees.

Input Format:
-------------
The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints:
------------
- Lengths AB and BC are natural numbers.
- Output should be in degrees (rounded to the nearest integer).

Output Format:
--------------
Output the angle in degrees with the degree symbol (°).
If the angle is 56.5000001°, output 57°.
If the angle is 56.5000000°, output 57°.
If the angle is 56.4999999°, output 56°.

Sample Input:
-------------
10
10

Sample Output:
--------------
45°
"""

# ----------------------------------------------------------------------
# SOLUTION 1: Using Built-in Math Functions
# ----------------------------------------------------------------------

import math  # Importing math module for trigonometric functions

# Step 1: Take input for side AB
AB = int(input().strip())  # Read the first input as an integer (length of AB)

# Step 2: Take input for side BC
BC = int(input().strip())  # Read the second input as an integer (length of BC)

# Step 3: Calculate the angle in radians
# math.atan2(y, x) computes the arctangent of (y/x) considering quadrant safety.
# Here, AB = opposite side, BC = adjacent side.
angle_rad = math.atan2(AB, BC)  # This returns the angle at B in radians

# Step 4: Convert radians to degrees
angle_deg = math.degrees(angle_rad)  # Convert the result from radians to degrees

# Step 5: Round to nearest integer
result = round(angle_deg)  # Round the angle to the nearest whole number

# Step 6: Print result with degree symbol
print(f"{result}{chr(176)}")  # chr(176) is the degree symbol (°)


# ----------------------------------------------------------------------
# SOLUTION 2: Without Using Built-in Trigonometric Functions
# ----------------------------------------------------------------------

# Here, we manually implement atan2 and degree conversion using Taylor Series
# expansion for arctan (Maclaurin series):
# arctan(x) ≈ x - x^3/3 + x^5/5 - x^7/7 + ... (valid for |x| <= 1)

# Step 1: Take inputs again (for independent solution run)
AB = int(input().strip())  # Length of AB (opposite side)
BC = int(input().strip())  # Length of BC (adjacent side)

# Step 2: Calculate ratio = opposite / adjacent
ratio = AB / BC  # Equivalent to tan(theta)

# Step 3: Implement arctan using Taylor Series expansion
# We take first 10 terms for reasonable accuracy
terms = 10
atan_value = 0.0
sign = 1  # Alternating signs in series (+, -, +, -)

for n in range(terms):
    power = 2 * n + 1  # Powers: 1, 3, 5, 7, ...
    term = (ratio ** power) / power  # Compute current term of the series
    atan_value += sign * term  # Add/subtract term
    sign *= -1  # Flip sign for next iteration

# atan_value now holds the angle in radians

# Step 4: Convert radians to degrees manually
# Formula: degrees = radians * (180 / π)
PI = 3.141592653589793  # Approximation of π
angle_deg_manual = atan_value * (180 / PI)  # Convert to degrees

# Step 5: Round to nearest integer
result_manual = round(angle_deg_manual)  # Round to nearest whole number

# Step 6: Print result with degree symbol
print(f"{result_manual}{chr(176)}")  # Print final result


# ----------------------------------------------------------------------
# TIME AND SPACE COMPLEXITY ANALYSIS
# ----------------------------------------------------------------------

"""
Solution 1 (Using Built-in Functions):
--------------------------------------
- Time Complexity:
    * atan2 and degrees are O(1) operations (constant time).
    * Input reading is O(1).
    => Overall Time Complexity: O(1)
- Space Complexity:
    * Only a few variables (AB, BC, angle_rad, angle_deg, result).
    * No extra data structures.
    => Overall Space Complexity: O(1)

Solution 2 (Without Built-in Functions):
----------------------------------------
- Time Complexity:
    * Taylor Series loop runs for a fixed number of terms (say 10).
    * Each iteration does O(1) work.
    => Overall Time Complexity: O(n) where n = number of terms.
       Since n is constant (10), effective complexity is O(1).
- Space Complexity:
    * Uses a few scalar variables (AB, BC, ratio, atan_value, PI).
    * Loop uses constant extra space.
    => Overall Space Complexity: O(1)

Conclusion:
-----------
Both solutions are effectively O(1) in time and O(1) in space.
However, the built-in function is more precise and faster,
while the manual method demonstrates the math behind it.
"""
