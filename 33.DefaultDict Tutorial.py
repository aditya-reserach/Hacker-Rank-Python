"""
Problem Statement:
-------------------
You are given two integers n and m.
- The next n lines contain words (Group A).
- The following m lines contain words (Group B).

For each word in Group B:
    - If the word exists in Group A, print all the positions (1-based index) where it appeared in Group A.
    - If the word does not exist in Group A, print -1.

Example:
--------
Input:
5 2
a
b
a
a
b
a
b

Output:
1 3 4
2 5

Explanation:
- Group A words = ["a", "b", "a", "a", "b"]
- Group B words = ["a", "b"]
Word "a" occurs at positions 1, 3, 4 → print "1 3 4"
Word "b" occurs at positions 2, 5 → print "2 5"
"""

# -----------------------------
# CODE 1: Using defaultdict (prebuilt function)
# -----------------------------

from collections import defaultdict  # Importing defaultdict from collections

if __name__ == '__main__':  # Ensures code only runs when executed directly
    A = defaultdict(list)  # Create a dictionary where each key has a default empty list

    # Read n (words in Group A) and m (words in Group B)
    n, m = map(int, input().split())

    # Loop through total n+m inputs
    for i in range(1, n + m + 1):
        word = input()  # Read word input

        if i <= n:  
            # First n inputs belong to Group A
            # Append the index of the word into dictionary
            A[word].append(i)  

        elif word in A.keys():
            # If word is in Group A, print all its stored positions
            print(*A[word])  

        else:
            # If word not found in Group A, print -1
            print(-1)


# -----------------------------
# CODE 2: Without defaultdict (manual dictionary)
# -----------------------------

if __name__ == "__main__":  # Ensures code only runs when executed directly
    n, m = map(int, input().split())  # Read n and m

    A = {}  # Create a normal dictionary

    # Loop through n+m inputs
    for i in range(1, n + m + 1):
        word = input().strip()  # Read word input (strip removes extra spaces)

        if i <= n:
            # First n inputs are for Group A

            # If the word is not yet in dictionary, create an empty list
            if word not in A:
                A[word] = []
            
            # Append the index position of word
            A[word].append(i)  

        else:
            # Now handling Group B queries
            if word in A:
                # If word exists, print all stored positions
                print(*A[word]) 
            else:
                # If not found, print -1
                print(-1)


"""
-------------------------------------
Time Complexity Analysis:
-------------------------------------

Let:
- n = number of words in Group A
- m = number of queries in Group B

1. Building dictionary (first n inputs):
   - For each word, insertion into dictionary/list = O(1) average
   - Total = O(n)

2. Processing m queries (next m inputs):
   - Each query checks membership in dictionary = O(1) average
   - Printing positions takes O(k), where k = number of occurrences of word
   - Across all queries, total printing ≤ n (because each word position belongs to some query at most once)
   - Total = O(m + n)

➡ Overall Time Complexity = O(n + m)

-------------------------------------
Space Complexity Analysis:
-------------------------------------
- Dictionary stores all n words with their indices
- Each index is stored exactly once
- Extra memory for m queries (constant storage for word input)
- Total = O(n)

-------------------------------------
How to think for complexity:
-------------------------------------
1. Identify input sizes → n (Group A) + m (Group B).
2. Break problem into two parts:
   - Dictionary building (depends on n).
   - Query answering (depends on m).
3. Consider cost of operations:
   - Dictionary insertion = O(1).
   - Lookup in dictionary = O(1).
   - Printing = O(k), but total printing ≤ n.
4. Combine → O(n + m) time, O(n) space.
"""
