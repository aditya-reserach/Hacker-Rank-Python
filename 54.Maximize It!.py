"""
================================================================================
Problem Statement: Maximize It! (Combinatorial Optimization Problem)
================================================================================

You are given K lists. Each list contains Ni integers. You need to pick exactly 
one integer from each list, then square that integer, and sum all these squared 
numbers together. Finally, take the result modulo M. The objective is to 
maximize this value.

--------------------------------------------------------------------------------
Input Format:
--------------------------------------------------------------------------------
The first line contains two space-separated integers:
    K -> the number of lists
    M -> the modulo base

The next K lines each describe a list:
    The first integer in a line is Ni -> the number of elements in the list
    The next Ni integers describe the contents of the list

--------------------------------------------------------------------------------
Output Format:
--------------------------------------------------------------------------------
Print the maximum value of (sum of selected squares) % M

--------------------------------------------------------------------------------
Constraints:
--------------------------------------------------------------------------------
1 <= K <= 7
1 <= Ni <= 7
1 <= M <= 1000
1 <= Elements of the lists <= 10^9

--------------------------------------------------------------------------------
Example:
--------------------------------------------------------------------------------
Input:
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10

Step by Step:
- List 1 = [5, 4] -> squared: [25, 16]
- List 2 = [7, 8, 9] -> squared: [49, 64, 81]
- List 3 = [5, 7, 8, 9, 10] -> squared: [25, 49, 64, 81, 100]

Pick one number from each list, compute sum of chosen squares % 1000.
The maximum such value is: 206

Output:
206

================================================================================
SOLUTION 1: Using itertools.product (prebuilt Cartesian product)
================================================================================
"""

from itertools import product  # import the itertools module for Cartesian product

# Step 1: Read K and M
K, M = list(map(int, input().split()))  # input().split() reads the line, map(int, ...) converts to int, list() stores as list [K, M]

# Step 2: Read all K lists
# For each list, skip the first element (list length) using [1::]
inp = [list(map(int, input().split()))[1::] for _ in range(K)]

# Step 3: Square all elements in each list
super_squared_elements = []  # to hold all lists of squared elements
for i in inp:  # iterate over each list
    squared_elements = []  # temp list for squared values
    for j in i:  # iterate each element in the current list
        squared_elements.append(j * j)  # square the element and append
    super_squared_elements.append(squared_elements)  # add squared list to master list

# Step 4: Generate Cartesian product of all squared lists
cartesian_product = list(product(*super_squared_elements))  
# product(*lists) picks one element from each list and generates all possible tuples

# Step 5: Compute (sum of tuple) % M for each combination
max_check_appended = []  # to store modulo results
for val in cartesian_product:  # iterate over each tuple from Cartesian product
    max_check_appended.append(sum(val) % M)  # sum the tuple, take modulo M, store in list

# Step 6: Print maximum modulo value
print(max(max_check_appended))  # maximum value from all modulo results

"""
--------------------------------------------------------------------------------
Time Complexity Analysis for Solution 1:
--------------------------------------------------------------------------------
- Squaring elements: O(S), where S = total number of elements across all lists
- Cartesian product generation: O(N1 * N2 * ... * Nk), exponential in K
- For each combination, we compute sum of K elements: O(K)
Total = O(K * Π(Ni)) where Ni is the size of each list
Space = O(Π(Ni)) to store all combinations explicitly

This brute-force approach is feasible because constraints are small (K <= 7, Ni <= 7).
================================================================================
SOLUTION 2: Without using prebuilt itertools.product (manual recursion)
================================================================================
"""

# Step 1: Read K and M
K, M = map(int, input().split())  # directly read K, M as integers

# Step 2: Read all lists and skip the first element (size)
inp = [list(map(int, input().split()))[1:] for _ in range(K)]

# Step 3: Square all elements in each list
super_squared_elements = []  # to hold squared lists
for i in inp:  # for each list
    squared_elements = []  # hold squared values
    for j in i:  # for each number in list
        squared_elements.append(j * j)  # square the number
    super_squared_elements.append(squared_elements)  # append to main list

max_mod = 0  # global variable to store maximum modulo result

# Step 4: Recursive function to simulate Cartesian product
def dfs(level, current_sum):  
    global max_mod  # use global to update maximum
    if level == K:  # base case: we have chosen one number from each list
        max_mod = max(max_mod, current_sum % M)  # compute modulo, update max
        return
    for val in super_squared_elements[level]:  # iterate over current list values
        dfs(level + 1, current_sum + val)  # recurse to next list, add chosen value

# Step 5: Start recursion from first list with sum = 0
dfs(0, 0)

# Step 6: Print result
print(max_mod)

"""
--------------------------------------------------------------------------------
Time Complexity Analysis for Solution 2:
--------------------------------------------------------------------------------
- Squaring elements: O(S), where S = total number of elements across all lists
- DFS recursion explores all possible combinations: O(Π(Ni)), same as product
- Each recursive path computes sums incrementally, so cost per path is O(1) (no need to sum entire tuple each time)
Total = O(Π(Ni)) where Ni is size of each list
Space = O(K) recursion stack depth (better than Solution 1 which stored all tuples)

"""
