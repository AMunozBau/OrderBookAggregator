from Objects.Core.Price import PriceData


class OrderBook:
    def __init__(self):
        self.asks = []
        self.bids = []

    def __repr__(self):
        return f"Asks: {self.asks}\nBids: {self.bids}"

    def update_bids(self, bids):
        self.bids = [PriceData(round(float(price), 2), round(float(amount), 7)) for price, amount in bids]

    def update_asks(self, asks):
        self.asks = [PriceData(round(float(price), 2), round(float(amount), 7)) for price, amount in asks]

    def calculate_average_price(order_book, target_quantity=10.0):
        def calculate_weighted_average(entries):
            total_price = sum(entry.price * entry.amount for entry in entries)
            total_quantity = sum(entry.amount for entry in entries)
            return total_price / total_quantity if total_quantity != 0 else 0.0

        buy_amount = 0.0
        buy_fills = []
        for ask_level in order_book.asks:
            if buy_amount + ask_level.amount > target_quantity:
                fill = PriceData(ask_level.price, target_quantity-buy_amount)
                buy_fills.append(fill)
                buy_amount += target_quantity-buy_amount
                break
            else:
                buy_fills.append(ask_level)
                buy_amount += ask_level.amount

        sell_amount = 0.0
        sell_fills = []
        for bid_level in order_book.bids:
            if sell_amount + bid_level.amount > target_quantity:
                fill = PriceData(bid_level.price, target_quantity-sell_amount)
                sell_fills.append(fill)
                sell_amount += target_quantity-sell_amount
                break
            else:
                sell_fills.append(bid_level)
                sell_amount += bid_level.amount

        average_buy_price = calculate_weighted_average(buy_fills)
        average_sell_price = calculate_weighted_average(sell_fills)

        return average_buy_price, average_sell_price
