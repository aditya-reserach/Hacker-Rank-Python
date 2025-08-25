"""
Problem Statement:

Exceptions
Errors detected during execution are called exceptions.

Examples:
- ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.
- ValueError: Raised when a built-in operation or function receives an argument that has the right type 
  but an inappropriate value.

Task:
You are given two values, a and b. 
Perform integer division and print a // b.

Input Format:
- The first line contains T, the number of test cases.
- The next T lines each contain the space separated values of a and b.

Constraints:
- Division must be integer division.
- Handle the exceptions ZeroDivisionError and ValueError.

Output Format:
- Print the result of a // b.
- In case of ZeroDivisionError or ValueError, print the error code.

Sample Input:
3
1 0
2 $
3 1

Sample Output:
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
"""

# -------------------------------
# CODE 1: Using prebuilt exception handling
# -------------------------------

# Read number of test cases as integer
t = int(input())  

# Loop through all test cases
for _ in range(t):
    # Read two inputs as strings (they may be invalid for int conversion)
    a, b = input().split()
    try:
        # Try converting both inputs to integers
        a = int(a)
        b = int(b)
        # Perform integer division using //
        print(a // b)
    except ZeroDivisionError as e:
        # Handles case when denominator is zero
        print("Error Code:", e)
    except ValueError as e:
        # Handles case when conversion to int fails (like '$')
        print("Error Code:", e)


# -------------------------------
# CODE 2: Without prebuilt exception handling
# -------------------------------

# Read number of test cases again
t = int(input())  

# Loop through all test cases
for _ in range(t):
    # Read raw input
    a, b = input().split()

    # --- Manual ValueError handling ---
    # Check if both inputs are valid integers without using int() exception catching
    # str.isdigit() checks for valid digits (doesn't handle negatives, so extend check manually)
    def is_integer(s):
        # If string starts with '-' and the rest are digits, it's valid integer
        if s.startswith('-') and s[1:].isdigit():
            return True
        # If all characters are digits (like '123')
        if s.isdigit():
            return True
        return False

    # If either input is not a valid integer, simulate ValueError
    if not is_integer(a) or not is_integer(b):
        print("Error Code: invalid literal for int() with base 10:", "'" + (a if not is_integer(a) else b) + "'")
        continue

    # Convert to integers now (safe conversion because checked)
    a = int(a)
    b = int(b)

    # --- Manual ZeroDivisionError handling ---
    if b == 0:
        print("Error Code: integer division or modulo by zero")
        continue

    # Otherwise perform integer division
    print(a // b)


# -------------------------------
# TIME COMPLEXITY ANALYSIS
# -------------------------------

"""
Code 1 (with prebuilt try/except):
- For each test case:
    - Conversion of inputs to int → O(1)
    - Division operation → O(1)
    - Exception handling (when triggered) → O(1)
- Total Time Complexity: O(T), where T = number of test cases.
- Space Complexity: O(1), since only a few variables are stored.

Code 2 (without prebuilt exception handling):
- For each test case:
    - is_integer() check for each input:
        * Worst-case, string length = n, so check is O(n).
        * Done twice (for a and b), so O(2n) ≈ O(n).
    - Division check → O(1)
- Total Time Complexity: O(T * n), where n = average length of the input string.
- Space Complexity: O(1), as only a few helper variables are stored.

Overall:
- Code 1 is more efficient because Python's built-in int() and exception handling are optimized in C.
- Code 2 is slightly less efficient due to manual string checks.
"""
