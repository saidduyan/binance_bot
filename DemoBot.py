from binance.client import Client
from binance.enums import *
import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import FisherIndicator

# Binance API keys
api_key = 'Lflh9vSjREmj0wEEElwxI3pgnVj6hg88094vj4l9wbDFrQKXKAIcuOixQ3gYo3TX'
api_secret = 'VRbeMzklCFswxGlPnLNfTZ8Y20UjGS87ukZ03tkaki8FPMXcqFvOJbBJaqZRaX1y'

client = Client(api_key, api_secret)

# Fetching historical data
klines = client.futures_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR, limit=100)

df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

# Preprocessing data
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)

# Calculate EMA
df['ema'] = EMAIndicator(close=df['close'], window=20).ema_indicator()

# Calculate Fisher Indicator
df['fisher'] = FisherIndicator(high=df['high'], low=df['low'], close=df['close'], window=9).fisher_transform()

# Implement your strategy based on the Fisher and EMA indicators
# For example:
last_fisher = df['fisher'][-2]
current_fisher = df['fisher'][-1]
last_ema = df['ema'][-2]
current_ema = df['ema'][-1]

if last_fisher < last_ema and current_fisher > current_ema:
    # Implement your buying logic here
    print("Buy signal")
elif last_fisher > last_ema and current_fisher < current_ema:
    # Implement your selling logic here
    print("Sell signal")
else:
    print("No trade signal")

# Implement your trading logic here