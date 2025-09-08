"""
Problem Statement:

You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

-------------------------------------------------------
Input Format:

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

-------------------------------------------------------
Constraints:
- 1 <= T <= 21
- 0 < len(set(A)) < 1000
- 0 < len(set(B)) < 1000

-------------------------------------------------------
Output Format:
Output True or False for each test case on separate lines.

-------------------------------------------------------
Sample Input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output:
True
False
False

-------------------------------------------------------
Explanation (Test Case 01):
Set A = {1, 2, 3, 5, 6}
Set B = {9, 8, 5, 6, 3, 2, 1, 4, 7}
All the elements of set A are present in set B.
Therefore, output is True.
"""

# ======================================================
# ========== Solution 1: Using Python built-ins =========
# ======================================================

# Read the number of test cases
t = int(input())  # 't' stores how many times we need to repeat the process

for _ in range(t):  # Loop through each test case
    nA = int(input())  # Read number of elements in set A (not strictly needed, but follows input format)
    A = set(map(int, input().split()))  # Convert the input line into integers and then into a set
    
    nB = int(input())  # Read number of elements in set B
    B = set(map(int, input().split()))  # Convert the input line into integers and then into a set
    
    # Use Python's built-in 'issubset' method to check if A ⊆ B
    print(A.issubset(B))  # Prints True if every element of A is in B, else False


"""
-------------------------------------------------------
Time Complexity Analysis (Solution 1):
- Reading input for A: O(nA)
- Reading input for B: O(nB)
- Constructing sets: O(nA + nB)
- Checking subset with issubset: O(nA) average case
Total = O(nA + nB)

Space Complexity (Solution 1):
- Two sets are stored: O(nA + nB)
"""


# ==========================================================
# ========== Solution 2: Manual implementation =============
# ==========================================================

# Read the number of test cases again for the second solution
t = int(input())  # New input for test cases

for _ in range(t):  # Loop through each test case
    nA = int(input())  # Read number of elements in A
    A = list(map(int, input().split()))  # Store A as a list
    
    nB = int(input())  # Read number of elements in B
    B = list(map(int, input().split()))  # Store B as a list
    
    # Assume A is subset of B until proven otherwise
    is_subset = True  
    
    # Check each element of A
    for elem in A:
        found = False  # Start by assuming this element is not in B
        
        # Search for elem in B manually
        for b in B:
            if elem == b:  # If we find a match
                found = True  # Mark as found
                break  # No need to keep searching for this element
        
        if not found:  # If an element from A was never found in B
            is_subset = False  # Then A is not a subset
            break  # Stop checking further
    
    print(is_subset)  # Print the result for this test case


"""
-------------------------------------------------------
Time Complexity Analysis (Solution 2):
- Reading input for A: O(nA)
- Reading input for B: O(nB)
- For each element in A, searching through all of B: O(nA * nB)
Total = O(nA * nB)

Space Complexity (Solution 2):
- Two lists are stored: O(nA + nB)
- A few scalar variables (is_subset, found) = O(1)
Total = O(nA + nB)
"""

# ======================================================
# Suggested Git Commit Message:
# "Add subset check problem with two solutions: one using built-in set functions and one manual implementation with detailed comments"
