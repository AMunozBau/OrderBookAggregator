import pytest

from Objects.Core.Book import OrderBook

from Utils.Agregator import OrderBookAggegator

FLOAT_TOLERANCE = 1e-10


# Helper function to assert equality of order books
def assert_order_books_equal(book1, book2):
    assert len(book1.asks) == len(book2.asks)
    for entry1, entry2 in zip(book1.asks, book2.asks):
        assert abs(entry1.price - entry2.price) < FLOAT_TOLERANCE
        assert entry1.amount_dict == entry2.amount_dict

    assert len(book1.bids) == len(book2.bids)
    for entry1, entry2 in zip(book1.bids, book2.bids):
        assert abs(entry1.price - entry2.price) < FLOAT_TOLERANCE
        assert entry1.amount_dict == entry2.amount_dict


# Fixture for sample order books with the same depth
@pytest.fixture
def sample_order_books_same_size():
    order_book_1 = OrderBook()
    order_book_1.update_bids([['45000', {"COIN": '0.1'}], ['44900', {"COIN": '0.2'}], ['44800', {"COIN": '0.3'}]])
    order_book_1.update_asks([['45500', {"COIN": '0.2'}], ['45600', {"COIN": '0.25'}], ['45700', {"COIN": '0.3'}]])

    order_book_2 = OrderBook()
    order_book_2.update_bids([['45000', {"GEMINI": '0.1'}], ['44900', {"GEMINI": '0.2'}], ['44800', {"GEMINI": '0.3'}]])
    order_book_2.update_asks([['45500', {"GEMINI": '0.2'}], ['45600', {"GEMINI": '0.25'}], ['45700', {"GEMINI": '0.3'}]])

    order_book_3 = OrderBook()
    order_book_3.update_bids([['45000', {"KRAKEN": '0.1'}], ['44900', {"KRAKEN": '0.2'}], ['44800', {"KRAKEN": '0.3'}]])
    order_book_3.update_asks([['45500', {"KRAKEN": '0.2'}], ['45600', {"KRAKEN": '0.25'}], ['45700', {"KRAKEN": '0.3'}]])

    expcted_book = OrderBook()
    expcted_book.update_bids([['45000', {'COIN': '0.1', 'GEMINI': '0.1', 'KRAKEN': '0.1'}],
                              ['44900', {'COIN': '0.2', 'GEMINI': '0.2', 'KRAKEN': '0.2'}],
                              ['44800', {'COIN': '0.3', 'GEMINI': '0.3', 'KRAKEN': '0.3'}]])
    expcted_book.update_asks([['45500', {'COIN': '0.2', 'GEMINI': '0.2', 'KRAKEN': '0.2'}],
                              ['45600', {'COIN': '0.25', 'GEMINI': '0.25', 'KRAKEN': '0.25'}],
                              ['45700', {'COIN': '0.3', 'GEMINI': '0.3', 'KRAKEN': '0.3'}]])

    return order_book_1, order_book_2, order_book_3, expcted_book


# Test for aggregating order books with the same size
def test_aggregate_books_same_size(sample_order_books_same_size):
    order_book_1, order_book_2, order_book_3, expcted_book = sample_order_books_same_size

    aggreator = OrderBookAggegator(order_book_1, order_book_2, order_book_3)
    aggregated_book = aggreator.aggregate()

    assert_order_books_equal(aggregated_book, expcted_book)


# Fixture for sample order books with different sizes
@pytest.fixture
def sample_order_books_different_size():
    order_book_1 = OrderBook()
    order_book_1.update_bids([['45000', {"COIN": '0.1'}], ['44900', {"COIN": '0.2'}], ['44800', {"COIN": '0.3'}],
                              ['44700', {"COIN": '0.5'}], ['44600', {"COIN": '0.8'}]])
    order_book_1.update_asks([['45500', {"COIN": '0.2'}], ['45600', {"COIN": '0.25'}], ['45700', {"COIN": '0.3'}],
                              ['45800', {"COIN": '0.4'}], ['45900', {"COIN": '0.5'}]])

    order_book_2 = OrderBook()
    order_book_2.update_bids([['45000', {"GEMINI": '0.1'}], ['44900', {"GEMINI": '0.2'}], ['44800', {"GEMINI": '0.3'}]])
    order_book_2.update_asks([['45500', {"GEMINI": '0.2'}], ['45600', {"GEMINI": '0.25'}], ['45700', {"GEMINI": '0.3'}]])

    order_book_3 = OrderBook()
    order_book_3.update_bids([['45000', {"KRAKEN": '0.1'}], ['44900', {"KRAKEN": '0.2'}], ['44800', {"KRAKEN": '0.3'}],
                              ['44600', {"KRAKEN": '0.4'}]])
    order_book_3.update_asks([['45500', {"KRAKEN": '0.2'}], ['45600', {"KRAKEN": '0.25'}], ['45700', {"KRAKEN": '0.3'}],
                              ['45800', {"KRAKEN": '0.5'}]])

    expcted_book = OrderBook()
    expcted_book.update_bids([['45000', {'COIN': '0.1', 'GEMINI': '0.1', 'KRAKEN': '0.1'}],
                              ['44900', {'COIN': '0.2', 'GEMINI': '0.2', 'KRAKEN': '0.2'}],
                              ['44800', {'COIN': '0.3', 'GEMINI': '0.3', 'KRAKEN': '0.3'}],
                              ['44700', {'COIN': '0.5'}],
                              ['44600', {'COIN': '0.8', 'KRAKEN': '0.4'}]])
    expcted_book.update_asks([['45500', {'COIN': '0.2', 'GEMINI': '0.2', 'KRAKEN': '0.2'}],
                              ['45600', {'COIN': '0.25', 'GEMINI': '0.25', 'KRAKEN': '0.25'}],
                              ['45700', {'COIN': '0.3', 'GEMINI': '0.3', 'KRAKEN': '0.3'}],
                              ['45800', {'COIN': '0.4', 'KRAKEN': '0.5'}],
                              ['45900', {'COIN': '0.5'}]])

    return order_book_1, order_book_2, order_book_3, expcted_book


# Test for aggregating order books with different sizes
def test_aggregate_books_different_size(sample_order_books_different_size):
    order_book_1, order_book_2, order_book_3, expcted_book = sample_order_books_different_size

    aggreator = OrderBookAggegator(order_book_1, order_book_2, order_book_3)
    aggregated_book = aggreator.aggregate()

    assert_order_books_equal(aggregated_book, expcted_book)


# Fixture for sample order books with only two books
@pytest.fixture
def sample_order_2_books():
    order_book_1 = OrderBook()
    order_book_1.update_bids([['45000', {"COIN": '0.1'}], ['44900', {"COIN": '0.2'}], ['44800', {"COIN": '0.3'}],
                              ['44700', {"COIN": '0.5'}], ['44600', {"COIN": '0.8'}]])
    order_book_1.update_asks([['45500', {"COIN": '0.2'}], ['45600', {"COIN": '0.25'}], ['45700', {"COIN": '0.3'}],
                              ['45800', {"COIN": '0.4'}], ['45900', {"COIN": '0.5'}]])

    order_book_2 = OrderBook()
    order_book_2.update_bids([['45000', {"GEMINI": '0.1'}], ['44900', {"GEMINI": '0.2'}], ['44800', {"GEMINI": '0.3'}]])
    order_book_2.update_asks([['45500', {"GEMINI": '0.2'}], ['45600', {"GEMINI": '0.25'}], ['45700', {"GEMINI": '0.3'}]])

    expcted_book = OrderBook()
    expcted_book.update_bids([['45000', {'COIN': '0.1', 'GEMINI': '0.1'}],
                              ['44900', {'COIN': '0.2', 'GEMINI': '0.2'}],
                              ['44800', {'COIN': '0.3', 'GEMINI': '0.3'}],
                              ['44700', {'COIN': '0.5'}],
                              ['44600', {'COIN': '0.8'}]])
    expcted_book.update_asks([['45500', {'COIN': '0.2', 'GEMINI': '0.2'}],
                              ['45600', {'COIN': '0.25', 'GEMINI': '0.25'}],
                              ['45700', {'COIN': '0.3', 'GEMINI': '0.3'}],
                              ['45800', {'COIN': '0.4'}],
                              ['45900', {'COIN': '0.5'}]])

    return order_book_1, order_book_2, expcted_book


# Test for aggregating only two order books
def test_aggregate_2_books(sample_order_2_books):
    order_book_1, order_book_2, expcted_book = sample_order_2_books

    aggreator = OrderBookAggegator(order_book_1, order_book_2, None)
    aggregated_book = aggreator.aggregate()

    assert_order_books_equal(aggregated_book, expcted_book)
