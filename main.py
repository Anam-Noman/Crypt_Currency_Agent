from agents import Agent, Runner, function_tool
import requests
from connection import config

@function_tool
def get_all_coins() -> list:
    url = "https://api.binance.com/api/v3/ticker/price"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return [{"error": "Unable to fetch all coins"}]

@function_tool
def get_coin_by_symbol(symbol: str) -> dict:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Unable to fetch data for {symbol}"}

crypto_agent = Agent(
    name="CryptoAgent",
    instructions="You are a helpful assistant that provides real-time cryptocurrency prices using Binance API.",
    tools=[get_all_coins, get_coin_by_symbol]
)
result = Runner.run_sync(
    crypto_agent,
    "What is the price of DOGE?",
    run_config=config
)
print( result.final_output)
