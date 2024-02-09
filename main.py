from Objects.Exchange.CoinBase import CoinBaseConnector
from Objects.Exchange.Gemini import GeminiConnector
from Objects.Exchange.Kraken import KrakenConnector

from Utils.Agregator import OrderBookAggegator


    
if __name__ == '__main__':
    symbol = 'BTC-USD'
    coinbase_connector = CoinBaseConnector()
    coinbase_connector.GetOrderBook(symbol)
    coinbase_connector.print_order_book()


    symbol = 'btcusd'
    gemini_connector = GeminiConnector()
    gemini_connector.GetOrderBook(symbol)
    gemini_connector.print_order_book()


    symbol = 'XXBTZUSD'
    kraken_connector = KrakenConnector()
    kraken_connector.GetOrderBook(symbol)
    kraken_connector.print_order_book()

    aggreator = OrderBookAggegator(coinbase_connector.order_book, gemini_connector.order_book, kraken_connector.order_book)
    agregated_book = aggreator.aggregate()
    print("")
    print("AGGREGATED:")
    print(agregated_book)