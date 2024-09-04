import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = 'https://www.gsmarena.com.bd/xiaomi-14t-pro/'
req = requests.get(url)
data = req.text

api_data = {}

soup = bs(data, 'html.parser')

phone_name = soup.find('h1').text
api_data['Phone Name'] = phone_name

phone_image = soup.find('div', {'class': 'col-xs-12 col-sm-6'}).find('img').get('src')
api_data['Phone Image'] = phone_image

h2 = soup.find('h2').text
api_data['H2'] = h2
h2_paragraph = soup.find('div', {'class':'col-md-9'}).find('p').text
api_data['H2 Paragraph'] = h2_paragraph

table_h2 = soup.find('div', {'class':'col-md-9'}).findAll('h2', {'class':'heading'})[1].text
api_data['Table H2'] = table_h2


tables = soup.findAll('table', {'class':'table_specs'})
for table in tables:
    table_rows = table.findAll('tr')
    for row in table_rows:
        table_data = row.findAll('td')
        if len(table_data) == 2:
            api_data[table_data[0].text] = table_data[1].text

pprint(api_data)