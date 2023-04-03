import matplotlib.pyplot as plt
import numpy as np


def graph(x_arr: list, y_arr: list):
    xpoints = np.array(x_arr)
    ypoints = np.array(y_arr)
    plt.plot(xpoints, ypoints, '-o', color='b', markersize=1)
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
