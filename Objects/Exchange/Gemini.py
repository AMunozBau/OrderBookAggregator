import requests
import json

from Objects.Exchange.IExchangeConnector import BaseExchangeConnector

class GeminiConnector(BaseExchangeConnector):
    def GetOrderBook(self, symbol):
        base_url = 'https://api.gemini.com'
        order_book_endpoint = f'/v1/book/{symbol}'
        url = f'{base_url}{order_book_endpoint}?limit_bids=10&limit_asks=10'
        response = requests.get(url)

        if response.status_code == 200:
            self.order_book = response.json()
            return self.order_book
        else:
            print(f'Error: {response.status_code}')
            return None
        
    def print_order_book(self):
        print("")
        print("GEMINI:")
        super().print_order_book(self.order_book)