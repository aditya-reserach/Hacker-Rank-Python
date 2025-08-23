"""
Problem Statement:
------------------
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321

Constraints:
------------
- Only one for-statement can be used.
- Only one print statement can be used.
- No string operations allowed.
- Palindromic pattern must be generated using arithmetic.
"""

# ----------------------------------------------------------
# CODE 1 : Using built-in function `pow`
# ----------------------------------------------------------

for i in range(1, int(input()) + 1):        # Loop from 1 up to N (inclusive), user inputs N
    print((pow(10, i) // 9) ** 2)           # Formula: (111...i)^2 generates the palindromic number

"""
Explanation of each line:
-------------------------
for i in range(1, int(input()) + 1):  
    - Takes integer input N from the user.
    - range(1, N+1) generates numbers 1,2,3,...,N.
    - Loop variable i represents the current row number.

print((pow(10, i) // 9) ** 2)  
    - pow(10, i) → gives 10^i.
    - pow(10, i) // 9 → creates a number with 'i' ones (e.g., 111..i times).
    - Example: pow(10, 3) = 1000 → 1000//9 = 111
    - Squaring this gives the palindromic row (111^2 = 12321).
    - This prints each line of the palindromic triangle.
"""

# Time Complexity: O(N)   → one loop runs N times, pow is O(1) per call.
# Space Complexity: O(1) → no extra memory used.


# ----------------------------------------------------------
# CODE 2 : Without using any prebuilt function (manual calculation)
# ----------------------------------------------------------

N = int(input())                            # Take input from user for triangle size
for i in range(1, N + 1):                   # Loop from 1 up to N (inclusive)
    num = 0                                 # Start with 0 for constructing the "111...i" number
    for j in range(i):                      # Inner loop to build number manually
        num = num * 10 + 1                  # Multiply existing number by 10 and add 1 → appends '1'
    print(num * num)                        # Square the built number to print palindrome row

"""
Explanation of each line:
-------------------------
N = int(input())  
    - Reads integer input for triangle size.

for i in range(1, N + 1):  
    - Outer loop from 1 to N, represents row number.

num = 0  
    - Initialize num = 0 before constructing the repeated ones.

for j in range(i):  
    - Inner loop runs 'i' times to construct number like 1, 11, 111, etc.

num = num * 10 + 1  
    - Appends digit '1' at the end of current number.
    - Example: i=3 → step1: num=1 → step2: num=11 → step3: num=111.

print(num * num)  
    - Squares the constructed number.
    - Automatically generates palindromic number.
"""

# Time Complexity: O(N^2) → Outer loop runs N times, inner loop runs up to i (1+2+...+N = O(N^2)).
# Space Complexity: O(1) → Only variables used, no extra space.

# ----------------------------------------------------------
# END OF FILE
# ----------------------------------------------------------
