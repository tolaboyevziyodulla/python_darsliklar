car = {'model' : 'ferrari', 'rang' : 'qip-qizil'}
print(car['model'])
print(car['rang'])

fruits = {'apple' : 10000, 'melon' : 20000, 'banana' : 25000}
print(f"Olma narxi {fruits['apple']} so'm")

student = {'ism' : 'to\'laboyev ziyOduLla', 'yosh' : 15, 't_yil' : 2011}
student['kurs'] = 3
student['fakultet'] = 'informatika'
print(f"{student['ism'].title()}, \
 {student['t_yil']}-yilda tug'ilgan, \
 {student['yosh']} yoshda, \
 fakultet: {student['fakultet']}, \
 {student['kurs']}-kurs talabasi")