"""
Problem: Mutations (HackerRank)

We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
Strings in Python are also immutable (cannot be modified in place). To "mutate" a string, we need to
reconstruct it.

Task:
-----
You are given a string, an index, and a character. Replace the character at the given index
with the new character and return the modified string.

Function Description:
---------------------
Complete the function mutate_string with the following parameters:
- string string: the string to change
- int position: the index to insert the character at
- string character: the character to insert

Returns:
- string: the altered string

Input Format:
-------------
The first line contains the string, s.
The second line contains an integer (position) and a string (character), separated by a space.

Sample Input:
-------------
abracadabra
5 k

Sample Output:
--------------
abrackdabra

----------------------------------------------------------------------
Notes / Explanation of Core Logic:
----------------------------------
We cannot directly assign a value to a string index in Python because strings are immutable.
Instead, we can use slicing to rebuild the string:

    return string[:position] + character + string[position + 1:]

Step by step (for string = "abracadabra", position = 5, character = "k"):
1. string[:position] → "abrac"   (everything before index 5)
2. character          → "k"
3. string[position+1:] → "dabra" (everything after index 5)
4. Concatenate → "abrac" + "k" + "dabra" = "abrackdabra"

Why position+1?
---------------
Because we want to REPLACE the character at that index, not keep it.
If we just used string[position:], the original character would remain.

----------------------------------------------------------------------
Time Complexity:
----------------
- Slicing a string takes O(n) time (where n = length of the string).
- Concatenation of strings also takes O(n).
- Overall time complexity: O(n)
- Space complexity: O(n), since a new string is created (strings are immutable).

This is efficient enough for typical input sizes on HackerRank.
----------------------------------------------------------------------
"""

def mutate_string(string, position, character):
    # string[:position]  →  Substring from start up to (but not including) index = position
    # character          →  The new character we want to insert
    # string[position+1:] →  Substring from index = position+1 to the end (skips the old char at position)
    # Concatenation      →  Joining these 3 parts gives us the updated string
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    # Step 1: Read the original string from input
    s = input().strip()

    # Step 2: Read the next input line, which contains two values:
    # - pos → the index (as a string initially)
    # - char → the replacement character
    pos, char = input().split()

    # Step 3: Convert pos into an integer because string indices must be integers
    pos = int(pos)

    # Step 4: Call the mutate_string function with (s, pos, char)
    result = mutate_string(s, pos, char)

    # Step 5: Print the final mutated string
    print(result)
