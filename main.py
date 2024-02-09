from Objects.Exchange.CoinBase import CoinBaseConnector
from Objects.Exchange.Gemini import GeminiConnector
from Objects.Exchange.Kraken import KrakenConnector

from Utils.Agregator import OrderBookAggegator
    
if __name__ == '__main__':
    symbol = 'BTC-USD'
    coinbase_connector = CoinBaseConnector()
    coinbase_connector.GetOrderBook(symbol)

    symbol = 'btcusd'
    gemini_connector = GeminiConnector()
    gemini_connector.GetOrderBook(symbol)

    symbol = 'XXBTZUSD'
    kraken_connector = KrakenConnector()
    kraken_connector.GetOrderBook(symbol)

    aggreator = OrderBookAggegator(coinbase_connector.order_book, gemini_connector.order_book, kraken_connector.order_book)
    agregated_book = aggreator.aggregate()

    target_amount = 10
    average_buy_price, average_sell_price = agregated_book.calculate_average_price(target_amount)
   
    print(f'Average Buy Price for {target_amount} BTC: {average_buy_price:.2f}')
    print(f'Average Sell Price for {target_amount} BTC: {average_sell_price:.2f}')