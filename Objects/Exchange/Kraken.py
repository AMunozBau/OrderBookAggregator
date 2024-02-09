import requests
from Objects.Exchange.IExchangeConnector import BaseExchangeConnector
from Objects.Core.Book import OrderBook


class KrakenConnector(BaseExchangeConnector):
    def GetOrderBook(self, symbol):
        base_url = 'https://api.kraken.com'
        url = f'{base_url}/0/public/Depth?pair={symbol}&count=10'
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f'Error: {response.status_code}')
            return None            

        response_json = response.json()["result"][symbol]
        asks_list = [[asks[0], asks[1]] for asks in response_json["asks"][:3]]
        bids_list = [[bids[0], bids[1]] for bids in response_json["bids"][:3]]

        order_book = OrderBook()
        order_book.update_bids(bids_list)
        order_book.update_asks(asks_list)

        self.order_book =  order_book
    
    def print_order_book(self):
        print("")
        print("KRAKEN:")
        super().print_order_book()