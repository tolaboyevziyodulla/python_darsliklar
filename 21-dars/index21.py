class Student:
    def __init__(self, name, surname, b_year):
        self.name = name
        self.surname = surname
        self.b_year = b_year

    def get_age(self, year):
        return year - self.b_year

    def tanishtir(self):
        return f"Ismim {self.name} {self.surname}, tug'ilgan yilim {self.b_year}"

student1 = Student("Ziyodulla", "Tolaboyev", 2011)
print(student1.tanishtir())
print(student1.get_age(2026))