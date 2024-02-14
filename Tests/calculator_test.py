import pytest

from Objects.Core.Book import OrderBook


def test_calculate_avg_price_1():
    # Create an OrderBook with sample bids and asks
    aggregated_book = OrderBook()
    aggregated_book.update_asks([['45500', {'COIN': '0.2', 'GEMINI': '0.2', 'KRAKEN': '0.2'}],
                                 ['45600', {'COIN': '0.25', 'GEMINI': '0.25', 'KRAKEN': '0.25'}],
                                 ['45700', {'COIN': '0.3', 'GEMINI': '0.3', 'KRAKEN': '0.3'}],
                                 ['45800', {'COIN': '0.4', 'KRAKEN': '0.5'}],
                                 ['45900', {'COIN': '0.5'}]])
    # Test various target quantities and expected average buy/sell prices
    assert aggregated_book.calculate_buy_limit_order_prices(0.01) == {'COIN': [45500.0, 0.01]}
    assert aggregated_book.calculate_buy_limit_order_prices(0.1) == {'COIN': [45500.0, 0.1]}
    assert aggregated_book.calculate_buy_limit_order_prices(0.2) == {'COIN': [45500.0, 0.2], 'GEMINI': [45500.0, 0.0]}
    assert aggregated_book.calculate_buy_limit_order_prices(0.3) == pytest.approx(
        {'COIN': [45500.0, 0.2], 'GEMINI': [45500.0, 0.09999999999999998]})
    assert aggregated_book.calculate_buy_limit_order_prices(0.4) == {'COIN': [45500.0, 0.2],
                                                                     'GEMINI': [45500.0, 0.2], 'KRAKEN': [45500.0, 0.0]}
    assert aggregated_book.calculate_buy_limit_order_prices(0.5) == pytest.approx(
        {'COIN': [45500.0, 0.2], 'GEMINI': [45500.0, 0.2], 'KRAKEN': [45500.0, 0.09999999999999998]})
    assert aggregated_book.calculate_buy_limit_order_prices(0.6) == pytest.approx(
        {'COIN': [45500.0, 0.2], 'GEMINI': [45500.0, 0.2], 'KRAKEN': [45500.0, 0.19999999999999996]})
