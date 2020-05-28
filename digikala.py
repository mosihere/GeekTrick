import requests
from bs4 import BeautifulSoup
import re
response = requests.get('https://www.digikala.com/search/category-laptop/')
soup = BeautifulSoup(response.text, 'html.parser')

data = soup('div', attrs={'class':'c-product-box__content'})

f = open('data.txt','w+')
counter = 0
for info in data:
    f.write(info.text)
    
f.close()
