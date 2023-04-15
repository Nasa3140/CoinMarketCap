"""
    The function retrieves the latest cryptocurrency listings from the CoinMarketCap API and prints them
    using the pprint module.
"""

# These lines of code are importing necessary modules and classes for making HTTP requests, handling
# exceptions, parsing JSON data using dictionary method, and pretty-printing data. Specifically:
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint

# These lines of code are defining the URL endpoint for the CoinMarketCap API and setting the API key
# to be used for authentication when making requests to the API.
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

API_KEY= "89d87944-6bdd-4151-8c36-78362338cb35"

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
            for currency_data in Data['data']:
                symbol = currency_data['symbol']
                usd_rate = currency_data['quote']['USD']['price']
                price = currency_data['quote']['USD']['price']
                pprint.pprint(f"Symbol: {symbol}, USD rate: {usd_rate}, Price: {price}")
                
        else:
            pprint.pprint("No data available.")
    
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        pprint.pprint(e)


# `if __name__ == "__main__":` is a conditional statement that checks if the current script is being
# run as the main program. If it is, then the `latest_list()` function is called, which retrieves the
# latest cryptocurrency data and prints it using the `pprint` module. After the function is executed,
# the message "Fetched CryptoCurrency data" is printed to indicate that the data has been successfully
# retrieved. This is a common way to structure Python scripts so that they can be imported as modules
# into other scripts without running the main code block.
if __name__ == "__main__":
    latest_list()
    print("Fetched CryptoCurrency data")
    