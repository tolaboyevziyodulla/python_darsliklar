student = {
    'ism' : 'ziyodulla',
    'familiya' : 'to\'laboyev',
    'yosh' : 15,
    'fakultet' : 'informatika',
    'kurs' : 2
}

# item()
# print(student.items())
for kalit, qiymat in student.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")

# keys()
# print(student.keys())
print('So\'rovnoma:')
for key in sorted(student):
    print(key.title() + ':')

# values()
# print(student.values())
print('Talabaning javoblari:')
for result in student.values():
    print(result)