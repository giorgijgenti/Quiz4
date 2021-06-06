import requests
from bs4 import BeautifulSoup
ind = 80
url = 'https://www.myparts.ge/ka/s/nawilebi-transmission_box_--?pr_type_id=1&v_type_id=0&cat_id=495&price_from=0&price_to=20000&Page='+str(ind)

file = open('Myparts.csv', 'w', encoding='utf-8_sig')
file.write('name, description\n')
r = requests.get(url)
# print(r)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
item_block = soup.find('div', class_='list-container')
# print(item_block)
all_item = item_block.find_all('div', class_='list-item')
# print(all_item)
for each in all_item:
    name = each.find('a', class_='header').text
    print(name)
    description = each.find('a', class_='short-description').text
    # print(description)
    file.write(name+','+description+'\n')
