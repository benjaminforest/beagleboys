import sys
import os, sys
from botorderclient import BotOrderClient

PROJECTS = {
    'ProjetTradingPythonPOO':{"path":('bot', 'Bot')},
}

for k, v in PROJECTS.items():
    sys.path.append(os.path.join(os.path.dirname(__file__), k ))
    if 'path' in v :
        tmpmod = __import__(v['path'][0])
        v['client'] = BotOrderClient()
        v['bot'] = getattr(tmpmod, v['path'][1])(v['client'])
        v['gains'] = []
        v['time'] = []

with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        for k, v in PROJECTS.items():
            if "bot" in v :
                v["bot"].process_candle(line)
                v["client"].process_candle(line)
                v['gains'] +=  [v["client"].gains()]
                v['time'] += [v['client'].last_time]

for k, v in PROJECTS.items():
    gain = 0
    if "bot" in v :
        gain = v["client"].gains()
    print(f"{k} : {gain}")