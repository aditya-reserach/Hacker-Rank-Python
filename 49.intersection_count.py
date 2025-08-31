"""
Problem Statement:
===================
You are given the roll numbers of students subscribed to the English newspaper and 
the roll numbers of students subscribed to the French newspaper. 
Your task is to find the number of students who have subscribed to both newspapers 
(i.e., the size of the intersection of the two sets).

Input Format:
--------------
- The first line contains an integer n, the number of students who have subscribed to the English newspaper.
- The second line contains n space-separated roll numbers of the students.
- The third line contains an integer m, the number of students who have subscribed to the French newspaper.
- The fourth line contains m space-separated roll numbers of the students.

Output Format:
---------------
- Print a single integer: the number of students who are subscribed to both newspapers.

Constraints:
-------------
1 <= n, m <= 10^5
Each roll number is a positive integer (unique within a single list but not necessarily unique across both).

Example:
---------
Input:
4
1 2 3 4
4
3 4 5 6

Output:
2
"""

# --------------------------------------------------------
# Solution 1: Using Python built-in functions (HackerRank style)
# --------------------------------------------------------

n = int(input())                           # number of English subscribers
english_rolls = set(map(int, input().split()))  # convert English roll numbers to a set

m = int(input())                           # number of French subscribers
french_rolls = set(map(int, input().split()))   # convert French roll numbers to a set

print(len(english_rolls.intersection(french_rolls)))  # intersection gives common elements; len() counts them

# ---------------- Explanation for Solution 1 ----------------
# - input() reads user input
# - int() converts it into integer
# - map(int, input().split()) converts each space-separated value into an integer
# - set(...) stores values in a hash set (fast lookups, no duplicates)
# - intersection(...) finds common elements between two sets
# - len(...) counts those elements
#
# Complexity (Solution 1):
# - Building each set: O(n) for English, O(m) for French
# - Intersection operation: O(min(n, m)) on average (hash lookups are O(1))
# - Overall Time Complexity: O(n + m)
# - Space Complexity: O(n + m) (for storing both sets)


# --------------------------------------------------------
# Solution 2: Manual implementation (without pre-built set operations)
# --------------------------------------------------------

n = int(input())                           # number of English subscribers
english_rolls = list(map(int, input().split()))  # roll numbers (store as list)

m = int(input())                           # number of French subscribers
french_rolls = list(map(int, input().split()))   # roll numbers (store as list)

english_dict = {}                          # dictionary to mark English subscribers
for roll in english_rolls:                 # iterate over English rolls
    english_dict[roll] = True              # mark each as present (True)

common_count = 0                           # variable to count intersection
for roll in french_rolls:                  # iterate over French rolls
    if roll in english_dict:               # check if also in English dictionary
        common_count += 1                  # increase count if common
        english_dict[roll] = False         # mark as False to avoid double counting

print(common_count)                        # print the final result

# ---------------- Explanation for Solution 2 ----------------
# - We store English rolls in a dictionary (hash map), using roll number as key
# - For each French roll, we check if it's present in the dictionary
# - If yes, we increment the counter and mark it False to avoid duplicates
#
# Complexity (Solution 2):
# - Building the dictionary from English rolls: O(n)
# - Checking each French roll: O(m), since hash map lookup is O(1) average
# - Overall Time Complexity: O(n + m)
# - Space Complexity: O(n) (dictionary for English rolls only)
#   Slightly better than Solution 1, which stores both sets.


