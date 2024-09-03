import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.gsmarena.com.bd/'
res = requests.get(url)
soup = bs(res.text, 'html.parser')
product_thumbs = soup.findAll('div', {'class':'product-thumb'})

for product in product_thumbs:
    product_urls = product.find('a').get('href')
    with open('urls.txt', 'a+') as file:
        file.writelines(product_urls + '\n')
