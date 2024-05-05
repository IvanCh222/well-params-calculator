
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
for i in range(1,50):
    driver.get('https://www.wildberries.ru/catalog/0/search.aspx?page='+str(i)+'&sort=popular&search=apple')


# Прокручиваем страницу
    driver.find_element('tag name', 'body').send_keys(Keys.END)
    time.sleep(4)  # Ждем некоторое время после каждой прокрутки

    html = driver.page_source
    soup = BS(html, 'html.parser')

    mem = soup.find_all('div', class_='product-card__wrapper')
    for item in mem:
        name = item.find('img', class_='j-thumbnail')
        print(name)