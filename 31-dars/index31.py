# # datetime moduli
import datetime as dt

# datetime classi
now = dt.datetime.now()
print(now)
print(now.date())
print(now.time())
print(now.hour)
print(now.minute)
print(now.second)

# date classi
today = dt.date.today()
print(f"Bugungi sana: {today}")
yesterday = dt.date(2026, 1, 17)
print(f"Ertangi sana: {yesterday}")

# time()
timeNow = now.time()
print(f"Hozir soat: {timeNow}")

# sanalar orasidagi farq
ramazon = dt.date(2026, 2, 18)
distance = ramazon - today
print(distance)
print(f"Ramazongacha {distance.days} kun qoldi")

football = dt.datetime(2026, 1, 25, 22, 00, 00)
distance = football - now
seconds = distance.seconds
minuts = int(seconds / 60)
hours = int(minuts / 60)
print(f"Futbol boshlanishiga {distance.days} kun-u {hours} soat qoldi")

# # math moduli
import math

PI = math.pi
print(f"PIning qiymati: {PI}")
E = math.e
print(f"e ning qiymati: {E}")

# trigonometriya
math.sin(math.pi / 2)
math.cos(0)
math.tan(PI)

# radianlar va burchaklar o'rtasidagi konversiya
math.degrees(math.pi / 2)
math.radians(90)

# logarifm
math.log(5)
math.log10(100)

# sonlarni yaxlitlash
x = 4.6
math.ceil(x)
math.floor(x)

# ildizlar
x = 625
math.sqrt(x)

# darajaga oshirish
math.pow(x, 3)
math.pow(x, 5)
math.pow(x, 1/3)

# # pprint
from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as file:
    bemor = json.load(file)

pprint(bemor)

# # regex
import re
from uzwords import words

word1 = 'темур'
word2 = 'томир'
word3 = 'тулпор'

andoza = "^т...р$"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))

matches = []
for word in words:
    if re.match(andoza, word):
        matches.append(word)
print(matches)

# emailni ajratib olish
text = 'Buyurtma va sotuvlar bilan bog‘lanish uchun sales@misol.uz ga xabar yuboring.'
andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza, text)
print(email)

# kuchli parolni tekshirish
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = 'Yangi parol kiriting'
msg += '(kamida 8ta belgidan iborat, kamida 1ta lotin bosh harf, 1ta kichik harf, '
msg += '1ta son va 1ta maxsus belgi bo\'lishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")