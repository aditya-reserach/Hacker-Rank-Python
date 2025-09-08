"""
Problem Statement:
------------------
In this challenge, you are asked to compute a score for a list of words based on the number of vowels each word contains.

Vowels are defined as: a, e, i, o, u, y

Scoring Rules:
- If a word contains an even number of vowels, its score is 2
- If a word contains an odd number of vowels, its score is 1
- The total score for the list is the sum of the scores of all words

Input Format:
-------------
- The first line contains a single integer n, the number of words.
- The second line contains n space-separated lowercase words.

Constraints:
------------
- Each word contains only lowercase English letters.
- Each word has at most 100 characters.

Output Format:
--------------
- Print a single integer: the total score.

Sample Input 0:
---------------
2
hacker book

Sample Output 0:
----------------
4

Explanation 0:
---------------
- 'hacker' has 2 vowels (even) → score 2
- 'book' has 2 vowels (even) → score 2
- Total score = 2 + 2 = 4

Sample Input 1:
---------------
3
programming is awesome

Sample Output 1:
----------------
4

Explanation 1:
---------------
- 'programming' has 3 vowels (odd) → score 1
- 'is' has 1 vowel (odd) → score 1
- 'awesome' has 4 vowels (even) → score 2
- Total score = 1 + 1 + 2 = 4
"""

# ------------------------- Solution 1: Using Python built-in functions/libraries -------------------------
import re, sys  # import 're' for regular expressions, 'sys' for reading input from stdin

# Compile a regex pattern to match any vowel (a, e, i, o, u, y)
# Using re.compile improves efficiency if the pattern is used multiple times
pat = re.compile(r'[aeiouy]')

# Read all input lines at once from standard input
# Example input: "2\nhacker book\n"
# .splitlines() splits input into a list of lines: ["2", "hacker book"]
# [1] selects the second line, which contains the words
# .split() splits the line into individual words: ["hacker", "book"]
l = sys.stdin.read().splitlines()[1].split()

# Initialize total score counter
total = 0

# Loop over each word in the list
for word in l:
    # re.findall(pat, word) finds all vowels in the current word
    # len(...) counts how many vowels are present
    # '& 1' checks if the count is odd (bitwise AND with 1)
    # 1 if count is odd, else 2 if count is even
    # Add this value to the running total
    total += 1 if len(re.findall(pat, word)) & 1 else 2

# Print the total score
print(total)

"""
Time and Space Complexity for Solution 1:
-----------------------------------------
Let n = number of words, m = average length of each word, N = total characters (n*m)

Time Complexity:
- Outer loop: runs n times → O(n)
- re.findall(pat, word) scans each character of the word → O(m)
- Total: O(n*m) = O(N)
- All other operations (len, &, addition) are O(1) → negligible

Space Complexity:
- pat is compiled once → O(1)
- re.findall creates a temporary list of vowels of size up to m → O(m) per word
- Total: O(m) temporary space

This is efficient and suitable for large inputs.
"""

# ------------------------- Solution 2: Manual implementation without prebuilt helpers -------------------------
import re  # import regex module

# Read number of words (though we do not actually need to use it)
n = int(input())

# Read the words as a list
s = input().split()

# Regex pattern as a string (not compiled)
ex = r'[aeiouy]'

# Initialize total score
score = 0

# Loop through each word in the list
for word in s:
    # re.findall(ex, word) finds all vowels in the current word
    # len(...) counts how many vowels
    a = len(re.findall(ex, word))
    
    # If the number of vowels is even, add 2 to the score
    if a % 2 == 0:
        score += 2
    # If the number of vowels is odd, add 1 to the score
    else:
        score += 1

# Print the final score
print(score)

"""
Time and Space Complexity for Solution 2:
-----------------------------------------
Let n = number of words, m = average length of each word, N = total characters (n*m)

Time Complexity:
- Outer loop: runs n times → O(n)
- re.findall(ex, word) scans each character of the word → O(m)
- Total: O(n*m) = O(N)
- Modulo operation and addition are O(1) → negligible

Space Complexity:
- re.findall creates a temporary list of vowels up to size m → O(m) per word
- Pattern string is stored → O(1)
- Total: O(m) temporary space

Notes:
- Solution 1 may be slightly faster in practice because the regex is compiled once.
- Solution 2 is easier to read and understand for beginners.
"""


