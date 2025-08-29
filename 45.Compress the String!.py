"""
Problem Statement:

In this task, we would like for you to appreciate the usefulness of the groupby() 
function of itertools. 

You are given a string S. Suppose a character 'c' occurs consecutively 'k' times in the string.
Replace these consecutive occurrences with (k, c) in the output.

Input Format:
    - A single line of input consisting of the string S.

Output Format:
    - A single line of output consisting of the modified string, where each group is represented as (count, digit).

Constraints:
    - All characters of S are digits between 0 and 9.

Example:
    Input:
        1222311
    Output:
        (1, 1) (3, 2) (1, 3) (2, 1)

Explanation:
    - The character '1' occurs once → (1, 1)
    - The character '2' occurs three times → (3, 2)
    - The character '3' occurs once → (1, 3)
    - The character '1' occurs twice → (2, 1)
"""

# --------------------------------------------------------------------------
# Solution 1: Using itertools.groupby() (Prebuilt Function)
# --------------------------------------------------------------------------

from itertools import groupby  # Importing the groupby function

# Take input from the user (a string of digits)
s = input()

# Iterate through grouped characters
for k, g in groupby(s):
    # 'k' is the current character
    # 'g' is an iterator over the group of consecutive characters
    # Convert group to list to count elements → len(list(g))
    # Convert character 'k' to integer
    # Print the tuple (count, number) with a space, no newline
    print(tuple([len(list(g)), int(k)]), end=' ')

# ---------------- Time Complexity Analysis (Solution 1) -------------------
# Let n = length of string
# - groupby(s) iterates through string once → O(n)
# - len(list(g)) builds a list of group elements → total across all groups = O(n)
# Overall Time Complexity: O(n)
# Space Complexity: O(n) (since lists of groups are created)


# --------------------------------------------------------------------------
# Solution 2: Without Prebuilt Functions (Manual Implementation)
# --------------------------------------------------------------------------

# Take input again (fresh run)
s = input()

# Initialize an empty list to store the result tuples
result = []

# Initialize counter to count consecutive occurrences
count = 1

# Start loop from 1 because we compare with the previous character
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        # If current char equals previous, increment count
        count += 1
    else:
        # If current char is different, the previous group ends
        # Append the tuple (count, int(previous character))
        result.append((count, int(s[i-1])))
        # Reset count for the new group
        count = 1

# After the loop, last group is not yet added
# Append the final group (count, last character)
result.append((count, int(s[-1])))

# Print result in the required format
for tup in result:
    print(tup, end=' ')

# ---------------- Time Complexity Analysis (Solution 2) -------------------
# Let n = length of string
# - Loop runs once through the string → O(n)
# - Appending to list is O(1) amortized
# Overall Time Complexity: O(n)
# Space Complexity: O(n) (result list stores group tuples)
