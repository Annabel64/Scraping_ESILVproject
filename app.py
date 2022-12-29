from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def compare_prices():
  prices = {}
  if request.method == 'POST':
    # Get the article name from the form submission
    article = request.form['article']
    
    # Make a request to the Amazon API to get the price
    amazon_url = 'https://www.amazon.com/api/price/article/' + article
    amazon_response = requests.get(amazon_url)
    amazon_price = amazon_response.json()['price']
    
    # Make a request to the Le Dénicheur API to get the price
    denicheur_url = 'https://www.denicheur.com/api/price/article/' + article
    denicheur_response = requests.get(denicheur_url)
    denicheur_price = denicheur_response.json()['price']
    
    # Add the prices to the prices dictionary
    prices['Amazon'] = amazon_price
    prices['Le Dénicheur'] = denicheur_price
  
  return render_template('index.html', prices=prices)

if __name__ == '__main__':
  app.run()
