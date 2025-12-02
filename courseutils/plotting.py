
import matplotlib.pyplot as plt

def line(x, y, title=None, xlabel=None, ylabel=None):
    plt.figure()
    plt.plot(x, y)
    if title: plt.title(title)
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    plt.tight_layout()
    return plt.gca()
