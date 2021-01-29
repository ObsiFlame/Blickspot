from bs4 import BeautifulSoup
import requests as re 

url = 'https://cyware.com/category/breaches-and-incidents-news'
html = re.get(url).text

soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())

for text in soup.find_all('div', class_ ='cy-panel'):
    print(text.h1.get_text())