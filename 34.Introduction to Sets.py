# ====================================================
# Problem Statement:
# ====================================================
# You are given an array of integers representing the heights of plants in a greenhouse.
# Your task is to compute the average height of all distinct heights.
# A set is an unordered collection of unique elements in Python.
# Using sets, you can automatically remove duplicate heights.
# The output should be a float rounded to 3 decimal places.
# 
# Input Format:
# - The first line contains an integer n, the size of the array.
# - The second line contains n space-separated integers representing the heights.
#
# Output Format:
# - A single float number rounded to 3 decimal places representing the average of distinct heights.
#
# Sample Input:
# 10
# 161 182 161 154 176 170 167 171 170 174
#
# Sample Output:
# 169.375
#
# ====================================================

# ====================================================
# Code 1: Using Prebuilt Functions (set, sum, len)
# ====================================================

def average(array):
    # Step 1: Convert array to set to get distinct heights
    # set(array) removes duplicate elements automatically
    # Example: [161, 182, 161] -> set([161, 182])
    distinct = set(array)
    
    # Step 2: Compute sum of all unique heights
    # sum(distinct) iterates through the set and adds all elements
    total = sum(distinct)
    
    # Step 3: Compute number of unique elements
    # len(distinct) returns the count of elements in the set
    count = len(distinct)
    
    # Step 4: Compute average
    # Divide sum by count to get average
    avg = total / count
    
    # Step 5: Return the average rounded to 3 decimal places
    return round(avg, 3)


if __name__ == '__main__':
    # Read number of heights
    n = int(input())
    
    # Read heights as space-separated integers and convert to list
    arr = list(map(int, input().split()))
    
    # Call the average function
    result = average(arr)
    
    # Print the result
    print(result)


# Time Complexity of Code 1:
# - Converting array to set: O(N) (iterate through array)
# - sum(distinct): O(N) (iterate through unique elements, max N)
# - len(distinct): O(1)
# Total: O(N) + O(N) + O(1) = O(2N) → O(N)
#
# Space Complexity of Code 1:
# - set(distinct) stores all unique elements: O(N)
# - Other variables are O(1)
# Total: O(N)


# ====================================================
# Code 2: Without Using Prebuilt Functions
# ====================================================

def average_manual(array):
    """
    Compute average of distinct elements without using set().
    """
    # Step 1: Initialize empty list to store unique heights
    unique = []
    
    # Step 2: Iterate over each element in the input array
    for height in array:
        # Check if height is already in unique list
        # If not, append it
        if height not in unique:
            unique.append(height)
    
    # Step 3: Compute sum of unique elements manually
    total = 0
    for val in unique:
        total += val
    
    # Step 4: Compute count of unique elements
    count = len(unique)
    
    # Step 5: Compute average
    avg = total / count
    
    # Step 6: Return average rounded to 3 decimal places
    return round(avg, 3)


if __name__ == '__main__':
    # Read input size
    n = int(input())
    
    # Read heights as integers
    arr = list(map(int, input().split()))
    
    # Call manual average function
    result = average_manual(arr)
    
    # Print result
    print(result)


# Time Complexity of Code 2:
# - Loop to build unique list: O(N^2) worst-case
#   (for each element, we check 'height not in unique', which is O(N))
# - Loop to sum unique: O(N) (at most N elements)
# Total: O(N^2 + N) → O(N^2)
#
# Space Complexity of Code 2:
# - unique list stores all distinct elements: O(N)
# - Other variables: O(1)
# Total: O(N)

# ====================================================
# Comparison Notes:
# - Code 1 (with set) is much faster for large inputs because it uses hash-based set lookup: O(N)
# - Code 2 (without set) is slower due to linear search in list for duplicates: O(N^2)
# - Space complexity is similar for both: O(N)
# ====================================================
