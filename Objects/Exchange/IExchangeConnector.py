class BaseExchangeConnector:
    def GetOrderBook(self, symbol):
        pass

    def print_order_book(self):
        print(self.order_book)
        # print("bids: ", self.order_book.bids)