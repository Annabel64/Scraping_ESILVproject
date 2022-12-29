# Scraping_ESILVproject
How can I minimize the price of shopping for high-end products on shopping sites (such as Amazon and Le Dénicheur), by comparing the offers on these sites?


## Overall idea of our project
### Project objectives
Our objective will be to create a simple application for comparing the selling prices of a given product between two reseller sites, for example Amazon and PriceSpy. Our application will allow you to enter the name of a product, and will scrape the data from each of these sites to locate the site on which the product is the cheapest. We would like to focus on high-end products (computers, fridges, etc.) so that we have to manage product warranties. Our application will therefore take into account the prices of guarantees (duration, price, conditions, etc.), deliveries, and will be able to display delivery times.
-> For example, if you want to buy an iphone, our application will compare the selling price + delivery on amazon and the price finder to return the most economical site to the user as well as the price detail.

### Problem
How to minimize the price of purchases of high-end products on resale sites (such as Amazon and Le Dénicheur), by comparing the offers on these sites?
-> We would leave to start, on Amazon and Le Dénicheur.


## Sites that will interest us

Our project will cross-check data from two reseller/vendor sites. We will choose these two sites among: Amazon, Rakuten, Le Dénicheur... Here are descriptions of the sites that interest us:
### Amazon
Link: https://www.amazon.fr/
Amazon is a mail-order e-commerce company based in Seattle, Washington. All sales transactions are processed electronically only.
The majority of items on Amazon are resale and are also present on the product's brand site.
-> For example, the Samsung brand may decide to sell their televisions on their Samsung site but also on Amazon to reach a wider audience.

### Rakuten
Link: https://fr.shopping.rakuten.com/
Rakuten is a Japanese e-commerce and online retail company based in Tokyo. Similar to Amazon, Rakuten resells items.

### Le Dénicheur
Link: https://ledenicheur.fr/
Le Dénicheur is a price and product comparison service. The goal is to help customers make the best purchasing decisions.
Information about referenced products is normally updated three to five times a day. The information is obtained via the merchants themselves or by an automatic online scanner of the merchant sites.


## Technical aspects of the project

### Tools to use
The libraries to use are:
-Request
- Bs4
- Celenium (to interact with, but hassle)
We want to code in python and will likely work with vscode and github on a python notebook (to allow for cleaner code segmentation).

### Project stages
The main stages of the project are:
- Successfully do it by hand
- Automate scraping
- Create the interface on which the user will use our technology

### The final render
In addition to the report and the presentation, we would like our technical rendering to be an application or a simplified web interface, allowing to take as input:
- The name of a product
- Or a list of products
- Or the photo of a product (bonus)
The application would return the expected result (the most economical site as well as the price detail). We could also, for example, add filtering options to the web interface, to target certain suppliers, set a minimum price, etc.



## Conclusion
In addition to being efficient and practical, our project brings real added value. Price comparison sites are multiplying, they allow significant savings to be made while being much more precise than a traditional search engine.
Our project constitutes a first version of what could be a much more global price comparator, bringing together several dozen sites (Amazon, Rakuten, le dénicheur, Ebay, Fnac, Darty, etc.).
