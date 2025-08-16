"""
=====================================================
Problem: Swap Case
=====================================================

You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase 
letters and vice versa.

-----------------------------------------------------
Example:
-----------------------------------------------------
Input:  Www.HackerRank.com
Output: wWW.hACKERrANK.COM

Input:  Pythonist 2
Output: pYTHONIST 2

-----------------------------------------------------
Function Description:
-----------------------------------------------------
Complete the function swap_case(s):

Parameters:
    string s: the string to modify

Returns:
    string: the modified string

-----------------------------------------------------
Input Format:
-----------------------------------------------------
A single line containing a string s.

-----------------------------------------------------
Constraints:
- String length <= 1000
- Characters may include letters, digits, spaces, and symbols

-----------------------------------------------------
Sample Input 0:
-----------------------------------------------------
HackerRank.com presents "Pythonist 2".

-----------------------------------------------------
Sample Output 0:
-----------------------------------------------------
hACKERrANK.COM PRESENTS "pYTHONIST 2".
=====================================================
"""

# =====================================================
# APPROACH 1: Using built-in function swapcase()
# =====================================================
def swap_case_with_builtin(s: str) -> str:
    """
    Uses Python's built-in str.swapcase() method
    which automatically flips the case of all letters.
    
    Time Complexity: O(n), where n = length of string
    Space Complexity: O(n), new string is created
    """
    return s.swapcase()


# =====================================================
# APPROACH 2: Manual implementation (without built-in)
# =====================================================
def swap_case_manual(s: str) -> str:
    """
    Manually swap cases by iterating over characters:
    - If char is lowercase, convert to uppercase
    - If char is uppercase, convert to lowercase
    - Else (digits, spaces, symbols), keep unchanged
    
    Time Complexity: O(n), where n = length of string
    Space Complexity: O(n), result string is created
    """
    result = ""  # empty string to build output
    
    for char in s:  # iterate through each character
        if char.islower():        # if character is lowercase
            result += char.upper()
        elif char.isupper():      # if character is uppercase
            result += char.lower()
        else:                     # if it's a number/symbol/space
            result += char
    
    return result


# =====================================================
# MAIN DRIVER CODE
# =====================================================
if __name__ == "__main__":
    s = input().strip()  # read input string
    
    # Option 1: Using built-in
    # print(swap_case_with_builtin(s))
    
    # Option 2: Manual (without built-in)
    print(swap_case_manual(s))
