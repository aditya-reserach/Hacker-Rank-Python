"""
===========================================================
Problem Statement:
===========================================================

A newly opened multinational brand has decided to base their company logo 
on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos 
based on this condition.

Your task:
----------
Given a string (company name in lowercase letters), find the top three 
most common characters in the string.

Rules for output:
-----------------
1. Print the three most common characters along with their occurrence count.
2. Sort in descending order of occurrence count.
3. If two characters have the same occurrence count, 
   then sort alphabetically (ascending order).

Input Format:
-------------
- A single line of input containing the string.

Constraints:
------------
- The string has at least 3 distinct characters.
- String only contains lowercase English letters.

Output Format:
--------------
- Print the three most common characters and their counts.
- Each character and its count should be printed on a separate line.

Sample Input 0:
---------------
aabbbccde

Sample Output 0:
----------------
b 3
a 2
c 2

Explanation 0:
--------------
- 'b' occurs 3 times → printed first.
- 'a' and 'c' both occur 2 times → tie resolved alphabetically: 'a' before 'c'.

===========================================================
Solution 1 (Using Python's prebuilt functions - collections.Counter)
===========================================================
"""

from collections import Counter  # Import Counter class for counting frequencies

if __name__ == '__main__':
    # Step 1: sort input alphabetically first
    # Sorting ensures that when counts are equal, alphabetical order is preserved
    for common in Counter(sorted(input())).most_common(3):
        # Step 2: Counter counts characters automatically
        # Step 3: most_common(3) returns top 3 items sorted:
        #         - By frequency in descending order
        #         - By alphabetical order for ties (because we pre-sorted input)
        print(common[0], common[1])  # Print character and its frequency


"""
===========================================================
Time Complexity Analysis for Solution 1:
===========================================================

1. sorted(input()) → O(n log n), where n = length of string.
2. Counter(...) → O(n), to count all characters.
3. most_common(3) → O(k log k), here k=number of unique characters (at most 26).
   → Effectively O(1).
4. Printing top 3 → O(1).

Overall: O(n log n)  [because sorting dominates].
Space Complexity: O(k), where k = number of unique characters (≤ 26).
"""


"""
===========================================================
Solution 2 (Without prebuilt functions - manual counting & sorting)
===========================================================
"""

if __name__ == '__main__':
    s = input().strip()  # Read input string and remove extra spaces

    # Step 1: Count character frequencies manually
    char_count = {}  # dictionary to store frequency of each char
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1  # if char already present, increment count
        else:
            char_count[ch] = 1   # otherwise initialize count with 1

    # Step 2: Convert dictionary items into a list of tuples
    items = []
    for key in char_count:
        items.append((key, char_count[key]))  # each element → (char, count)

    # Step 3: Manual sorting (frequency desc, char asc)
    # We'll use a custom bubble-sort style (O(n^2)) but sufficient for small input.
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            # First compare frequency → want descending order
            if items[i][1] < items[j][1]:
                items[i], items[j] = items[j], items[i]
            # If frequency is same → compare alphabetically (ascending)
            elif items[i][1] == items[j][1] and items[i][0] > items[j][0]:
                items[i], items[j] = items[j], items[i]

    # Step 4: Print top 3 characters
    for i in range(min(3, len(items))):
        print(items[i][0], items[i][1])


"""
===========================================================
Time Complexity Analysis for Solution 2:
===========================================================

1. Counting frequencies → O(n).
2. Creating list of tuples → O(k), where k = unique characters (≤ 26).
3. Manual sorting using nested loop (bubble sort) → O(k^2).
   → Since k ≤ 26, this is practically constant time.
4. Printing top 3 → O(1).

Overall: O(n + k^2). For small k, effectively O(n).
Space Complexity: O(k).
"""