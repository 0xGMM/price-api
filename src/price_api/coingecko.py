import httpx

from price_api.constants import url_price_coingecko



def fetch_coin_prices() -> list[dict]:

    response = httpx.get(url_price_coingecko)
    data = response.json()

    return data
