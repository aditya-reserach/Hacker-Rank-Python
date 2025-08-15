"""
Problem Statement:
------------------
You are given a list of words. Some words may appear more than once.

Your task is to:
1. Print the total number of **distinct words**.
2. Print the number of **occurrences of each distinct word**, in the order they first appeared.

Definitions:
- A distinct word: a word that appears at least once.
- Order of first appearance: If a word appears more than once, count it only the first time when ordering.

Input Format:
-------------
The first line contains an integer N — the number of words.
The next N lines each contain one word (lowercase English letters only).

Output Format:
--------------
On the first line, print the number of distinct words.
On the second line, print the frequencies of these distinct words (in the order of first appearance), space-separated.

Constraints:
------------
- 1 <= N <= 10^5
- Words consist only of lowercase English letters (a-z)

Sample Input:
-------------
4
bcdef
abcdefg
bcde
bcdef

Sample Output:
--------------
3
2 1 1

Explanation:
------------
- "bcdef" appears twice.
- "abcdefg" and "bcde" appear once.
- Order of appearance: bcdef, abcdefg, bcde → so output their counts in that order.

"""

# ------------------------------------------
# Approach 1: Using collections.Counter
# ------------------------------------------

from collections import Counter

# Step 1: Read number of words
n = int(input())

# Step 2: Read all words into a list
words = [input().strip() for _ in range(n)]

# Step 3: Use Counter to count occurrences
# Counter maintains insertion order in Python 3.7+
word_counts = Counter(words)

# Step 4: Print total number of distinct words
print(len(word_counts))

# Step 5: Print the frequencies in order of first appearance
print(*word_counts.values())

# Time Complexity:
# ----------------
# - Reading input: O(N)
# - Counting words using Counter: O(N)
# - Printing results: O(N)
# => Overall Time Complexity: **O(N)**

# Space Complexity:
# -----------------
# - Storing words: O(N)
# - Counter storage: O(M), where M = number of distinct words
# => Overall Space: **O(N)**

# ------------------------------------------
# Approach 2: Manual Dictionary Counting
# ------------------------------------------

# Step 1: Read number of words
n = int(input())

# Step 2: Use an ordinary dictionary to count word frequencies
word_counts = {}  # Maintains order of insertion since Python 3.7+

# Step 3: Read and count words
for _ in range(n):
    word = input().strip()
    if word in word_counts:
        word_counts[word] += 1  # Increment count if word already exists
    else:
        word_counts[word] = 1   # Add new word with initial count 1

# Step 4: Print number of unique words
print(len(word_counts))

# Step 5: Print frequencies in the order of first appearance
print(*word_counts.values())

# Time Complexity:
# ----------------
# - Reading input: O(N)
# - Each dictionary operation (check + insert/update): O(1) average
# - Final print loop: O(N)
# => Overall Time Complexity: **O(N)**

# Space Complexity:
# -----------------
# - Dictionary stores up to N unique words: O(N)
# => Overall Space: **O(N)**
