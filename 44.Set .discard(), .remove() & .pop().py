"""
Problem Statement:
------------------
You are given a non-empty set `s` containing integers. 
You must execute a sequence of commands on this set. 
The commands will be one of the following three operations:

1. pop
   - Removes and returns an arbitrary element from the set.
   - If the set is empty, it raises a KeyError.

2. remove x
   - Removes element `x` from the set if it exists.
   - If element `x` does not exist, it raises a KeyError.

3. discard x
   - Removes element `x` from the set if it exists.
   - If element `x` does not exist, it does nothing.
   - Does not raise an error.

Task:
-----
Execute the given commands on the set. 
After processing all commands, print the sum of the elements remaining in the set.

Input Format:
-------------
- First line: integer n, number of elements in the set.
- Second line: n space-separated integers, elements of the set.
- Third line: integer m, number of commands.
- Next m lines: each line contains one command (either "pop", "remove x", or "discard x").

Constraints:
------------
- 0 < n <= 100
- Elements are non-negative integers ≤ 9
- Number of commands m ≤ 100

Output Format:
--------------
Print a single integer: the sum of all elements left in the set after executing all commands.

Sample Input:
-------------
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5

Sample Output:
--------------
4

Explanation:
------------
After executing the operations, the set contains {4}.
Hence, the sum is 4.
"""

# ============================================================
# ✅ Solution 1: Using Python Built-in Functions
# ============================================================

# Step 1: Read number of elements in the set
n = int(input())   # O(1)

# Step 2: Read the elements and store in a set
s = set(map(int, input().split()))   # O(n)

# Step 3: Read number of commands
N = int(input())   # O(1)

# Step 4: Loop through each command
for _ in range(N):   # O(m), where m = number of commands
    cmd = input().split()   # O(1) to split command
    if cmd[0] == 'pop':     # check first word
        s.pop()             # O(1) average (removes arbitrary element)
    elif cmd[0] == 'remove':
        s.remove(int(cmd[-1]))   # O(1) average
    elif cmd[0] == 'discard':
        s.discard(int(cmd[-1]))  # O(1) average

# Step 5: Print the sum of the remaining set
print(sum(s))   # O(k), where k = size of final set

"""
Time Complexity Analysis (Solution 1):
--------------------------------------
- Reading input: O(n)
- Processing m commands: O(m)
- Summing remaining set: O(k), k ≤ n
=> Total = O(n + m + k) ≈ O(n + m)

Since n, m ≤ 100 → Very efficient.
"""


# ============================================================
# ✅ Solution 2: Without Using Built-in Functions
# (Manual implementation of pop, remove, discard, and sum)
# ============================================================

# Step 1: Read number of elements in the set
n = int(input())   # O(1)

# Step 2: Read elements into a Python set (allowed for uniqueness, but we won't use set methods)
s = set(map(int, input().split()))   # O(n)

# Step 3: Read number of commands
m = int(input())   # O(1)

# Step 4: Process commands manually
for _ in range(m):   # O(m)
    cmd = input().split()   # O(1)

    if cmd[0] == "pop":
        # Manually remove the smallest element to make behavior deterministic
        if len(s) == 0:
            raise KeyError("pop from empty set")   # mimic Python error
        smallest = min(s)   # O(k), k = size of current set
        s = {x for x in s if x != smallest}   # O(k), rebuild set without smallest

    elif cmd[0] == "remove":
        x = int(cmd[1])
        if x not in s:          # O(1) average (membership check)
            raise KeyError(x)   # mimic Python's remove behavior
        s = {v for v in s if v != x}   # O(k), rebuild set

    elif cmd[0] == "discard":
        x = int(cmd[1])
        if x in s:                   # O(1) average
            s = {v for v in s if v != x}   # O(k), rebuild set

# Step 5: Manually compute sum of set elements
total = 0
for val in s:    # O(k)
    total += val
print(total)

"""
Time Complexity Analysis (Solution 2):
--------------------------------------
- Reading input: O(n)
- Processing commands:
   * pop → O(k) because of min() + rebuild
   * remove → O(k) because of rebuild
   * discard → O(k) in worst case
- Summing elements → O(k)
=> Worst-case per operation = O(k)
=> Total = O(n + m*k)

Since n, m ≤ 100 and k ≤ n, this is still efficient, 
but less optimal than Solution 1.
"""

# ============================================================
# End of File
# ============================================================
