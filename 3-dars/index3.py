cars = ['bmw', 'audi', 'marsedes', 'hyuindai', 'volvo']
print(cars)

# cars.sort()
# print(cars)
print(sorted(cars))

# cars.sort(reverse=True)
# print(cars)
print(sorted(cars, reverse=True))

cars.reverse()
print(cars)

nums = list(range(1, 10, 2))
print(nums)
print(max(nums))
print(min(nums))
print(sum(nums))

cars2 = cars[0:3]
print(cars2)

cars3 = cars[:]
cars3.append('porsche')
print(cars3)