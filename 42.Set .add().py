"""
Problem: Stamp Collection (HackerRank Problem)

You are given a number of country stamps collected by a person. Some stamps may be from the same country, 
and duplicates should not be counted. You must find the total number of distinct country stamps.

-------------------------------------------------------
Input Format:
- The first line contains an integer N, the number of country stamps.
- The next N lines each contain the name of a country.

Output Format:
- Output the total number of distinct country stamps.

-------------------------------------------------------
Constraints:
1 <= N <= 1000
The country name consists of only English letters.

-------------------------------------------------------
Example:
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
- The unique countries are {UK, China, USA, France, NewZealand}
- Hence, answer = 5
"""

# -------------------------------------------------------
# 🔹 Solution 1: Using Python's built-in set() (Best + Efficient)
# -------------------------------------------------------

# Step 1: Read the total number of country stamps
n = int(input().strip())  # O(1) operation

# Step 2: Use set comprehension to store countries
# - A set automatically ignores duplicates
# - We read n times and add to the set
unique_countries = {input().strip() for _ in range(n)}  # O(n) average time

# Step 3: Output the total number of unique countries
print(len(unique_countries))  # O(1)

"""
✅ Time Complexity (Solution 1):
- Reading N inputs → O(n)
- Insertion into set → O(1) average per element (hashing)
- Total → O(n)

✅ Space Complexity (Solution 1):
- We store only unique countries in a set → O(n)
- Hence, space = O(n)
"""

# -------------------------------------------------------
# 🔹 Solution 2: Without using prebuilt set() (Manual Implementation)
# -------------------------------------------------------

# Step 1: Read the total number of country stamps
m = int(input().strip())  # O(1)

# Step 2: Create an empty list to track unique countries manually
unique_country_list = []  # Initially empty → O(1)

# Step 3: Loop over each input country
for _ in range(m):  # Runs m times → O(m)
    country = input().strip()  # Read one country name
    
    # Flag to check if the country already exists
    is_present = False  # O(1)
    
    # Check manually if the country is already stored
    # This requires scanning the entire list in worst case
    for c in unique_country_list:  # O(k), where k is current unique count
        if c == country:  # Comparison O(1)
            is_present = True
            break  # Exit once found
    
    # If not found, add to our manual "unique list"
    if not is_present:
        unique_country_list.append(country)  # O(1)

# Step 4: Output the total number of unique countries
print(len(unique_country_list))  # O(1)

"""
✅ Time Complexity (Solution 2):
- Reading M inputs → O(m)
- Checking duplicates manually → Worst case O(m) for each input
- Total worst-case → O(m²)

✅ Space Complexity (Solution 2):
- We store only unique countries in a list → O(m)
- Hence, space = O(m)
"""

# -------------------------------------------------------
# 📌 Final Notes:
# - Solution 1 is much faster and recommended in real-world coding (O(n)).
# - Solution 2 demonstrates the manual approach without using prebuilt set() 
#   but is slower (O(n²)).
# -------------------------------------------------------
