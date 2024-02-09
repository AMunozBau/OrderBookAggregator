class PriceData:
    def __init__(self, price, amount):
        # Initialize PriceData object with price and amount
        self.price = price
        self.amount = amount

    def __repr__(self):
        # String representation of the PriceData object. (Mainly for debugging)
        return f"[Price: {self.price} Amount: {self.amount}]"
