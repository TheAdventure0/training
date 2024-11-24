grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2],
          [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

one = sum(grades[0]) / len(grades[0])
two = sum(grades[1]) / len(grades[1])
three = sum(grades[2]) / len(grades[2])
four = sum(grades[3]) / len(grades[3])
fifth = sum(grades[4]) / len(grades[4])
g_ = [one, two, three, four, fifth]

stud = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
sorted_s = sorted(students)
a = sorted_s[0]
b = sorted_s[1]
j = sorted_s[2]
k = sorted_s[3]
s = sorted_s[4]
s_ = [a, b, j, k, s]

dictionary = dict(zip(s_, g_))
print(dictionary)