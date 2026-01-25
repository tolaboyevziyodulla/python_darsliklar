import datetime

vaqt = datetime.datetime.now()
print('hozirgi vaqt', vaqt)

#bu pythonning math ishlashi
import math
raqam = 4

kvadrat = raqam * raqam
print('kvadrat:', kvadrat)

ildiz = math.sqrt(raqam)
print('ildiz:', ildiz)

#random bilan ishlash
import random

rand = ['apple', 'microsoft', 'samsung']
print('random1:', random.choice(rand))

print('random2:', random.randrange(10))

print('random3:', random.randint(2, 6))

print('random4:', random.random())

random.shuffle(rand)
print('random5:', rand)

random.seed(12)
print('random6:', random.random())

#list
thislist = ['apple', 'microsoft', 'samsung']
print(thislist[-2])
print(thislist[0:2])
if 'apple' in thislist:
    print('yes!!!!!!!!!!!!!!!!!!!')
thislist.append('poco')
thislist.remove('microsoft')
print(thislist)
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1)

#tuple
thistuple = ('apple', 'microsoft', 'samsung')
y = list(thistuple)
y[0] = 'poco'
thistuple = tuple(y)
print(thistuple)
for x in thistuple:
    print(x)

#set
thisset = {'apple', 'microsoft', 'samsung'}
print(thisset)
for y in thisset:
    print(y)

#int
a = 2
print(type(a))
temp = 1_233_486
print(temp)

#float
s = 3.67
print(type(s), s)

t_yil = int(input("Tug'ilgan yilingizni kiriting: " ))
yosh = datetime.datetime.now().year - t_yil
print('Siz', yosh, 'yoshdasiz')

