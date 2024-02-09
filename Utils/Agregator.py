from Objects.Core.Book import OrderBook
from Objects.Core.Price import PriceData


class OrderBookAggegator:
    def __init__(self, coinbase_book, gemini_book, kraken_book):
        self.coinbase_book = coinbase_book
        self.gemini_book = gemini_book
        self.kraken_book = kraken_book

    def aggregate(self):
        aggregated_order_book = OrderBook()

        # Aggregate bids
        books_bids = self.coinbase_book.bids + self.gemini_book.bids
        if self.kraken_book:
            books_bids = self.coinbase_book.bids + self.gemini_book.bids + self.kraken_book.bids
        aggregated_bids = {}
        for entry in books_bids:
            if entry.price in aggregated_bids:
                aggregated_bids[entry.price] += entry.amount
            else:
                aggregated_bids[entry.price] = entry.amount

        aggregated_order_book.bids = [PriceData(price, aggregated_bids[price]) for price in sorted(aggregated_bids.keys(), reverse=True)]

        # Aggregate asks
        books_asks = self.coinbase_book.asks + self.gemini_book.asks
        if self.kraken_book:
            books_asks = self.coinbase_book.asks + self.gemini_book.asks + self.kraken_book.asks
        aggregated_asks = {}
        for entry in books_asks:
            if entry.price in aggregated_asks:
                aggregated_asks[entry.price] += entry.amount
            else:
                aggregated_asks[entry.price] = entry.amount

        aggregated_order_book.asks = [PriceData(price, aggregated_asks[price]) for price in sorted(aggregated_asks.keys())]

        return aggregated_order_book
