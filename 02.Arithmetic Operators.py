# This line ensures the code inside runs only when the script is executed directly,
# NOT when imported as a module in another script.
if __name__ == '__main__':

    # Take user input for 'a' as a string, then convert it to an integer.
    # We use int() because input() returns a string, and we need numbers for calculations.
    a = int(input())

    # Same as above: take input for 'b' and convert to integer.
    b = int(input())

    # Print the sum of 'a' and 'b' to the console.
    # '+' operator adds two numbers.
    print(a + b)

    # Print the difference of 'a' and 'b'.
    # '-' operator subtracts b from a.
    print(a - b)

    # Print the product of 'a' and 'b'.
    # '*' operator multiplies two numbers.
    print(a * b)


