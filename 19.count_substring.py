"""
Problem Statement:
------------------
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format:
-------------
The first line of input contains the original string.
The second line contains the substring.

Output Format:
--------------
Output a single integer: the total number of occurrences of the substring in the original string.

Constraints:
------------
- Each character in the string is an ASCII character.

Sample Input:
--------------
ABCDCDC
CDC

Sample Output:
--------------
2

Time Complexity Analysis:
-------------------------
- Let n = length of the main string
- Let m = length of the substring

1. The loop runs (n - m + 1) times.
2. Each substring comparison (string[i:i+m]) takes O(m) time in the worst case.
3. Therefore, total time complexity = O(n * m).
4. Space complexity = O(1), since we only use a counter variable.
"""


def count_substring(string, sub_string):
    # Initialize a counter to keep track of how many times
    # we find 'sub_string' inside 'string'.
    count = 0

    # We want to slide a window of length equal to 'sub_string'
    # across 'string'. The last valid starting point for this
    # window is at index: len(string) - len(sub_string).
    # That's why the range ends at (len(string) - len(sub_string) + 1).
    for i in range(len(string) - len(sub_string) + 1):

        # For each position i, we extract a slice of 'string'
        # starting at index i and having length equal to 'sub_string'.
        # Example: if string = "ABCDCDC", sub_string = "CDC"
        # and i = 2 → string[2:5] = "CDC".
        # This slice operation creates a temporary substring to compare.
        if string[i:i+len(sub_string)] == sub_string:

            # If the extracted slice matches sub_string,
            # we increase our counter by 1.
            count += 1

    # After the loop finishes, 'count' holds the total number
    # of times 'sub_string' appeared in 'string'.
    return count


if __name__ == '__main__':
    # Take input for the main string from the user.
    # .strip() removes leading/trailing spaces or newline characters.
    string = input().strip()

    # Take input for the substring to search.
    sub_string = input().strip()

    # Call our function with the given inputs.
    result = count_substring(string, sub_string)

    # Print the result, which is the number of times the substring occurs.
    print(result)
