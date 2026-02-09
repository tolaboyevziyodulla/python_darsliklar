class Person:
    '''Shaxs haqida ma'lumot'''
    def __init__(self, name, surname, passport, b_year):
        '''Shaxsning xususiyatlari'''
        self.name = name
        self.surname = surname
        self.passport = passport
        self.b_year = b_year

    def get_info(self):
        info = f"{self.name} {self.surname}"
        info += f"Passport:{self.passport}, {self.b_year}-yilda tug'ilgan"
        return info

    def get_age(self, year):
        '''Shaxsning yoshini qaytaruvchi metod'''
        return year - self.b_year
    
class Student(Person):
    '''Talaba classi'''
    def __init__(self, name, surname, passport, b_year, id, adres):
        '''Talabaning xususiyatlari'''
        super().__init__(name, surname, passport, b_year)
        self.id = id
        self.round = 1
        self.adres = adres

    def get_id(self):
        '''Talabaning ID raqami'''
        return self.id
    
    def get_round(self):
        '''Talabaning o'qish bosqichi'''
        return self.round
        

class Adres:
    '''Manzil haqida class'''
    def __init__(self, uy, kocha, mahalla, tuman, viloyat):
        '''Manzil xususiyatlari'''
        self.uy = uy
        self.kocha = kocha
        self.mahalla = mahalla
        self.tuman = tuman
        self.viloyat = viloyat

    def get_adres(self):
        '''Manzilni ko'rish'''
        adres = f"{self.viloyat} viloyati, {self.tuman} tumani, {self.mahalla} mahalla, "
        adres += f"{self.kocha} ko'cha, {self.uy}-uy"

student1_adres = Adres(55, "Ma'rifat", 'Changtepa', 'O\'rta Chirchiq', 'Toshkent')
student1 = Student("Hasan", "Husanov", "FA0116783", 2009, "0000090", student1_adres)

print(student1.adres.get_adres())