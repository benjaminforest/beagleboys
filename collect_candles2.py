from shared import shared
import json
import pandas as pd

import finnhub
finnhub_client = finnhub.Client(api_key="c7ttg6iad3ifisk2drlg")

import time
import datetime
d = datetime.date(2022,3,1)
start_unixtime = time.mktime(d.timetuple())

d = datetime.datetime.now().date()
stop_unixtime = time.mktime(d.timetuple())

dataframes = []

for symbol in shared.SYMBOLS:
    success = False
    while not success:
        try:
            df = pd.DataFrame(finnhub_client.stock_candles(symbol, '1', int(start_unixtime), int(stop_unixtime)))
            df["SYMBOL"] = symbol
            dataframes += [df]
            success = True
        except finnhub.FinnhubAPIException:
            print("waiting to have access to api again (free trial limitation)")
            time.sleep(1)


data = pd.concat(dataframes)
data = data.sort_values(by=['t'])

with open("candle_sample_contest.txt", 'w') as fp:
    def write_line(row):
        line = json.dumps({row['SYMBOL']:{'c':row['c'],
                                          'h':row['h'],
                                          'l':row['l'],
                                          'o':row['o'],
                                          's':row['s'],
                                          't':row['t'],
                                          'v':row['v']}})+"\n"
        fp.write(line)
    data.apply(write_line, axis=1)
