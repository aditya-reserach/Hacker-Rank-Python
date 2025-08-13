# This is the main entry point of the Python program.
# The `if __name__ == '__main__':` block ensures that this code is only run
# when the script is executed directly, and NOT when it's imported as a module in another script.
if __name__ == '__main__':

    # Prompting the user to input an integer.
    # `input()` reads the input as a string.
    # `int()` converts the string to an integer type.
    # This is necessary because input from `input()` is always a string, but we need integers for division.
    a = int(input())

    # Similarly, taking another integer input from the user and converting it to int.
    b = int(input())

    # Performing integer (floor) division using `//`.
    # This returns the result of the division, rounded down to the nearest whole number.
    # For example: 7 // 2 = 3
    # It is useful when you want to discard the decimal part.
    print(a // b)

    # Performing floating-point (true) division using `/`.
    # This returns the exact division result with decimals (if any).
    # For example: 7 / 2 = 3.5
    # It is used when precision is important.
    print(a / b)
