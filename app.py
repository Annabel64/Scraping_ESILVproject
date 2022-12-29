from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def compare_prices():
  prices = {}
  if request.method == 'POST':
    # Get the article name from the form submission
    article = request.form['article']
    
    # Make a request to Amazon and parse the HTML content
    amazon_url = 'https://www.amazon.com/s?k=' + article
    amazon_response = requests.get(amazon_url, verify=False)
    amazon_soup = BeautifulSoup(amazon_response.text, 'html.parser')

    # Extract the prices from the HTML content
    amazon_prices = amazon_soup.find_all(class_='a-price')
    if amazon_prices:
      amazon_price = amazon_prices[0].get_text()
    else:
      amazon_price = None

  
    # Make a request to Le Dénicheur and parse the HTML content
    denicheur_url = 'https://ledenicheur.fr/search?search=' + article
    denicheur_response = requests.get(denicheur_url, verify=False)
    denicheur_soup = BeautifulSoup(denicheur_response.text, 'html.parser')
    
    # Extract the prices from the HTML content
    denicheur_prices = denicheur_soup.find_all(class_="Text--1d9bgzp ilIDIB")
    if denicheur_prices:
      denicheur_monnaie = denicheur_prices[0].text.split('\xa0')[1]
      denicheur_prices = [denicheur_prices[i].text.replace(",", ".") for i in range(len(denicheur_prices))]
      denicheur_prices = [float(price.split('\xa0')[0]) for price in denicheur_prices]
      denicheur_price = denicheur_prices[0]
    else:
      denicheur_price = None
      denicheur_monnaie = None
    
    
    # Add the prices to the prices dictionary
    prices['Amazon'] = amazon_price
    prices['Le Dénicheur'] = str(denicheur_price) + " " + str(denicheur_monnaie)

  
  return render_template('index.html', prices=prices)

if __name__ == '__main__':
  app.run()
