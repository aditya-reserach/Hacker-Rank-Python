"""
Problem Statement:
-----------------
One of the built-in functions of Python is `divmod`, which takes two arguments 
and returns a tuple containing the quotient first and then the remainder.

For example:
>>> print(divmod(177, 10))
(17, 7)

Here:
- Integer division: 177 // 10 = 17
- Modulo operator: 177 % 10 = 7

Task:
-----
Read in two integers, `a` and `b`, and print three lines:
1. The integer division result a // b
2. The result of the modulo operation a % b
3. The tuple (a // b, a % b) which is equivalent to divmod(a, b)

Input Format:
-------------
- The first line contains the first integer, `a`.
- The second line contains the second integer, `b`.

Output Format:
--------------
- Print three lines as described above.

Sample Input:
-------------
177
10

Sample Output:
--------------
17
7
(17, 7)

-----------------------------------------------------------------
CODE 1: Using Python Operators (//, %, divmod)
-----------------------------------------------------------------
"""

# Read two integers from user input
a, b = int(input()), int(input())  # a = first integer, b = second integer

# Print the integer division result (quotient)
print(a // b)  # // gives quotient (floor division in Python)

# Print the remainder of the division
print(a % b)  # % gives remainder after dividing a by b

# Print the tuple (quotient, remainder) using divmod
print(divmod(a, b))  # divmod returns (a // b, a % b)

"""
Time Complexity Analysis (CODE 1):
----------------------------------
- a // b → O(1) (constant time operation by CPU)
- a % b  → O(1)
- divmod(a, b) → O(1) (internally same as computing quotient and remainder once)
Overall Time Complexity = O(1)
Space Complexity = O(1)
"""


"""
-----------------------------------------------------------------
CODE 2: Without Using divmod() or % Operator
          (Manually calculating remainder)
-----------------------------------------------------------------
"""

# Read two integers from user input
a = int(input())  # First integer
b = int(input())  # Second integer

# Compute the quotient using integer division
quotient = a // b  # Using floor division operator

# Compute the remainder manually instead of using %
# remainder = a - (quotient * b)
remainder = a - (quotient * b)

# Print the quotient
print(quotient)

# Print the remainder
print(remainder)

# Print the tuple (quotient, remainder) manually
print((quotient, remainder))

"""
Time Complexity Analysis (CODE 2):
----------------------------------
- Quotient calculation (a // b) → O(1)
- Multiplication (quotient * b) → O(1)
- Subtraction (a - product) → O(1)
Overall Time Complexity = O(1)
Space Complexity = O(1)
"""

# End of file
