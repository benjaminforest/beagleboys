import sys
import os, sys
from botorderclient import BotOrderClient
from shared.earningsplotter2 import EarningsPlotter
import time
import numpy as np

PROJECTS = {
    'ProjetTradingPythonPOO':{"path":('bot', 'Bot')},
}

def initialize_projects(projects):
    """Load projects and ensure use dvariables are initialized
    """
    for k, v in projects.items():
        sys.path.append(os.path.join(os.path.dirname(__file__), k ))
        try:
            v['client'] = BotOrderClient()
            v['gains'] = []
            v['time'] = []
            if 'path' in v :
                tmpmod = __import__(v['path'][0])
                v['bot'] = getattr(tmpmod, v['path'][1])(v['client'])
        except Exception:
            print(f"Warning : project {k} with value {v} was not initilized")

def play_candle_file(filename, projects, delay_s=0):
    """Test projects on candlefile
    """
    plotter = EarningsPlotter(projects)
    with open(filename, "r") as fp:
        lines = fp.readlines()
        for line in lines:
            print(line)
            plotter.update_projects_graphs()
            # time.sleep(delay_s)
            for _, v in projects.items():
                if "bot" in v :
                    try:
                        v["bot"].process_candle(line)
                        v["client"].process_candle(line)
                        v['gains'] = np.append( v['gains'], v["client"].gains())
                        v['time'] = np.append( v['time'], v['client'].last_raw_time)
                    except Exception:
                        pass

def display_gains(projects):
    """ reads projects dicts to display each project recorded earning
    """
    for k, v in projects.items():
        gains = v["client"].gains()
        print(f"{k} : {gains}")


initialize_projects(PROJECTS)
play_candle_file("candle_sample.txt", PROJECTS, 0.01)
display_gains(PROJECTS)
