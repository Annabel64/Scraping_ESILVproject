import requests
from bs4 import BeautifulSoup

url = "https://ledenicheur.fr/product.php?p=5683804"
html = requests.get(url).text


soup = BeautifulSoup(html, 'html.parser')
# prices = soup.find_all(class_="Text--1d9bgzp ilIDIB")
# nom=soup.find_all(class_="Text--1d9bgzp bYZpdo titlesmalltext")
# Find class that contains 'FirstImage'
img = soup.find_all('img')
alt = [i for i in img if i.get('alt') == "Apple iPhone 13 5G 4Go RAM 128Go"]
print(alt[0].get('src'))
# price = None
# monnaie = None
# if prices:
#     monnaie = prices[0].text.split('\xa0')[1]
#     prices = [prices[i].text.replace(",", ".") for i in range(len(prices))]
#     prices = [float(price.split('\xa0')[0]) for price in prices]
#     price = prices[0]

# print("prix : ", price)
# print("monnaie : ", monnaie)
# print("image : ", img)
# print("nom : ", nom[0].text)