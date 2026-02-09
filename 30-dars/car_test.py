import unittest
from index32 import Car

class CarTest(unittest.TestCase):
    '''Car classini tekshirish'''
    def setUp(self):
        make = 'GM'
        model = 'malibu'
        year = 2020
        self.price = 40000
        self.km = 100000
        self.car1 = Car(make, model, year)
        self.car2 = Car(make, model, year, price=self.price, km=self.km)

    def test_create(self):
        self.assertIsNotNone(self.car1.make)
        self.assertIsNotNone(self.car1.model)
        self.assertIsNotNone(self.car1.year)
        self.assertIsNone(self.car1.price)
        self.assertEqual(0, self.car1.get_km())
        self.assertEqual(self.price, self.car2.price)

    def test_add_km(self):
        self.car1.add_km(self.km)
        self.assertEqual(self.km, self.car1.get_km())
        new_km = -5000
        try:
            self.car1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)

unittest.main()