import requests
from bs4 import BeautifulSoup

url = "https://ledenicheur.fr/search?search=iphone%2012"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
prices = soup.find_all(class_="Text--1d9bgzp ilIDIB")
nom=soup.find_all(class_="Text--1d9bgzp bYZpdo titlesmalltext")
img = soup.find(class_="ImageContainer-sc-4o01vu-2 WqEZk")
price = None
monnaie = None
if prices:
    monnaie = prices[0].text.split('\xa0')[1]
    prices = [prices[i].text.replace(",", ".") for i in range(len(prices))]
    prices = [float(price.split('\xa0')[0]) for price in prices]
    price = prices[0]



print("prix : ", price)
print("monnaie : ", monnaie)
print("image : ", img)
print("nom : ", nom[0].text)
