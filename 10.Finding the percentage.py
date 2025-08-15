"""
student_average.py

This script takes input for a number of students, their marks, and a specific student's name.
It then calculates and prints the average of that student's marks rounded to 2 decimal places.

Author: [Your Name]
Created on: [Date]
Usage: Run the script and follow the input prompts.

Sample Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:
56.00
"""

#Approch: 1


# This block ensures that the code only runs when this script is executed directly.
# It's a common Python practice to separate script execution from module usage.
if __name__ == '__main__':
    
    # Read the total number of student records to be entered.
    # This input defines how many times we need to run the loop to collect student data.
    n = int(input())
    
    # Initialize an empty dictionary to store student names as keys and their scores as values.
    # The structure will be: {'StudentName': [score1, score2, score3]}
    student_marks = {}
    
    # Loop runs 'n' times to collect input for each student.
    for _ in range(n):
        # Take a single input line for name and marks, separated by spaces.
        # The first value will be the student's name, and the rest will be the marks.
        # Using unpacking: 'name' stores the first word, '*line' collects the rest as a list.
        name, *line = input().split()
        
        # Convert the list of string marks into floats for accurate average calculation.
        # map() applies float() to each element in the list.
        scores = list(map(float, line))
        
        # Add the student and their scores to the dictionary.
        # 'name' is the key, and 'scores' (a list of floats) is the value.
        student_marks[name] = scores

    # Read the name of the student whose average marks we want to calculate.
    query_name = input()
    
    # Retrieve the list of marks for the given student from the dictionary using the key.
    # Since the input is guaranteed to contain this name, no need for error handling here.
    marks = student_marks[query_name]
    
    # Calculate the average of the marks.
    # sum(marks) adds all the scores, len(marks) gets the number of scores.
    average = sum(marks) / len(marks)
    
    # Print the average rounded to 2 decimal places using format string.
    # This ensures professional and consistent numeric formatting in the output.
    print("{:.2f}".format(average))



# Approch 2

print(f"{sum(student_marks[query_name]) / len(student_marks[query_name]):.2f}")