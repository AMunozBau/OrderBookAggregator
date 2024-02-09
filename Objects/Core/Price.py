class PriceData:
    def __init__(self, price, amount):
        self.price = price
        self.amount = amount 

    def __repr__(self):
        return f"[Price: {self.price} Amount: {self.amount}]"
