"""
    The function retrieves the latest cryptocurrency listings from the CoinMarketCap API and prints them
    using the pprint module.
"""

# These lines of code are importing necessary modules and classes for making HTTP requests, handling
# exceptions, parsing JSON data, and pretty-printing data using List method. Specifically:
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint

# These lines of code are defining the URL endpoint for the CoinMarketCap API and setting the API key
# to be used for authentication when making requests to the API.
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

API_KEY= "Your API_KEY"

def latest_list():
    """
    The function retrieves the latest cryptocurrency data for a specified limit and converts it to USD.
    """

    parameters = {
    # 'symbol':'BTC',
    # 'start':'1',
    'limit':'5',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
    }

    session = Session()
    session.headers.update(headers)


    # Json = requests.get(url, params=parameters, headers=headers).json()
    
    try:
        response = session.get(url, params=parameters, headers=headers)
        Data= json.loads(response.text)
        if len(Data) > 0:
            list=[]
            for currency_data in Data['data']:
                symbol = currency_data['symbol']
                usd_rate = currency_data['quote']['USD']['price']
                price = currency_data['quote']['USD']['price']
                list.append([symbol, usd_rate, price])
                for currency in list:
                    pprint.pprint(currency)

        else:
            pprint.pprint("No data available.")
    
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        pprint.pprint(e)



if __name__ == "__main__":
    latest_list()
    print("Fetching CryptoCurrency data")
    
