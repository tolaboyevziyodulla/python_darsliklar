def do_grade(names):
    """Baho beruvchi funksiya"""
    grades = {}
    while names:
        name = names.pop()
        grade = input(f"Talaba {name.title()}ning bahosi: ")
        grades[name] = int(grade)
    return grades
students = ['ali', 'vali', 'hasan', 'husan']
grades = do_grade(students[:])
print(grades)