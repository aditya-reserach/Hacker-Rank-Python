"""
Problem Statement:
-----------------
You are asked to ensure that the first and last names of people begin with a 
capital letter in their passports. For example:

Input:
------
chris alan

Output:
-------
Chris Alan

Rules:
------
- Only the first character of each word should be capitalized.
- If a word starts with a non-alphabetic character (e.g., "12abc"), 
  it should remain unchanged except the rest of the word stays same.
- Words are separated by spaces.
"""

# ---------------------------------------------------------
# Approach 1: Using Prebuilt Function .capitalize()
# ---------------------------------------------------------
def solve_with_builtin(s):
    """
    Approach:
    - Split the string into words using split(' ') 
      (keeps correct spacing including multiple spaces).
    - For each word, use str.capitalize() which:
        -> Makes the first character uppercase (if alphabetic).
        -> Converts the rest of the word to lowercase.
    - Join the words back with spaces.

    Example:
        Input: "chris alan"
        Step1: ["chris", "alan"]
        Step2: ["Chris", "Alan"]
        Output: "Chris Alan"

    Time Complexity: O(n)
        - Each character is processed once during split + capitalize + join.
    Space Complexity: O(n)
        - Temporary list of words and final result string.
    """
    return ' '.join(word.capitalize() for word in s.split(' '))


# ---------------------------------------------------------
# Approach 2: Without Using Prebuilt Functions
# ---------------------------------------------------------
def manual_capitalize(word):
    """
    Manually capitalize a single word:
    - If word is empty, return "".
    - If the first character is alphabetic:
        -> Convert it to uppercase manually using ASCII difference.
    - Append the rest of the word unchanged (do NOT lowercase).
    
    Example:
        "chris" -> "Chris"
        "alan"  -> "Alan"
        "12abc" -> "12abc"  (unchanged first character)
    """
    if word == "":
        return ""
    
    first_char = word[0]
    
    # If first character is between 'a' and 'z', make it uppercase
    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)  # ASCII difference
    
    # Append rest of word unchanged
    return first_char + word[1:]


def solve_without_builtin(s):
    """
    Approach:
    - Split the input into words using split(' ').
    - Apply manual_capitalize() for each word.
    - Join the words back with spaces.

    Example:
        Input: "chris alan"
        Step1: ["chris", "alan"]
        Step2: ["Chris", "Alan"]
        Output: "Chris Alan"

    Time Complexity: O(n)
        - Each character in the string is processed once.
    Space Complexity: O(n)
        - Temporary list of words and final string.
    """
    return ' '.join(manual_capitalize(word) for word in s.split(' '))


# ---------------------------------------------------------
# Main Driver Code
# ---------------------------------------------------------
if __name__ == "__main__":
    s = input("Enter full name: ")

    print("\n--- Approach 1: With Built-in capitalize() ---")
    print(solve_with_builtin(s))

    print("\n--- Approach 2: Manual Implementation ---")
    print(solve_without_builtin(s))
