"""
-------------------------------------------------------------
Problem: "Introduction to Sets" (HackerRank Style)

TASK:
You are given a sequence of country stamps (strings). Some country
stamps may be repeated. Your task is to count the number of distinct
countries from the input.

INPUT FORMAT:
- The first line contains an integer n, the number of country stamps.
- The next n lines each contain the name of one country stamp (a string).

OUTPUT FORMAT:
- Print a single integer: the number of distinct country stamps.

CONSTRAINTS:
- 0 <= n <= 1000
- Each country name is a string containing only letters (a–z, A–Z).

EXAMPLE:
Input:
7
UK
China
USA
France
NewZealand
UK
France

Output:
5

Explanation:
The unique countries are:
UK, China, USA, France, NewZealand → total count = 5.

-------------------------------------------------------------
Below are TWO SOLUTIONS:

1) Solution using Python's built-in "set" data structure.
   (Efficient: O(n) average time complexity)

2) Solution WITHOUT using prebuilt set/dictionary functions.
   (Manual uniqueness tracking using a list. Less efficient: O(n^2))

Each line of code is commented in detail.
-------------------------------------------------------------
"""


# -------------------------------------------------------------
# SOLUTION 1: Using Python's built-in "set"
# -------------------------------------------------------------

# Read the number of country stamps
n = int(input().strip())  # .strip() removes any extra spaces/newlines

# Initialize an empty set to hold unique country names
country_set = set()

# Loop over n times to read each country
for _ in range(n):
    country = input().strip()  # Read a country name
    country_set.add(country)   # Add it to the set (duplicates ignored automatically)

# Finally, print the size of the set → number of unique countries
print(len(country_set))

"""
TIME COMPLEXITY (Solution 1):
- Insertion into a set is O(1) on average (due to hashing).
- We do this n times → O(n).
- Final len() is O(1).
Total Time = O(n)

SPACE COMPLEXITY (Solution 1):
- We store at most n unique countries in the set.
- Space = O(n).
"""



# -------------------------------------------------------------
# SOLUTION 2: WITHOUT using prebuilt "set"
# (Manual uniqueness tracking with a list)
# -------------------------------------------------------------

# Read the number of country stamps again
n = int(input().strip())

# Initialize an empty list to hold only unique country names
unique_countries = []

# Loop over n times to read each country
for _ in range(n):
    country = input().strip()  # Read a country name
    
    # Flag variable to check if this country already exists
    is_present = False
    
    # Manually check if the country is already in unique_countries
    for c in unique_countries:   # Iterate through all stored unique entries
        if c == country:         # If we find a match
            is_present = True    # Mark as present
            break                # Stop checking further
    
    # If not present, add to the list
    if not is_present:
        unique_countries.append(country)

# Finally, print the size of the unique_countries list
print(len(unique_countries))

"""
TIME COMPLEXITY (Solution 2):
- For each of the n inputs, we may scan the list of unique_countries.
- In the worst case, unique_countries length = n, so scanning takes O(n).
- Therefore, worst-case time = O(n^2).
- Final len() is O(1).
Total Time = O(n^2)

SPACE COMPLEXITY (Solution 2):
- We store at most n unique countries in the list.
- Space = O(n).
"""

# -------------------------------------------------------------
# END OF FILE
# -------------------------------------------------------------
