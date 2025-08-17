def is_leap(year):
    # Initially assume the year is NOT a leap year
    leap = False
    
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 4, check if it is NOT divisible by 100,
        # or if it is divisible by 400 (special century rule)
        if (year % 100 != 0) or (year % 400 == 0):
            leap = True  # Year qualifies as a leap year
    
    # Return True if leap year, otherwise False
    return leap

# Take input from the user (convert to integer)
year = int(input("Enter a year: "))

# Call the function and print whether the year is leap or not
print(is_leap(year))
