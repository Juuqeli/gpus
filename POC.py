#POC for the ability to web scrape GPU prices from tori.fi website.
#Phase 2: would include the scraping of a retailer website and calculating/predicting the difference in prices for each day/best day to buy a gpu etc.
#Phase 3: cloud integration, saving the results to a database hosted on the cloud or locally, Github
#Phase 4: A production ready product, possibly a website to display results and visualize the data

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    url = f'https://www.tori.fi/koko_suomi/tietokoneet_ja_lisalaitteet/komponentit?ca=18&cg=5030&c=5038&st=s&st=k&st=u&st=h&st=g&st=b&com=graphic_card&w=3&o={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('a', class_ = 'item_row_flex')
    for i in divs:
        item_id = i.get('id').replace('item_', '')
        title = i.find('div', class_ = 'li-title').text
        price_euros = i.find('p', class_ = 'list_price ineuros').text.replace(' €','')
        listing_date = i.find('div', class_ = 'date_image').text.replace('\n','').replace('\t', '')
        location = i.find('div', class_ = 'cat_geo clean_links').text.replace('\n','').replace('\t', '').replace('Myydään','').replace('Ostetaan','')
        product_link = i.get('href')
        GPU = {
            'item_id': item_id,
            'title': title,
            'price_in_euros': price_euros,
            'listing_date': listing_date,
            'location': location,
            'product_link': product_link
        }
        if user_input == False:
            gpu_list.append(GPU)
        else:
            if re.search(user_input, title):
                gpu_list.append(GPU)
    return

#try and except!
def last_page():
    last_page = extract(1).find_all('a', {'rel': 'nofollow', 'href': True, 'class': False, 'id': False})
    last_page_actual = last_page[1].get('href')
    range_stop_at = last_page_actual[(len(last_page_actual)-2):len(last_page_actual)]
    return (int(range_stop_at) + 1)

user_input = input('What kind of a GPU would u like to search for? E.g. try typing 3070 or press Enter to search for all GPUs\n')

gpu_list = []

lastPage = last_page()

for i in range(1,lastPage):
    extr = extract(i)
    transform(extr)
    print(f'Getting page {i} from tori.fi')

df = pd.DataFrame(gpu_list)
df = df.set_index('item_id')
df = df.sort_values(by = 'price_in_euros')

print(df)


df.to_csv('gpu_list.csv')