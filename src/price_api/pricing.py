


def is_valid_symbol(symbol:str) -> bool:

    if not symbol:
        return False

    return symbol.isalpha()

def format_price_response(coin:dict) -> dict:

    result : dict = {}
    result["symbol"] = coin["symbol"]
    result["name"] = coin["name"]
    result["price"] = coin["current_price"]

    return result

        

def format_price_list(coins: list[dict]) -> list[dict]:

    coins_list_formatted : list = []
    for coin in coins:
        result = format_price_response(coin)
        coins_list_formatted.append(result)

    return coins_list_formatted