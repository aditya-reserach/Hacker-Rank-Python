"""
Problem: Cube Piles

You are given several piles of cube blocks. Each cube has a side length.
At each step, you can only pick a block either from the leftmost pile or the rightmost pile.
The objective is to determine if it is possible to build a new pile of cubes such that
each cube placed on the pile is of equal or smaller side length than the cube below it
(i.e., the pile must be in non-increasing order from bottom to top).

-------------------------------------------------
Input Format:
- The first line contains an integer T, the number of test cases.
- For each test case:
  - The first line contains an integer n, the number of cube blocks.
  - The second line contains n space-separated integers, representing the side lengths of the blocks.

Output Format:
- For each test case, output "Yes" if it is possible to stack the cubes into a single pile
  following the rules, or "No" otherwise.

-------------------------------------------------
Constraints:
1 <= T <= 5
1 <= n <= 10^5
1 <= cube size <= 10^9

-------------------------------------------------
Example:
Input:
2
6
4 3 2 1 3 4
3
1 3 2

Output:
Yes
No
-------------------------------------------------
"""

# -------------------------------------------------
# Solution 1: Using Python built-in functions (HackerRank style)
# -------------------------------------------------

# Read number of test cases
import math  # importing math to use math.inf (represents infinity)

T = int(input())  # input() reads a line, int() converts it to integer

for _ in range(T):  # loop through each test case
    n = int(input())  # number of blocks in this test
    blocks = list(map(int, input().split()))  
    # input().split() splits the line into a list of strings
    # map(int, ...) converts each string to int
    # list(...) collects the results into a list

    top = math.inf  
    # We start with infinity, meaning the first block can be any size.
    # math.inf is used because no block can be larger than infinity.

    result = "Yes"  # assume possible until proven otherwise

    while blocks:  
        # while there are still blocks remaining
        left = blocks[0]   # leftmost block
        right = blocks[-1] # rightmost block

        # choose the larger block between left and right
        if left >= right:
            chosen = blocks.pop(0)  
            # pop(0) removes and returns the first element (O(n) operation)
        else:
            chosen = blocks.pop()  
            # pop() with no index removes and returns the last element (O(1) operation)

        # check if chosen block can be placed on top of pile
        if chosen <= top:
            top = chosen  # update the new top block
        else:
            result = "No"  # cannot place, so fail
            break

    print(result)  # output Yes or No for this test case

# -------------------------------------------------
# Complexity Analysis (Solution 1):
# -------------------------------------------------
# Let n = number of blocks in a test case.
# - Each iteration processes one block (n iterations total).
# - pop(0) is O(n) because it shifts elements in the list.
# - Worst case: O(n^2) time complexity.
# - Space complexity: O(n) for storing the blocks list.
# -------------------------------------------------


# -------------------------------------------------
# Solution 2: Manual implementation (no built-ins like max, map, math.inf, pop)
# -------------------------------------------------

T = int(input())  # read number of test cases

for _ in range(T):  # process each test case
    n = int(input())  # read number of blocks
    raw = input().split()  # split into list of strings

    # Manually convert list of strings to integers (no map())
    blocks = []
    for x in raw:
        blocks.append(int(x))

    # Instead of math.inf, use a very large number (since max cube size <= 1e9)
    top = 10**18  # sufficiently large value acting like infinity

    result = "Yes"  # assume possible

    left = 0               # pointer to leftmost index
    right = n - 1          # pointer to rightmost index

    while left <= right:   # until pointers cross
        # Manually choose the larger block (no max())
        if blocks[left] >= blocks[right]:
            chosen = blocks[left]
            left += 1  # move left pointer inward
        else:
            chosen = blocks[right]
            right -= 1  # move right pointer inward

        # check placement
        if chosen <= top:
            top = chosen
        else:
            result = "No"
            break

    print(result)

# -------------------------------------------------
# Complexity Analysis (Solution 2):
# -------------------------------------------------
# Let n = number of blocks in a test case.
# - Each iteration processes one block (n iterations total).
# - No pop(0), just index manipulation (O(1) per step).
# - Time complexity: O(n).
# - Space complexity: O(n) for storing the blocks list.
# -------------------------------------------------