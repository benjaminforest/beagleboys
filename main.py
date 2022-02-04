from trading_bot import g1bot

robot1 = g1bot.Groupe1Robot() # hérite de RapTouRobot

with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines(1000)
    for line in lines:
        robot1.process_candle(line)

