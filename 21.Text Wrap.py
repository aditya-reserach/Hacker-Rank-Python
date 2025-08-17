"""
Problem: Text Wrap (HackerRank)

You are given a string and a width.
Your task is to wrap the string into a paragraph of the given width.

Function Description:
---------------------
Complete the function wrap(string, max_width).

Parameters:
    string (str): a long string to wrap
    max_width (int): the width to wrap to

Returns:
    str: a single string with newline characters ('\n') where the breaks should be

Input Format:
-------------
- The first line contains a string, string.
- The second line contains the width, max_width.

Constraints:
------------
- 0 < len(string) <= 1000
- 0 < max_width <= len(string)

Sample Input 0:
---------------
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0:
----------------
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

# -------------------------------------------------------------------
# Approach A: Using basic Python built-ins (range, slicing, join)
# -------------------------------------------------------------------
def wrap_builtin(string, max_width):
    """
    This function splits the string into chunks of length max_width
    using slicing inside a loop, and then joins them with '\n'.
    """
    result = []
    # Loop from 0 until end of string, moving in steps of max_width
    for i in range(0, len(string), max_width):
        # Slice from i to i+max_width
        result.append(string[i:i+max_width])
    # Join all chunks into a single string separated by newline
    return "\n".join(result)

# Time Complexity:
# ----------------
# Loop runs n/max_width times, but each character is touched once.
# O(n) time, where n = len(string).
# O(n) space for storing result list.


# -------------------------------------------------------------------
# Approach B: Without using prebuilt functions (manual implementation)
# -------------------------------------------------------------------
def wrap_manual(string, max_width):
    """
    This function avoids using join, range, or append.
    It manually builds the result by counting characters
    and inserting a newline after every max_width characters.
    """
    result = ""   # Final wrapped string
    count = 0     # Counter for current line length
    
    # Loop over each character in the string
    for ch in string:
        result += ch       # Add character to the result
        count += 1         # Increase counter
        
        # If we reached max_width characters, insert newline
        if count == max_width:
            result += "\n"
            count = 0      # Reset counter for next line
    
    return result

# Time Complexity:
# ----------------
# Each character is processed exactly once.
# O(n) time, where n = len(string).
# O(n) space for the result string.


# -------------------------------------------------------------------
# Driver code
# -------------------------------------------------------------------
if __name__ == '__main__':
    # Read input values
    string = input().strip()
    max_width = int(input().strip())

    # Run both approaches and print results
    print("----- Approach A (Using Built-ins) -----")
    print(wrap_builtin(string, max_width))

    print("----- Approach B (Manual, No Built-ins) -----")
    print(wrap_manual(string, max_width))
