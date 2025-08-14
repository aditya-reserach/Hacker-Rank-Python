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

if __name__ == '__main__':
    # List to store student data in the format: [name, score]
    students = []

    # Reading the number of students
    n = int(input("Enter number of students: "))

    # Collecting student names and scores
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Extracting all unique scores and sorting them to find the second lowest
    unique_scores = sorted(set(score for _, score in students))
    second_lowest = unique_scores[1]

    # Finding all students with the second lowest score
    second_lowest_students = [name for name, score in students if score == second_lowest]

    # Printing names in alphabetical order
    for name in sorted(second_lowest_students):
        print(name)


# Approch 2

