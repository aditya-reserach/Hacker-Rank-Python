# This line checks whether the current script is being run directly by the Python interpreter.
# If it is, the code inside this block will run. If the script is imported elsewhere, this block won't execute.
if __name__ == '__main__':

    # Reads a line of input from the user (as a string) and converts it to an integer.
    # The integer 'n' will be used to determine how many times the loop should run.
    n = int(input())

    # A for-loop that runs from 0 to n-1. 'i' takes values 0, 1, 2, ..., n-1 one at a time.
    for i in range(n):

        # Squares the current value of 'i'. This value is stored back into 'i'.
        # Note: This does not affect the next loop value; the loop will still assign the next integer to 'i'.
        i = i * i

        # Prints the squared value of 'i' to the console.
        # Each result appears on a new line.
        print(i)
