from random import *

def son_top(x = 10):
    rand_num = randint(1, x)
    print(f"Men 1dan {x}gacha son o'yladim. Topa olasizmi?")
    taxmins = 0
    while True:
        taxmins += 1
        taxmin = int(input('>>> '))
        if taxmin < rand_num:
            print(f"Xato. Men o'ylagan son bundan kattaroq. Qayta urining: ")
        elif taxmin > rand_num:
            print(f"Xato. Men o'ylagan son bundan kichikroq. Qayta urining: ")
        elif taxmin == rand_num:
            break
    print(f"Tabriklayman. {taxmins} ta urinishda men o'ylagan sonni topdingiz!")
    return taxmins

def son_top_pc(x = 10):
    input(f"1dan {x}gacha son o'ylang va istalgan tugmani bosing. Men topaman. ")
    low = 1
    tit = x
    taxmins = 0
    while True:
        taxmins += 1
        if low != tit:
            taxmin = randint(1, x)
        else:
            taxmin = low
        answer = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t), kichik(-), katta(+): ".lower())
        if answer == '-':
            tit = taxmin - 1
        elif answer == '+':
            low  = taxmin + 1
        elif answer == 't':
            break
    print(f"{taxmins} urinishda topdim!")
    return taxmins

