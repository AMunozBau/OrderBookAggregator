import sys

from Objects.Exchange.CoinBase import CoinBaseConnector
from Objects.Exchange.Gemini import GeminiConnector
from Objects.Exchange.Kraken import KrakenConnector

from Utils.Agregator import OrderBookAggegator


def main(target_amount=10, use_kraken_exchange=False):
    # Define the trading symbol for ConBase exchanges
    symbol = 'BTC-USD'

    # Initialize Coinbase connector and get order book
    coinbase_connector = CoinBaseConnector()
    coinbase_connector.get_order_book(symbol)

    # For Gemini exchange, use a different symbol format
    symbol = 'btcusd'
    gemini_connector = GeminiConnector()
    gemini_connector.get_order_book(symbol)

    # If using Kraken exchange, initialize Kraken connector and get order book
    if use_kraken_exchange:
        symbol = 'XXBTZUSD'
        kraken_connector = KrakenConnector()
        kraken_connector.get_order_book(symbol)

        # Initialize OrderBookAggregator with all three exchange order books
        aggregator = OrderBookAggegator(coinbase_connector.order_book, gemini_connector.order_book,
                                        kraken_connector.order_book)
    else:
        # If not using Kraken, initialize OrderBookAggregator without Kraken order book
        aggregator = OrderBookAggegator(coinbase_connector.order_book, gemini_connector.order_book, None)

    # Aggregate the order books
    aggregated_book = aggregator.aggregate()

    buy_limit_orders_dict = aggregated_book.calculate_buy_limit_order_prices(target_amount)
    print(buy_limit_orders_dict)


# Entry point of the script
if __name__ == '__main__':
    # Parse command-line arguments
    arguments = sys.argv

    # Set default values
    use_kraken_exchange = False
    target_amount = 10

    # Check if target_amount is provided as a command-line argument
    if len(arguments) > 1:
        try:
            target_amount = float(arguments[1])
        except ValueError:
            print("Error: Invalid input for target_amount. Using the default value of 10.")

    # Check if use_kraken_exchange is provided as a command-line argument
    if len(arguments) > 2:
        try:
            use_kraken_exchange = arguments[2].lower() in ['true', '1', 't', 'y', 'yes']
        except ValueError:
            print("Error: Invalid input for use_kraken_exchange. Not considering it.")

    # Call the main function with the parsed arguments
    main(target_amount, use_kraken_exchange)
