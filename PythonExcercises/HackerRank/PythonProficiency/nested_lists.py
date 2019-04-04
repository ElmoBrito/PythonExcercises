'''
https://www.hackerrank.com/challenges/nested-list/problem

Nested Lists
Given the names and grades for each student in a Physics class of N students, store them in a nested list
and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each
name on a new line.

Input Format
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and
the second line contains their grade.

Constraints:
-  2 <= N <= 5
- There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple
students, order their names alphabetically and print each one on a new line.

Sample Input 0
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

Sample Output 0
Berry
Harry

Explanation 0
There are students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of belongs to Tina. The second lowest grade of belongs to both Harry and
Berry, so we order their names alphabetically and print each name on a new line.
'''



python_students = []
scores = []
student_num = int(input())

if __name__ == '__main__':
    
    for _ in range(student_num):

        # Meets contraint 2 <= N <= 5, if there are more than 5 students loop exits
        if not 2 <= student_num <= 5:
            break
        
        name = input()
        score = float(input())

        # Adds list [score, name] to python_students list
        python_students.append([score, name])

        # Sorts python_students list in ascending order 
        python_students = sorted(python_students)
        
        # Adds scores to scores list 
        scores.append(score)

    # Sorts scores in ascending order; lowest -> highest
    sorted_scores = sorted(scores)

    # Stores lowest score for comparison
    lowest_score = sorted_scores[0]

    scd_lowest = [s for s in sorted_scores if s > lowest_score][0]
    """ List comprehinsion that sets variable s to interate through sorted_scores.
    
    Variable s is compared to the stored lowest score. If it is greater than lowest score
    it is returned as the list scd_lowest with the second lowest score in index [0]

    Adding index [0] at the end of the list comprehension returns the value in that index,
    similar to lowest_score = sorted_scores[0]
    """
    # For loop that goes through python_students list with variable s for score and n for name
    for s in python_students:

        # Condition that compares score in list to the score saved in scd_lowest
        if s[0] == scd_lowest:

            # If true, the students name will be printed
            print(s[1])
