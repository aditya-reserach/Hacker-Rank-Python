#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 3: Generate all combinations of a string up to length k
===============================================================

You are given a string S and an integer k. 
The task is to print all possible combinations, of lengths 1 to k, from the string in lexicographic sorted order.

Input Format:
-------------
A single line containing a string and an integer separated by space.

Output Format:
--------------
Each combination printed on a separate line.

Sample Input:
-------------
HACK 2

Sample Output:
--------------
A
C
H
K
AC
AH
AK
CH
CK
HK
"""

# ====================================================
# Code 1: Using itertools.combinations
# ====================================================
from itertools import combinations  # import prebuilt combinations function

# Read input: string and k
s, k = input().split()  # Example input: "HACK 2"

# Generate all combinations for lengths 1 to k
# sorted(s) ensures lexicographic order
# For each length r (1 to k), generate combinations and join tuple into string
print('\n'.join(''.join(c) for r in range(int(k)) for c in combinations(sorted(s), r + 1)))

"""
Explanation of Code 1:
----------------------
1. sorted(s) → ensures lexicographic order of characters.
2. range(int(k)) → iterate over lengths 0 to k-1 (we add 1 for actual length r+1).
3. combinations(sorted(s), r + 1) → generates all combinations of length r+1 as tuples.
4. ''.join(c) → convert tuple of characters into string.
5. '\n'.join(...) → join all combinations by newline and print at once.
6. Efficient memory use: itertools generates combinations on-the-fly (generator).

Time Complexity: O(Σ C(n,r) * r) for r = 1..k
Space Complexity: O(1) extra memory (generator used)
"""

# ====================================================
# Code 2: Manual Implementation (without prebuilt function)
# ====================================================
def combine(s, k):
    """
    Generate all combinations of lengths 1 to k from string s in lexicographic order
    using manual recursion (backtracking).
    """
    s = sorted(s)  # sort string for lexicographic order

    def backtrack(start, path, length):
        """
        Recursive backtracking function to generate combinations.

        start: index to start choosing from
        path: current combination being built
        length: target length of current combination
        """
        # Base case: if path reaches target length, print it
        if len(path) == length:
            print("".join(path))
            return

        # Explore further elements from start index
        for i in range(start, len(s)):
            path.append(s[i])               # choose character s[i]
            backtrack(i + 1, path, length) # recurse for next elements
            path.pop()                      # backtrack: remove last element

    # Loop through lengths 1 to k to generate all combinations
    for length in range(1, k + 1):
        backtrack(0, [], length)

# ====================================================
# Main function to read input and call manual combine
# ====================================================
if __name__ == "__main__":
    # Read input line, e.g., "HACK 2"
    string_input, k_input = input().split()
    k_input = int(k_input)  # convert k to integer

    # Call manual combination function
    combine(string_input, k_input)

"""

Time Complexity:
----------------
Total combinations for lengths 1..k = C(n,1) + C(n,2) + ... + C(n,k)
Each combination takes O(length) to join & print.
Total ≈ O(Σ (r * C(n,r))) for r = 1..k

Space Complexity:
-----------------
- Recursion stack depth = length of combination = O(k)
- Path list = O(k)
- Total ≈ O(k) extra memory
"""

# ====================================================
# Efficiency Ranking
# ====================================================
"""
Time Complexity (both codes generate all combinations):
1. Code 1 (itertools) = O(Σ (r * C(n,r))) for r = 1..k
2. Code 2 (manual)    = O(Σ (r * C(n,r))) for r = 1..k

Space Complexity:
1. Code 1 (itertools) = O(1) extra memory (uses generator)
2. Code 2 (manual)    = O(k) extra memory for recursion stack and path

Conclusion:
-------------
- Code 1 is slightly more memory efficient due to generator usage.
- Code 2 is manual and suitable for understanding recursion and backtracking.
"""
