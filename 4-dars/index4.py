guests = ['Ali', 'Vali', 'Kamol', 'Hasan', 'Husan', 'Olim']
for guest in guests:
    print('Salom', guest)
    print('Xayr,', guest)

nums = list(range(1, 11))
for num in nums:
    print(f"{num}ning kvadrati {num ** 2}ga teng")

nums  = list(range(11))
nums_kv = []
for num in nums:
    nums_kv.append(num ** 2)
print(nums_kv)

friends = []
print('5ta do\'stingizni ismini yozing')
for n in range(5):
    friends.append(input(f"{n + 1}-do'stingizni ismini yozing: "))
print(friends)