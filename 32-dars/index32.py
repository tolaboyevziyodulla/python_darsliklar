# # googletrans
from googletrans import Translator
translate = Translator()

# sodda tarjimalar
text_uz = 'Python - dunyodagi eng mashxur dasturlash tili'
translater = translate.translate(text_uz)
print(translater.origin)
print(translater.text)
print(translater.src)
translater = translate.translate(text_uz, dest='ru')
print(translater.text)

# murakkabroq tarjima AI
msg = "Tarjima uchun so'z kiriting(chiqib ketish uchun 'q' deb yozing): "

while True:
    text = input(msg)
    if text == 'q':
        break
    else:
        translater = translate.translate(text, src='uz', dest='en')
        print(translater.text)

# # requests
import requests
from pprint import pprint

# oddiy chaqirish
sayt = 'https://kun.uz/news/main'
r = requests.get(sayt)
pprint(r.text)

# restcountries API
country = 'Uzbekistan'
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json.keys())
print(r_json['capital'])

# # gooogletrans va requests
url = 'https://api.advideslip.com/advise'
r = requests.get(url)
advise = r.json()['slip']['advise']
print(advise)

translater = Translator()
translate = translater.translate(advise, dest='uz')
print(translate.text)

# # bs4 BeatifulSoup
from bs4 import BeautifulSoup

sayt = 'https://kun.uz/news/main'
r = requests.get(sayt)
pprint(r.text)

soup = BeautifulSoup(r.text, 'html.parper')
print(soup.prettify())
news = soup.find_all(class_='news-title')
print(news[0].text)