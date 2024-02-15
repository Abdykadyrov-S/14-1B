from aiogram import Bot, Dispatcher, types, executor
from bs4 import BeautifulSoup
import requests

bot = Bot(token='6330444950:AAGMd4Rha6xfIc5KRw6dko6ooPBmIS8on3M')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет!")

@dp.message_handler(commands='acer')
async def start(message:types.Message):
    await message.answer("Топ ноутбуков от фирмы Acer в магазине Barmak:")
    url = 'https://barmak.store/category/Acer/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")


    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")

@dp.message_handler(commands='Asus')
async def start(message:types.Message):
    await message.answer("Топ ноутбуков от фирмы Asus в магазине Barmak:")
    url = 'https://barmak.store/category/Asus/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    all_laptops_name = soup.find_all('div', class_ = "tp-product-tag-2")
    all_laptops_price = soup.find_all('span', class_ = "tp-product-price-2 new-price")


    for name, price in zip(all_laptops_name, all_laptops_price):
        await message.answer(f"{name.text} - {price.text}")


executor.start_polling(dp)