from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import csv


source = requests.get('https://www.rockporthomerentals.com/category/all-rentals?cat=200&page=3&o=-1').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape3.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'price', 'guest', 'bedrooms', 'bathrooms'])

for rental_info in soup.find_all('div',  class_='property-list-wrapper'):

    #print(rental_info.prettify())

    title = rental_info.find('h4', class_='property-list-title').text
    price = rental_info.find('h2', class_='property-list-price').text
    guest = rental_info.find('li', class_='item-guests').text
    bedrooms = rental_info.find('li', class_='item-bedroom').text
    bathrooms = rental_info.find('li', class_='item-bathrooms').text

    df = pd.DataFrame([title, price, guest, bedrooms, bathrooms], index=['Property Title:','Price:', 'Guests:', 'bedrooms:', 'bathrooms:'])

    print(df)

    csv_writer.writerow([title, price, guest, bedrooms, bathrooms])

csv_file.close()