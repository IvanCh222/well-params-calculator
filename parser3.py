from bs4 import BeautifulSoup as BS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('https://www.youtube.com/watch?v=HZdaR_Y7I7k')


# Прокручиваем страницу
driver.find_element('tag name', 'body').send_keys(Keys.END)
time.sleep(5)  # Ждем некоторое время после каждой прокрутки

html = driver.page_source
soup = BS(html, 'html.parser')

mem = soup.find_all('yt-formatted-string', class_='style-scope ytd-comment-renderer')
for item in mem:
    print(item.text)