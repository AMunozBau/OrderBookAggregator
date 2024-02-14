import requests

from Objects.Exchange.IExchangeConnector import BaseExchangeConnector
from Objects.Core.Book import OrderBook


class CoinBaseConnector(BaseExchangeConnector):
    def get_order_book(self, symbol):
        # Define the base URL and endpoint for Coinbase API
        base_url = 'https://api.pro.coinbase.com'
        order_book_endpoint = f'/products/{symbol}/book'
        url = f'{base_url}{order_book_endpoint}?level=2'

        # Make a GET request to the API
        response = requests.get(url)

        # Check if the response is successful (status code 200)
        if response.status_code != 200:
            print(f'Error: {response.status_code}')
            return None

        # Parse the JSON response
        response_json = response.json()

        # Extract ask and bid data from the response
        asks_list = [[asks[0], {"COIN": asks[1]}] for asks in response_json["asks"]]
        bids_list = [[bids[0], {"COIN": bids[1]}] for bids in response_json["bids"]]

        # Create an OrderBook object and update it with the retrieved data
        order_book = OrderBook()
        order_book.update_bids(bids_list)
        order_book.update_asks(asks_list)

        # Store the order book in the connector instance
        self.order_book = order_book

    def print_order_book(self):
        # Print the order book information for Coinbase. (Mainly for debugging)
        print("\nCOINBASE:")
        super().print_order_book()
