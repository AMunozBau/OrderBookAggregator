import requests

from Objects.Exchange.IExchangeConnector import BaseExchangeConnector

class CoinBaseConnector(BaseExchangeConnector):
    def GetOrderBook(self, symbol):
        base_url = 'https://api.pro.coinbase.com'
        order_book_endpoint = f'/products/{symbol}/book'
        url = f'{base_url}{order_book_endpoint}?level=2'
        response = requests.get(url)

        if response.status_code == 200:
            self.order_book = response.json()
            return self.order_book
        else:
            print(f'Error: {response.status_code}')
            return None
    
    def print_order_book(self):
        print("")
        print("COINBASE:")
        super().print_order_book( self.order_book)