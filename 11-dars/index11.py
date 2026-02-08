# while and list

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz!")
# names = []
# n = 1
# while True:
#     ques = f"{n}-do'stingizni kiriting: "
#     name = input(ques)
#     names.append(name)
#     repeat = input("Yana ism qo'shasizmi? (ha/yo'q): ")
#     n += 1
#     if repeat != 'ha':
#         break
# print("Do'stlaringiz ro'yxati:")
# for name in names:
#     print(name.title())

print("Do'stlaringiz yoshini saqlaymiz.")
friends = {}
flag = True
while flag:
    name = input("Do'stingizning ismini kiriting: ")
    year = input(f"{name.title()}ning yoshini kiriting: ")
    friends[name] = int(year)

    answer = input("Yana ma'lumot qo'shasizmi? (ha/yo'q): ")
    if answer == 'ha':
        flag = True
    elif answer == 'yo\'q':
        flag = False
for name, year in friends.items():
    print(f"{name.title()} {year} yoshda")

cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)

students = ['husan', 'hasan', 'olim', 'botir']
grade_students = {}
while students:
    student = students.pop()
    grade = input(f"{student.title()}ning bahosini kiriting: ")
    print(f"{student.title()} baholandi")
    grade_students[student] = int(grade)