"""
==============================
Problem Statement
==============================
You are given two integers n and m.

- First, you will input n words (Group A).
- Then, you will input m words (Group B).

For each word in Group B, you must print the positions (indices) where that word appeared in Group A.
If the word does not appear in Group A, print -1.

Example:
---------
Input:
5 2
a
b
a
c
a
a
d

Output:
1 3 5
-1

Explanation:
-------------
- Group A = ["a", "b", "a", "c", "a"]
- Group B = ["a", "d"]

For "a" → appears at positions [1, 3, 5].
For "d" → does not appear → print -1.
"""


# ========================================================
# CODE 1: Using collections.defaultdict (Prebuilt Function)
# ========================================================
from collections import defaultdict

if __name__ == "__main__":
    # Read n and m from input
    n, m = map(int, input().split())

    # Create defaultdict with list as default type
    # This allows appending without checking if key exists
    A = defaultdict(list)

    # Loop from 1 to n+m (1-indexed as per problem statement)
    for i in range(1, n + m + 1):
        word = input().strip()  # Read each word

        if i <= n:
            # First n words → belongs to Group A
            # Store the index where the word appeared
            A[word].append(i)
        else:
            # Remaining m words → belongs to Group B
            if word in A:  # If word exists in Group A
                print(*A[word])  # Print all indices
            else:
                print(-1)  # Word not found


"""
==============================
Time Complexity (Code 1)
==============================
- Reading n + m words → O(n + m).
- Storing Group A (n words) → Each insertion into defaultdict list is O(1).
  Total = O(n).
- Querying Group B (m words):
    - Lookup in dictionary (hashmap) → O(1) average.
    - Printing indices → O(k), where k = occurrences of word.
  Total = O(m + total output size).
Overall Time Complexity: O(n + m + total_output).

==============================
Space Complexity (Code 1)
==============================
- Dictionary stores n keys (unique words at most) with lists.
- Worst case → each of n words is unique → O(n).
- Extra input storage negligible.
Overall Space Complexity: O(n).
"""


# ========================================================
# CODE 2: Without Prebuilt Function (Manual Dictionary)
# ========================================================
if __name__ == "__main__":
    # Read n and m from input
    n, m = map(int, input().split())

    # Normal dictionary for storing Group A word positions
    A = {}

    # Loop through n+m words
    for i in range(1, n + m + 1):
        word = input().strip()

        if i <= n:
            # First n words → Group A
            # If word not in dictionary, create an empty list
            if word not in A:
                A[word] = []
            # Append current index
            A[word].append(i)
        else:
            # Group B words
            if word in A:  # If word exists in Group A
                print(*A[word])  # Print indices
            else:
                print(-1)  # Not found


"""
==============================
Time Complexity (Code 2)
==============================
- Reading n + m words → O(n + m).
- Storing Group A (n words):
    - Each dictionary insertion/search is O(1) average.
    - Total = O(n).
- Querying Group B (m words):
    - Lookup O(1) average per query.
    - Printing indices O(k).
    - Total = O(m + total output size).
Overall Time Complexity: O(n + m + total_output).

==============================
Space Complexity (Code 2)
==============================
- Dictionary stores up to n unique words with lists of indices.
- Worst case space = O(n).
- No extra library overhead.
Overall Space Complexity: O(n).
"""
