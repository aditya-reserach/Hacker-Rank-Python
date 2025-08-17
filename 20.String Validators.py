"""
Problem Statement:
------------------
Python has built-in string validation methods for basic data. 
It can check if a string is composed of alphabetical characters, 
alphanumeric characters, digits, etc.

Methods Recap:
--------------
- str.isalnum() → True if all characters are alphanumeric (a-z, A-Z, 0-9)
- str.isalpha() → True if all characters are alphabets (a-z, A-Z)
- str.isdigit() → True if all characters are digits (0-9)
- str.islower() → True if all characters are lowercase (a-z)
- str.isupper() → True if all characters are uppercase (A-Z)

Task:
-----
You are given a string.
Your task is to find out if the string contains:
1. Any alphanumeric characters
2. Any alphabetical characters
3. Any digits
4. Any lowercase characters
5. Any uppercase characters

Input Format:
-------------
- A single line containing a string.

Output Format:
--------------
- In the first line, print True if the string has any alphanumeric characters, else False.
- In the second line, print True if the string has any alphabetical characters, else False.
- In the third line, print True if the string has any digits, else False.
- In the fourth line, print True if the string has any lowercase characters, else False.
- In the fifth line, print True if the string has any uppercase characters, else False.

Sample Input:
-------------
qA2

Sample Output:
--------------
True
True
True
True
True
"""

# ---------------------------------------------------------------------------
# Approach 1: Using Built-in String Methods
# ---------------------------------------------------------------------------
# - Python provides built-in methods like isalnum(), isalpha(), etc.
# - We can use a generator expression inside any() to check if at least
#   one character in the string satisfies the condition.
#
# Time Complexity: O(n), where n = length of string
# (We may check each character once in worst case).
# Space Complexity: O(1), only boolean values stored.
# ---------------------------------------------------------------------------

def validate_with_builtins(s):
    # Check if there is at least one alphanumeric character
    print(any(c.isalnum() for c in s))

    # Check if there is at least one alphabetic character
    print(any(c.isalpha() for c in s))

    # Check if there is at least one digit
    print(any(c.isdigit() for c in s))

    # Check if there is at least one lowercase character
    print(any(c.islower() for c in s))

    # Check if there is at least one uppercase character
    print(any(c.isupper() for c in s))


# ---------------------------------------------------------------------------
# Approach 2: Without Using Built-in Methods
# ---------------------------------------------------------------------------
# - Instead of prebuilt methods, we use ASCII values to check.
#   ord(c) gives ASCII value of a character c.
#   '0'–'9' → 48–57
#   'A'–'Z' → 65–90
#   'a'–'z' → 97–122
# - We manually check whether characters fall into these ranges.
#
# Time Complexity: O(n), we traverse the string once.
# Space Complexity: O(1), only a few booleans used.
# ---------------------------------------------------------------------------

def validate_without_builtins(s):
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    for c in s:
        ascii_val = ord(c)  # convert char → ASCII

        # Check alphanumeric (digit OR alphabet)
        if (48 <= ascii_val <= 57) or (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
            has_alnum = True

        # Check alphabet
        if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
            has_alpha = True

        # Check digit
        if 48 <= ascii_val <= 57:
            has_digit = True

        # Check lowercase
        if 97 <= ascii_val <= 122:
            has_lower = True

        # Check uppercase
        if 65 <= ascii_val <= 90:
            has_upper = True

    # Print results
    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)


# ---------------------------------------------------------------------------
# Driver Code
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    s = input("Enter a string: ")

    print("\n--- Using Built-in Methods ---")
    validate_with_builtins(s)

    print("\n--- Without Using Built-in Methods ---")
    validate_without_builtins(s)
