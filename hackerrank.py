from hackerrank.ConsoleReader import *
from hackerrank.SortingList import *
# Enter your code here. Read input from STDIN. Print output to STDOUT

N = get_int()

a_list = []

for i in range(N):
    name = get_string()
    grade = get_float()
    a_list.append([name, grade])

names, grades = zip(*a_list)

second_smallest = find_second_last_index_without_sorting_entire_list_ignoring_duplicates(grades,
                                                                                         SortingOperation.DESCENDING)

result_names = [name for name, grade in a_list if grade == second_smallest]

result_names.sort()

[print(name) for name in result_names]
