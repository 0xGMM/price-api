# uv run python -m price_api.main
import uvicorn

from fastapi import FastAPI
from price_api.pricing import format_price_list
from price_api.coingecko import fetch_coin_prices

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/prices")
def prices():
    raw_data = fetch_coin_prices()    
    return format_price_list(raw_data)  


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
