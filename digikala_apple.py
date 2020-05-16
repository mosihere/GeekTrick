import requests
import re
from bs4 import BeautifulSoup

response = requests.get('https://www.digikala.com/brand/apple/') 
soup = BeautifulSoup(response.text,'html.parser')

data = soup('div', attrs={'class':'c-product-box__content'})

f = open('apple.txt','w+')
for stuff in data:
    print(stuff.text)
    print()
    f.write(stuff.text)