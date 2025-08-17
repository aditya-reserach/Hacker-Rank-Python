# This block checks whether the script is being run directly (not imported)
# It ensures that the code inside runs only when you execute this file
if __name__ == '__main__':

    # Get input from the user, remove any surrounding whitespace, and convert it to an integer
    n = int(input("Enter a number: ").strip())

    # Check if the number is odd (i.e., not divisible by 2)
    if n % 2 != 0:
        # Odd numbers are always considered "Weird"
        print("Weird")

    # If the number is even and in the range 2 to 5 (inclusive)
    elif n % 2 == 0 and 2 <= n <= 5:
        # These even numbers are "Not Weird" based on the rules
        print("Not Weird")

    # If the number is even and in the range 6 to 20 (inclusive)
    elif n % 2 == 0 and 6 <= n <= 20:
        # These even numbers are considered "Weird"
        print("Weird")

    # For all other even numbers (i.e., even and greater than 20)
    else:
        # These numbers are considered "Not Weird"
        print("Not Weird")
