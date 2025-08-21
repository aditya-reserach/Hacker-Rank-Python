"""
Problem Statement:
-----------------
A shoe shop owner has a collection of shoes in his shop.
- The first input line contains the total number of shoes (X).
- The second line contains the space-separated list of shoe sizes available in the shop.
- The third input line contains the number of customers (N).
- The next N lines contain two integers each:
    - Desired shoe size (size)
    - Price the customer is willing to pay (price)

Rules:
------
- A customer will only buy a shoe if the desired size is available in stock.
- Once a shoe size is sold, it cannot be sold again (stock decreases by 1).
- The task is to calculate the total amount of money earned by the shop owner.

Constraints:
------------
- 0 < X < 10^3   (Number of shoes)
- 0 < N < 10^3   (Number of customers)
- Shoe sizes and prices are integers.

Output:
-------
Print the total money earned.

Example:
--------
Input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Output:
200
"""

# =====================================================================
# ✅ Solution 1: Without using prebuilt functions (Manual Dictionary)
# =====================================================================

# Step 1: Read the total number of shoes in the shop.
X = int(input().strip())  # Example: 10

# Step 2: Read the shoe sizes in stock and store them in a list.
# Example input: 2 3 4 5 6 8 7 6 5 18
shoe_list = list(map(int, input().split()))

# Step 3: Create a dictionary to count how many shoes of each size exist.
shoe_stock = {}  # Initialize empty dictionary
for size in shoe_list:  # Loop over each shoe size in the list
    if size in shoe_stock:
        # If size already exists in dictionary, increase its count
        shoe_stock[size] += 1
    else:
        # Otherwise, add it with count = 1
        shoe_stock[size] = 1

# Step 4: Read the number of customers
N = int(input().strip())  # Example: 6

# Step 5: Initialize total money earned to 0
total_money = 0

# Step 6: Process each customer's request
for _ in range(N):  # Loop N times (for each customer)
    size, price = map(int, input().split())  # Read desired size and offered price
    # Check if the requested size exists in stock and count > 0
    if size in shoe_stock and shoe_stock[size] > 0:
        total_money += price          # Add the price to total earnings
        shoe_stock[size] -= 1         # Reduce available stock of that size by 1

# Step 7: Print the total money earned
print(total_money)

"""
Time Complexity (Solution 1):
-----------------------------
- Building dictionary: O(X)  [one pass over shoe_list]
- Processing customers: O(N) [one pass over N customers]
- Overall: O(X + N)
- Space Complexity: O(U) where U = number of unique shoe sizes
"""

# =====================================================================
# ✅ Solution 2: Using collections.Counter (Prebuilt Function)
# =====================================================================

# Import Counter class from collections module
from collections import Counter

# Step 1: Read the total number of shoes in the shop.
X = int(input().strip())  # Example: 10

# Step 2: Use Counter to build dictionary of shoe sizes automatically
# Counter creates a dictionary-like object: {shoe_size: count}
# Example: Counter([2,3,4,5,6,8,7,6,5,18]) -> {2:1, 3:1, 4:1, 5:2, 6:2, 8:1, 7:1, 18:1}
shoe_stock = Counter(map(int, input().split()))

# Step 3: Read number of customers
N = int(input().strip())  # Example: 6

# Step 4: Initialize total money earned to 0
total_money = 0

# Step 5: Process each customer's request
for _ in range(N):  # Loop over each customer
    size, price = map(int, input().split())  # Read desired size and offered price
    if shoe_stock[size] > 0:       # If stock for requested size > 0
        total_money += price       # Add price to total earnings
        shoe_stock[size] -= 1      # Reduce stock by 1

# Step 6: Print the total money earned
print(total_money)

"""
Time Complexity (Solution 2):
-----------------------------
- Counter creation: O(X) [optimized C implementation under the hood]
- Processing customers: O(N)
- Overall: O(X + N)
- Space Complexity: O(U) where U = number of unique shoe sizes
"""
