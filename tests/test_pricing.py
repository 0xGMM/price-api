import pytest

from price_api.pricing import format_price_list, format_price_response, is_valid_symbol


def test_classic_symbol():
    assert is_valid_symbol("BTC")


def test_empty_symbol():
    assert not is_valid_symbol("")


def test_numeric_symbol():
    assert not is_valid_symbol("BTC1")


def test_format_price_response():
    coin = {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "current_price": 50000}
    result = format_price_response(coin)
    assert result == {"symbol": "btc", "name": "Bitcoin", "price": 50000}


def test_format_price_list():
    price_list = [
        {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "current_price": 50000},
        {"id": "bitcoin", "symbol": "eth", "name": "Ethereum", "current_price": 2000},
    ]

    result_list = format_price_list(price_list)

    assert result_list == [
        {"symbol": "btc", "name": "Bitcoin", "price": 50000},
        {"symbol": "eth", "name": "Ethereum", "price": 2000},
    ]


def test_format_price_response_missing_key():
    coin = {"symbol": "btc", "name": "Bitcoin"}  # pas de current_price
    with pytest.raises(KeyError):
        format_price_response(coin)
