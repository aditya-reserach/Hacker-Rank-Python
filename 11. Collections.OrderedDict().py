"""
Problem Statement:
------------------
You are the manager of a supermarket. You have a list of items along with their prices
that customers bought on a particular day.

Your task is to print each item name and the net price (i.e., total price for that item)
in the order of their first occurrence.

Definitions:
- item_name: The name of the item (can have spaces).
- net_price: The total price calculated by summing prices for all entries of the same item.

Input Format:
-------------
The first line contains an integer N — the number of items.
The next N lines each contain the item name and price, separated by a space.
Item names may contain multiple words.

Output Format:
--------------
Print the item name and net price for each item in the order of first occurrence.

Constraints:
------------
- 0 < N <= 10^5
- 1 <= price <= 10^4

Sample Input:
-------------
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output:
--------------
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""

# ------------------------------------------
# Approach 1: Using split() and join() with OrderedDict
# ------------------------------------------

from collections import OrderedDict  # Import OrderedDict to maintain insertion order

n = int(input())  # Read number of inputs and convert it to integer
item_list = OrderedDict()  # Create an OrderedDict to store items with total price

for _ in range(n):  # Loop through all input lines
    item = input().split()  # Split the input string into words (item parts + price)
    key = ' '.join(item[:-1])  # Join all words except the last one as item name
    value = int(item[-1])  # Convert the last word to integer (price)
    item_list[key] = item_list.get(key, 0) + value  # Add price to existing or new item

for k, v in item_list.items():  # Iterate over OrderedDict to print results
    print(k, v)

# Time Complexity:
# ----------------
# - Splitting and joining item name: O(k), where k = number of words in item name (usually small)
# - Looping through N inputs: O(N)
# - Dictionary operations (get, update): O(1) average per operation
# - Final print loop: O(M), where M = number of unique items
# => Overall Time Complexity: **O(N + M)** ≈ **O(N)**



# ------------------------------------------
# Approach 2: Cleaner unpacking with split() and join()
# ------------------------------------------

from collections import OrderedDict  # Again, import OrderedDict

N = int(input())  # Read number of items
od = OrderedDict()  # Create OrderedDict to store item-price mapping

for _ in range(N):  # Loop through each line of input
    line = input().split()  # Split the input string into list
    item, price = ' '.join(line[:-1]), int(line[-1])  # Unpack: item is all words except last, price is last
    od[item] = od.get(item, 0) + int(price)  # Use get() to add new or accumulate price

for item, price in od.items():  # Loop and print item with its net price
    print(item, price)

# Time Complexity:
# ----------------
# - Each split and join: O(k), small constant
# - Loop through N items: O(N)
# - Dictionary updates: O(1) average
# - Final loop to print: O(M)
# => Overall Time Complexity: **O(N + M)** ≈ **O(N)**



# ------------------------------------------
# Approach 3: Using rsplit() for robustness (handles edge cases better)
# ------------------------------------------

from collections import OrderedDict  # Import OrderedDict one more time for clarity

items = OrderedDict()  # Initialize OrderedDict

n = int(input())  # Read number of lines

for _ in range(n):  # Loop through inputs
    line = input().rstrip()  # Remove any trailing spaces/newlines
    name, price = line.rsplit(' ', 1)  # rsplit ensures we split only at the last space (item name can have spaces)
    price = int(price)  # Convert price to integer

    if name in items:  # If item already exists, add to the current total
        items[name] += price
    else:  # Otherwise, initialize it
        items[name] = price

for item_name, unit_price in items.items():  # Loop through OrderedDict to print
    print(f"{item_name} {unit_price}")  # Print in required format

# Time Complexity:
# ----------------
# - rsplit is more efficient than split + join for long item names: O(k), constant time per line
# - Loop through N items: O(N)
# - Dictionary insert/lookup: O(1) average
# - Final output loop: O(M)
# => Overall Time Complexity: **O(N + M)** ≈ **O(N)**
