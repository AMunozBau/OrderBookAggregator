import requests

from Objects.Exchange.IExchangeConnector import BaseExchangeConnector
from Objects.Core.Book import OrderBook


class GeminiConnector(BaseExchangeConnector):
    def get_order_book(self, symbol):
        # Define the base URL and endpoint for Gemini API
        base_url = 'https://api.gemini.com'
        order_book_endpoint = f'/v1/book/{symbol}'
        url = f'{base_url}{order_book_endpoint}?limit_bids=25&limit_asks=25'

        # Make a GET request to the API
        response = requests.get(url)

        # Check if the response is successful (status code 200)
        if response.status_code != 200:
            print(f'Error: {response.status_code}')
            return None

        # Parse the JSON response
        response_json = response.json()

        # Extract ask and bid data from the response
        asks_list = [[asks['price'], asks['amount']] for asks in response_json["asks"]]
        bids_list = [[bids['price'], bids['amount']] for bids in response_json["bids"]]

        # Create an OrderBook object and update it with the retrieved data
        order_book = OrderBook()
        order_book.update_bids(bids_list)
        order_book.update_asks(asks_list)

        # Store the order book in the connector instance
        self.order_book = order_book

    def print_order_book(self):
        # Print the order book information for Gemini. (Mainly for debugging)
        print("\nGEMINI:")
        super().print_order_book()
