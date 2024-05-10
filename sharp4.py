import requests as req
from bs4 import BeautifulSoup
import fake_useragent

catalog_page = 1
url = "https://zastavok.net"
for catalog_page in range(1, 3101):
    page_url = f"{url}/{catalog_page}"
    page_html = req.get(page_url).text
    page_soup = BeautifulSoup(page_html, 'lxml')
    page_block = page_soup.find("div", class_="block-photo")
    image_divs = page_block.find_all('div', class_='short_prev')

    image_number = 1
    for div in image_divs:
        predwnld_path = div.find('a').get('href')
        predwnld_url = f"{url}{predwnld_path}"
        predwnld_html = req.get(predwnld_url).text
        predwnld_soup = BeautifulSoup(predwnld_html, 'lxml')
        predwnld_block = predwnld_soup.find('div', class_='block_down')

        dwnld_path = predwnld_block.find('a', id='orig_size').get('href')
        dwnld_link = f"{url}{dwnld_path}"

        image_bytes = req.get(dwnld_link).content
        with open(f"sharp4_files/image{catalog_page}_{image_number}.jpg", 'wb') as image_file:
            image_file.write(image_bytes)
            print(f"Image{catalog_page}.{image_number} downloaded")

        image_number += 1
    catalog_page += 1

