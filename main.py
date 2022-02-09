import sys
import os, sys
import importlib
from botorderclient import BotOrderClient

PROJECTS = {
    'ProjetTradingPythonPOO':{"path":('bot', 'Bot'),
    },
    'python-sassou/trad_sassou_bot':{"path":('sassou_bot', 'SassouBot')},
    'Robot-trading-PNL':{"path":('trading_bot', 'Pnl'),
    },
    'Trading-Bot':{},
    'MSPR_bot_trade':{"path":("selecaoBot", "selecaoBot")},
    'Projet-Transversal/trading_bot':{},
    'Site-trading-':{"path":('robotrading', 'RoboTrading')},
    'WEBEROES':{"path":("jesuisfort", "JeSuisFort")}
}

for k, v in PROJECTS.items():
    sys.path.append(os.path.join(os.path.dirname(__file__), k ))
    try:
        if 'path' in v :
            tmpmod = __import__(v['path'][0])
            v['client'] = BotOrderClient()
            v['bot'] = getattr(tmpmod, v['path'][1])(v['client'])
    except Exception:
        pass

with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines(1000)
    for line in lines:
        for k, v in PROJECTS.items():
            if "bot" in v :
                v["client"].process_candle(line)
                v["bot"].process_candle(line)

for k, v in PROJECTS.items():
    gain = 0
    if "bot" in v :  gain = v["client"].gains()
    print(f"{k} : {gain}")
