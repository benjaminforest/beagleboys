# -*- coding: utf-8 -*-
"""
This example demonstrates many of the 2D plotting capabilities
in pyqtgraph. All of the plots may be panned/scaled by dragging with
the left/right mouse buttons. Right click on any plot to show a context menu.
"""

from shared import shared
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import random
import json

def rand_color():
    return list(np.random.choice(range(256), size=3))

app = pg.mkQApp("Beagleboys Trading Contest")

global g_win
g_win = pg.GraphicsLayoutWidget(show=True, title="Beagleboys Trading Contest")
g_win.resize(1000,600)
g_win.setWindowTitle('Beagleboys Trading Contest')


global g_projects
g_projects = shared.PROJECTS
g_projects = shared.initialize_projects(g_projects)

filename = "candle_sample_contest.txt"
global g_file
g_file = open(filename, "r")

global g_shares
g_shares = {}

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

global g_plot
g_plot = g_win.addPlot(col=1, rowspan = 6, title="Beagleboys Trading Contest", axisItems = {'bottom': pg.DateAxisItem()})

global g_legend, g_legend_actions
g_legend = pg.LegendItem((80,60), offset=(70,20), brush="w", labelTextColor="k")
g_legend.setParentItem(g_plot.graphicsItem())

for k, v in g_projects.items():
    v['curve'] = g_plot.plot(x=v['time'], y=v["gains"], pen= rand_color(), name=k )
    g_legend.addItem(v['curve'], k)

g_plot.setLabel('left', "Gains", units='$')
g_plot.setLabel('bottom', "Temps", units='time')
g_plot.setLogMode(x=False, y=False)

global g_linecounter
g_linecounter = 0

shared.play_candle_file(filename, g_projects)

line = g_file.readline()
while line:
    candle_dict = json.loads(line)
    for k, v in candle_dict.items():
        if k in g_shares:
            g_shares[k][0].append(v['t'])
            g_shares[k][1].append(v['c'])
        else:
            action_plot = g_win.addPlot(col=2, title=k, axisItems = {'bottom': pg.DateAxisItem()})
            g_win.nextRow()
            g_shares[k] = ([v['t']], [v['c']], action_plot.plot( pen= rand_color(), name=k ))
    line = g_file.readline()

for k, v in g_projects.items():
    v['curve'].setData(x=v['time'], y=v['gains'])

for k, v in g_shares.items():
    v[2].setData(x=v[0], y=v[1])

shared.display_gains(g_projects)

# timer = QtCore.QTimer()
# timer.timeout.connect(update)
# timer.start(0)

if __name__ == '__main__':
    pg.exec()
