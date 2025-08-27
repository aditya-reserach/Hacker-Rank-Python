"""
Problem Statement:
You are given:
- An integer n (size of array) and m (size of sets A and B, not always needed explicitly).
- An array arr of n integers.
- Two disjoint sets A and B.

Your task:
You start with happiness = 0.
- For every element in arr:
    - If the element is in set A, increase happiness by +1.
    - If the element is in set B, decrease happiness by -1.
    - Otherwise, no change.

Finally, print the total happiness.

------------------------------------------
Input Format:
n m
arr (n space-separated integers)
A (m space-separated integers)
B (m space-separated integers)

------------------------------------------
Output Format:
A single integer: total happiness.

------------------------------------------
Example:
Input:
3 2
1 5 3
3 1
5 7

Output:
1
Explanation:
- 1 is in A → happiness = +1
- 5 is in B → happiness = 0
- 3 is in A → happiness = 1
Final Answer = 1
"""

# ------------------------------------------
# Solution 1: Using Prebuilt Functions
# ------------------------------------------

# Read integers n and m from input
n, m = map(int, input().split())

# Read array elements (arr will have n elements)
arr = input().split()

# Read set A
A = set(input().split())

# Read set B
B = set(input().split())

# Compute happiness using Python set membership and sum
total_happiness = sum((x in A) - (x in B) for x in arr)

# Print result
print(total_happiness)

"""
Time Complexity (Solution 1):
- For each element in arr (n elements), we check membership in sets A and B.
- Membership check in a set is O(1) average case.
- Total = O(n)

Space Complexity (Solution 1):
- arr takes O(n)
- A and B take O(m) each
- Total = O(n + m)
"""

# ------------------------------------------
# Solution 2: Without Prebuilt Set Functions
# ------------------------------------------

# Reset inputs again for the second solution
n, m = map(int, input().split())
arr = input().split()
A_list = input().split()
B_list = input().split()

# Convert A and B into normal lists (no sets allowed)
# We will manually check membership
happy = 0

# Loop through each element of arr
for element in arr:
    # Check membership in A manually (linear search)
    found_in_A = False
    for a in A_list:
        if element == a:
            found_in_A = True
            break

    if found_in_A:
        happy += 1
        continue  # skip checking in B if already found in A

    # Check membership in B manually (linear search)
    found_in_B = False
    for b in B_list:
        if element == b:
            found_in_B = True
            break

    if found_in_B:
        happy -= 1

print(happy)

"""
Time Complexity (Solution 2):
- For each element in arr (n elements), 
  we check in list A (m elements) → O(m)
  if not found, check in list B (m elements) → O(m)
- Worst-case: O(n * m)

Space Complexity (Solution 2):
- arr takes O(n)
- A_list and B_list take O(m) each
- No extra structures
- Total = O(n + m)
"""
