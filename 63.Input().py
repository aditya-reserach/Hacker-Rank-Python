# Python 2.x solution for verifying if a polynomial evaluates to a given value
#
# Problem Statement:
# You are given a polynomial of a single variable x.
# You are also given values of x and k. The task is to verify if P(x) == k.
#
# Constraints:
# - All coefficients of the polynomial are integers.
# - x and k are integers.
#
# Input Format:
# - First line: space-separated integers x and k
# - Second line: a polynomial expression in terms of x
#
# Output Format:
# - Print True if P(x) == k, else print False
#
# Example:
# Input:
# 1 4
# x**3 + x**2 + x + 1
# Output:
# True

# Step 1: Read the values of x and k
# map(int, input().split()) takes the input string, splits it by spaces, 
# converts each element to an integer, and returns a list of integers.
# Then we unpack it into variables x and k.
x, k = map(int, input().split())  # Example: input "1 4" -> x=1, k=4

# Step 2: Read the polynomial expression from input and evaluate it at x
# input() in Python 2 evaluates the expression as Python code.
# eval(input()) evaluates the polynomial string, using the current value of x.
# Then, we compare the result with k using ==, which returns True or False.
print(eval(input()) == k)  # Example: input "x**3 + x**2 + x + 1" -> True

# Detailed explanation of how it works:
# - If x=1, k=4, and polynomial = "x**3 + x**2 + x + 1"
# - eval("x**3 + x**2 + x + 1") computes 1**3 + 1**2 + 1 + 1 = 4
# - 4 == 4 -> True, which is printed

# ---------------------------------------------------------------
# Time Complexity Analysis:
# ---------------------------------------------------------------
# - map(int, input().split()) -> O(1), since we are only reading 2 integers.
# - eval(input()) -> O(n) where n is the length of the polynomial expression string.
#   Evaluating the polynomial requires computing each term once (for simple arithmetic operations).
# Overall Time Complexity: O(n), dominated by evaluating the polynomial expression.

# Space Complexity Analysis:
# - Storing x and k requires O(1) space.
# - Storing the polynomial string requires O(n) space, where n is the length of the input string.
# Overall Space Complexity: O(n).
