# -------------------------------------------------------
# Problem Statement:
# You are given a set A and N other sets.
# Your job is to find whether set A is a strict superset 
# of each of the N sets.
#
# A strict superset means:
#   - A must contain every element of the smaller set.
#   - A must also have at least one element that the smaller set does not.
#
# Input Format:
#   - First line: space-separated elements of set A.
#   - Second line: integer N (number of other sets).
#   - Next N lines: space-separated elements of each set.
#
# Output Format:
#   - Print True if A is a strict superset of all N sets.
#   - Otherwise, print False.
#
# Constraints:
#   - All input values are integers.
#   - No duplicate elements within a single set.
#   - Number of sets N >= 1
#
# Example:
# Input:
#   1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
#   2
#   1 2 3 4 5
#   100 11 12
#
# Output:
#   False
#
# Explanation:
#   - A is a strict superset of {1,2,3,4,5}
#   - But not a strict superset of {100,11,12} 
#     (since 100 is missing in A).
#   => Final output: False
# -------------------------------------------------------


# =======================================================
# ===============  SOLUTION 1 (with built-ins) ==========
# =======================================================

# Read the main set A
A = set(map(int, input().split()))  # Convert input into integers, store as a set

# Read number of other sets
N = int(input())  # Number of sets to check against A

# Assume result is True initially
result = True  # We start with the assumption that A is strict superset of all sets

# Loop through N times (one for each smaller set)
for _ in range(N):
    other_set = set(map(int, input().split()))  # Read another set
    
    # Use Python built-in: issuperset() checks if all elements of other_set are in A
    # Also check A != other_set to ensure "strict" (A must have something extra)
    if not (A.issuperset(other_set) and A != other_set):
        result = False  # If one set fails, mark result False
        break           # Stop checking further, no need to continue

# Print the final result
print(result)


# -------------------------------------------------------
# Time Complexity Analysis (Solution 1 with built-ins):
# -------------------------------------------------------
# Let:
#   - |A| = size of main set A
#   - |B| = average size of each smaller set
#   - N   = number of smaller sets
#
# issuperset(other_set) internally checks membership for all |B| elements.
# Each membership check in a set is O(1) average case (hash table lookup).
#
# For each set B:
#   - Checking issuperset → O(|B|)
#   - Checking A != B → O(1) for length, O(min(|A|, |B|)) worst-case element compare,
#     but average case is near O(1) since lengths differ often.
#
# Total time = O(N * |B|)
#
# Space Complexity:
#   - Storing set A → O(|A|)
#   - Each other_set read one at a time → O(|B|)
#   - No extra space beyond these sets → O(|A| + |B|)
# -------------------------------------------------------


# =======================================================
# ===============  SOLUTION 2 (manual check) ============
# =======================================================

# Read the main set A again (since previous input is consumed)
A = set(map(int, input().split()))  # Convert input into integers, store as a set

# Read number of other sets
N = int(input())  # Number of sets to check against A

# Assume result is True initially
result = True  # Assume A is strict superset of all sets until proven otherwise

# Loop through each of the N sets
for _ in range(N):
    other_set = set(map(int, input().split()))  # Read another set
    
    # Start by assuming A contains all elements of other_set
    is_superset = True
    
    # Check manually if every element of other_set is in A
    for elem in other_set:
        if elem not in A:       # If even one element missing
            is_superset = False # Mark as not superset
            break               # Stop checking further
    
    # Strict condition: A must have at least one extra element
    has_extra = len(A) > len(other_set)
    
    # If either condition fails, A is not a strict superset
    if not (is_superset and has_extra):
        result = False
        break

# Print the final result
print(result)


# -------------------------------------------------------
# Time Complexity Analysis (Solution 2 manual):
# -------------------------------------------------------
# Let:
#   - |A| = size of main set A
#   - |B| = average size of each smaller set
#   - N   = number of smaller sets
#
# For each smaller set B:
#   - We iterate over all |B| elements.
#   - Each membership check `elem in A` is O(1) average (set hash lookup).
#   - So, checking superset manually → O(|B|)
#   - Length comparison len(A) > len(B) → O(1)
#
# Total time = O(N * |B|)
#
# Space Complexity:
#   - Storing set A → O(|A|)
#   - Each other_set read one at a time → O(|B|)
#   - No other major structures → O(|A| + |B|)
# -------------------------------------------------------
