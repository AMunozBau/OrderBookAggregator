import requests

from Objects.Exchange.IExchangeConnector import BaseExchangeConnector
from Objects.Core.Book import OrderBook

class CoinBaseConnector(BaseExchangeConnector):
    def GetOrderBook(self, symbol):
        base_url = 'https://api.pro.coinbase.com'
        order_book_endpoint = f'/products/{symbol}/book'
        url = f'{base_url}{order_book_endpoint}?level=2'
        response = requests.get(url)

        if response.status_code != 200:
            print(f'Error: {response.status_code}')
            return None            
        
        response_json = response.json()
        asks_list = [[asks[0], asks[1]] for asks in response_json["asks"][:3]]
        bids_list = [[bids[0], bids[1]] for bids in response_json["bids"][:3]]

        order_book = OrderBook()
        order_book.update_bids(bids_list)
        order_book.update_asks(asks_list)

        self.order_book = order_book
    
    def print_order_book(self):
        print("")
        print("COINBASE:")
        super().print_order_book()