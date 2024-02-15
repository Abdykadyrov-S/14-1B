from bs4 import BeautifulSoup
import requests

def parsing_barmak():
    url = 'https://www.sulpak.kg/f/smartfoniy/osh/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")
    all_laptops_image = soup.find_all('img', class_ = "image-size-cls")

    for image in all_laptops_image:
        result = image['src']
        print(result)
        # print(image['src'])

    # print(all_laptops_name)
    # print(all_laptops_price)

    for name, price in zip(all_laptops_name, all_laptops_price):
        # result = "".join(name.text)
        print(name.text, price.text)

parsing_barmak()