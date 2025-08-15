# list_operations.py

"""
This program performs a sequence of operations on a list based on user commands.

Supported operations:
- insert i e   : Insert integer 'e' at position 'i'
- print        : Print the current state of the list
- remove e     : Remove the first occurrence of integer 'e'
- append e     : Append integer 'e' to the end of the list
- sort         : Sort the list in ascending order
- pop          : Remove the last element from the list
- reverse      : Reverse the list

Input:
- First line contains an integer N (number of commands)
- Next N lines contain one command each

Output:
- For every 'print' command, output the current list on a new line
"""

if __name__ == '__main__':
    # Read number of commands from input
    N = int(input())

    # Initialize an empty list to perform operations on
    lst = []

    # Loop to process each command line
    for _ in range(N):
        # Read the command, split it into parts
        command = input().strip().split()

        # The first word is the operation, the rest are arguments
        operation = command[0]

        # Perform corresponding operation based on command
        if operation == 'insert':
            # Insert value (int) at a specified index
            index = int(command[1])
            value = int(command[2])
            lst.insert(index, value)

        elif operation == 'print':
            # Print the current state of the list
            print(lst)

        elif operation == 'remove':
            # Remove the first occurrence of the given value
            value = int(command[1])
            lst.remove(value)

        elif operation == 'append':
            # Append value to the end of the list
            value = int(command[1])
            lst.append(value)

        elif operation == 'sort':
            # Sort the list in ascending order
            lst.sort()

        elif operation == 'pop':
            # Remove the last element from the list
            lst.pop()

        elif operation == 'reverse':
            # Reverse the list (in-place)
            lst.reverse()
