"""
============================================================
The Minion Game - Problem Statement
============================================================

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
------------
1. Both players are given the same string S.
2. Both players have to make substrings using the letters of the string.
3. Stuart has to make words starting with CONSONANTS.
4. Kevin has to make words starting with VOWELS.
5. The game ends when both players have made all possible substrings.

Scoring:
---------
- A player gets +1 point for each occurrence of the substring in the string.
- Example:
    String = "BANANA"
    Kevin's substring = "ANA"
    "ANA" occurs 2 times in "BANANA".
    Hence, Kevin will get 2 points.

Vowels are defined as: A, E, I, O, U
(Note: In this problem, 'Y' is NOT considered a vowel)

Task:
------
You need to determine the winner of the game and their score.

Input Format:
-------------
- A single line of input containing the string S.
- The string S will contain only uppercase letters (A-Z).

Constraints:
------------
- 0 < len(S) <= 10^6

Output Format:
--------------
- Print the winner's name and their score separated by a space.
- If the game is a draw, print "Draw".

Sample Input:
-------------
BANANA

Sample Output:
--------------
Stuart 12
============================================================
"""


# ============================================================
# Solution 1: Optimized Approach (O(N))
# ============================================================

def minion_game_optimized(string):
    """
    Optimized solution for The Minion Game.

    Logic:
    -------
    - Instead of generating all substrings (which is expensive),
      we can directly calculate the contribution of each index.
    - For a character at index i, the number of substrings that 
      start at that character = (len(string) - i).
    - Assign these counts to Kevin (if vowel) or Stuart (if consonant).

    Time Complexity: O(N)
    ----------------------
    - We only loop through the string once.
    - Each step does O(1) work.
    """

    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            # Kevin scores for substrings starting with a vowel
            kevin_score += (length - i)
        else:
            # Stuart scores for substrings starting with a consonant
            stuart_score += (length - i)

    # Determine winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


# ============================================================
# Solution 2: Brute Force Approach (O(N^2))
# ============================================================

def minion_game_bruteforce(string):
    """
    Brute Force solution for The Minion Game.

    Logic:
    -------
    - Generate ALL possible substrings manually (no prebuilt slicing).
    - For each substring, count how many times it occurs in the string.
    - Assign points based on starting character (vowel/consonant).

    Note:
    -----
    This is only for understanding. For large inputs (len(S) > 5000),
    this will be extremely slow and impractical.

    Time Complexity: O(N^2) to generate substrings 
                     + O(N) to count occurrences
                     = O(N^3) worst case.
    """

    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    # Manually generate substrings (without Python slicing)
    for i in range(length):
        for j in range(i, length):
            # Build substring character by character
            substring = ""
            for k in range(i, j + 1):
                substring += string[k]

            # Count occurrences manually
            count = 0
            for x in range(length - len(substring) + 1):
                match = True
                for y in range(len(substring)):
                    if string[x + y] != substring[y]:
                        match = False
                        break
                if match:
                    count += 1

            # Assign points
            if substring[0] in vowels:
                kevin_score += count
            else:
                stuart_score += count

    # Determine winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


# ============================================================
# Driver Code
# ============================================================

if __name__ == "__main__":
    # Example Input
    s = "BANANA"

    print("=== Optimized Solution ===")
    minion_game_optimized(s)

    print("\n=== Brute Force Solution (Slow) ===")
    minion_game_bruteforce(s)
