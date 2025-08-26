"""
Problem Statement:
------------------
You are given two timestamps in the format:
    Day dd Mon yyyy hh:mm:ss +xxxx
where:
    - Day is the day of the week (e.g., Sun, Mon, Tue)
    - dd is the day of the month (01 to 31)
    - Mon is the month name (e.g., Jan, Feb, Mar)
    - yyyy is the year (e.g., 2024)
    - hh:mm:ss is the time of the day in 24-hour format
    - +xxxx or -xxxx is the timezone offset from UTC

Your task:
----------
Write a function `time_delta(t1, t2)` that calculates the absolute difference 
between these two timestamps in SECONDS.

Constraints:
------------
- The input format strictly follows the above format.
- You will be given `t`, the number of test cases.
- For each test case, you are given two timestamps, and you must print the difference.

Example:
--------
Input:
1
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000

Output:
25200

Explanation:
------------
The two timestamps differ by exactly 7 hours (7 * 3600 = 25200 seconds).
"""

# ========================================================================
# CODE 1: Using Python's built-in datetime module (Efficient Solution)
# ========================================================================

from datetime import datetime

def time_delta(t1, t2):
    # Define the format of input timestamp strings
    time_format = "%a %d %b %Y %H:%M:%S %z"
    
    # Convert timestamp string into datetime object with timezone info
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    
    # Calculate the absolute difference in seconds
    return str(int(abs((dt1 - dt2).total_seconds())))

# -------------------------
# Driver code for CODE 1
# -------------------------
if __name__ == "__main__":
    t = int(input().strip())        # Read number of test cases
    for _ in range(t):
        t1 = input().strip()        # Read first timestamp
        t2 = input().strip()        # Read second timestamp
        print(time_delta(t1, t2))   # Print result for each test case


"""
Approach for Code 1:
--------------------
1. Parse timestamps into datetime objects (O(1) operation).
2. Subtract them to get timedelta object.
3. Convert timedelta into total seconds and return absolute value.

Time Complexity (Code 1):
-------------------------
- Parsing datetime: O(1) (since it's fixed format and length)
- Subtraction: O(1)
- Conversion to seconds: O(1)
=> Overall per test case = O(1)
=> For t test cases = O(t)
"""

# ========================================================================
# CODE 2: Without using prebuilt datetime functions (Manual Parsing)
# ========================================================================

# Map month names to numbers for conversion
month_map = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
    "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
    "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

def parse_timestamp(ts):
    # Split timestamp into components
    parts = ts.split()
    # Extract individual values
    day = int(parts[1])                           # Day of month
    month = month_map[parts[2]]                   # Convert month string to number
    year = int(parts[3])                          # Year
    time_parts = parts[4].split(":")              # Split HH:MM:SS
    hour, minute, second = map(int, time_parts)   # Convert to integers
    tz_sign = 1 if parts[5][0] == '+' else -1     # Timezone sign (+ or -)
    tz_hour = int(parts[5][1:3])                  # Timezone hours
    tz_minute = int(parts[5][3:])                 # Timezone minutes
    tz_offset = tz_sign * (tz_hour * 3600 + tz_minute * 60)  # Offset in seconds
    return year, month, day, hour, minute, second, tz_offset

def is_leap_year(year):
    # Leap year check rule
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def days_in_month(year, month):
    # Number of days in each month
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def to_seconds(year, month, day, hour, minute, second, tz_offset):
    # Convert full timestamp into total seconds from year 0
    days = 0
    for y in range(0, year):
        days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        days += days_in_month(year, m)
    days += (day - 1)
    total_seconds = days * 86400 + hour * 3600 + minute * 60 + second
    # Adjust for timezone offset
    return total_seconds - tz_offset

def time_delta_manual(t1, t2):
    y1, m1, d1, h1, mi1, s1, tz1 = parse_timestamp(t1)
    y2, m2, d2, h2, mi2, s2, tz2 = parse_timestamp(t2)
    sec1 = to_seconds(y1, m1, d1, h1, mi1, s1, tz1)
    sec2 = to_seconds(y2, m2, d2, h2, mi2, s2, tz2)
    return str(abs(sec1 - sec2))

# -------------------------
# Driver code for CODE 2
# -------------------------
if __name__ == "__main__":
    t = int(input().strip())            # Number of test cases
    for _ in range(t):
        t1 = input().strip()
        t2 = input().strip()
        print(time_delta_manual(t1, t2))


"""
Approach for Code 2:
--------------------
1. Parse the timestamp manually into year, month, day, hour, minute, second, and timezone.
2. Convert the timestamp into "total seconds from year 0" considering leap years and days in month.
3. Adjust the total seconds with timezone offset.
4. Subtract both timestamps to get absolute difference.

Time Complexity (Code 2):
-------------------------
- Parsing timestamp: O(1) (fixed number of operations per string).
- Converting year → seconds: O(Y) where Y = year value (looping from 0 to year).
- Converting months → seconds: O(12) ≈ O(1).
- Rest of operations: O(1).

=> Overall per test case ≈ O(Y), where Y is the year number (can be large).
=> For t test cases = O(t * Y).
"""
