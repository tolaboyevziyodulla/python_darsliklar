class Avto:
    '''Avtomobil classi'''
    def __init__(self, make, model, color, year, price):
        '''Avtomobil xususiyatlari'''
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

#   def __str__(self):
#       return f"Avto: {self.make} {self.model}"
    
    def __str__(self):
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self, y):
        return self.price == y.price
    
    def __lt__(self, y):
        return self.price < y.price
    
    def __le__(self, y):
        return self.price <= y.price
    

avto1 = Avto("Chevrolet", "Trekcer", "oq", 2024, 20000)
avto2 = Avto("GM", "Lacetti", "qora", 2022, 10000)
avto3 = Avto("Chevrolet", "Lacetti", "oq", 2022, 10000)
print(avto1)
print(avto1 == avto2)
print(avto1 > avto2)
print(avto1 <= avto2)
print(avto1 >= avto2)
print(avto1 < avto2)

class Avtosalon:
    '''Avtosalon classi'''
    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def add_avto(self, *result):
        for avto in result:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print('Avto kiriting')

    def __getitem__(self, index):
        return self.avtolar[index]
    
    def __len__(self):
        return len(self.avtolar)
    
    def __setitem__(self, index, result):
        self.avtolar[index] = result
    
    def __call__(self, *result):
        if result:
            for avto in result:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
        
    def __add__(self, boshqa_salon):
        if isinstance(boshqa_salon, Avtosalon):
            new_salon = Avtosalon(f"{self.name} {boshqa_salon.name}")
            return new_salon
    

salon1 = Avtosalon('MaxAvto')
salon2 = Avtosalon('Avto Lider')
# salon1.add_avto(avto1, avto2)
salon2(avto3)
# salon1[0] = avto3
print(len(salon1))
# print(salon1[0])
# print(salon1[1])
# print(salon1[:])
print(salon1 + salon2)