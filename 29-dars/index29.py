def get_full_name(name, surname, father_name = ''):
    if father_name:
        return f"{name} {surname} {father_name}".title()
    else:
        return f"{name} {surname}".title()

def getArea(r, pi = 3.14159):
    '''Doiraning yuzini qaytaruvchi funksiya'''
    return pi * (r ** 2)

def getPerimeter(r, pi = 3.14159):
    '''Doiraning perimeter qaytaruvchi funksiya'''
    return 2 * pi * r

print(getPerimeter(3))