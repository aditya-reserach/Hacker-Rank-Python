"""
Problem Statement:
------------------
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase 
letters and vice versa.

For Example:
------------
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2       → pYTHONIST 2  

Function Description:
---------------------
Complete the swap_case function.

swap_case has the following parameters:
- string s: the string to modify

Returns:
--------
string: the modified string

Input Format:
-------------
A single line containing a string.

Constraints:
------------
- Only ASCII A-Z and a-z are considered letters.
- Other characters (digits, symbols, spaces) remain unchanged.

Sample Input 0:
---------------
HackerRank.com presents "Pythonist 2".

Sample Output 0:
----------------
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

# ------------------------------------------------------------
# Approach 1: Using Python's built-in swapcase()
# ------------------------------------------------------------
def swap_case_builtin(s: str) -> str:
    """
    Use Python's built-in str.swapcase() function.
    
    Time Complexity: O(n)  (n = length of string)
    Space Complexity: O(n) (new string created)
    """
    return s.swapcase()


# ------------------------------------------------------------
# Approach 2: Manual Implementation (No Prebuilt Functions)
# ------------------------------------------------------------
def swap_case_manual(s: str) -> str:
    """
    Manually swap cases without using str.swapcase(), lower(), upper(), 
    islower(), isupper(), etc.

    Logic:
    - 'a'..'z' → 'A'..'Z'  (subtract 32 in ASCII)
    - 'A'..'Z' → 'a'..'z'  (add 32 in ASCII)
    - Others unchanged

    Time Complexity: O(n)  (looping through all characters once)
    Space Complexity: O(n) (new list/string built)
    """
    result = []  # build output in a list for efficiency
    for ch in s:
        # if lowercase
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
        # if uppercase
        elif 'A' <= ch <= 'Z':
            result.append(chr(ord(ch) + 32))
        else:
            result.append(ch)  # keep unchanged (digits, spaces, symbols)
    return ''.join(result)


# ------------------------------------------------------------
# Main execution
# ------------------------------------------------------------
if __name__ == "__main__":
    s = input().strip()   # read input string
    
    # Uncomment one of the below lines depending on which approach you want
    
    # Approach 1: Using built-in function
    # print(swap_case_builtin(s))
    
    # Approach 2: Manual ASCII conversion (no prebuilt methods)
    print(swap_case_manual(s))
