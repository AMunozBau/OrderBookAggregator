from Objects.Core.Price import PriceData


class OrderBook:
    def __init__(self):
        # Initialize empty lists for asks and bids
        self.asks = []
        self.bids = []

    def __repr__(self):
        # String representation of the order book
        return f"Asks: {self.asks}\nBids: {self.bids}"

    def update_bids(self, bids):
        # Update bids with new data
        # Convert input data to PriceData objects and round values
        self.bids = [PriceData(round(float(price), 2), dict_exchange) for price, dict_exchange in bids]

    def update_asks(self, asks):
        # Update asks with new data
        # Convert input data to PriceData objects and round values
        self.asks = [PriceData(round(float(price), 2), dict_exchange) for price, dict_exchange in asks]

    def calculate_buy_limit_order_prices(self, target_quantity=10.0):
        buy_amount = 0.0
        buy_limit_orders_dict = {}
        for ask_level in self.asks:
            for exchange_name in ask_level.amount_dict.keys():
                if buy_amount + float(ask_level.amount_dict[exchange_name]) > target_quantity:
                    level_amount = target_quantity-buy_amount
                    level_price = ask_level.price
                    if exchange_name in buy_limit_orders_dict:
                        level_list = [level_price, buy_limit_orders_dict[exchange_name][1] + level_amount]
                    else:
                        level_list = [level_price, level_amount]
                    buy_limit_orders_dict[exchange_name] = level_list
                    return buy_limit_orders_dict
                else:
                    level_amount = float(ask_level.amount_dict[exchange_name])
                    level_price = ask_level.price
                    if exchange_name in buy_limit_orders_dict:
                        level_list = [level_price, buy_limit_orders_dict[exchange_name][1] + level_amount]
                    else:
                        level_list = [level_price, level_amount]
                    buy_limit_orders_dict[exchange_name] = level_list
                    buy_amount += level_amount
