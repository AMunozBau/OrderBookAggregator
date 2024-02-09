import pytest

from Objects.Core.Book import OrderBook


def test_calculate_avg_price_1():
    aggregated_book = OrderBook()
    aggregated_book.update_bids([['45000', '0.1'], ['44900', '0.2'], ['44800', '0.3']])
    aggregated_book.update_asks([['45500', '0.2'], ['45600', '0.25'], ['45700', '0.3']])

    assert aggregated_book.calculate_average_price(0.01) == (45500.0, 45000.0)
    assert aggregated_book.calculate_average_price(0.1) == (45500.0, 45000.0)
    assert aggregated_book.calculate_average_price(0.2) == (45500, 44950.0)
    assert aggregated_book.calculate_average_price(0.3) == pytest.approx((45533.33, 44933.33))
    assert aggregated_book.calculate_average_price(0.4) == (45550.0, 44900.0)
    assert aggregated_book.calculate_average_price(0.5) == (45570.0, 44880.0)
    assert aggregated_book.calculate_average_price(0.6) == pytest.approx((45591.66, 44866.66))




