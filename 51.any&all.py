"""
===============================================
Problem Statement
===============================================

You are given a space separated list of integers. 
If all the integers are positive, then you need to check 
if any integer is a palindromic integer.

-----------------------------------------------
Input Format
-----------------------------------------------
- The first line contains an integer n, the total number of integers in the list.
- The second line contains the space separated list of n integers.

-----------------------------------------------
Output Format
-----------------------------------------------
- Print True if all the conditions of the problem statement are satisfied.
- Otherwise, print False.

-----------------------------------------------
Constraints
-----------------------------------------------
- 1 <= n <= 10^5  (number of integers can be large)
- Each integer may have multiple digits.
- Integers can be positive or negative.

-----------------------------------------------
Sample Input
-----------------------------------------------
5
12 9 61 5 14

-----------------------------------------------
Sample Output
-----------------------------------------------
True

-----------------------------------------------
Explanation
-----------------------------------------------
Condition 1: All the integers in the list are positive.
Condition 2: 9 and 5 are palindromic integers.
Both conditions are satisfied → Output is True.
"""

# ==========================================================
# Solution 1: Using Python Built-in Functions (Concise Way)
# ==========================================================

# Read the first input line, which is the number of integers (n).
n = int(input())

# Read the second input line, split it into parts (strings of numbers).
# These are not yet integers, so we keep them as strings first.
arr = input().split()

# Use Python's built-in 'all()' to check if every number > 0.
# We cast each element 'x' into an integer before comparing.
# 'all()' returns True if all comparisons are True, otherwise False.
all_positive = all(int(x) > 0 for x in arr)

# Use Python's built-in 'any()' to check if at least one palindrome exists.
# For palindrome check: 'x == x[::-1]' reverses the string and compares.
# If any element satisfies this, 'any()' returns True.
has_palindrome = any(x == x[::-1] for x in arr)

# Print the final result: both conditions must be True.
print(all_positive and has_palindrome)


# ----------------------------------------------------------
# Time Complexity (Solution 1)
# ----------------------------------------------------------
# - all(): iterates over n elements, each int(x) takes O(1) → O(n).
# - any(): iterates over n elements, each palindrome check compares digits.
#   If max digits per number = d, checking x == x[::-1] costs O(d).
#   → Total = O(n * d).
# - Overall: O(n * d).
#
# Space Complexity:
# - arr stores n numbers as strings → O(n * d).
# - No extra significant memory besides arr.
# - Overall: O(n * d).



# ==========================================================
# Solution 2: Manual Implementation Without Built-ins
# ==========================================================

# Read the first input line again (n = number of integers).
n = int(input())

# Read the second input line, split it into integers directly.
arr = list(map(int, input().split()))

# Flag to check if all numbers are positive.
all_positive = True

# Flag to check if at least one number is a palindrome.
has_palindrome = False

# Iterate through each number in the list.
for num in arr:
    # Check positivity: if any number <= 0, condition fails.
    if num <= 0:
        all_positive = False

    # ----------------------------
    # Palindrome Check (Manual)
    # ----------------------------
    # Make a copy of the number into 'temp' because we will modify it.
    temp = num

    # Variable to hold the reversed number we will build.
    rev = 0

    # Loop until 'temp' becomes zero.
    while temp > 0:
        # Extract the last digit of 'temp' using modulo 10.
        digit = temp % 10

        # Add this digit to the reversed number.
        # Multiply rev by 10 (shift digits left), then add digit.
        rev = rev * 10 + digit

        # Remove the last digit from 'temp' by integer division by 10.
        temp //= 10

    # After the loop ends, 'rev' holds the reversed version of num.
    # If the reversed number equals the original, it's a palindrome.
    if rev == num:
        has_palindrome = True

# Print the final result.
print(all_positive and has_palindrome)


# ----------------------------------------------------------
# Time Complexity (Solution 2)
# ----------------------------------------------------------
# - Loop goes over n numbers.
# - For each number, we perform digit extraction and reversal.
#   If a number has d digits, reversing it costs O(d).
# - Total = O(n * d).
#
# Space Complexity:
# - Only uses a few integer variables (temp, rev, digit, flags).
# - No extra arrays or strings allocated.
# - Overall: O(1) additional space (besides input array).
