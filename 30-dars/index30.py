class Car:
    def __init__(self, make, model, year, km = 0, price = None):
        self.make = make
        self.model = model
        self.year = year
        self.__km = km
        self.price = price

    def add_km(self, km):
        '''Mashinaning kmsini qo'shish'''
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("kmni kamaytirib bo'lmaydi")