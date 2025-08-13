# This checks whether the script is being run directly (not imported as a module).
# Only then, it executes the code inside the if-block.
# This is good practice in Python to avoid unwanted behavior when code is reused.
if __name__ == '__main__':

    # Read an integer from user input and convert it from string to integer using int().
    # This integer 'n' will determine how many numbers we include in our final output.
    n = int(input())

    # Initialize an empty string to hold the final result.
    # We use a string here because we want to concatenate digits (as characters) together.
    result = ""

    # Start a loop from 1 to n (inclusive) using range(1, n+1)
    # range() excludes the end value, so we add +1 to include 'n'.
    # This loop ensures every number from 1 up to 'n' gets added to the result.
    for i in range(1, n+1):

        # Convert the current integer 'i' to a string using str().
        # This is necessary because we are building a string and can't add an integer directly.
        # Then we append this string to the result variable using += (string concatenation).
        result += str(i)

    # After all numbers are added, we print the final result.
    # This will be one continuous string of numbers without spaces or separators.
    print(result)
