import sys
import os
from botorderclient import BotOrderClient

SYMBOLS = ["AAPL", "TSLA", "ATVI", "DIS", "AMZN", "BINANCE:BTCUSDT"]
PROJECTS = {
    'Bot-Trading-EPSI':{"path":('nemo', 'Nemo')},
    'JSP':{"path":('', '')},
    'MSPR_bot_trade':{"path":("selecaoBot", "selecaoBot")},
    'ProjetTradingPythonPOO':{"path":('bot', 'Bot')},
    'Projet-Transversal/trading_bot':{},
    'python-sassou/trad_sassou_bot':{"path":('sassou_bot', 'SassouBot')},
    'Robot-trading-PNL':{"path":('trading_bot', 'Pnl')},
    'Site-trading-':{"path":('robotrading', 'RoboTrading')},
    'Trading-Bot':{},
    'Trading-Bot-ESC':{"path":('robot', 'Robot')},
    'WEBEROES':{"path":("jesuisfort", "JeSuisFort")}
}

def initialize_projects(projects):
    """Load projects and ensure use dvariables are initialized
    """
    for k, v in projects.items():
        try:
            sys.path.append(os.path.join(os.path.dirname(__file__) + "/../", k ))
            v['client'] = BotOrderClient()
            v['gains'] = []
            v['time'] = []
            if 'path' in v :
                tmpmod = __import__(v['path'][0])
                v['bot'] = getattr(tmpmod, v['path'][1])(v['client'])
        except Exception:
            print(f"WARNING : bot {k} not loaded")
    return projects

def play_line(line, projects):
    """process one line of data on all available bots

    Args:
        line (_type_): _description_
        projects (_type_): _description_
    """
    for _, v in projects.items():
        if "bot" in v :
            v["client"].process_candle(line)
            v["bot"].process_candle(line)
            v['gains'] += [v["client"].gains()]
            v['time'] += [v['client'].last_raw_time]
    return projects

def play_candle_file(filename, projects):
    """Test projects on candlefile
    """
    fp = open(filename, "r")
    line = fp.readline()
    while(line):
        play_line(line, projects)
        line = fp.readline()

def display_gains(projects):
    """ reads projects dicts to display each project recorded earning
    """
    for k, v in projects.items():
        gains = v["client"].gains()
        print(f"{k} : {gains}")
