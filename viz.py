import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

def pid_plot(ax1, setPoint, processVariable):
    sp = setPoint
    pv = processVariable
    # xs = []
    ys = []
    for line in pv:
        # xs.append(t)
        ys.append(line)
    ax1.clear()
    ax1.plot(ys)
    plt.show()

def animate(fig, plot, interval=1000):
    ani = animation.FuncAnimation(fig, plot, interval)
    plt.show()


