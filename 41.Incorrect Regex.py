"""
Problem Statement:
-----------------
You are given a string.
Your task is to find out whether it is a valid regex or not.

Input Format:
-------------
- The first line contains an integer T, the number of test cases.
- The next T lines each contain a string representing a regex pattern.

Constraints:
------------
- 1 <= T <= 100
- Length of regex string is reasonable to check validity.
- Input strings consist of standard regex characters.

Output Format:
--------------
For each test case, print "True" if the string is a valid regex,
otherwise print "False".

Sample Input:
-------------
2
.*\+
.*+

Sample Output:
--------------
True
False

Explanation:
------------
- ".*\+" is a valid regex (matches ".*" followed by a literal "+").
- ".*+" is invalid because "+" is applied to "*" (multiple repeat).
"""

# =====================================================================
# ✅ Solution 1: Using Python's built-in re.compile (Best HackerRank Style)
# =====================================================================

# Import the 're' module (regular expressions library in Python).
# This gives us the function re.compile() that can test if a regex is valid.
import re

# Step 1: Read number of test cases.
# raw_input() is used in Python 2 to read user input as a string.
# .strip() removes any leading or trailing spaces/newlines.
T = int(raw_input().strip())

# Step 2: Loop over the given number of test cases.
for _ in range(T):  # '_' is used because we don't need the loop variable.
    pattern = raw_input().strip()  # Read one regex string.
    try:
        # Step 3: Try compiling the regex pattern.
        # If it is valid, re.compile() succeeds.
        re.compile(pattern)
        print("True")   # If compilation successful, print True.
    except re.error:
        # Step 4: If regex compilation raises an error,
        # it means the regex is invalid.
        print("False")

"""
Time Complexity (Solution 1):
-----------------------------
- re.compile() runs in O(M), where M is the length of the regex string.
- Looping T test cases -> O(T * M).
- Space Complexity: O(1) extra (re.compile uses internal structures).
- Overall: O(T * M).
"""

# =====================================================================
# ✅ Solution 2: Manual Regex Validator (Without Prebuilt Functions)
# =====================================================================

# Import sys to read all input lines at once.
# This helps in handling multiple test cases efficiently.
import sys

# Define a function that manually checks if a regex string is valid.
def is_valid_regex(p):
    n = len(p)           # Total length of regex string.
    i = 0                # Pointer/index to traverse the string.
    stack = []           # Used for keeping track of '(' and ')'.
    prev = None          # Stores the type of previous character.

    # Traverse through all characters of the string.
    while i < n:
        ch = p[i]        # Current character at position i.

        # Case 1: Escape sequence (e.g., \+)
        if ch == '\\':
            i += 1       # Move to next character.
            if i >= n:   # If '\' is last character, invalid.
                return False
            prev = 'literal'  # Escaped character counts as literal.
            i += 1       # Move past escaped character.
            continue

        # Case 2: Opening parenthesis '('
        if ch == '(':
            stack.append(')')  # Push closing bracket expectation.
            prev = 'open'      # Last seen was an opening bracket.
            i += 1
            continue

        # Case 3: Closing parenthesis ')'
        if ch == ')':
            if not stack or stack.pop() != ')':  # Check balance.
                return False
            prev = 'close'  # Last seen was a closing bracket.
            i += 1
            continue

        # Case 4: Character set '[ ... ]'
        if ch == '[':
            j = i + 1
            if j >= n:
                return False
            found = False
            while j < n:
                if p[j] == '\\':  # Skip escaped chars inside [].
                    j += 2
                    continue
                if p[j] == ']':   # Found closing bracket.
                    found = True
                    break
                j += 1
            if not found:
                return False
            prev = 'literal'
            i = j + 1   # Move pointer after ']'
            continue

        # Case 5: Quantifiers {m,n}
        if ch == '{':
            j = i + 1
            if j < n and p[j].isdigit():
                while j < n and p[j].isdigit():
                    j += 1
                if j < n and p[j] == ',':
                    j += 1
                    while j < n and p[j].isdigit():
                        j += 1
                if j < n and p[j] == '}':
                    if prev not in ('literal', 'close'):
                        return False
                    prev = 'quantifier'
                    i = j + 1
                    continue
            prev = 'literal'
            i += 1
            continue

        # Case 6: Quantifiers *, +, ?
        if ch in '*+?':
            if prev not in ('literal', 'close'):  # Must follow a literal.
                return False
            prev = 'quantifier'
            i += 1
            continue

        # Case 7: Extra closing brackets '}' or ']'
        if ch == '}' or ch == ']':
            return False

        # Default: Treat as literal.
        prev = 'literal'
        i += 1

    # At the end, check if stack is empty (all '(' closed).
    if stack:
        return False
    return True

# Step 1: Read all input lines.
data = sys.stdin.read().strip().splitlines()
if not data:
    sys.exit(0)

# Step 2: First line is number of test cases.
t = int(data[0].strip())

# Step 3: Process each regex string line.
for line in data[1:1+t]:
    s = line.rstrip('\n')  # Remove trailing newline.
    print("True" if is_valid_regex(s) else "False")

"""
Time Complexity (Solution 2):
-----------------------------
- We scan each regex string once, character by character: O(M).
- Checking brackets, sets, and quantifiers involves inner scanning but each character is processed only once overall.
- So each string is validated in O(M).
- For T test cases -> O(T * M).
- Space Complexity: O(M) in worst case (stack + temporary parsing).
"""
