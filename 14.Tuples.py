# ------------------------------------------------------------
# Problem Statement:  Python: 2
# 
# Task
# Given an integer, n, and n space-separated integers as input, 
# create a tuple, t, of those integers. 
# Then compute and print the result of hash(t).
#
# Note: hash() is one of the functions in the __builtins__ module, 
# so it need not be imported.
#
# Input Format
# - The first line contains an integer, n, denoting the number of elements in the tuple.
# - The second line contains n space-separated integers describing the elements in tuple t.
#
# Output Format
# - Print the result of hash(t).
#
# Sample Input 0
# 2
# 1 2
#
# Sample Output 0
# 3713081631934410656
# ------------------------------------------------------------

if __name__ == "__main__":
    
    n = int(raw_input())                       # Read the number of elements
    list_name = map(int, raw_input().split())  # Read space-separated integers and convert to list of int
    print(hash(tuple(list_name)))              # Convert list to tuple, compute hash, and print result


# ------------------------------------------------------------
# Time Complexity Analysis:
#
# 1. Reading input:
#    - raw_input() → O(1) for first line
#    - raw_input().split() → O(n) (splitting n integers)
#
# 2. map(int, ...) → O(n) (converting n strings to integers)
#
# 3. tuple(list_name) → O(n) (copying n elements into a tuple)
#
# 4. hash(tuple) → O(n) (hashing function processes each element once)
#
# Overall Time Complexity: O(n)
#
# Space Complexity:
# - O(n) for storing the list of integers
# - O(n) for creating the tuple
# ------------------------------------------------------------
