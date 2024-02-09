import requests
import json

from Objects.Exchange.IExchangeConnector import BaseExchangeConnector
from Objects.Core.Book import OrderBook

class GeminiConnector(BaseExchangeConnector):
    def GetOrderBook(self, symbol):
        base_url = 'https://api.gemini.com'
        order_book_endpoint = f'/v1/book/{symbol}'
        url = f'{base_url}{order_book_endpoint}?limit_bids=10&limit_asks=10'
        response = requests.get(url)

        if response.status_code != 200:
            print(f'Error: {response.status_code}')
            return None            
        
        response_json = response.json()
        asks_list = [[asks['price'], asks['amount']] for asks in response_json["asks"]]
        bids_list = [[bids['price'], bids['amount']] for bids in response_json["bids"]]

        order_book = OrderBook()
        order_book.update_bids(bids_list)
        order_book.update_asks(asks_list)

        self.order_book = order_book
        
    def print_order_book(self):
        print("")
        print("GEMINI:")
        super().print_order_book()