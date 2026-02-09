def hella_do():
    """Salom beruvchi funksiya"""
    print('Assalomu alaykum')
hella_do()

def kv(x):
    """Kvadrat funksiya"""
    print(x ** 2)
kvd = int(input("Lyubboy son yoz!!!: "))
kv(kvd)

import datetime
def year_count(name, y_year, j_year = datetime.datetime.now().year):
    """Yosh hisoblovchi funksiya"""
    print(f"{name.title()} {j_year-y_year} yoshda")
year_count(y_year=2011, name='ziyoDULla')