

#try and except!
def last_page():
    last_page = extract(1).find_all('a', {'rel': 'nofollow', 'href': True, 'class': False, 'id': False})
    last_page_actual = last_page[1].get('href')
    range_stop_at = last_page_actual[(len(last_page_actual)-2):len(last_page_actual)]
    return (int(range_stop_at) + 1)


lastPage = last_page()

for page in range(1,2): #call lastpage() here
    extr = extract(page)
    transform(extr)
    print(f'Getting page {page} from tori.fi')

df = pd.DataFrame(gpu_list)
df = df.set_index('item_id')
df = df.sort_values(by = 'price_in_euros')

#print(df)


df.to_csv('gpu_list.csv')