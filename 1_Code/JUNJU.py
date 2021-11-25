import requests
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

import pandas as pd

url = "https://www.tripadvisor.co.kr/Attractions-g1143545-Activities-Jeonju_Jeollabuk_do.html"
res = requests.get(url)
print(res)
# soup = BeautifulSoup(res.text, 'html.parser')
# title = soup.find_all('span', {'name': 'title'})
# location = []
# for name in title[:10]:
#     place = str(name.text).split('.')
#     location.append(place[1])
#
# print(location)