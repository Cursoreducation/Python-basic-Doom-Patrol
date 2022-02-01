import csv
from bs4 import BeautifulSoup
from config import Config

def create_file():
    file = open(Config.FILE_URL, 'w')
    csvwriter = csv.writer(file)
    csvwriter.writerow(['title', 'price'])
    file.close()

def get_count_of_pages(content):
    soup = BeautifulSoup(content, 'html.parser')
    pagination_list = soup.find(class_='pagination')
    last_el = pagination_list.find_all('li')[-1].find('a')
    link=last_el['href']
    return link[-1]

def save_row(data):
    file = open(Config.FILE_URL, 'a')
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()

def get_all_items(content):
    soup = BeautifulSoup(content, 'html.parser')
    all_items = soup.find_all(class_='catalog-item__entry')
    items_list = []
    for item in all_items:
        title_object = item.find(class_='catalog-item__title')
        title = title_object.find('a').text
        price = item.find(class_='catalog-item__price').text
        print(title)
        print(price)
        items_list.append([title, price])
    save_row(items_list)