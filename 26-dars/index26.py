# file larni ochish

# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close()

with open('pi.txt') as file:
    PI = file.read()

PI = PI.rstrip()
PI = PI.replace('\n', '')
PI = float(PI)
print(PI)
print(type(PI))

# file matni ustida amallar

filename = 'data_students.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

with open(filename) as file:
    students = file.readlines()

students = [student.rstrip() for student in students]
print(students)

filename = 'new_file.txt'

name = 'Tulabayev Ziyodulla:kamina-yu kamtarin'
b_year = 2011
with open(filename, 'w') as file:
    file.write(name + '\n')
    file.write(str(b_year) + '\n')

with open(filename, 'a') as file:
    file.write("ALijon Valiyev\n")
    file.write('2000\n')

import pickle

student1 = {'name': 'hasan', 'surname': 'husanov', 'b_year' : 2003, 'kurs' : 2}
student2 = {'name': 'alijon', 'surname': 'valiyev', 'b_year' : 2004, 'kurs' : 1}

with open('info.pcl', 'wb') as file:
    pickle.dump(student1, file)
    pickle.dump(student2, file)