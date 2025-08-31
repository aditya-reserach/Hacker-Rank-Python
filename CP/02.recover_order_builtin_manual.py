"""
Problem Statement:

Given two lists:
1. order: a list containing a permutation of integers from 1 to n.
2. friends: a list of integers which is a subset of order, strictly increasing.

Task:
Return a list containing the elements from 'friends' that appear in 'order', 
in the same order as they appear in 'order'.

Input Format:
- order: List[int], 1 <= len(order) <= 100, contains each integer from 1 to n exactly once
- friends: List[int], 1 <= len(friends) <= min(8, len(order)), strictly increasing, 1 <= friends[i] <= n

Output Format:
- List[int] containing elements of friends in the order they appear in 'order'.

Example:
order = [3, 1, 4, 5, 2]
friends = [2, 3, 5]
Output: [3, 5, 2]

Constraints:
1 <= n == len(order) <= 100
order contains every integer from 1 to n exactly once
1 <= len(friends) <= min(8, n)
1 <= friends[i] <= n
friends is strictly increasing
"""

# ------------------- Solution 1: Using Python built-in functions / libraries -------------------

from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Step 1: Convert friends list to a set for O(1) lookup
        # Using Python's built-in set() function to optimize membership test
        friends_set = set(friends)  # O(m) time to build the set, O(m) space
        # Step 2: Use list comprehension to iterate over each element in 'order'
        # Check if the element exists in the set of friends, if yes include it
        result = [num for num in order if num in friends_set]  # O(n) iterations, O(1) lookup per element
        # Step 3: Return the resulting list
        return result

# ------------------- Solution 2: Manual implementation without built-in helpers -------------------

class SolutionManual:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Step 1: Initialize an empty list to store the common elements
        result = []  # O(1) space initially
        # Step 2: Iterate through each element in 'order'
        for num in order:  # Outer loop O(n)
            # Step 3: Inner loop: check if 'num' exists in 'friends' list manually
            found = False  # Flag to track if num exists in friends
            for f in friends:  # Inner loop O(m)
                if num == f:  # Compare current order element with friend
                    found = True
                    break  # Exit inner loop once match is found
            # Step 4: If found in friends, append to result list
            if found:
                result.append(num)  # O(1) per append
        # Step 5: Return the final ordered list
        return result

# ------------------- Time and Space Complexity Analysis -------------------

"""
Solution 1 (Using set):
- Time Complexity:
    1. Creating friends_set: O(m), where m = len(friends)
    2. List comprehension: iterate over n elements of order, each lookup O(1)
       → O(n)
    Total Time Complexity: O(n + m)
- Space Complexity:
    1. friends_set requires O(m) space
    2. result list requires O(k) space, where k = number of elements in intersection
    Total Space Complexity: O(m + k)

Solution 2 (Manual):
- Time Complexity:
    1. Outer loop over order: O(n)
    2. Inner loop over friends: O(m)
       → For each element in order, we do up to m comparisons
    Total Time Complexity: O(n * m)
- Space Complexity:
    1. result list requires O(k) space
    2. Only constant extra space for variables 'found' and loop counters
    Total Space Complexity: O(k)
- Note: For given constraints (n <= 100, m <= 8), even O(n*m) is acceptable.
"""

# ------------------- Example Run -------------------

if __name__ == "__main__":
    order = [3, 1, 4, 5, 2]
    friends = [2, 3, 5]

    sol1 = Solution()
    print("Built-in solution result:", sol1.recoverOrder(order, friends))

    sol2 = SolutionManual()
    print("Manual solution result:", sol2.recoverOrder(order, friends))
