#동적 생성되는 data 크롤링
#Selenium 모듈 사용
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import selenium
from selenium import webdriver
import time



def Gang_get_url(url):
    driver = webdriver.Chrome("../Driver/chromedriver")
    driver.get(url)
    time.sleep(3)
    whole_page = driver.page_source
    soup = BeautifulSoup(whole_page,'html.parser')
    all_page = soup.find_all('button',{'class':'btn btn--pagination btn--small pagination__page'})
    for last_page in all_page[-1]:
        page =int(last_page)
        URL = [f"https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81421%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset={i}&ra=&overlayMode=" for i in range(int(page))]
        return URL
def Bu_get_url(url):
    driver = webdriver.Chrome("../Driver/chromedriver")
    driver.get(url)
    time.sleep(3)
    whole_page = driver.page_source
    soup = BeautifulSoup(whole_page,'html.parser')
    all_page = soup.find_all('button',{'class':'btn btn--pagination btn--small pagination__page'})
    for last_page in all_page[-1]:
        page =int(last_page)
        URL = [f"https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81491%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset={i}&ra=&overlayMode=" for i in range(int(page))]
        return URL
def Mok_get_url(url):
    driver = webdriver.Chrome("../Driver/chromedriver")
    driver.get(url)
    time.sleep(3)
    whole_page = driver.page_source
    soup = BeautifulSoup(whole_page,'html.parser')
    all_page = soup.find_all('button',{'class':'btn btn--pagination btn--small pagination__page'})
    for last_page in all_page[-1]:
        page =int(last_page)
        URL = [f"https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81505%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset={i}&ra=&overlayMode=" for i in range(int(page))]
        return URL
def An_get_url(url):
    driver = webdriver.Chrome("../Driver/chromedriver")
    driver.get(url)
    time.sleep(3)
    whole_page = driver.page_source
    soup = BeautifulSoup(whole_page,'html.parser')
    all_page = soup.find_all('button',{'class':'btn btn--pagination btn--small pagination__page'})
    for last_page in all_page[-1]:
        page =int(last_page)
        URL = [f"https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81458%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset={i}&ra=&overlayMode=" for i in range(int(page))]
        return URL
def Jun_get_url(url):
    driver = webdriver.Chrome("../Driver/chromedriver")
    driver.get(url)
    time.sleep(3)
    whole_page = driver.page_source
    soup = BeautifulSoup(whole_page,'html.parser')
    all_page = soup.find_all('button',{'class':'btn btn--pagination btn--small pagination__page'})
    time.sleep(3)
    for last_page in all_page[-1]:
        page =int(last_page)
        URL = [f"https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81521%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset={i}&ra=&overlayMode=" for i in range(int(page))]
        return URL

def get_Inn_info(url_list):
    df_fin = pd.DataFrame()
    for page in url_list:
        # accom_dict = {}
        driver = webdriver.Chrome("../Driver/chromedriver")
        driver.get(page)
        #숙박 업소 이름
        time.sleep(5) # 넉넉하게 멈추는 시간 넣기
        name_list = driver.find_elements_by_css_selector('span.item-link')
        name = [names.text for names in name_list]
        #가격 정보
        time.sleep(5)  # 넉넉하게 멈추는 시간 넣기
        price_list = driver.find_elements_by_css_selector('strong.accommodation-list__price--45dcc')
        price = [prices.text for prices in price_list]
        accom_dict = {'가격': price}
        df = pd.DataFrame(accom_dict)
        df_fin = pd.concat([df_fin,df],ignore_index=True)
    return df_fin


