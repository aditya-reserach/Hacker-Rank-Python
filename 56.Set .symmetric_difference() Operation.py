"""
====================================================
Problem Statement
====================================================

Students of District College have subscriptions to English and French newspapers. 
Some students have subscribed to English only, some have subscribed to French only, 
and some have subscribed to both newspapers.

You are given two sets of student roll numbers:
    - One set has subscribed to the English newspaper
    - One set has subscribed to the French newspaper

Your task is to find the total number of students who have subscribed 
to either the English or the French newspaper but not both.

----------------------------------------------------
Input Format
----------------------------------------------------
The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space-separated list of student roll numbers 
    who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space-separated list of student roll numbers 
    who have subscribed to the French newspaper.

----------------------------------------------------
Constraints
----------------------------------------------------
1 <= Total number of students in English set <= 1000
1 <= Total number of students in French set <= 1000
Roll numbers are integers and unique within each set.

----------------------------------------------------
Output Format
----------------------------------------------------
Output a single integer: the total number of students who have subscriptions 
to the English or the French newspaper but not both.

----------------------------------------------------
Sample Input
----------------------------------------------------
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

----------------------------------------------------
Sample Output
----------------------------------------------------
8

----------------------------------------------------
Explanation
----------------------------------------------------
- English subscribers: {1,2,3,4,5,6,7,8,9}
- French subscribers:  {10,1,2,3,11,21,55,6,8}
- Symmetric difference: {4,5,7,9,10,11,21,55}
- Total count = 8
====================================================
"""

# ==================================================
# Solution 1: Using built-in symmetric_difference()
# ==================================================

# Read input: first line is integer number of English subscribers
n = int(input())  # O(1) operation, reading one integer

# Read the roll numbers for English subscribers and convert into a set
m = set(input().split())  # O(n) to split string into list, O(n) to create set

# Read input: number of French subscribers
x = int(input())  # O(1) operation

# Read the roll numbers for French subscribers and convert into a set
y = set(input().split())  # O(m) to split string, O(m) to create set

# Use built-in symmetric_difference to find students in either set but not both
print(len(m.symmetric_difference(y)))  # O(n+m) for symmetric difference, O(1) for len()


"""
----------------------------------------------------
Time Complexity Analysis for Solution 1
----------------------------------------------------
- Reading inputs: O(n + m) (splitting and set conversion)
- symmetric_difference: O(n + m) (each element checked once in hash set)
- len(): O(1)
Total Time Complexity = O(n + m)

----------------------------------------------------
Space Complexity Analysis for Solution 1
----------------------------------------------------
- Two sets stored: O(n + m)
- Temporary set created by symmetric_difference: O(n + m)
Total Space Complexity = O(n + m)
"""


# ==================================================
# Solution 2: Without using prebuilt symmetric_difference()
# ==================================================

# Read input: first line is integer number of English subscribers
n = int(input())  # O(1)

# Read the roll numbers for English subscribers and convert into a set
english = set(input().split())  # O(n)

# Read input: number of French subscribers
x = int(input())  # O(1)

# Read the roll numbers for French subscribers and convert into a set
french = set(input().split())  # O(m)

# Compute difference manually: elements in English but not in French
diff1 = [e for e in english if e not in french]  # O(n), membership test O(1) each

# Compute difference manually: elements in French but not in English
diff2 = [f for f in french if f not in english]  # O(m), membership test O(1) each

# Total number of students in symmetric difference = size of diff1 + size of diff2
print(len(diff1) + len(diff2))  # O(1)


"""
----------------------------------------------------
Time Complexity Analysis for Solution 2
----------------------------------------------------
- Reading inputs: O(n + m)
- Checking elements of english against french: O(n)
- Checking elements of french against english: O(m)
- len() operations: O(1)
Total Time Complexity = O(n + m)

----------------------------------------------------
Space Complexity Analysis for Solution 2
----------------------------------------------------
- Two sets stored: O(n + m)
- Two temporary lists diff1 and diff2: O(n + m)
Total Space Complexity = O(n + m)

----------------------------------------------------
Key Difference
----------------------------------------------------
Solution 1 uses Python's built-in efficient C-implemented function,
while Solution 2 manually simulates the logic with list comprehensions.
Both achieve the same time complexity (O(n+m)), but Solution 1 is 
slightly faster in practice due to optimized internals.
"""
