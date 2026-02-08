cars = ['bmw', 'kia', 'hyundai', 'audi', 'volvo', 'byd']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

ism = input('Ismingiz nima?\n>>>>')
if ism.lower() != 'mittipit':
    print(f"Uzr {ism.title()}, biz MittiPitni kutyapmiz")
else:
    print('chiz, chichqoq!!!!!!!!!!!!!!!!!!!')

yosh = int(input("Yoshingiz nechada?\n>>> "))
if yosh >= 18:
    print('Xush kelibsiz!!!')
else:
    print('Kirish taqiqlanadi!!!')