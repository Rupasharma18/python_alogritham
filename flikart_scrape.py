import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

# url = 'https://www.flipkart.com/search?q=mi+mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY'
# def getRequestSoup(url):
# 	return BeautifulSoup(requests.get(url).text,'html.parser')
# kart_data = getRequestSoup(url)
# data = kart_data.find('div', class_="_1HmYoV _35HD7C")
# for name in kart_data.find_all('div', {"class":"bhgxx2 col-12-12"}):
#     for i in  name.find_all('div',{'class':'_3wU53n'}):
#         print (i.text)
#         for r in name.find_all('div', {'class':'_1vC4OE _2rQ-NK'}):
#             print (r.text)
count = 0            
for page in range(1,11):
    count = count + 1
    print (count)
    my_url = 'https://www.flipkart.com/search?q=mi+mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY'.format(page)
    res = requests.get(my_url)
    soup = BeautifulSoup(res.text, "html.parser")
    for name in soup.find_all('div', {"class":"bhgxx2 col-12-12"}):
        for names in  name.find_all('div',{'class':'_3wU53n'}):
            print (names.text)
            for price in name.find_all('div', {'class':'_1vC4OE _2rQ-NK'}):
                print (price.text)
                          