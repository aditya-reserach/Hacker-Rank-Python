"""
Problem Statement:
------------------
In Python, strings can be split and joined using built-in functions. 

Example:
    >>> a = "this is a string"
    >>> a = a.split(" ")   # a is converted to a list of strings. 
    >>> print(a)
    ['this', 'is', 'a', 'string']

    Joining a string is simple:
    >>> a = "-".join(a)
    >>> print(a)
    this-is-a-string 

Task:
-----
You are given a string. 
1. Split the string on a space delimiter (" ") 
2. Join the words using a hyphen ("-").

Function Description:
---------------------
Complete the split_and_join function.

split_and_join has the following parameters:
    string line: a string of space-separated words

Returns:
    string: the resulting string with words joined by '-'

Input Format:
-------------
- A single line containing a string consisting of space-separated words.

Output Format:
--------------
- A single line containing the modified string.

Sample Input:
-------------
this is a string

Sample Output:
--------------
this-is-a-string
"""

# -------------------------------------------------------
# Solution 1: Using Prebuilt Functions (split and join)
# -------------------------------------------------------

def split_and_join(line):
    """
    Approach:
    - Use str.split(" ") to split the string by spaces into a list of words.
    - Use str.join("-") to join the list back into a single string separated by "-".

    Time Complexity:
    - Splitting the string: O(n), where n is the length of the string
    - Joining the list: O(n), since all characters are traversed once
    - Overall: O(n)

    Space Complexity:
    - O(n) for storing the list of words
    """
    words = line.split(" ")   # Split on spaces
    return "-".join(words)    # Join using '-'


# -------------------------------------------------------
# Solution 2: Without Using Prebuilt Split/Join
# -------------------------------------------------------

def split_and_join_manual(line):
    """
    Approach:
    - Traverse the string character by character.
    - Build words manually (simulate split).
    - Store them in a list.
    - Then, construct the final string by inserting '-' manually (simulate join).

    Time Complexity:
    - Traversing the string once: O(n)
    - Constructing the output string: O(n)
    - Overall: O(n)

    Space Complexity:
    - O(n) for storing intermediate words and final result
    """
    words = []
    current_word = ""

    # Step 1: Manually split the string into words
    for char in line:
        if char == " ":
            if current_word != "":  # Only append if word is non-empty
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:  # Append the last word if exists
        words.append(current_word)

    # Step 2: Manually join words using '-'
    result = ""
    for i in range(len(words)):
        result += words[i]
        if i != len(words) - 1:  # Don't add '-' after the last word
            result += "-"

    return result


# -------------------------------------------------------
# Main Function: Execution starts here
# -------------------------------------------------------

if __name__ == '__main__':
    # Read input from user
    line = input().strip()

    # Using built-in functions
    result_builtin = split_and_join(line)
    print("Output using built-in functions:", result_builtin)

    # Using manual implementation
    result_manual = split_and_join_manual(line)
    print("Output using manual implementation:", result_manual)
