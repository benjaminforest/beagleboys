import sys
import os, sys
from botorderclient import BotOrderClient

PROJECTS = {
    'ProjetTradingPythonPOO':{"path":('bot', 'Bot')},
    'Trading-Bot-ESC':{"path":('robot', 'Robot')},
    'Bot-Trading-EPSI':{"path":('nemo', 'Nemo')},
    'python-sassou/trad_sassou_bot':{"path":('sassou_bot', 'SassouBot')},
    'Robot-trading-PNL':{"path":('trading_bot', 'Pnl')},
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
            v['gains'] = []
            v['time'] = []
    except Exception:
        pass


with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        for k, v in PROJECTS.items():
            if "bot" in v :
                try:
                    v["bot"].process_candle(line)
                    v["client"].process_candle(line)
                    v['gains'] +=  [v["client"].gains()]
                    v['time'] += [v['client'].last_time]
                except Exception:
                    pass

for k, v in PROJECTS.items():
    gain = 0
    if "bot" in v :
        gain = v["client"].gains()
    print(f"{k} : {gain}")



import matplotlib.pyplot as plt

figure, ax = plt.subplots()

plt.title("Gains against time",fontsize=25)

plt.xlabel("Time",fontsize=18)
plt.ylabel("Gains",fontsize=18)

for k, v in PROJECTS.items():
    if "bot" in v :
        print("Drawing" + k)
        v["line"], = ax.plot(v["time"], v["gains"])
        v["line"].set_label(k)

ax.legend()
plt.show()