"""
Problem Statement:
------------------
You are given an integer array nums.

Return the smallest absent positive integer in nums such that it is strictly greater than the average of all elements in nums.

The average of an array is defined as the sum of all its elements divided by the number of elements.

------------------
Input / Output:
- Input: nums (a list of integers)
- Output: an integer (the smallest absent positive integer greater than the average)

------------------
Constraints:
- 1 <= nums.length <= 100
- -100 <= nums[i] <= 100

------------------
Examples:

Example 1:
Input: nums = [3,5]
Output: 6
Explanation:
The average of nums is (3 + 5) / 2 = 8 / 2 = 4.
The smallest absent positive integer greater than 4 is 6.

Example 2:
Input: nums = [-1,1,2]
Output: 3
Explanation:
The average of nums is (-1 + 1 + 2) / 3 = 2 / 3 = 0.667.
The smallest absent positive integer greater than 0.667 is 3.

Example 3:
Input: nums = [4,-1]
Output: 2
Explanation:
The average of nums is (4 + (-1)) / 2 = 3 / 2 = 1.5.
The smallest absent positive integer greater than 1.5 is 2.
"""

# =====================================================
# First Solution: Using Python’s built-in functions/libraries
# (HackerRank style coding: concise but explained line-by-line)
# =====================================================

def smallestMissingInteger_builtin(nums):
    # Find the length of the list
    n = len(nums)  # O(1) operation, accessing length attribute of list
    
    # Calculate average using built-in sum and division
    avg = sum(nums) / n  # sum(nums) is O(n), division is O(1)
    
    # Convert list into a set for O(1) membership lookup
    nums_set = set(nums)  # O(n) to build set
    
    # Start candidate from the greater of 1 or int(avg) + 1
    candidate = max(1, int(avg) + 1)  # O(1) comparisons and arithmetic
    
    # Keep checking until we find the required number
    while True:  # loop runs until return statement
        if candidate not in nums_set:  # O(1) membership check due to set
            return candidate  # return candidate when not in nums_set
        candidate += 1  # increment candidate if present in nums_set


# -----------------------------------------------------
# Time Complexity Analysis (Built-in approach):
# -----------------------------------------------------
# 1. sum(nums) -> O(n)
# 2. set(nums) -> O(n)
# 3. while loop -> at most O(n + max_val) iterations
#    - Each membership check is O(1)
#    - With constraints n <= 100 and max_val <= 100, at most ~200 checks
# Total: O(n + max_val), but bounded small -> practically O(1)
#
# Space Complexity:
# - nums_set uses O(n) space
# - Other variables use O(1)
# Total: O(n)


# =====================================================
# Second Solution: Manual Implementation (without relying on sum/set/max helpers)
# =====================================================

def smallestMissingInteger_manual(nums):
    # Step 1: Compute length of nums manually
    n = 0  # initialize counter
    for _ in nums:  # iterate through each element
        n += 1  # increment count
    # n now contains the length of the list
    
    # Step 2: Compute sum manually
    total = 0  # initialize sum accumulator
    for x in nums:  # iterate over each element
        total += x  # add each number to total
    
    # Step 3: Compute average
    avg = total / n  # division O(1)
    
    # Step 4: Build manual set-like structure (list of unique elements)
    nums_unique = []  # store unique values manually
    for x in nums:  # iterate through original list
        if x not in nums_unique:  # check manually if already exists
            nums_unique.append(x)  # append if not present
    # nums_unique now behaves like a set but with O(k) lookup
    
    # Step 5: Compute starting candidate manually
    # First compute int(avg) manually (truncate toward zero in Python by casting to int)
    start = int(avg) + 1  # O(1) operation
    if start < 1:  # ensure positive
        start = 1
    
    # Step 6: Loop until we find missing positive
    candidate = start
    while True:  # infinite loop until return
        found = False  # assume candidate not present
        for x in nums_unique:  # check manually for membership
            if candidate == x:  # if candidate exists
                found = True  # mark as found
                break  # exit loop early
        if not found:  # if candidate not in nums_unique
            return candidate  # return candidate
        candidate += 1  # else increment candidate and continue


# -----------------------------------------------------
# Time Complexity Analysis (Manual approach):
# -----------------------------------------------------
# 1. Length computation -> O(n)
# 2. Sum computation -> O(n)
# 3. Unique list building -> O(n^2) (because each "x not in nums_unique" is O(k), worst case O(n))
# 4. While loop:
#    - Each candidate check involves scanning nums_unique (O(n))
#    - At most (n + max_val) candidates checked
#    - Total worst-case loop cost = O(n * (n + max_val))
#
# Total: O(n^2 + n * max_val)
# For n=100, max_val=100, worst ~ O(20,000) → still feasible.
#
# Space Complexity:
# - nums_unique stores up to n unique elements -> O(n)
# - Other variables use O(1)
# Total: O(n)


# =====================================================
# Example Runs (Quick Check)
# =====================================================

