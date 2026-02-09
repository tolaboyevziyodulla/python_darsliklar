from uuid import uuid4

class Avto:
    '''Avtomobil classi'''
    __num_auto = 0
    def __init__(self, make, model, color, year, price, km = 0):
        '''Avtomobil xususiyatlari'''
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Avto.__num_auto += 1

    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        '''Mashinaning km siga km qo'shish'''
        if km >= 0:
            self.__km += km
        else:
            print("Mashinaning kilometrini kamaytirib bo'lmaydi")
    
    @classmethod
    def get_num_auto(cls):
        return cls.__num_auto
        
    