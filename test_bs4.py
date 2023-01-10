import requests
from bs4 import BeautifulSoup

url = "https://fr.shopping.rakuten.com/search/iphone+12"
html = requests.get(url).text


soup = BeautifulSoup(html, 'html.parser')
prices = soup.find_all(class_="new_product_advertised")
nom=soup.find_all(class_="description_styleTitle_KPO lh-title normal mv0 b di")
img = soup.find(class_="productList_layoutImgGrid_902")


print("prix : ", prices)
print("image : ", img)
print("nom : ", nom)
