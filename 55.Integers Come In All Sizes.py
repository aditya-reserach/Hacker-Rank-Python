"""
================================================================================
PROBLEM STATEMENT
================================================================================

Integers in Python can be as big as the bytes in your machine's memory. There is 
no limit in size as there is in other programming languages like C++ (int or 
long long int). As we know, the result of exponentiation grows very fast with 
increasing powers.

Let's do some calculations on very large integers.

--------------------------------------------------------------------------------
TASK
--------------------------------------------------------------------------------
Read four numbers, a, b, c, and d, and print the result of (a^b + c^d).

--------------------------------------------------------------------------------
INPUT FORMAT
--------------------------------------------------------------------------------
Integers a, b, c, and d are given on four separate lines, respectively.

--------------------------------------------------------------------------------
CONSTRAINTS
--------------------------------------------------------------------------------
- Each input value is an integer.
- The exponents b and d may be large.
- The result of a^b or c^d may exceed the limit of 64-bit integers.

--------------------------------------------------------------------------------
OUTPUT FORMAT
--------------------------------------------------------------------------------
Print the result of (a^b + c^d) on one line.

--------------------------------------------------------------------------------
SAMPLE INPUT
--------------------------------------------------------------------------------
9
29
7
27

--------------------------------------------------------------------------------
SAMPLE OUTPUT
--------------------------------------------------------------------------------
4710194409608608369201743232

Note: This result is bigger than a 64-bit integer (long long int in C++). 
Python can handle this due to its arbitrary-precision integer support.

================================================================================
SOLUTION 1: Using Python Built-in Functions
================================================================================
This is the short HackerRank-style solution that uses Python's built-in map() 
and pow() functions.
================================================================================
"""

# Read four integers from input using list comprehension and map.
# [input() for i in range(4)] → collects 4 separate inputs into a list of strings.
# map(int, ...) → converts each string to an integer.
# a, b, c, d = ... → unpacks the list of 4 integers into 4 variables.
a, b, c, d = map(int, [input() for i in range(4)])

# Calculate a^b using pow(a, b) and c^d using pow(c, d).
# pow() is a built-in Python function optimized for exponentiation.
# Then we add them together and print the result.
print((pow(a, b) + pow(c, d)))


"""
================================================================================
SOLUTION 2: Manual Implementation Without Prebuilt Helpers
================================================================================
This solution avoids using prebuilt helpers like map() and pow(). Instead:
- It manually converts string input into integers.
- It manually computes exponentiation using a loop.
================================================================================
"""

# Step 1: Take 4 inputs as strings using list comprehension.
inputs = [input() for i in range(4)]

# Step 2: Convert the string inputs into integers manually (without int()).
# We do this by processing each character, calculating its numeric value, and
# building the number digit by digit using ASCII codes.
numbers = []  # This list will store the converted integers.
for x in inputs:
    num = 0  # Initialize a variable to build the integer value.
    for ch in x:  # Loop through each character of the string.
        # ord(ch) returns the ASCII code of the character.
        # ord('0') is 48, so (ord(ch) - ord('0')) gives the digit's integer value.
        digit = ord(ch) - ord('0')
        num = num * 10 + digit  # Build the number by shifting digits left.
    numbers.append(num)  # Add the converted integer to the list.

# Unpack the four integers from the list into variables a, b, c, d.
a, b, c, d = numbers

# Step 3: Define a manual power function without using pow().
# It multiplies the base by itself exp times.
def power(base, exp):
    result = 1  # Initialize result to 1 (identity for multiplication).
    for i in range(exp):  # Repeat multiplication 'exp' times.
        result *= base
    return result  # Return the final result.

# Step 4: Calculate the final result using the manual power function.
result = power(a, b) + power(c, d)

# Step 5: Print the result.
print(result)


"""
================================================================================
TIME & SPACE COMPLEXITY ANALYSIS
================================================================================

SOLUTION 1 (Built-in Functions):
--------------------------------
- Input Reading: O(4) = O(1), because we read 4 inputs.
- map(int, ...): Each string conversion takes O(L), where L is the length of 
  the string. For 4 inputs, total O(4L) = O(L).
- pow(a, b): Python's built-in pow() uses fast exponentiation (exponentiation by 
  squaring). Time complexity is O(log b).
- pow(c, d): Similarly, O(log d).
- Total Time Complexity: O(L + log b + log d).
- Space Complexity: O(1) additional space beyond input storage, since pow() 
  operates efficiently.

SOLUTION 2 (Manual Implementation):
-----------------------------------
- Input Reading: O(4) = O(1).
- Manual Conversion: For each input of length L, conversion takes O(L). For 4 
  inputs, O(4L) = O(L).
- Manual power(a, b): Performs b multiplications. Time complexity is O(b).
- Manual power(c, d): Performs d multiplications. Time complexity is O(d).
- Total Time Complexity: O(L + b + d).
- Space Complexity: O(1) additional space beyond input storage, since we only 
  store a few integers and intermediate results.

================================================================================
COMPARISON:
- Built-in pow() is significantly faster because it uses exponentiation by 
  squaring (O(log n)) instead of repeated multiplication (O(n)).
- For very large exponents, Solution 1 is much more efficient.
- Both solutions demonstrate how Python can handle arbitrarily large integers.
"""
