import json

class BotOrderClient():
    """
    Client used to compare bots
    """
    def __init__(self):
        self.start_money = 100000
        self.money = self.start_money
        self.actions = {}
        self.prices = {}

    def process_candle(self, message):
        """
        Called for every messsage in stock data
        """
        parsed = json.loads(message)
        for k, v in parsed.items():
            if 'c' in v:
                self.prices[k] = v['c']

    def sell(self, key:str, quantity:int):
        """
        call this functin to sell quantity action of type key.
        ex : sell('AAPL', 100) to sell 100 apple actions.
        """
        if self.actions[key] < quantity:
            raise f"Trying to sell {quantity} {key} actions but only {self.actions[key]} are available"
        self.money += self.prices[key]*quantity
        self.actions[key] -= quantity

    def buy(self, key:str, quantity:int):
        """
        buy quantity actions of type key.
        ex buy('AAPL', 100) to buy 100 Apple actions
        """
        total = self.prices[key]*quantity
        if total > self.money:
            raise Exception(f"Not enough money to buy {quantity} {key} actions. You've got only {self.money} and {total} is requested.")
        else:
            self.money -= total
            self.actions[key] += quantity

    def gains(self):
        """
        returns earned money since the creation of the client
        Note : this can be negative.
        """
        return self.money - self.start_money