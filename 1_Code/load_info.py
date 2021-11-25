from Function import *
import pandas as pd
url1 = 'https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81421%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode='
url2 = "https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81491%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode="
url3 = "https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81505%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode="
url4 = "https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81458%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode="
url5 = "https://www.trivago.co.kr/?aDateRange%5Barr%5D=2021-08-23&aDateRange%5Bdep%5D=2021-08-24&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=7&aRooms%5B0%5D%5Badults%5D=2&cpt2=81521%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=20000&address=&addressGeoCode=&offset=0&ra=&overlayMode="

# Gangneung = Gang_get_url(url1)
# Andong = An_get_url(url4)
# Busan = Bu_get_url(url2)
Mokpo = Mok_get_url(url3)
Junju = Jun_get_url(url5)
Mokpo_info_dict = get_Inn_info(Mokpo)
Junju_info_dict = get_Inn_info(Junju)
Mokpo_info_dict.to_csv('../crawl_data/mokpo_info.csv')
Junju_info_dict.to_csv('../crawl_data/junju_info.csv')



