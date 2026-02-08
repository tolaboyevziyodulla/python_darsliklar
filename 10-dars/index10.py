# input()
name = input("Ismingiz nima? ")
quas = f"Salom {name.title()}, Yoshingiz nechada? "
year = input(quas)
year = int(year)
height = input("Bo'yingiz necha metr? ")
height = float(height)
print(f"Ism: {name.title()}, "
    f"Yosh: {year} yosh, "
    f"Bo'y: {height}m")

# while
num = 0
while num <= 5:
    print(num)
    num += 1

# while and input()
# print("Kirtilgan sonning kvadratini qaytaruvchi dastur.")
# ques = "Istalgan son kiriting "
# ques += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# result = ''
# while result != 'exit':
#     result = input(ques)
#     if result != 'exit':
#         print(float(result) ** 2)
# print("Dastur tugadi!")

# flag
# print("Kirtilgan sonning kvadratini qaytaruvchi dastur.")
# ques = "Istalgan son kiriting "
# ques += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# flag = True
# while flag:
#     result = input(ques)
#     if result == 'exit':
#         flag = False
#     else:
#         print(float(result) ** 2)
# print("Dastur tugadi!")

# break while
print("Kirtilgan sonning kvadratini qaytaruvchi dastur.")
ques = "Istalgan son kiriting "
ques += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    result = input(ques)
    if result  == 'exit':
        break
    else:
        print(float(result) ** 2)
print('Dastur tugadi!')

# break for
nums = list(range(1, 11))
for num in nums:
    if num == 5:
        break
    print(f"{num}ning kvadrati {num ** 2}ga teng")

# continue
nums = list(range(1, 11))
for num in nums:
    if num == 5:
        continue
    print(f"{num}ning kvadrati {num ** 2}ga teng")

# infinite loop
num = 0

while num < 10:
    if num % 2 != 0:
        continue
    else:
        print(num)

while num < 10:
    if num % 2 != 0:
        continue
    else:
        print(num)
    num += 1

num = 1
while num > 0:
    num += 1
    if num % 2 != 0:
        continue
    else:
        print(num)