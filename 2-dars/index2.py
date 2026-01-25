fruits = ['apple', 'pine -apple', 'gear']
fruits[1] = 'banana'
fruits.append('mittivoy')
fruits.insert(2, 'melon')
del fruits[3]
# fruits.remove('mittivoy')
tanbal = fruits.pop(-1)
print(tanbal)
print(fruits)