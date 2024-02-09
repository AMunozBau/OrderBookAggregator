import requests
from Objects.Exchange.IExchangeConnector import BaseExchangeConnector

class KrakenConnector(BaseExchangeConnector):
    def GetOrderBook(self, symbol):
        base_url = 'https://api.kraken.com'
        url = f'{base_url}/0/public/Depth?pair={symbol}&count=10'
        response = requests.get(url)

        if response.status_code == 200:
            self.order_book = response.json()['result'][symbol]
            return  self.order_book
        else:
            print(f'Error: {response.status_code}')
            return None
    
    def print_order_book(self):
        print("")
        print("KRAKEN:")
        super().print_order_book( self.order_book)