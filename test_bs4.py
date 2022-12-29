import requests
from bs4 import BeautifulSoup

url = "https://www.leboncoin.fr/recherche?text=iphone%2012"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
prices = soup.find_all(class_='_137P- _3j0OU P4PEa')
print(prices) #si affiche liste vide = pas bon signe
