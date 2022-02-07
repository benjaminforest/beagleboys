from shared import shared
import json
import finnhub
finnhub_client = finnhub.Client(api_key="c7ttg6iad3ifisk2drlg")

import time
import datetime
d = datetime.date(2022,2,1)
start_unixtime = time.mktime(d.timetuple())

d = datetime.date(2022,2,3)
stop_unixtime = time.mktime(d.timetuple())

for symbol in shared.SYMBOLS:
    success = False
    while not success:
        try:
            data = {symbol:finnhub_client.stock_candles(symbol, '1', int(start_unixtime), int(stop_unixtime))}
            success = True
        except finnhub.FinnhubAPIException:
            print("waiting to have access to api again (free trial limitation)")
            time.sleep(1)


with open("candle_sample2.txt", 'w') as fp:

            line = json.dumps(data)+"\n"
            print(line)
            fp.write(line)
