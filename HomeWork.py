# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],
#           [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# GPA_1 = sum(grades[0]) / len(grades[0])
# GPA_2 = sum(grades[1]) / len(grades[1])
# GPA_3 = sum(grades[2]) / len(grades[2])
# GPA_4 = sum(grades[3]) / len(grades[3])
# GPA_5 = sum(grades[4]) / len(grades[4])
# grades_all = [GPA_1, GPA_2, GPA_3, GPA_4, GPA_5]
#
# stud = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
# name_list = sorted(students)
# name_1 = name_list[0]
# name_2 = name_list[1]
# name_3 = name_list[2]
# name_4 = name_list[3]
# name_5 = name_list[4]
# name_all = [name_1, name_2, name_3, name_4, name_5]
#
# dictionary = dict(zip(name_all, grades_all))
# print(dictionary)


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],
          [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dictionary = {}
students_sort = sorted(students)

dictionary[students_sort[0]] = sum(grades[0]) / len(grades[0])
dictionary[students_sort[1]] = sum(grades[1]) / len(grades[1])
dictionary[students_sort[2]] = sum(grades[2]) / len(grades[2])
dictionary[students_sort[3]] = sum(grades[3]) / len(grades[3])
dictionary[students_sort[4]] = sum(grades[4]) / len(grades[4])

print(dictionary)
