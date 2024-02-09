from Objects.Core.Price import PriceData

class OrderBook:
    def __init__(self):
        self.asks = []
        self.bids = []

    def update_bids(self, bids):
        self.bids = [PriceData(price, amount) for price, amount in bids]

    def update_asks(self, asks):
        self.asks = [PriceData(price, amount) for price, amount in asks]

    def __repr__(self):
        return f"Asks: {self.asks}\nBids: {self.bids}"
        # return f"Asks: {self.asks}"
   