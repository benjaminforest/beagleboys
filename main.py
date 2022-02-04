import sys
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'Trading-Bot'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Projet-Transversal'))

from trading_bot import auto_bot

robot1 = auto_bot.AutoBot() # hérite de RapTouRobot

with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines(1000)
    for line in lines:
        robot1.process_candle(line)

