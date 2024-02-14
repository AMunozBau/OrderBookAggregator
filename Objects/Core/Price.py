class PriceData:
    def __init__(self, price, amount_dict):
        # Initialize PriceData object with price and amount
        self.price = price
        self.amount_dict = amount_dict   # dictionary like {"EXCHANGE_NAME": amount}

    def __repr__(self):
        # String representation of the PriceData object. (Mainly for debugging)
        return f"[Price: {self.price} Amount: {self.amount_dict}]"
