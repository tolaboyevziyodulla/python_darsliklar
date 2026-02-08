car0 = {
    'model' : 'lacetti',
    'rang' : 'oq',
    'yil' : 2018,
    'narh' : 13000
}

car1 = {
    'model' : 'gentra',
    'rang' : 'qizil',
    'yil' : 2019,
    'narh' : 20000
}

car2 = {
    'model' : 'nexia 3',
    'rang' : 'qora',
    'yil' : 2015,
    'narh' : 9000
}

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")
    print(f"{car['rang'].title()} {car['model']}")


programmers = {
    'ali' : ['python', 'c++'],
    'vali' : ['html', 'css', 'js'],
    'hasan' : ['php', 'sql'],
    'husan' : ['python', 'php'],
    'maryam' : ['c++', 'c#']
}

for name, lengs in programmers.items():
    print(f"\n{name.title()} quyidagi dasturlash tillarini biladi:")
    for leng in lengs:
        print(f"{leng.upper()}, ", end = '')

forjobs = {
    'ali' : {'familiya' : 'valiyev',
             't_yil' : 1995,
             'malumot' : 'oliy',
             'tillar' : ['html', 'css', 'js']},
    'vali' : {'familiya' : 'aliyev',
             't_yil' : 2001,
             'malumot' : 'o\'rta-maxsus',
             'tillar' : ['python', 'c++']},
    'hasan' : {'familiya' : 'husanov',
             't_yil' : 1999,
             'malumot' : 'maxsus',
             'tillar' : ['python', 'php']}
}

for name, info in forjobs.items():
    print(f"\n{name.title()} {info['familiya'].title()}. "
          f"{info['t_yil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for leng in info['tillar']:
        print(leng.upper())