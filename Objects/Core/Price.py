class PriceData:
    def __init__(self, price, amount, timestamp="", n_orders=""):
        self.price = price
        self.amount = amount 
        self.timestamp = timestamp
        self.n_orders = n_orders

    def __repr__(self):
        return f"[Price: {self.price} Amount: {self.amount} Timestamp: {self.timestamp}, Orders: {self.n_orders}]"
   