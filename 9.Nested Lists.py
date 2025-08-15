"""
Problem: Given a list of student names and their corresponding grades,
identify the student(s) with the second lowest grade and print their names
in alphabetical order, each on a new line.

Input:
- First line: Integer, the number of students.
- For each student:
    - Line 1: Student name (string)
    - Line 2: Student grade (float)

Output:
- Name(s) of student(s) having the second lowest grade, in alphabetical order.
- Each name is printed on a new line.

Constraints:
- There will always be at least one student with the second lowest grade.

Example Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Example Output:
Berry
Harry
"""


# Approch 1

# This line ensures that the code below runs only when the script is executed directly,
# not when it is imported as a module in another script.
if __name__ == '__main__':

    # Initialize an empty list to store student records (each as [name, score])
    student = []

    # Loop to take input for the given number of students
    for _ in range(int(input())):
        name = input()              # Take the student's name as input
        score = float(input())      # Take the student's score as a float
        student.append([name,score])  # Append the [name, score] pair to the student list

    # Create a sorted list of unique scores using set and sorted
    # This removes duplicates and sorts the scores in ascending order
    scores = sorted(set(s[1] for s in student))

    # Get the second lowest score (at index 1 of the sorted list)
    second_lowest = scores[1]
    
    # Create a list of names of students who have the second lowest score
    result = [s[0] for s in student if s[1] == second_lowest]
    
    # Sort the names alphabetically and print each on a new line
    for name in sorted(result):
        print(name)




