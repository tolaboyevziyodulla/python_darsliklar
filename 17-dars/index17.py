# lambda funksiyasi bilan ishlash
import math

length1 = lambda pi, r : 2 * pi * r
print(length1(math.pi, 10))

daraja = lambda x, y : x ** y
print(daraja(3, 8))

def daraja(n):
    return lambda x : x ** n

kv = daraja(2)
print(kv(111111111))

# map funsiyasi bilan ishlash
nums = list(range(11))

ildizlar = list(map(math.sqrt, nums))
print(ildizlar)

# def daraja2(x):
#     '''Berilgan sonning kvadratini qaytaruvchi funksiya'''
#     return x * x
# print(list(map(daraja2, nums)))

kv_s = list(map(lambda x: x * x, nums))
print(kv_s)

a = [4, 5, 6]
b = [5, 6, 7]
a_pl_b = list(map(lambda x, y: x + y, a, b))
print(a_pl_b)

# filter funksiyasi bilan ishlash
from random import *
nums = sample(range(100), 10)
print(nums)

# def juft(x):
#     '''xning juftligini aniqlovchi funksiya'''
#     return x % 2 == 0
# juft_nums = list(filter(juft, nums))

juft_nums = list(filter(lambda num: num % 2 == 0, nums))
print(juft_nums)

fruits = ['olma', 'anor', 'behi', 'anjir', 'shaftoli', 'o\'rik', 'banan']

letter = 'b'
fruits_b = list(filter(lambda fruit: fruit.startswith(letter), fruits))
print(fruits_b)

fruits2 = list(filter(lambda fruit: len(fruit) <= 5, fruits))
print(fruits2)