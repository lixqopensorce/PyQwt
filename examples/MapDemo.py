#!/usr/bin/env python

import random, sys, time
try:
    import resource
    has_resource = 1
except ImportError:
    has_resource = 0

from qt import *
from qwt import *
from Numeric import *

def standard_map(x, y, kappa):
    """provide one interate of the inital conditions (x, y)
       for the standard map with parameter kappa.
    """
    y_new=y-kappa*sin(2.0*pi*x)
    x_new=x+y_new

    # bring back to [0,1.0]^2
    if( (x_new>1.0) or (x_new<0.0) ):
         x_new=x_new-floor(x_new)
    if( (y_new>1.0) or (y_new<0.0) ):
         y_new=y_new-floor(y_new)

    return x_new, y_new

# standard_map


class MapDemo(QMainWindow):

    def __init__(self, *args):
        QMainWindow.__init__(self, *args)

        self.plot = plot = QwtPlot(self)
        self.setCentralWidget(plot)

        # Initialize map data
        self.count = self.i = 1000
        self.xs = zeros(self.count, Float)
        self.ys = zeros(self.count, Float)

        self.kappa = 0.2

        plot.setTitle("A Simple Map Demonstration")

        self.curve = plot.insertCurve("Map")

        plot.setCurveSymbol(self.curve, QwtSymbol(
            QwtSymbol.Ellipse, QBrush(Qt.red), QPen(Qt.blue), QSize(5, 5)))

        plot.setCurvePen(self.curve, QPen(Qt.cyan))

        plot.setAxisTitle(QwtPlot.xBottom, "x")
        plot.setAxisTitle(QwtPlot.yLeft, "y")
    
        # Set scales
        plot.setAxisScale(QwtPlot.xBottom, 0.0, 1.0)
        plot.setAxisScale(QwtPlot.yLeft, 0.0, 1.0)

        self.toolBar = QToolBar(self)
        
        sizeBox = QHBox(self.toolBar)
        QLabel("Count:", sizeBox)
        sizeCounter = QwtCounter(sizeBox)
        sizeCounter.setRange(0, 1000000, 100)
        sizeCounter.setValue(self.count)
        sizeCounter.setNumButtons(3)
        self.connect(
            sizeCounter, SIGNAL('valueChanged(double)'), self.setCount)

        self.toolBar.setStretchableWidget(QWidget(self.toolBar))

        tickBox = QHBox(self.toolBar)
        QLabel("Ticks (ms):", tickBox)
        tickCounter = QwtCounter(tickBox)
        # 1 tick = 1 ms, 10 ticks = 10 ms (Linux clock is 100 Hz)
        self.ticks = 10
        tickCounter.setRange(0, 1000, 1)
        tickCounter.setValue(self.ticks)
        tickCounter.setNumButtons(3)
        self.connect(
            tickCounter, SIGNAL('valueChanged(double)'), self.setTicks)
        self.tid = self.startTimer(self.ticks)

        self.timer_tic = None
        self.user_tic = None
        self.system_tic = None
        
        plot.replot()

    # __init__()
        
    def setCount(self, count):
        self.count = self.i = count
        self.xs = zeros(self.count, Float)
        self.ys = zeros(self.count, Float)
        self.i = self.count
        self.killTimer(self.tid)
        self.tid = self.startTimer(self.ticks)

    # setCount()

    def setTicks(self, ticks):
        self.i = self.count
        self.ticks = int(ticks)
        self.killTimer(self.tid)
        self.tid = self.startTimer(ticks)

    # setTicks()
        
    def resizeEvent(self, event):
        self.plot.resize(event.size())
        self.plot.move(0, 0)

    # resizeEvent()

    def moreData(self):
        if self.i == self.count:
            self.i = 0
            self.x = random.random()
            self.y = random.random()
            self.xs[self.i] = self.x
            self.ys[self.i] = self.y
            self.i += 1
            if has_resource:
                self.user_toc, self.system_toc = resource.getrusage(
                    resource.RUSAGE_SELF)[:2]
                if self.user_tic:
                    print "user: %s s;" % (self.user_toc-self.user_tic),
                self.user_tic = self.user_toc
                if self.system_tic:
                    print "system: %s s;" % (self.system_toc-self.system_tic),
                self.system_tic = self.system_toc
            self.timer_toc = time.time()
            if self.timer_tic:
                print "wall: %s s." % (self.timer_toc-self.timer_tic)
            self.timer_tic = self.timer_toc
        else:
            self.x, self.y = standard_map(self.x, self.y, self.kappa)
            self.xs[self.i] = self.x
            self.ys[self.i] = self.y
            self.i += 1

    # moreData()
        
    def timerEvent(self, e):
        self.moreData()
        self.plot.setCurveData(self.curve, self.xs[:self.i], self.ys[:self.i])
        self.plot.replot()

    # timerEvent()

# class MapDemo


def make():
    demo = MapDemo()
    demo.resize(600, 600)
    demo.show()
    return demo

# make()

def main(args):
    app = QApplication(args)
    demo = make()
    app.setMainWidget(demo)
    app.exec_loop()

# main()

# Admire! 
if __name__ == '__main__':
    main(sys.argv)
