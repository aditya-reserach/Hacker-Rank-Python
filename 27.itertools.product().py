#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: Cartesian Product of Two Lists
Difficulty: Easy
Tags: Itertools, Cartesian Product, Nested Loops

Problem Statement
-----------------
You are given two lists A and B. Your task is to compute their Cartesian product A × B.
The Cartesian product of two sets A and B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B.

Example
--------
Input:
1 2
3 4

Output:
(1, 3) (1, 4) (2, 3) (2, 4)

Input Format
------------
- First line: space-separated integers of list A
- Second line: space-separated integers of list B

Output Format
-------------
- Print space-separated tuples representing the Cartesian product in sorted order.

Constraints
-----------
- Lists contain distinct integers
- 1 <= size(A), size(B) <= 1000

Edge Cases
----------
- Small lists like [1], [2] → output is (1,2)
- Larger lists → must still compute efficiently
"""

# ====================================================
# Code 1: Manual Nested Loops (with map & tuple)
# ====================================================

def solve_with_loops():
    """
    Compute Cartesian Product using nested loops.
    Each line is explained in detail below.
    """

    # Read first line of input, split by spaces, convert each element to int, and make it a tuple
    A = tuple(map(int, input().split()))
    # input().split() → reads input like "1 2" → ['1', '2']
    # map(int, ...) → converts each string to int → [1, 2]
    # tuple(...) → converts list to tuple → (1, 2)

    # Repeat for second line
    B = tuple(map(int, input().split()))
    # e.g., input "3 4" → tuple([3,4]) → (3,4)

    # Outer loop: iterate through each element in A
    for x in A:
        # Inner loop: iterate through each element in B
        for y in B:
            # Print the tuple (x, y)
            # end=' ' ensures no newline after each print; tuples are separated by spaces
            print((x, y), end=" ")
    # Add newline after all tuples printed for cleanliness
    print()

"""
Time & Space Complexity — Code 1
--------------------------------
- Outer loop runs |A| times
- Inner loop runs |B| times
- Total operations = |A| × |B|
- Time complexity = O(|A| × |B|)
- Space complexity = O(1) (prints directly without storing results)
"""

# ====================================================
# Code 2: Using itertools.product
# ====================================================

from itertools import product  # import product to generate Cartesian product efficiently

def solve_with_itertools():
    """
    Compute Cartesian Product using itertools.product
    Each line explained in comments.
    """

    # Read two lines of input, convert each to list of integers using map and list comprehension
    lists = [list(map(int, input().split())) for _ in range(2)]
    # Breakdown:
    # - range(2) → loop twice (once for A, once for B)
    # - input().split() → splits line into strings
    # - map(int, ...) → converts strings to ints
    # - list(...) → converts map object to list
    # Example after two lines:
    # lists = [[1, 2], [3, 4]]

    # Compute Cartesian product using product(list1, list2)
    # The * operator unpacks tuples so print prints them space-separated
    print(*product(lists[0], lists[1]))
    # product([1,2],[3,4]) → generates [(1,3),(1,4),(2,3),(2,4)]
    # print(*...) → prints (1,3) (1,4) (2,3) (2,4)

"""
Time & Space Complexity — Code 2
--------------------------------
- Time: O(|A| × |B|) → must generate each pair
- Space: O(1) → generator yields tuples lazily, no full list stored
"""

# ====================================================
# Code 3: Fully Manual Implementation (no prebuilt helpers)
# ====================================================

def solve_without_prebuilt():
    """
    Compute Cartesian Product without using any helper functions.
    Each line is explained below.
    """

    # Step 1: Read first line as raw string
    line1 = input().strip()  # "1 2"
    # Step 2: Split by spaces to get list of string numbers
    A_str = line1.split(" ")  # ['1', '2']
    # Step 3: Convert each string manually to integer and store in list A
    A = []
    for val in A_str:
        A.append(int(val))  # A becomes [1,2]

    # Step 4: Repeat for second line of input
    line2 = input().strip()  # "3 4"
    B_str = line2.split(" ")  # ['3', '4']
    B = []
    for val in B_str:
        B.append(int(val))  # B becomes [3,4]

    # Step 5: Prepare result string to store all tuples
    result = ""
    # Step 6: Use nested loops to create every pair
    for i in range(len(A)):
        for j in range(len(B)):
            # Build tuple as string manually: "(A[i], B[j])"
            pair = "(" + str(A[i]) + ", " + str(B[j]) + ")"
            # Append to result with space separator
            result += pair + " "
    # Step 7: Print the final string, removing trailing space
    print(result.strip())

"""
Time & Space Complexity — Code 3
--------------------------------
- Time: O(|A| × |B|) → nested loops generate all pairs
- Space: O(|A| + |B| + |A|×|B|) 
  - |A| + |B| for storing input arrays
  - |A|×|B| for result string
- Less memory-efficient than Code 1 & 2
"""

# ====================================================
# Efficiency Ranking
# ====================================================
"""
Time Complexity (all three are optimal):
1. Code 1 = O(|A| × |B|)
2. Code 2 = O(|A| × |B|)
3. Code 3 = O(|A| × |B|)

Space Complexity:
1. Code 1 = O(1) → most efficient
2. Code 2 = O(1) → same as Code 1, elegant
3. Code 3 = O(|A| × |B|) → least efficient due to full result string
"""

# ====================================================
# Minimal Test Harness
# ====================================================

def _run_examples():
    from io import StringIO
    import sys

    example_input = """1 2
3 4
"""
    # Redirect stdin to simulate input
    sys.stdin = StringIO(example_input)
    print("Code 1 Output:")
    solve_with_loops()

    sys.stdin = StringIO(example_input)
    print("Code 2 Output:")
    solve_with_itertools()

    sys.stdin = StringIO(example_input)
    print("Code 3 Output:")
    solve_without_prebuilt()

if __name__ == "__main__":
    _run_examples()
