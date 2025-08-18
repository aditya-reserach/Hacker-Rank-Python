"""
Problem Statement:
-----------------
Given an integer n, print the following values for each integer from 1 to n:

- Decimal
- Octal
- Hexadecimal (capitalized)
- Binary

All four values must be printed on a single line in the order specified above.
Each value should be right-aligned to match the width of the binary value of n.

Function Description:
---------------------
Complete the function `print_formatted(number)`.

Input:
------
A single integer denoting n.

Constraints:
------------
1 <= n <= 99

Output Format:
--------------
Print n lines, one for each integer from 1 to n.
Each line should contain the decimal, octal, hexadecimal, and binary values,
right-aligned to the width of the binary value of n.

Sample Input:
-------------
17

Sample Output:
--------------
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""

# ---------------------------------------------------------
# Approach 1: Using Built-in Conversions + rjust()
# ---------------------------------------------------------
def print_formatted_builtin(number):
    """
    Approach:
    - Use bin(), oct(), hex() built-ins for conversions.
    - Strip prefixes using slicing [2:].
    - Use rjust(width) to right-align columns.

    Time Complexity: O(n log n)
        - Each conversion takes O(log n) (depends on digits).
        - Loop runs n times.
    Space Complexity: O(log n)
        - Temporary string storage.
    """
    width = len(bin(number)) - 2  # length of binary representation without "0b"
    for i in range(1, number + 1):
        deci   = str(i).rjust(width)
        octal  = oct(i)[2:].rjust(width)
        hexa   = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(deci, octal, hexa, binary)


# ---------------------------------------------------------
# Approach 2: Without Using Prebuilt Functions
# ---------------------------------------------------------
def to_base(num, base):
    """Manual conversion of decimal to given base (2, 8, 16)."""
    digits = "0123456789ABCDEF"
    result = ""
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result if result != "" else "0"

def pad_right(text, width):
    """Manually pad spaces for right alignment."""
    return " " * (width - len(text)) + text

def print_formatted_manual(number):
    """
    Approach:
    - Implement base conversions manually (binary, octal, hex).
    - Implement manual right alignment instead of rjust().

    Time Complexity: O(n log n)
        - Each base conversion uses repeated division (O(log n)).
        - Loop runs n times.
    Space Complexity: O(log n)
        - Temporary strings for conversion.
    """
    width = len(to_base(number, 2))  # length of largest binary
    for i in range(1, number + 1):
        deci   = pad_right(str(i), width)
        octal  = pad_right(to_base(i, 8), width)
        hexa   = pad_right(to_base(i, 16), width)
        binary = pad_right(to_base(i, 2), width)
        print(deci, octal, hexa, binary)


# ---------------------------------------------------------
# Approach 3: Pythonic Solution with f-strings + bit_length()
# ---------------------------------------------------------
def print_formatted_fstring(number):
    """
    Approach:
    - Use f-strings with format specifiers.
    - Use number.bit_length() to determine width (binary length).
    - Built-in formatting supports decimal, octal, hex, and binary directly.

    Time Complexity: O(n log n)
        - Formatting each number depends on its digit length.
    Space Complexity: O(log n)
        - Temporary formatted strings.
    """
    pad = number.bit_length()  # number of bits required for binary of n
    for i in range(1, number + 1):
        # d = decimal, o = octal, X = hex uppercase, b = binary
        print(f"{i:>{pad}} {i:>{pad}o} {i:>{pad}X} {i:>{pad}b}")


# ---------------------------------------------------------
# Main Driver Code
# ---------------------------------------------------------
if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("\n--- Approach 1: Built-ins ---")
    print_formatted_builtin(n)

    print("\n--- Approach 2: Manual Conversion ---")
    print_formatted_manual(n)

    print("\n--- Approach 3: f-strings + bit_length ---")
    print_formatted_fstring(n)
