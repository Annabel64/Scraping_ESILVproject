from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def compare_prices():
  names = {}
  images = {}
  prices = {}
  if request.method == 'POST':
    # Get the article name from the form submission
    article = request.form['article']
    
    # Make a request to Amazon and parse the HTML content
    amazon_url = 'https://www.amazon.com/s?k=' + article
    amazon_response = requests.get(amazon_url, verify=False)
    amazon_soup = BeautifulSoup(amazon_response.text, 'html.parser')

    # Extract the information from the HTML content
    amazon_names = amazon_soup.find_all(class_='a-size-medium a-color-base a-text-normal')
    amazon_images = amazon_soup.find_all(class_='s-image')
    amazon_prices = amazon_soup.find_all(class_='a-price')
    amazon_name = None
    amazon_image = None
    amazon_price = None
    if amazon_names:
      amazon_name = amazon_names[0].text
    if amazon_images:
      amazon_image = amazon_images['src'].text
    if amazon_prices:
      amazon_price = amazon_prices[0].text
      

  
    # Make a request to Le Dénicheur and parse the HTML content
    denicheur_url = 'https://ledenicheur.fr/search?search=' + article
    denicheur_response = requests.get(denicheur_url, verify=False)
    denicheur_soup = BeautifulSoup(denicheur_response.text, 'html.parser')
    
    # Extract the information from the HTML content
    denicheur_prices = denicheur_soup.find_all(class_="Text--1d9bgzp ilIDIB")
    denicheur_names = denicheur_soup.find_all(class_="Text--1d9bgzp bYZpdo titlesmalltext")
    denicheur_images = denicheur_soup.find_all(class_="ImageContainer-sc-4o01vu-2 WqEZk")
    denicheur_name = None
    denicheur_image = None
    denicheur_price = None
    denicheur_monnaie = None
    if denicheur_names:
      denicheur_name = denicheur_names[0].text
    if denicheur_images:
      denicheur_image = denicheur_images['src']
    if denicheur_prices:
      denicheur_monnaie = denicheur_prices[0].text.split('\xa0')[1]
      denicheur_prices = [denicheur_prices[i].text.replace(",", ".") for i in range(len(denicheur_prices))]
      denicheur_prices = [float(price.split('\xa0')[0]) for price in denicheur_prices]
      denicheur_price = denicheur_prices[0]
    
      
    # Add the names to the names dictionary
    names['Amazon'] = amazon_name
    names['Le Dénicheur'] = denicheur_name

    # Add the images to the images dictionary
    images['Amazon'] = amazon_image
    images['Le Dénicheur'] = denicheur_image

    # Add the prices to the prices dictionary
    prices['Amazon'] = amazon_price
    prices['Le Dénicheur'] = str(denicheur_price) + " " + str(denicheur_monnaie)

  
  return render_template('index.html', prices=prices, names=names, images=images)

if __name__ == '__main__':
  app.run()
