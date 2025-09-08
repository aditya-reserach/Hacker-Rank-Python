# --------------------------------------------------------------
# Problem: Set Mutations
# --------------------------------------------------------------
# You are given a set A and N other sets.
# Each of the N sets must apply a mutation operation on A:
#   - update
#   - intersection_update
#   - difference_update
#   - symmetric_difference_update
#
# After performing all operations, print the sum of elements in set A.
#
# Input Format:
# ---------------
# 1. The first line contains integer len(A), the number of elements in set A.
# 2. The second line contains space-separated integers, the elements of set A.
# 3. The third line contains integer N, the number of other sets.
# 4. The next 2*N lines contain details of the N sets:
#       - First line: operation name and integer (size of other set, not used).
#       - Second line: space-separated integers, elements of the other set.
#
# Output Format:
# ----------------
# Print one integer: the sum of elements in the final set A.
#
# Constraints:
# ---------------
# - 0 < len(A) <= 1000
# - 0 < N <= 100
# - Elements are integers
#
# Sample Input:
# ---------------
# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66
#
# Sample Output:
# ---------------
# 38
#
# Explanation:
# ---------------
# After performing all operations step by step:
# 1. intersection_update keeps only common elements
# 2. update adds elements
# 3. symmetric_difference_update keeps exclusive elements
# 4. difference_update removes specified elements
# Final set = {1,2,3,4,5,6,8,9}, sum = 38
# --------------------------------------------------------------


# --------------------------------------------------------------
# Solution 1: Using built-in set mutation functions
# --------------------------------------------------------------

# Read number of elements in set A (not needed directly in Python but required by problem format)
len_A = int(input())  # e.g., len_A = 16

# Read the elements of set A
A = set(map(int, input().split()))  # creates a set with all input numbers

# Read the number of operations
N = int(input())  # e.g., N = 4

# Loop through each of the N operations
for _ in range(N):  # repeat N times
    operation, _ = input().split()  # read operation name and size (size ignored)
    other_set = set(map(int, input().split()))  # read the elements of the other set
    getattr(A, operation)(other_set)  # dynamically call the method on A (e.g., A.update(...))

# After all operations are complete, print the sum of elements in A
print(sum(A))  # sum() adds up all elements in the set


# --------------------------------------------------------------
# Solution 2: Without using built-in mutation functions
# --------------------------------------------------------------

# Read number of elements in set A again for second solution
len_A = int(input())  # size of set A
A = set(map(int, input().split()))  # initial set A
N = int(input())  # number of operations

# Loop through each of the N operations
for _ in range(N):  # repeat N times
    operation, _ = input().split()  # read operation name and size
    other_set = set(map(int, input().split()))  # read the elements of the other set

    if operation == "update":
        # Add all elements from other_set into A
        for elem in other_set:
            A.add(elem)

    elif operation == "intersection_update":
        # Keep only elements that are in both A and other_set
        new_A = set()
        for elem in A:
            if elem in other_set:
                new_A.add(elem)
        A = new_A

    elif operation == "difference_update":
        # Remove elements from A that are also in other_set
        new_A = set()
        for elem in A:
            if elem not in other_set:
                new_A.add(elem)
        A = new_A

    elif operation == "symmetric_difference_update":
        # Keep elements that are in A or in other_set but not in both
        new_A = set()
        for elem in A:
            if elem not in other_set:
                new_A.add(elem)
        for elem in other_set:
            if elem not in A:
                new_A.add(elem)
        A = new_A

# Print the sum of final elements in A
print(sum(A))


# --------------------------------------------------------------
# Time and Space Complexity Analysis
# --------------------------------------------------------------

# Solution 1 (Built-ins):
# - Each operation runs in O(min(len(A), len(other_set))) time internally.
# - Over N operations, total time = O(sum of all set sizes processed).
# - Space complexity: O(len(A) + len(other_set)) because sets are stored in memory.
# - Very efficient because Python's C-implemented methods handle operations.

# Solution 2 (Manual):
# - update: O(len(other_set)) because each element is added.
# - intersection_update: O(len(A)) because we check each element of A.
# - difference_update: O(len(A)) because we check each element of A.
# - symmetric_difference_update: O(len(A) + len(other_set)) because we check both sets.
# - Over N operations, total time = O(sum of all sizes across operations).
# - Space complexity: O(len(A) + len(other_set)) because we sometimes create new sets.
# - Slightly slower than built-ins due to Python-level loops instead of C.

# In both solutions, the complexity scales linearly with the total number of elements processed.
# --------------------------------------------------------------

# Suggested git commit message:
# "Add set mutation problem solutions: built-in and manual implementations with full explanations"
# --------------------------------------------------------------
# Problem: Set Mutations
# --------------------------------------------------------------
# You are given a set A and N other sets.
# Each of the N sets must apply a mutation operation on A:
#   - update
#   - intersection_update
#   - difference_update
#   - symmetric_difference_update
#
# After performing all operations, print the sum of elements in set A.
#
# Input Format:
# ---------------
# 1. The first line contains integer len(A), the number of elements in set A.
# 2. The second line contains space-separated integers, the elements of set A.
# 3. The third line contains integer N, the number of other sets.
# 4. The next 2*N lines contain details of the N sets:
#       - First line: operation name and integer (size of other set, not used).
#       - Second line: space-separated integers, elements of the other set.
#
# Output Format:
# ----------------
# Print one integer: the sum of elements in the final set A.
#
# Constraints:
# ---------------
# - 0 < len(A) <= 1000
# - 0 < N <= 100
# - Elements are integers
#
# Sample Input:
# ---------------
# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66
#
# Sample Output:
# ---------------
# 38
#
# Explanation:
# ---------------
# After performing all operations step by step:
# 1. intersection_update keeps only common elements
# 2. update adds elements
# 3. symmetric_difference_update keeps exclusive elements
# 4. difference_update removes specified elements
# Final set = {1,2,3,4,5,6,8,9}, sum = 38
# --------------------------------------------------------------


# --------------------------------------------------------------
# Solution 1: Using built-in set mutation functions
# --------------------------------------------------------------

# Read number of elements in set A (not needed directly in Python but required by problem format)
len_A = int(input())  # e.g., len_A = 16

# Read the elements of set A
A = set(map(int, input().split()))  # creates a set with all input numbers

# Read the number of operations
N = int(input())  # e.g., N = 4

# Loop through each of the N operations
for _ in range(N):  # repeat N times
    operation, _ = input().split()  # read operation name and size (size ignored)
    other_set = set(map(int, input().split()))  # read the elements of the other set
    getattr(A, operation)(other_set)  # dynamically call the method on A (e.g., A.update(...))

# After all operations are complete, print the sum of elements in A
print(sum(A))  # sum() adds up all elements in the set


# --------------------------------------------------------------
# Solution 2: Without using built-in mutation functions
# --------------------------------------------------------------

# Read number of elements in set A again for second solution
len_A = int(input())  # size of set A
A = set(map(int, input().split()))  # initial set A
N = int(input())  # number of operations

# Loop through each of the N operations
for _ in range(N):  # repeat N times
    operation, _ = input().split()  # read operation name and size
    other_set = set(map(int, input().split()))  # read the elements of the other set

    if operation == "update":
        # Add all elements from other_set into A
        for elem in other_set:
            A.add(elem)

    elif operation == "intersection_update":
        # Keep only elements that are in both A and other_set
        new_A = set()
        for elem in A:
            if elem in other_set:
                new_A.add(elem)
        A = new_A

    elif operation == "difference_update":
        # Remove elements from A that are also in other_set
        new_A = set()
        for elem in A:
            if elem not in other_set:
                new_A.add(elem)
        A = new_A

    elif operation == "symmetric_difference_update":
        # Keep elements that are in A or in other_set but not in both
        new_A = set()
        for elem in A:
            if elem not in other_set:
                new_A.add(elem)
        for elem in other_set:
            if elem not in A:
                new_A.add(elem)
        A = new_A

# Print the sum of final elements in A
print(sum(A))


# --------------------------------------------------------------
# Time and Space Complexity Analysis
# --------------------------------------------------------------

# Solution 1 (Built-ins):
# - Each operation runs in O(min(len(A), len(other_set))) time internally.
# - Over N operations, total time = O(sum of all set sizes processed).
# - Space complexity: O(len(A) + len(other_set)) because sets are stored in memory.
# - Very efficient because Python's C-implemented methods handle operations.

# Solution 2 (Manual):
# - update: O(len(other_set)) because each element is added.
# - intersection_update: O(len(A)) because we check each element of A.
# - difference_update: O(len(A)) because we check each element of A.
# - symmetric_difference_update: O(len(A) + len(other_set)) because we check both sets.
# - Over N operations, total time = O(sum of all sizes across operations).
# - Space complexity: O(len(A) + len(other_set)) because we sometimes create new sets.
# - Slightly slower than built-ins due to Python-level loops instead of C.

# In both solutions, the complexity scales linearly with the total number of elements processed.
# --------------------------------------------------------------


