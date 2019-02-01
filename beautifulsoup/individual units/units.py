from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import csv


source = requests.get('https://www.rockporthomerentals.com/vacation-rental-home.asp?PageDataID=152670').text

soup = BeautifulSoup(source, 'lxml')

#csv_file = open('cms_scrape3.csv', 'w')

#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['title', 'price', 'guest', 'bedrooms', 'bathrooms'])
mylist=[]
for rental_info in soup.find_all('td', class_='property-calendar-td-bd'):

    #jan = rental_info.find('div', class_='outer-calendar-table').text
    janbooked = rental_info.find_all('span')[0].text

    mylist.append(janbooked)
df = pd.DataFrame(mylist)

print(mylist)


