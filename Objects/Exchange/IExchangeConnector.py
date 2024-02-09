class BaseExchangeConnector:
    def get_order_book(self, symbol):
        pass

    def print_order_book(self):
        print(self.order_book)
