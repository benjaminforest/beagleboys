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

def rand_color():
    return list(np.random.choice(range(256), size=3))

app = pg.mkQApp("Beagleboys Trading Contest")

win = pg.GraphicsLayoutWidget(show=True, title="Beagleboys Trading Contest")
win.resize(1000,600)
win.setWindowTitle('Beagleboys Trading Contest')


global g_projects
g_projects = shared.PROJECTS
g_projects = shared.initialize_projects(g_projects)

global g_file
g_file = open("candle_sample.txt", "r")

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

global g_plot

g_plot = win.addPlot(title="Multiple curves", axisItems = {'bottom': pg.DateAxisItem()})
for k, v in g_projects.items():
    v['curve'] = g_plot.plot(x=v['time'], y=v["gains"], pen= rand_color(), name=k )

g_plot.setLabel('left', "Gains", units='$')
g_plot.setLabel('bottom', "Temps", units='time')
g_plot.setLogMode(x=False, y=False)

def update():
    """update graph
    """
    global g_projects, g_plot, g_file
    line = g_file.readline()
    if(line):
        shared.play_line(line, g_projects)
        for k, v in g_projects.items():
            v['curve'].setData(x=v['time'], y=v['gains'])

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

if __name__ == '__main__':
    pg.exec()
