from bs4 import BeautifulSoup
import datetime

today = datetime.date.today()

def transform(soup):
    divs = soup.find_all('a', class_ = 'item_row_flex')
    for i in divs:
        item_id = i.get('id').replace('item_', '')
        title = i.find('div', class_ = 'li-title').text
        price_euros = int(i.find('p', class_ = 'list_price ineuros').text.replace(' €',''))
        listing_date = i.find('div', class_ = 'date_image').text.replace('\n','').replace('\t', '').replace('eilen', str(today.replace(day=today.day - 1))).replace('tänään', str(today)).strip()
        location = i.find('div', class_ = 'cat_geo clean_links').text.replace('\n','').replace('\t', '').replace('Myydään','').replace('Ostetaan','').replace('Vaihdetaan','')
        product_link = i.get('href')
        GPU = {
            'item_id': item_id,
            'title': title,
            'price_in_euros': price_euros,
            'listing_date': listing_date,
            'location': location,
            'product_link': product_link
        }
        gpu_list.append(GPU)
    return

gpu_list = []