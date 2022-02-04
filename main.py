import sys
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'WEBEROES'))

import weberoesbot

robot1 = weberoesbot.WebEroesBot() # hérite de RapTouRobot

with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines(1000)
    for line in lines:
        robot1.process_candle(line)

print(robot1.gains())