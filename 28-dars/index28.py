# ValueError va try, except, else
age = input('Yoshingizni kiriting: ')

# try:
#     age = int(age)
#     print(f"Siz {2026 - age}-yilda tu'ilgansiz")
# except:
#     print('Butn son kirit, to\'nkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!!!!!!!!')

try:
    age = int(age)
except ValueError:
    print('Butn son kirit, to\'nkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!!!!!!!!!!')
else:
    print(f"Siz {2026 - age}-yilda tu'ilgansiz")


# ZeroDivisionError
x, y = 5, 10
try:
    y / (x - 5)
except ZeroDivisionError:
    print("0ga bo'lib bo'lmaydi, to'nkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!!!!!!!")

# IndexError
fruits = ['olma', 'anor', 'anjir', 'uzum']
try:
    print(fruits[4])
except IndexError:
    print(f"Ro'yxatda {len(fruits)} ta meva bor,to'nkaaaaaaaaaaaaaaaaaaaaaaaa!!!!!!!!!!")

# KeyError
user = {
    'username' : 'Ziyodulla Hacker',
    'status' : 'admin',
    'email' : 'tolaboyevziyodulla@gmail.com',
    'phone' : '+998997808747'
}

key = 'tel'
try:
    print(f"Foydalanuvchi: {user[key]}")
except:
    print("Bunday kalit mavjuud emas")

# FileNotFoundError
filename = 'data.txt'
try:
    with open(filename) as file:
        text = file.read()
except FileNotFoundError:
    print(f"{filename} fayli mavjud emas")

# pass
fruits = ['olma', 'anor', 'anjir', 'uzum']
try:
    print(fruits[4])
except IndexError:
    pass

# try, except, except, else
n = input('Butun son kiriting: ')
try:
    n = int(n)
    x = 20 / n
except ValueError:
    pass
except ZeroDivisionError:
    print("0ga bo'lib bo'lmaydi")
else:
    print(f"x={x}")