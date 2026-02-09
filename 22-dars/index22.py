class Student:
    '''Talabaning classi'''
    def __init__(self, name, surname, b_year):
        self.name = name
        self.surname = surname
        self.b_year = b_year
        self.kurs = 1

    def get_info(self):
        '''Talaba haqida ma\'lumot'''
        return f"{self.surname} {self.name}. {self.kurs}-bosqich talabasi"
    
    def get_fullname(self):
        '''Talbaning to'liq ismini qaytarish'''
        return f"{self.name} {self.surname}"
    
    def get_name(self):
        '''Talabaning ismini qaytaradi'''
        return self.name
    
    def get_lastname(self):
        '''Talabaning familiyasini qaytaradi'''
        return self.surname
    
    def set_kurs(self, new_kurs):
        '''Talabani kursini yangilash'''
        self.kurs = new_kurs

    def update_kurs(self):
        '''Talabaning bosqichini 1taga ko'paytirish'''
        self.kurs += 1

def see_methods(klass):
    return [method for method in dir(klass) if not method.startswith('__')]

class Fan:
    '''Fan nomli class'''
    def __init__(self, name):
        self.name = name
        self.students_num = 0
        self.students = []

    def add_students(self, student):
        '''Fanga talabani qo\'shish'''
        self.students.append(student)
        self.students_num += 1

    def get_students(self):
        '''Fanga yozilgan talabalar haqida ma'lumot'''
        return [student.get_fullname() for student in self.students]



student1 = Student("Ziyodulla", "Tulabayev", 2011)
student2 = Student("Hasan", "Husanov", 2009)
# student.set_kurs(3)
student1.update_kurs()
student2.update_kurs()
print(student1.get_info())
print(student2.get_info())
print(see_methods(Student))
# print(student1.__dict__)
print(student1.__dict__.keys())


math = Fan("Great Math")
math.add_students(student1)
math.add_students(student2)
print(math.get_students())