import json
class BeagleBot():
    """Bot class
    """
    def __init__(self, client):
        """
        client is used to issue orders
        """
        self.client = client
        self.count_aapl = 0
        self.total_aapl = 0
        self.previous_price = 0

    def process_candle(self, candle_msg:str):
        """This function is called when a new candle_msg is received.
            Candle message is a string of the form:
            {'symbol_key' : {'c': [174.3], 'h': [174.3], 'l': [174.19], 'o': [174.19], 's': 'ok', 't': [1643670000], 'v': [1888]}

            Note that there are list, so you can have multiple candles in one message.
        """
        candle_dict = json.loads(candle_msg)
        for k, v in candle_dict.items():
            if 'AAPL' == k:
                self.update_aapl_mean(v)
                self.sell_if_needed(k, v)

    def update_aapl_mean(self, v):
        self.count_aapl += 1
        self.total_aapl += v['c']

    def sell_if_needed(self, k, v):
        if v['c'] < self.previous_price :
            self.client.sell(k, 1)
        elif self.client.money > v['c']:
            self.client.buy(k, 1)
