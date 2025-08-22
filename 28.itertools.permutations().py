#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 2: Generate all permutations of a string of length k
============================================================

You are given a string S and an integer k. 
The task is to print all possible permutations of size k from the string in lexicographic sorted order.

Input Format:
-------------
A single line containing a string and an integer separated by space.

Output Format:
--------------
Each permutation of length k printed on a separate line.

Sample Input:
-------------
HACK 2

Sample Output:
--------------
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

Explanation:
------------
All possible size k permutations of the string "HACK" are printed in lexicographic sorted order.
"""

# ====================================================
# Code 1: Using itertools.permutations
# ====================================================

from itertools import permutations  # Import prebuilt function to generate permutations

# Read input: string and k
s, k = input().split()  # Example input: "HACK 2"

# Loop through all permutations of length k from sorted string
for i in permutations(sorted(s), int(k)):
    # Each i is a tuple of characters, join to form string
    print(''.join(i))  # Print each permutation

"""
Explanation of Code 1:
----------------------
1. sorted(s) ensures lexicographic order of characters in the string.
2. permutations(sorted(s), int(k)) generates all possible length-k tuples.
3. ''.join(i) converts each tuple into a string for printing.
4. Directly prints permutations without storing all in a separate list (efficient memory use).

Time Complexity: O(k * P(n,k)) where P(n,k) = n!/(n-k)!
Space Complexity: O(1) additional space (generator used)
"""

# ====================================================
# Code 2: Manual Implementation (without prebuilt function)
# ====================================================

def permute(s, k):
    """
    Generate all permutations of length k from string s in lexicographic order
    using manual recursion (backtracking).
    
    Parameters:
    - s: input string
    - k: length of each permutation
    """

    # -----------------------------
    # Inner recursive function
    # -----------------------------
    def backtrack(path, used):
        """
        Recursive backtracking function to generate permutations.

        Parameters:
        - path: current permutation being built as a list of characters
        - used: boolean list indicating which characters in s are already used
        """
        # 1. Base Case: If the current path has length k
        if len(path) == k:
            # Join list of characters into string and print
            print("".join(path))
            return  # stop recursion for this path

        # 2. Iterate through all characters in the sorted string
        for i in range(len(s)):
            # Skip if this character is already used in current path
            if used[i]:
                continue

            # Skip duplicate characters to avoid repeated permutations
            # Only skip if it's the same as previous AND previous is not used
            if i > 0 and s[i] == s[i-1] and not used[i-1]:
                continue

            # 3. Choose the character s[i]
            path.append(s[i])  # add character to current path
            used[i] = True     # mark character as used

            # 4. Recurse to continue building the permutation
            backtrack(path, used)

            # 5. Undo the choice (backtrack) to explore other possibilities
            path.pop()        # remove last character
            used[i] = False   # mark character as unused for future paths

    # -----------------------------
    # Prepare for recursion
    # -----------------------------
    s = sorted(s)            # sort characters to ensure lexicographic order
    used = [False] * len(s)  # boolean array to track used characters
    backtrack([], used)       # start recursion with empty path

# ====================================================
# Main function to read input and call manual permute
# ====================================================
if __name__ == "__main__":
    # Read input line, e.g., "HACK 2"
    input_line = input().strip()
    
    # Split into string and k
    string_input, k_input = input_line.split()
    k_input = int(k_input)  # Convert k to integer

    # Call the manual permutation function
    permute(string_input, k_input)

"""
Explanation of Code 2:
----------------------
1. sort(s) ensures lexicographic order.
2. path stores current characters in recursion.
3. used array tracks characters already in path.
4. Recursive backtracking builds all permutations of length k.
5. Backtracking (append → recurse → pop) ensures all combinations are explored.
6. Avoids duplicates by checking previous character in sorted list.

Time Complexity: O(k * P(n,k)) where P(n,k) = n!/(n-k)!
Space Complexity: O(n + k) → used array O(n), path O(k), recursion stack O(k)
"""

# ====================================================
# Efficiency Ranking
# ====================================================
"""
Time Complexity (both codes generate all permutations):
1. Code 1 (itertools) = O(k * P(n,k))
2. Code 2 (manual)    = O(k * P(n,k))

Space Complexity:
1. Code 1 (itertools) = O(1) extra memory (uses generator)
2. Code 2 (manual)    = O(n + k) extra memory for recursion, used array, path

Conclusion:
-------------
- Code 1 is slightly more memory efficient due to generator.
- Code 2 is fully manual and good for understanding recursion and backtracking.
"""
