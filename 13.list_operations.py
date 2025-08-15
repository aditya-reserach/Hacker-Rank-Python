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
    # Read the number of commands to be executed
    N = int(input())

    # Initialize an empty list
    lst = []

    # Loop through each command input
    for _ in range(N):
        # Read the command and split it into components
        command = input().strip().split()

        # Check the command type and execute the corresponding operation
        if command[0] == 'insert':
            # Inserts value at specified index
            # Time Complexity: O(n)
            lst.insert(int(command[1]), int(command[2]))

        elif command[0] == 'print':
            # Prints the current state of the list
            # Time Complexity: O(n)
            print(lst)

        elif command[0] == 'remove':
            # Removes the first occurrence of the specified value
            # Time Complexity: O(n)
            lst.remove(int(command[1]))

        elif command[0] == 'append':
            # Appends value at the end of the list
            # Time Complexity: O(1) amortized
            lst.append(int(command[1]))

        elif command[0] == 'sort':
            # Sorts the list in ascending order
            # Time Complexity: O(n log n)
            lst.sort()

        elif command[0] == 'pop':
            # Removes the last element of the list
            # Time Complexity: O(1)
            lst.pop()

        elif command[0] == 'reverse':
            # Reverses the list
            # Time Complexity: O(n)
            lst.reverse()
