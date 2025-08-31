"""
Problem Statement:
==================
You are given two collections of integers. Each collection may contain duplicate values.
Your task is to find how many unique integers exist across both collections combined
(i.e., the size of the union of the two sets).

Input Format:
-------------
- The first line contains an integer n, the number of elements in the first collection.
- The second line contains n space-separated integers (the elements of the first collection).
- The third line contains an integer m, the number of elements in the second collection.
- The fourth line contains m space-separated integers (the elements of the second collection).

Output Format:
--------------
- Output a single integer: the number of unique elements across both collections.

Constraints:
------------
- 1 <= n, m <= 10^5
- Each integer is between -10^9 and 10^9
- Input may contain duplicates, but only unique values should be counted.

Example:
--------
Input:
3
1 2 3
4
2 3 4 5

Output:
5

Explanation:
First collection = {1, 2, 3}
Second collection = {2, 3, 4, 5}
Union = {1, 2, 3, 4, 5}
Size of union = 5
"""

# ============================================================
# Solution 1: Using Python's built-in data structures (HackerRank style)
# ============================================================

# Read an integer n (size of first collection)
n = int(input())
# Read n space-separated integers, convert each to int, and build a set (automatically removes duplicates)
m = set(map(int, input().split()))

# Read an integer x (size of second collection)
x = int(input())
# Read x space-separated integers, convert each to int, and build another set
y = set(map(int, input().split()))

# Take the union of the two sets (all unique elements from both), then measure its length
print(len(m.union(y)))

"""
Explanation of Solution 1:
--------------------------
1. The 'set' constructor in Python automatically removes duplicates.
2. 'm.union(y)' constructs a new set containing all elements from both m and y.
3. 'len(...)' returns the number of elements in that union set.

Time Complexity (Solution 1):
-----------------------------
- Reading n integers and converting to int: O(n)
- Creating set m: O(n)
- Reading x integers and converting to int: O(x)
- Creating set y: O(x)
- Union operation m.union(y): O(n + x) (each element from both sets must be hashed and inserted)
- len(...) is O(1)
=> Total Time: O(n + x)

Space Complexity (Solution 1):
------------------------------
- set m: stores up to n unique elements
- set y: stores up to x unique elements
- union result: up to n + x unique elements
=> Total Space: O(n + x)
"""

# ============================================================
# Solution 2: Manual implementation without relying on prebuilt set/union
# ============================================================

# Read an integer n (size of first collection)
n = int(input())
# Read n space-separated integers and store them in a list
m_list = list(map(int, input().split()))

# Read an integer x (size of second collection)
x = int(input())
# Read x space-separated integers and store them in a list
y_list = list(map(int, input().split()))

# Initialize an empty dictionary to simulate a set (keys will be unique)
seen = {}
# Initialize a counter to track number of unique elements
count = 0

# Process each element from the first list
for val in m_list:
    # If value not already in dictionary, add it and increment counter
    if val not in seen:
        seen[val] = True
        count += 1

# Process each element from the second list
for val in y_list:
    # If value not already in dictionary, add it and increment counter
    if val not in seen:
        seen[val] = True
        count += 1

# Print final count of unique elements
print(count)

"""
Explanation of Solution 2:
--------------------------
1. Instead of using set, we simulate uniqueness with a dictionary.
   - Keys of dictionary behave like set elements (unique).
2. As we process each element from both lists:
   - If it's not already in 'seen', we add it and increase 'count'.
   - If it's already present, we skip it (ensuring uniqueness).
3. At the end, 'count' contains the total number of unique elements.

Time Complexity (Solution 2):
-----------------------------
- Reading n integers: O(n)
- Reading x integers: O(x)
- Loop over n elements: O(n)
   * Each dictionary lookup/insertion is O(1) average
- Loop over x elements: O(x)
   * Each dictionary lookup/insertion is O(1) average
=> Total Time: O(n + x)

Space Complexity (Solution 2):
------------------------------
- m_list: O(n)
- y_list: O(x)
- dictionary 'seen': O(n + x) in worst case (all unique)
=> Total Space: O(n + x)

Notes on Tradeoffs:
-------------------
- Solution 1 is shorter and uses Python's set data structure directly.
- Solution 2 is longer but avoids using 'set' or 'union' and demonstrates manual uniqueness handling.
- Both have the same asymptotic time and space complexity: O(n + x).
- Solution 2 may use slightly more memory because it keeps the original lists, but avoids creating an extra union set.
"""


