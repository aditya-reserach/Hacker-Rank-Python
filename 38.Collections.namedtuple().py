"""
===========================================================
Problem Statement:
===========================================================

Dr. John Wesley has a spreadsheet containing a list of students' ID, MARKS, NAME, and CLASS.

Your task is to help Dr. Wesley calculate the **average marks** of the students.

Notes:
1. The spreadsheet’s columns can appear in **any order**. 
   (For example: "ID MARKS NAME CLASS" or "MARKS CLASS NAME ID").
2. The column names are fixed: ID, MARKS, CLASS, NAME (spelling and case won’t change).
3. You need to calculate the **average of MARKS column**.
4. The output should be printed rounded to **2 decimal places**.

-----------------------------------------------------------
Input Format:
-----------------------------------------------------------
- The first line contains an integer N, the total number of students.
- The second line contains the column names in any order.
- The next N lines contain the details (ID, MARKS, NAME, CLASS).

-----------------------------------------------------------
Output Format:
-----------------------------------------------------------
- Print the average marks rounded to 2 decimal places.

-----------------------------------------------------------
Sample Input:
-----------------------------------------------------------
5
ID MARKS NAME CLASS
1 97 Raymond 7
2 50 Steven 4
3 91 Adrian 9
4 72 Stewart 5
5 80 Peter 6

-----------------------------------------------------------
Sample Output:
-----------------------------------------------------------
78.00

-----------------------------------------------------------
Explanation:
-----------------------------------------------------------
Average = (97 + 50 + 91 + 72 + 80) / 5 = 78.00
===========================================================
"""

# =========================================================
# Code 1: Using collections.namedtuple (with prebuilt functions)
# =========================================================

from collections import namedtuple  # Import namedtuple to create lightweight objects

# Read the total number of students
n, student = int(input()), namedtuple('student', input().split())

# Explanation of the line below:
# - input().split() → reads the column names (ID, MARKS, NAME, CLASS) in any order
# - namedtuple creates a class with these column names as attributes
# - student(*input().split()) → unpacks each student line into the namedtuple
# - .MARKS → retrieves the MARKS field
# - int(...) → converts MARKS to integer
# - sum([...]) → sums up all MARKS values
# - divide by n → compute average
# - round(..., 2) → round to 2 decimal places
print(round(sum([int(student(*input().split()).MARKS) for i in range(n)]) / n, 2))

"""
-----------------------------------------------------------
Time Complexity (Code 1):
- Reading input for n students → O(n)
- Creating namedtuple objects → O(1) per student → O(n)
- Summing MARKS → O(n)
=> Overall Time Complexity: O(n)

Space Complexity:
- Stores only n student objects temporarily → O(n)
- No extra data structures
=> Overall Space Complexity: O(n)
-----------------------------------------------------------
"""

# =========================================================
# Code 2: Without using prebuilt functions (manual approach)
# =========================================================

# Read total number of students
n = int(input())  

# Read the column names and split into list
columns = input().split()  

# Find the index of "MARKS" column manually
marks_index = -1
for i in range(len(columns)):  
    if columns[i] == "MARKS":  
        marks_index = i  
        break  

# Initialize total marks
total_marks = 0  

# Loop over each student
for _ in range(n):
    student_data = input().split()  # Read the student's full data line
    
    # Convert marks from string to integer manually
    digit_string = student_data[marks_index]  
    marks_value = 0  
    for ch in digit_string:  
        # Convert each character into its numeric value using ASCII
        marks_value = marks_value * 10 + (ord(ch) - ord('0'))  
    
    # Add marks to total
    total_marks += marks_value  

# Compute average
average = total_marks / n  

# Round average to 2 decimal places manually
average = int(average * 100 + 0.5) / 100  

# Print result formatted to 2 decimals
print(f"{average:.2f}")  

"""
-----------------------------------------------------------
Time Complexity (Code 2):
- Reading input for n students → O(n)
- For each student, converting marks string to integer:
   - Each character processed once → O(k), where k is number of digits in marks
   - In practice, k is small (≤ 3 for typical marks)
=> Overall Time Complexity: O(n)

Space Complexity:
- Only stores running total and current student line → O(1)
=> Overall Space Complexity: O(1)
-----------------------------------------------------------
"""
