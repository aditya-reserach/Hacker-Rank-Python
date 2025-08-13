"""
Problem: List Comprehensions - 3D Grid Coordinates

You are given three integers x, y, and z representing the dimensions of a cuboid,
and a fourth integer n.

Task:
Print a list of all possible coordinates [i, j, k] on a 3D grid such that:
    0 <= i <= x
    0 <= j <= y
    0 <= k <= z
    and i + j + k != n

Use list comprehensions to solve the problem instead of nested loops.
The output list must be in lexicographic increasing order.

Input Format:
Four integers, one on each line:
    x
    y
    z
    n

Constraints:
    0 <= x, y, z <= 100
    0 <= n <= x + y + z

Sample Input:
1
1
1
2

Sample Output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Explanation:
All combinations of i, j, k from 0 to x/y/z are generated.
Combinations where the sum i + j + k equals n are excluded.
"""

if __name__ == '__main__':
    # Read input values for dimensions and the constraint value
    x = int(input())  # Maximum value for i (inclusive)
    y = int(input())  # Maximum value for j (inclusive)
    z = int(input())  # Maximum value for k (inclusive)
    n = int(input())  # Sum value to exclude from the results

    # Using list comprehension to generate valid coordinate combinations
    result = [
        [i, j, k]
        for i in range(x + 1)       # range is exclusive, so we use x + 1 to include x
        for j in range(y + 1)       # similarly, include y
        for k in range(z + 1)       # and include z
        if (i + j + k) != n         # exclude combinations where the sum equals n
    ]

    # Print the final list of valid coordinates
    print(result)
