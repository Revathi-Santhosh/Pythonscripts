# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
#
# Input Format
#
# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.
#
# Constraints
#
# There will always be one or more students having the second lowest grade.
# Output Format
#
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
#
# Berry
# Harry
# Explanation 0
#
# There are  students in this class whose names and grades are assembled to build the following list:
#
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
if __name__ == '__main__':

        rem_dump = []
        scores_list = []
        grades_list = []
        for _ in range(int(input())):
            name = input()
            score = float(input())
            scores_list.append(score)
            grades_list.append([name,score])
        print(grades_list,scores_list)

        for i in scores_list:
            if i not in rem_dump:
                rem_dump.append(i)
        print(rem_dump)
        h_s = min(rem_dump)
        print(h_s)
        print(rem_dump)
        rem_dump.remove(h_s)
        print(rem_dump)
        sec_score = min(rem_dump)
        print(sec_score)

        for h in grades_list:
            if sec_score in h:
                print(h[0])