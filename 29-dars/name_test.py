import unittest
from index31 import get_full_name, getArea, getPerimeter

# class NameTest(unittest.TestCase):
#     def test_full_name(self):
#         name = get_full_name('ziyodulla', 'tolaboyev')
#         self.assertEqual(name, 'Ziyodulla Tolaboyev')

#     def test_father_name(self):
#         name = get_full_name('ziyodulla', 'tolaboyev', 'alisherovich')
#         self.assertEqual(name, 'Ziyodulla Tolaboyev Alisherovich')

# unittest.main()

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975)
        self.assertAlmostEqual(getArea(10), 314.159)

    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)

unittest.main()