"""
Problem Statement:

You are given a spreadsheet that contains a list of athletes and their details 
(such as age, height, weight and so on). You are required to sort the data 
based on the k-th attribute and print the final resulting table. 

Note that k is indexed from 0 to m-1, where m is the number of attributes.

If two attributes are the same for different rows (for example, if two athletes 
are of the same age), print the row that appeared first in the input.

------------------------------------------------------------
Input Format:
- The first line contains n and m separated by a space.
- The next n lines each contain m elements (the table of athlete data).
- The last line contains k (the attribute index to sort by).

Constraints:
- 1 <= n <= 1000
- 1 <= m <= 100
- Each element is an integer.

------------------------------------------------------------
Output Format:
- Print the n lines of the sorted table.
- Each line should contain the space separated elements.

------------------------------------------------------------
Sample Input 0:
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output 0:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

Explanation 0:
The details are sorted based on the second attribute (index 1, zero-indexed).
------------------------------------------------------------
"""

# ------------------------------------------------------------
# Solution 1: Using Python's built-in sorting (HackerRank style)
# ------------------------------------------------------------

if __name__ == '__main__':
    nm = input().split()                      # Read first line as strings and split into a list
    n = int(nm[0])                            # Convert first part to integer → number of rows
    m = int(nm[1])                            # Convert second part to integer → number of columns

    arr = []                                  # Create an empty list to store the table
    for _ in range(n):                        # Repeat n times (for each row of the table)
        arr.append(list(map(int, input().split())))
        # input().split() → splits the line into pieces (strings)
        # map(int, ...)   → converts each piece into integer
        # list(...)       → converts the map object into a list
        # arr.append(...) → add this list (row) to the table

    k = int(input())                          # Read the column index to sort by

for info in sorted(arr, key=lambda x: x[k]):  # Use sorted() with a key function
    # sorted(arr, key=lambda x: x[k]) → 
    # - looks at each row x in arr
    # - extracts the k-th element (x[k])
    # - sorts the entire list based on those values
    # Sorting is stable: equal elements keep their original order

    print(*info)                              # Print row values space-separated
    # *info unpacks the list, so [7, 1, 0] becomes "7 1 0"


"""
Time Complexity Analysis (Solution 1):
- sorted() in Python uses Timsort.
- Worst case: O(n log n), where n is number of rows.
- Each comparison involves accessing one element (O(1)).
- Total time: O(n log n).
- Example: for n = 1000, complexity is about 1000 log(1000) ≈ 10,000 operations.

Space Complexity (Solution 1):
- arr stores n * m integers → O(n*m).
- sorted() creates a new sorted list → O(n).
- Total: O(n*m + n) ≈ O(n*m).
"""

# ------------------------------------------------------------
# Solution 2: Manual Bubble Sort Implementation (No built-ins)
# ------------------------------------------------------------

if __name__ == '__main__':
    nm = input().split()                      # Read first line as strings and split
    n = int(nm[0])                            # Convert first part to integer → number of rows
    m = int(nm[1])                            # Convert second part to integer → number of columns

    arr = []                                  # Create empty list for the table
    for _ in range(n):                        # Repeat n times to read rows
        arr.append(list(map(int, input().split())))
        # Read a row, split into pieces, convert to integers, store as list

    k = int(input())                          # Read the column index to sort by

    # Bubble Sort Algorithm
    for i in range(n):                        # Outer loop → do n passes
        for j in range(0, n - i - 1):         # Inner loop → compare neighbors
            if arr[j][k] > arr[j+1][k]:       # Compare k-th column values
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # If out of order, swap rows

    for row in arr:                           # Print final sorted table
        print(*row)                           # Print space-separated row values


"""
Time Complexity Analysis (Solution 2):
- Bubble Sort has two nested loops.
- Outer loop runs n times.
- Inner loop runs (n-i-1) times → total about n*(n-1)/2 ≈ O(n^2).
- Each comparison is O(1).
- Total time: O(n^2).
- Example: for n = 1000, about 1,000,000 comparisons.

Space Complexity (Solution 2):
- arr stores n * m integers → O(n*m).
- No extra data structures (only swaps in place).
- Total: O(n*m).
"""

