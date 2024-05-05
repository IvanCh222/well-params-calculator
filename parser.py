import requests
from bs4 import BeautifulSoup as BS
from openpyxl import Workbook
import json


navitoys_url = 'https://navitoys.ru/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

catalogue = ['iphone','noutbuki_apple','ipad','monobloki_apple_imac','chasy__apple_watch','naushniki']
data = []

def get_soup(url):
  res=requests.get(url,headers)
  return BS(res.text, 'html.parser')



for i in range(0,5):
  for item  in range(1,13):
    html = get_soup(navitoys_url+'catalogue/'+catalogue[i]+'/?page='+str(item))
    mem = html.find_all('div', class_='catalog__item')

    for item in mem:
      name = item.find('a', class_='card__name-link')
      price = item.find('div', class_='card__price-current')
      data.append([name.text, price.text[:-2]])





# Создаем новую книгу Excel
wb = Workbook()
ws = wb.active

# Записываем данные в лист
for row in data:
    ws.append(list(row))

# Сохраняем книгу
wb.save('/Users/mac/Desktop/pytest/data.xlsx')

with open('/Users/mac/Desktop/pytest/data.json', 'w') as filew:
  json.dump(data, filew)

