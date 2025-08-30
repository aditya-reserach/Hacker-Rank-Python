"""
============================================================
Problem Statement
============================================================

The dot tool returns the dot product of two arrays.

Example:
---------
import numpy
A = numpy.array([1, 2])
B = numpy.array([3, 4])
print(numpy.dot(A, B))  # Output: 11

The cross tool returns the cross product of two arrays.

Example:
---------
import numpy
A = numpy.array([1, 2])
B = numpy.array([3, 4])
print(numpy.cross(A, B))  # Output: -2

Task:
------
You are given two arrays (matrices) A and B. Both have dimensions N x N.
Your task is to compute their matrix product (A × B).

Input Format:
--------------
The first line contains the integer N (the size of the square matrix).
The next N lines each contain N space-separated integers describing matrix A.
The following N lines each contain N space-separated integers describing matrix B.

Output Format:
---------------
Print the matrix multiplication of A and B as a 2D array (like NumPy format).

Constraints:
-------------
1 <= N <= 100
-100 <= elements of A, B <= 100

Sample Input:
--------------
2
1 2
3 4
1 2
3 4

Sample Output:
---------------
[[ 7 10]
 [15 22]]
============================================================
"""

# ==========================================================
# SOLUTION 1: Using Python's built-in NumPy library (HackerRank style)
# ==========================================================

import numpy as np  # Import the numpy library, which provides optimized matrix operations

# Step 1: Read the input integer N (dimension of the square matrix)
n = int(input())  # input() reads a line from standard input, int() converts it to integer

# Step 2: Read N lines, each containing N integers, to form matrix A
A = [list(map(int, input().split())) for _ in range(n)]
# - input().split() reads a line and splits it into parts (strings) by spaces
# - map(int, ...) converts each string to integer
# - list(...) converts the mapped values into a list
# - This happens for each row, repeated N times in the list comprehension

# Step 3: Read N lines, each containing N integers, to form matrix B
B = [list(map(int, input().split())) for _ in range(n)]

# Step 4: Convert lists A and B into numpy arrays
A = np.array(A)
B = np.array(B)

# Step 5: Perform matrix multiplication using NumPy's matmul (optimized in C)
result = np.matmul(A, B)

# Step 6: Print the result directly (NumPy prints in matrix style)
print(result)

# -------------------------
# Time Complexity Analysis:
# -------------------------
# - Input reading: O(N^2) for matrix A + O(N^2) for matrix B = O(N^2)
# - np.matmul uses optimized BLAS libraries, but theoretically the complexity is O(N^3)
#   (because every result cell requires N multiplications and N-1 additions)
# - Total Time = O(N^3) (though in practice much faster due to vectorization)
#
# -------------------------
# Space Complexity Analysis:
# -------------------------
# - Matrix A storage: O(N^2)
# - Matrix B storage: O(N^2)
# - Result matrix storage: O(N^2)
# - Total = O(N^2)
#
# NumPy may also use additional temporary arrays internally, but asymptotically space is O(N^2).

# ==========================================================
# SOLUTION 2: Manual Implementation Without NumPy
# ==========================================================

# Step 1: Read input integer N again (to keep code independent)
n = int(input())

# Step 2: Read N lines for matrix A
A = [list(map(int, input().split())) for _ in range(n)]

# Step 3: Read N lines for matrix B
B = [list(map(int, input().split())) for _ in range(n)]

# Step 4: Initialize result matrix filled with zeros
result = [[0 for _ in range(n)] for _ in range(n)]
# - Outer list comprehension runs n times (rows)
# - Inner list comprehension runs n times (columns), filling each with 0
# - So result is an n x n matrix of zeros

# Step 5: Perform matrix multiplication using triple nested loops
for i in range(n):          # Loop over rows of A (0 to n-1)
    for j in range(n):      # Loop over columns of B (0 to n-1)
        for k in range(n):  # Loop over elements in row i of A and column j of B
            # Multiply element from row i of A and column j of B, add to current cell
            result[i][j] += A[i][k] * B[k][j]

# Step 6: Print the result row by row
for row in result:
    print(row)
# Each row is printed as a Python list (like [7, 10]) to match typical HackerRank output

# -------------------------
# Time Complexity Analysis:
# -------------------------
# - Input reading: O(N^2) + O(N^2) = O(N^2)
# - Initialization of result matrix: O(N^2)
# - Triple nested loop:
#   * Outer loop runs N times (rows of A)
#   * Middle loop runs N times (columns of B)
#   * Inner loop runs N times (dot product calculation)
#   * Total = N * N * N = O(N^3)
# - Printing result: O(N^2)
# - Total Time = O(N^3)
#
# -------------------------
# Space Complexity Analysis:
# -------------------------
# - Matrix A: O(N^2)
# - Matrix B: O(N^2)
# - Result: O(N^2)
# - No extra structures beyond these
# - Total = O(N^2)
#
# Note: This implementation is straightforward but much slower than NumPy’s optimized version.
