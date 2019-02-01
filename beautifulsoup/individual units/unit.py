from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from pandas import DataFrame
import csv


source = requests.get('https://www.rockporthomerentals.com/property/the-peacock-palace').text

soup = BeautifulSoup(source, 'lxml')

#csv_file = open('cms_scrape3.csv', 'w')

#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['title', 'price', 'guest', 'bedrooms', 'bathrooms'])

for rental_info in soup.find_all('tr'):

    #jan = rental_info.find('div', class_='outer-calendar-table').text
    janbooked = rental_info.find_all('td', class_='property-calendar-td-bd')

    #number = janbooked.find('span')

    #print(rental_info.prettify())

    #title = rental_info.find('h4', class_='property-list-title').text
    #price = rental_info.find('h2', class_='property-list-price').text
    #guest = rental_info.find('li', class_='item-guests').text
    #bedrooms = rental_info.find('li', class_='item-bedroom').text
    #bathrooms = rental_info.find('li', class_='item-bathrooms').text

    #df = pd.DataFrame([title, price, guest, bedrooms, bathrooms], index=['Property Title:','Price:', 'Guests:', 'bedrooms:', 'bathrooms:'])

    print(janbooked)

    #csv_writer.writerow([title, price, guest, bedrooms, bathrooms])

