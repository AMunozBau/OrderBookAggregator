import sys

from Objects.Exchange.CoinBase import CoinBaseConnector
from Objects.Exchange.Gemini import GeminiConnector
from Objects.Exchange.Kraken import KrakenConnector

from Utils.Agregator import OrderBookAggegator


def main(target_amount=10, use_kraken_exchange=False):
    symbol = 'BTC-USD'
    coinbase_connector = CoinBaseConnector()
    coinbase_connector.GetOrderBook(symbol)

    symbol = 'btcusd'
    gemini_connector = GeminiConnector()
    gemini_connector.GetOrderBook(symbol)

    if use_kraken_exchange:
        symbol = 'XXBTZUSD'
        kraken_connector = KrakenConnector()
        kraken_connector.GetOrderBook(symbol)

        aggreator = OrderBookAggegator(coinbase_connector.order_book, gemini_connector.order_book,
                                       kraken_connector.order_book)
    else:
        aggreator = OrderBookAggegator(coinbase_connector.order_book, gemini_connector.order_book, None)

    agregated_book = aggreator.aggregate()

    average_buy_price, average_sell_price = agregated_book.calculate_average_price(target_amount)

    print(f'Average Buy Price for {target_amount} BTC: {average_buy_price:.2f}')
    print(f'Average Sell Price for {target_amount} BTC: {average_sell_price:.2f}')


if __name__ == '__main__':
    arguments = sys.argv

    use_kraken_exchange = False

    if len(arguments) > 1:
        try:
            target_amount = float(arguments[1])
        except ValueError:
            print("Error: Invalid input for target_amount. Using the default value of 10.")
            target_amount = 10
    elif len(arguments) > 2:
        try:
            use_kraken_exchange = arguments[2].lower() in ['true', '1', 't', 'y', 'yes']
        except ValueError:
            print("Error: Invalid input for use_kraken_exchange. Not considering it.")
            target_amount = 10
    else:
        target_amount = 10

    main(target_amount, use_kraken_exchange)