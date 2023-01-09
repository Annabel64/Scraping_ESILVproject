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
    
    # Make a request to amazon and parse the HTML content
    amazon_url = 'https://www.amazon.fr/s?k=' + article
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
      amazon_name = None
    if amazon_images:
      amazon_image = None
    if amazon_prices:
      amazon_price = None

    # Make a request to LDLC and parse the HTML content
    backMarket_url = 'https://www.backmarket.fr/fr-fr/search?q=' + article+"/"
    backMarket_response = requests.get(backMarket_url, verify=False)
    backMarket_soup = BeautifulSoup(backMarket_response.text, 'html.parser')

    # Extract the information from the HTML content
    backMarket_names = backMarket_soup.find_all(class_="body-1-bold duration-200 line-clamp-1 md:mb-1 md:mt-0 mt-1 normal-case overflow-ellipsis overflow-hidden text-black transition-all")
    backMarket_images = backMarket_soup.find_all(class_="flex-shrink-0 md:h-[13.8rem] md:mx-0 md:my-4 md:relative md:w-full mr-4")
    backMarket_prices = backMarket_soup.find_all(class_="body-2-bold text-black")
    backMarket_name = None
    backMarket_image = None
    backMarket_price = None
    if backMarket_names:
      backMarket_name = backMarket_names[0].text.replace(" ","").replace("\n"," ")
    if backMarket_images:
      backMarket_image = None
    if backMarket_prices:
      backMarket_price = backMarket_prices[0].text.replace(" ","").replace("\n"," ")
      

  
    # Make a request to Le Dénicheur and parse the HTML content
    denicheur_url = 'https://ledenicheur.fr/search?search=' + article
    denicheur_response = requests.get(denicheur_url, verify=False)
    denicheur_soup = BeautifulSoup(denicheur_response.text, 'html.parser')
    
    # Extract the information from the HTML content
    denicheur_prices = denicheur_soup.find_all(class_="Text--1g7udhx dACZCW")
    denicheur_names = denicheur_soup.find_all(class_="Text--1g7udhx bzdbPv titlesmalltext")
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
      denicheur_price = denicheur_prices[0].text


    # Make a request to LDLC and parse the HTML content
    ldlc_url = 'https://www.ldlc.com/recherche/' + article+"/"
    ldlc_response = requests.get(ldlc_url, verify=False)
    ldlc_soup = BeautifulSoup(ldlc_response.text, 'html.parser')
    
    # Extract the information from the HTML content
    ldlc_prices = ldlc_soup.find_all(class_="price")
    ldlc_names = ldlc_soup.find_all(class_="title-3")
    ldlc_images = ldlc_soup.find_all(class_="pic")
    ldlc_name = None
    ldlc_image = None
    ldlc_price = None
    if ldlc_names:
      ldlc_name = ldlc_names[0].text
    if ldlc_images:
      ldlc_image = None
    if ldlc_prices:
      ldlc_price = ldlc_prices[0].text
    
      
    # Add the names to the names dictionary
    names['Amazon'] = amazon_name
    names['Back Market'] = backMarket_name
    names['Le Dénicheur'] = denicheur_name
    names['LDLC'] = ldlc_name

    # Add the images to the images dictionary
    images['Amazon'] = amazon_image
    images['Back Market'] = backMarket_image
    images['Le Dénicheur'] = denicheur_image
    images['LDLC'] = ldlc_image

    # Add the prices to the prices dictionary
    prices['Amazon'] = amazon_price
    prices['Back Market'] = backMarket_price
    prices['Le Dénicheur'] = denicheur_price
    prices['LDLC'] = ldlc_price

  
  return render_template('index.html', prices=prices, names=names, images=images)

if __name__ == '__main__':
  app.run()
