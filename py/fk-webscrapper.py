from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome(executable_path='C:/Users/darsa/chromedriver/chromedriver.exe')
products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product
driver.get("https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/fully-automatic-front-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Fully%20Automatic%20Front%20Load")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
# print(soup.encode("utf-8"))
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class': 'hGSR34'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
driver.quit()
