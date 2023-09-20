#POC for the ability to web scrape GPU prices from tori.fi website.
#Phase 2: would include the scraping of a retailer website and calculating/predicting the difference in prices for each day/best day to buy a gpu etc.
#Phase 3: cloud integration, saving the results to a database hosted on the cloud or locally, Github
#Phase 4: A production ready product, possibly a website to display results and visualize the data

from pymongo import MongoClient
import psycopg2
from databases import collection
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from transform import transform, gpu_list



def extract(page):
    url = f'https://www.tori.fi/koko_suomi/tietokoneet_ja_lisalaitteet/komponentit?ca=18&cg=5030&c=5038&st=s&st=k&st=u&st=h&st=g&st=b&com=graphic_card&w=3&o={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def load_to_mongodb(extracted_html):
    document = {
        "html_content": str(extracted_html),
        #"site_page_number": extracted_html.find('p', class_ = 'no_margin').contents[1],
        "source": "tori",
        "load_time": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")
    }
    collection.insert_one(document)

#define a function to load transformed data to postgres

for page in range(1,2): #call lastpage() here
    print(f'Extracting page {page} from tori.fi and loading to MongoDB')
    parsed_html = extract(page)
    load_to_mongodb(parsed_html)
    transform(parsed_html)

#print(gpu_list)

