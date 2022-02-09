import plotly.graph_objects as go

import json
from datetime import date, datetime

open_prices = []
high_prices = []
dates = []
low_prices = []
close_prices = []

with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        parsed = json.loads(line)
        if 'AAPL' in parsed:
            parsed = parsed['AAPL']
            open_prices += [parsed['o']]
            close_prices += [parsed['c']]
            low_prices += [parsed['l']]
            high_prices += [parsed['h']]
            dates += [datetime.fromtimestamp(parsed['t'])]

fig = go.Figure(data=[go.Candlestick(x=dates,
                open=open_prices,
                high=high_prices,
                low=low_prices,
                close=close_prices)])

fig.show()