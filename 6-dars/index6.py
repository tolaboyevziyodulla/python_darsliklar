yosh = int(input('Yoshingiz nechada?\n>>> '))
if yosh <= 4:
    money = 0
elif yosh <= 12:
    money = 5000
elif yosh <= 18:
    money = 10000
else:
    money = 20000
print(f"Sizga kirish {money} so'm")

day = input("Bugun qaysi kun?\n>>> ")

if day.lower() == 'shanba' or day.lower() == 'yakshanba':
    print('Bugun dam olish kuni')
else:
    print('Bugun ish kuni')

temp = float(input('Bugun qanday harorat?\n>>> '))
if day.lower() == 'yakshanba' and temp >= 30:
    print('Cho\'milgani ketdu!!!')
elif day.lower() == 'yakshnba' and temp < 30:
    print('Uyda yot, tushundingmi!?')

money = 20000
salat = False
tea = True
bread = True
comp = True
cake = False

if salat:
    print('Mijoz salat oldi')
    money = money + 10000

if tea:
    money = money + 5000
    print('Mijoz choy oldi')

if bread:
    money = money + 4000
    print('Mijoz non oldi')

if comp:
    money = money + 15000
    print('Mijoz kompot oldi')

if cake:
    money = money + 18000
    print('Mijoz shirinlik oldi')
print(f"Jami narh {money} so'm bo'ldi")

menu = ['manti', 'shashlik', 'norin', 'qozonkabob', 'sho\'rva']
meet = input('Nima ovqat yeysiz?\n>>> ')
if meet.lower() in menu:
    print('Buyurtma qabul qilindi')
else:
    print('Afsuski, bizda bunday ovqat yo\'q')