class BaseExchangeConnector:
    def GetOrderBook(self, symbol):
        pass

    def print_order_book(self, order_book):
        if order_book:
            for key in order_book:
                if key == "bids":
                    print(key,":", order_book[key][:3])
                elif key == "asks":
                    print(key,":", order_book[key][:3])
                else:
                    print(key,":", order_book[key])