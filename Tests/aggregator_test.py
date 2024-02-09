import pytest

from Objects.Core.Book import OrderBook

from Utils.Agregator import OrderBookAggegator

FLOAT_TOLERANCE = 1e-10

def assert_order_books_equal(book1, book2):
    assert len(book1.asks) == len(book2.asks)
    for entry1, entry2 in zip(book1.asks, book2.asks):
        assert abs(entry1.price - entry2.price) < FLOAT_TOLERANCE
        assert abs(entry1.amount - entry2.amount) < FLOAT_TOLERANCE

    assert len(book1.bids) == len(book2.bids)
    for entry1, entry2 in zip(book1.bids, book2.bids):
        assert abs(entry1.price - entry2.price) < FLOAT_TOLERANCE
        assert abs(entry1.amount - entry2.amount) < FLOAT_TOLERANCE

@pytest.fixture
def sample_order_books_same_size():
    order_book_1 = OrderBook()
    order_book_1.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3']])
    order_book_1.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3']])

    order_book_2 = OrderBook()
    order_book_2.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3']])
    order_book_2.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3']])

    order_book_3 = OrderBook()
    order_book_3.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3']])
    order_book_3.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3']])

    expcted_book = OrderBook()
    expcted_book.update_bids([['45000', '0.3'], ['44900', '0.6'], ['44800', '0.9']])
    expcted_book.update_asks([['45500', '0.6'], ['45600', '0.75'], ['45700', '0.9']])

    return order_book_1, order_book_2, order_book_3, expcted_book

def test_aggregate_books_same_size(sample_order_books_same_size):
    order_book_1, order_book_2, order_book_3, expcted_book = sample_order_books_same_size

    aggreator = OrderBookAggegator(order_book_1, order_book_2, order_book_3)
    aggregated_book = aggreator.aggregate()    

    assert_order_books_equal(aggregated_book, expcted_book)



@pytest.fixture
def sample_order_books_different_size():
    order_book_1 = OrderBook()
    order_book_1.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3'], ['44700', '0.5'], ['44600', '0.8']])
    order_book_1.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3'], ['45800', '0.4'], ['45900', '0.5']])

    order_book_2 = OrderBook()
    order_book_2.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3']])
    order_book_2.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3']])

    order_book_3 = OrderBook()
    order_book_3.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3'], ['44600', '0.4']])
    order_book_3.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3'], ['45800', '0.5']])

    expcted_book = OrderBook()
    expcted_book.update_bids([['45000', '0.3'], ['44900', '0.6'], ['44800', '0.9'], ['44700', '0.5'], ['44600', '1.2']])
    expcted_book.update_asks([['45500', '0.6'], ['45600', '0.75'], ['45700', '0.9'], ['45800', '0.9'], ['45900', '0.5']])

    return order_book_1, order_book_2, order_book_3, expcted_book

def test_aggregate_books_different_size(sample_order_books_different_size):
    order_book_1, order_book_2, order_book_3, expcted_book = sample_order_books_different_size

    aggreator = OrderBookAggegator(order_book_1, order_book_2, order_book_3)
    aggregated_book = aggreator.aggregate()    

    assert_order_books_equal(aggregated_book, expcted_book)

@pytest.fixture
def sample_order_2_books():
    order_book_1 = OrderBook()
    order_book_1.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3'], ['44700', '0.5'], ['44600', '0.8']])
    order_book_1.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3'], ['45800', '0.4'], ['45900', '0.5']])

    order_book_2 = OrderBook()
    order_book_2.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3']])
    order_book_2.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3']])

    expcted_book = OrderBook()
    expcted_book.update_bids([['45000', '0.2'], ['44900', '0.4'], ['44800', '0.6'], ['44700', '0.5'], ['44600', '0.8']])
    expcted_book.update_asks([['45500', '0.4'], ['45600', '0.5'], ['45700', '0.6'], ['45800', '0.4'], ['45900', '0.5']])

    return order_book_1, order_book_2, expcted_book

def test_aggregate_2_books(sample_order_2_books):
    order_book_1, order_book_2, expcted_book = sample_order_2_books

    aggreator = OrderBookAggegator(order_book_1, order_book_2, None)
    aggregated_book = aggreator.aggregate()    

    assert_order_books_equal(aggregated_book, expcted_book)
