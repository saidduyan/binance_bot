import time
from binance.client import Client

# Binance API keys
api_key = 'Lflh9vSjREmj0wEEElwxI3pgnVj6hg88094vj4l9wbDFrQKXKAIcuOixQ3gYo3TX'
api_secret = 'VRbeMzklCFswxGlPnLNfTZ8Y20UjGS87ukZ03tkaki8FPMXcqFvOJbBJaqZRaX1y'

client = Client(api_key, api_secret)

while True:
    try:
        # Fetch the current price of BTC
        btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
        print(f"Current BTC price: {btc_price['price']}")
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(10)  # Sleep for 10 seconds before fetching the price again
