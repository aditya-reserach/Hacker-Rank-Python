"""
Problem Statement: Find The Least Frequent Digit

Given an integer n, find the digit that occurs least frequently in its decimal representation.
If multiple digits have the same frequency, choose the smallest digit.

Return the chosen digit as an integer.

The frequency of a digit x is the number of times it appears in the decimal representation of n.

Input Format:
- A single integer n

Output Format:
- An integer representing the least frequent digit

Constraints:
1 <= n <= 2^31 - 1

Example 1:
Input: n = 1553322
Output: 1
Explanation: The least frequent digit in n is 1, which appears only once. All other digits appear twice.

Example 2:
Input: n = 723344511
Output: 2
Explanation: The least frequent digits in n are 7, 2, and 5; each appears only once. The smallest among them is 2.
"""

# ------------------------ Solution 1: Using Python Built-in Functions ------------------------
class SolutionBuiltIn:
    def getLeastFrequentDigit(self, n: int) -> int:
        # Step 1: Convert the integer into a string so we can iterate through digits
        digits = str(n)
        
        # Step 2: Count frequency of each digit using a dictionary
        freq = {}
        for d in digits:
            freq[d] = freq.get(d, 0) + 1  # get current count, add 1
        
        # Step 3: Find the minimum frequency value among the counted digits
        min_freq = min(freq.values())
        
        # Step 4: Collect all digits with the minimum frequency
        candidates = [int(d) for d, f in freq.items() if f == min_freq]
        
        # Step 5: Return the smallest digit among candidates
        return min(candidates)

"""
Time Complexity Analysis:
- Converting n to string: O(d), where d = number of digits in n
- Counting frequency with dictionary: O(d)
- Finding min frequency: O(k), where k = number of unique digits (<=10)
- Creating candidates list: O(k)
- Finding min among candidates: O(k)
Overall: O(d + k) ~ O(1) since d <= 10 and k <= 10 for 32-bit integer

Space Complexity Analysis:
- freq dictionary stores up to 10 key-value pairs: O(1)
- candidates list stores at most 10 elements: O(1)
- digits string: O(d) ~ O(1)
Overall: O(1)
"""

# ------------------------ Solution 2: Manual Implementation Without Built-ins ------------------------
class SolutionManual:
    def getLeastFrequentDigit(self, n: int) -> int:
        # Step 1: Initialize frequency array for digits 0-9
        freq = [0] * 10
        
        # Step 2: Count frequency of each digit using arithmetic (no str() conversion)
        temp = n
        while temp > 0:
            digit = temp % 10     # get last digit
            freq[digit] += 1      # increment its count
            temp //= 10           # remove last digit
        
        # Step 3: Find the least frequent digit manually
        min_freq = None
        result = None
        
        for d in range(10):
            if freq[d] > 0:
                if min_freq is None or freq[d] < min_freq:
                    min_freq = freq[d]
                    result = d
                # If frequency is equal, we keep the smaller digit automatically because we iterate from 0-9
        
        return result

"""
Time Complexity Analysis:
- Counting digits using modulo and division: O(d), where d = number of digits (~10 max)
- Iterating over 0-9 to find minimum frequency: O(10) ~ O(1)
Overall: O(d) ~ O(1)

Space Complexity Analysis:
- freq array is fixed size 10: O(1)
- No other significant storage used
Overall: O(1)
"""

# ------------------------ Test Cases ------------------------
if __name__ == "__main__":
    # Built-in solution test
    sol1 = SolutionBuiltIn()
    print(sol1.getLeastFrequentDigit(1553322))   # Expected Output: 1
    print(sol1.getLeastFrequentDigit(723344511)) # Expected Output: 2

    # Manual solution test
    sol2 = SolutionManual()
    print(sol2.getLeastFrequentDigit(1553322))   # Expected Output: 1
    print(sol2.getLeastFrequentDigit(723344511)) # Expected Output: 2


