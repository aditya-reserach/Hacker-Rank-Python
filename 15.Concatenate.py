"""
=====================================================
Problem Statement
=====================================================

Concatenate Two Arrays

You are given two integer arrays of size N x P and M x P 
(N and M are rows, P is the number of columns). 
Your task is to concatenate the arrays along axis = 0 
(i.e., vertically stack them one after another).

-----------------------------------------------------
Input Format:
-----------------------------------------------------
- The first line contains space separated integers: N, M, P
- The next N lines contain the first array (N rows, P columns)
- The next M lines contain the second array (M rows, P columns)

-----------------------------------------------------
Output Format:
-----------------------------------------------------
- Print the concatenated array of size (N+M) x P in a 
  NumPy-like format.

-----------------------------------------------------
Sample Input:
-----------------------------------------------------
4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4

-----------------------------------------------------
Sample Output:
-----------------------------------------------------
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]

=====================================================
Approach 1: Using NumPy (built-in library)
=====================================================
- Use numpy.array() to create arrays.
- Use numpy.concatenate() with axis=0 to join them.
- Print the result.

Time Complexity: O((N+M) * P)
    - Reading input → O((N+M) * P)
    - Concatenation in NumPy → O((N+M) * P)
Space Complexity: O((N+M) * P)

=====================================================
Approach 2: Without NumPy (manual implementation)
=====================================================
- Read the values manually into lists.
- Append rows of the second array after the first array.
- Write a custom pretty-printer to display the result in 
  NumPy-like format.

Time Complexity: O((N+M) * P)
    - Reading input → O((N+M) * P)
    - Concatenation (manual) → O((N+M) * P)
Space Complexity: O((N+M) * P)
"""

# =====================================================
# APPROACH 1: Using NumPy (built-in library)
# =====================================================
def approach_with_numpy():
    # Import numpy library (provides built-in arrays and operations)
    import numpy as np
    
    # Step 1: Read the values of N, M, P
    # N = rows of first array
    # M = rows of second array
    # P = number of columns in both arrays
    N, M, P = map(int, input().split())
    
    # Step 2: Read the first array
    # We use list comprehension:
    #   - for _ in range(N): repeat N times
    #   - input().split() reads P numbers per row
    #   - map(int, ...) converts them to integers
    array1 = [list(map(int, input().split())) for _ in range(N)]
    
    # Step 3: Read the second array in the same way (M rows)
    array2 = [list(map(int, input().split())) for _ in range(M)]
    
    # Step 4: Convert lists to NumPy arrays for easier operations
    arr1 = np.array(array1)
    arr2 = np.array(array2)
    
    # Step 5: Concatenate along axis=0 (row-wise stacking)
    result = np.concatenate((arr1, arr2), axis=0)
    
    # Step 6: Print the result (NumPy automatically formats like the example)
    print(result)


# =====================================================
# APPROACH 2: Without NumPy (manual implementation)
# =====================================================
def approach_without_numpy():
    # Step 1: Read N, M, P
    N, M, P = map(int, input().split())
    
    # Step 2: Read the first array manually into a list of lists
    array1 = [list(map(int, input().split())) for _ in range(N)]
    
    # Step 3: Read the second array manually into a list of lists
    array2 = [list(map(int, input().split())) for _ in range(M)]
    
    # Step 4: Concatenate manually by adding lists together
    # In Python, list1 + list2 = combined list
    result = array1 + array2
    
    # Step 5: Pretty-print result in NumPy-like format
    # We cannot just print(result) because it would give:
    # [[1, 2], [3, 4]]
    # (with commas). NumPy does not show commas, so we build manually.
    
    print("[", end="")  # Opening outer bracket
    
    # Loop over each row in result
    for i, row in enumerate(result):
        print("[", end="")  # Opening bracket for the row
        
        # Loop over each number in row
        for j, val in enumerate(row):
            if j < len(row) - 1:
                # If not last element, print with a space
                print(val, end=" ")
            else:
                # Last element → print without extra space
                print(val, end="")
        
        # After finishing the row, decide how to close it
        if i < len(result) - 1:
            # Not last row → close row and move to next line
            print("]")
            print(" ", end="")  # Leading space for next row (NumPy style)
        else:
            # Last row → close row but do not move to new line
            print("]", end="")
    
    print("]")  # Closing outer bracket


# =====================================================
# MAIN DRIVER
# =====================================================
if __name__ == "__main__":
    # You can uncomment whichever approach you want to run

    # Approach 1: Using NumPy (easier, shorter)
    # approach_with_numpy()

    # Approach 2: Without NumPy (manual, educational)
    approach_without_numpy()
