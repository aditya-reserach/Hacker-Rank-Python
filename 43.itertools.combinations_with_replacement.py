"""
Problem Statement:
-----------------
You are given a string S and an integer size R.
Your task is to print all possible size R replacement combinations of the string in lexicographic sorted order.

- Combinations can include the same character multiple times.
- Characters in each combination must appear in lexicographic order.

Input Format:
-------------
A single line containing the string S and integer R separated by space.

Constraints:
------------
- String S contains only uppercase letters A-Z.
- 1 <= R <= len(S)

Output Format:
--------------
Print each combination on a separate line in lexicographic sorted order.

Sample Input:
-------------
HACK 2

Sample Output:
--------------
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

Explanation:
------------
- We generate all combinations of size 2 with replacement. 
- Output is sorted lexicographically.
"""

# =====================================================================
# ✅ Solution 1: Using itertools.combinations_with_replacement (Best HackerRank Style)
# =====================================================================

# Step 1: Import the combinations_with_replacement function
from itertools import combinations_with_replacement

# Step 2: Read input
# Input is string and size separated by space
string, size = input().split()

# Step 3: Sort the string to ensure lexicographic order
string = sorted(string)  # e.g., 'HACK' -> ['A','C','H','K']

# Step 4: Convert size to integer
size = int(size)

# Step 5: Generate all combinations with replacement
for combo in combinations_with_replacement(string, size):
    # combo is a tuple of characters; join them into a string
    print("".join(combo))

"""
Time Complexity (Solution 1):
-----------------------------
- Number of combinations with replacement = C(n + r - 1, r), where n = len(string), r = size
- Each combination takes O(r) to join and print
- Total = O(C(n+r-1, r) * r)
- Space Complexity:
- Uses generator internally, stores one combination at a time → O(r) per combination
- Sorting string initially → O(n log n)
"""

# =====================================================================
# ✅ Solution 2: Manual recursive solution (Without Prebuilt Functions)
# =====================================================================

def generate_combinations_with_replacement(chars, size, start=0, current=""):
    """
    Recursive function to generate combinations with replacement.
    
    Parameters:
    chars  : sorted list of characters
    size   : target length of each combination
    start  : index to ensure lexicographic order
    current: current combination being built
    """
    # Base case: if current combination reaches required size
    if len(current) == size:
        print(current)  # Print the combination
        return
    
    # Recursive case: iterate from 'start' index to allow replacement
    for i in range(start, len(chars)):
        # Append current character and recurse
        generate_combinations_with_replacement(chars, size, i, current + chars[i])

# Step 1: Read input
string2, size2 = input().split()
string2 = sorted(string2)  # Ensure lexicographic order
size2 = int(size2)

# Step 2: Call recursive function to generate and print all combinations
generate_combinations_with_replacement(string2, size2)

"""
Time Complexity (Solution 2):
-----------------------------
- Each recursive call generates a combination of length 'size'
- Number of combinations = C(n + r - 1, r)
- Each combination requires O(r) to build string (current + chars[i])
- Total = O(C(n+r-1, r) * r)
- Space Complexity:
- Recursive stack can go up to depth r → O(r)
- Each combination string → O(r)
- Sorting input string → O(n log n)
"""

# -------------------------------------------------------
# 📌 Final Notes:
# - Solution 1 is optimal and recommended for HackerRank / real problems (fast and clean)
# - Solution 2 is educational to understand recursion and how combinations with replacement work manually
# -------------------------------------------------------
