"""
Problem Statement:
------------------
Given a string `string` and an integer `k`, split the string into substrings of length `k`.
For each substring:
    - Remove duplicate characters, keeping only the first occurrence.
    - Print the modified substring.

Example:
--------
Input:
    string = "AABCAAADA"
    k = 3

Substrings of length 3:
    "AAB", "CAA", "ADA"

Processing:
    - "AAB" → "AB"
    - "CAA" → "CA"
    - "ADA" → "AD"

Output:
    AB
    CA
    AD

We will solve this in two different ways:
    1. Manual implementation using sets.
    2. Pythonic implementation using textwrap and dict.fromkeys().
"""

# --------------------------------------------------------
# Solution 1: Manual Implementation (Beginner Friendly)
# --------------------------------------------------------
def merge_the_tools_manual(string, k):
    """
    Splits the string into chunks of size k,
    removes duplicates manually using a set(),
    and prints the cleaned substrings.
    """
    for i in range(0, len(string), k):  # Step through string in steps of size k
        substring = string[i:i + k]     # Extract substring of length k
        seen = set()                    # To track characters we've already added
        result = ""                     # To build the substring without duplicates

        for char in substring:          # Loop through each character in substring
            if char not in seen:        # If character not already added
                seen.add(char)          # Mark character as seen
                result += char          # Append character to result string

        print(result)                   # Print the processed substring


# --------------------------------------------------------
# Solution 2: Pythonic Implementation (Concise)
# --------------------------------------------------------
from textwrap import wrap

def merge_the_tools_pythonic(string, k):
    """
    Splits the string into chunks of size k using textwrap.wrap(),
    removes duplicates using dict.fromkeys() (preserves order),
    and prints the cleaned substrings.
    """
    for word in wrap(string, k):                     # Split string into substrings of length k
        print(''.join(dict.fromkeys(word)))          # dict.fromkeys removes duplicates while keeping order


# --------------------------------------------------------
# Time Complexity Analysis
# --------------------------------------------------------

"""
Let:
    n = length of the input string
    k = size of each substring

Solution 1 (Manual):
--------------------
1. Outer loop runs n/k times (one for each substring).
2. For each substring of length k, we loop over k characters.
3. Each set lookup (char not in seen) is O(1) average.

Total complexity:
    O(n)  [because we process every character exactly once]

Solution 2 (Pythonic):
----------------------
1. wrap(string, k) splits the string into n/k substrings → O(n).
2. For each substring of length k:
   - dict.fromkeys(word) iterates over k characters → O(k).
   - join() concatenates k characters → O(k).
   So per substring = O(k).

Total complexity:
    O(n)  [again, we process every character exactly once]

Space Complexity (Both):
------------------------
- We store at most k characters in a set/dict at a time.
- Space = O(k).
"""

# --------------------------------------------------------
# Example Run (Uncomment to test)
# --------------------------------------------------------
if __name__ == "__main__":
    s = "AABCAAADA"
    k = 3

    print("Manual Solution Output:")
    merge_the_tools_manual(s, k)

    print("\nPythonic Solution Output:")
    merge_the_tools_pythonic(s, k)
