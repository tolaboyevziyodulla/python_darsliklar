def but_name_do(name, surname, dad_name = ''):
    """To'liq ism qaytaruvchi funksiya"""
    if dad_name:
        but_name = f"{name} {dad_name} {surname}"
    else:
        but_name = f"{name} {surname}"
    return but_name.title()
student = but_name_do(surname='to\'laboYEv', name='ziyoDULla', dad_name='alisherovich')
print(student)

def avto_info(comp, model, color, corob, year, price=None):
    avto = {
        'kompaniya' : comp,
        'model' : model,
        'korobka' : corob,
        'rang' : color,
        'yil' : year,
        'narh' : price
    }
    return avto
avto = avto_info('GM', 'Malibu', 'qora', 'avtomat', 2018, 2700)
