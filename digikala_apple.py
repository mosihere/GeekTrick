import requests
import re
from bs4 import BeautifulSoup
import csv

response = requests.get('https://www.digikala.com/brand/apple/?has_selling_stock=1&pageno=1&sortby=4') 
soup = BeautifulSoup(response.text,'html.parser')

data = soup.find_all('div', attrs={'class':'c-product-box__content'})

f = open('apple.csv','w+')

for stuff in data:
    f.write(re.sub(r'\s+',' ',stuff.text))
    f.write('\n')
    
f.close()