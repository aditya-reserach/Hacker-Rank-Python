# ----------------------------------------------------------------
# Problem Statement:
# ----------------------------------------------------------------
# You are given a date in the format MM DD YYYY. Your task is to find
# the day of the week for that date and print it in UPPERCASE.
# ----------------------------------------------------------------
# Input Format:
# Single line containing month, day, and year separated by space.
# Example: 08 05 2015
# ----------------------------------------------------------------
# Constraints:
# All inputs are valid dates.
# ----------------------------------------------------------------
# Output Format:
# Output the correct day in capital letters.
# Example Output: WEDNESDAY
# ----------------------------------------------------------------
# Sample Input:
# 08 05 2015
# Sample Output:
# WEDNESDAY
# ----------------------------------------------------------------

# -------------------------------
# Code 1: Using Python's calendar module
# -------------------------------

# Import calendar module to access weekday functions
import calendar

# Read input as space-separated integers: Month, Day, Year
Month, date, year = map(int, input().split())

# calendar.weekday(year, month, day) returns:
# 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
# calendar.day_name[index] returns the corresponding weekday name
# .upper() converts the weekday string to uppercase
print(calendar.day_name[calendar.weekday(year, Month, date)].upper())

# Time Complexity of Code 1:
# O(1) -> All operations (weekday lookup, day_name access) are constant time
# Space Complexity of Code 1:
# O(1) -> Only integer variables and a fixed-length weekday list are used

# -------------------------------
# Code 2: Without using prebuilt function (Zeller's Congruence)
# -------------------------------

# Read input again for independent execution
month, day, year = map(int, input().split())

# Adjust month and year for Zeller's formula:
# Treat Jan and Feb as months 13 and 14 of the previous year
if month < 3:
    month += 12  # Convert Jan/Feb to 13/14
    year -= 1    # Year is reduced by 1 for Zeller's formula

# Assign variables for Zeller's formula
q = day          # Day of the month
m = month        # Adjusted month
K = year % 100   # Last two digits of year (year of the century)
J = year // 100  # Zero-based century

# Zeller's Congruence formula:
# h = (q + 13*(m+1)//5 + K + K//4 + J//4 + 5*J) % 7
# Returns: 0=Saturday, 1=Sunday, ..., 6=Friday
h = (q + (13*(m + 1)) // 5 + K + K//4 + J//4 + 5*J) % 7

# Map Zeller's output to weekday names in UPPERCASE
days = ["SATURDAY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

# Print the corresponding weekday
print(days[h])

# Time Complexity of Code 2:
# O(1) -> Only arithmetic operations are performed, no loops
# Space Complexity of Code 2:
# O(1) -> Only integers and a fixed list of 7 strings are used

# ----------------------------------------------------------------
# Summary of Approaches:
# ----------------------------------------------------------------
# Code 1 (calendar module):
#   - Easy to implement, built-in correctness
#   - Uses prebuilt module functions
#   - Time complexity: O(1), Space complexity: O(1)
#
# Code 2 (Zeller's Congruence):
#   - Pure formula-based approach, no prebuilt functions
#   - Requires arithmetic and careful handling of months
#   - Time complexity: O(1), Space complexity: O(1)
# ----------------------------------------------------------------
