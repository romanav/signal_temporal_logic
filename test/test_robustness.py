import matplotlib.pyplot as plt
import numpy as np

from src.Robustness import Elementary
from src.maxmin import supermaxmin


def robustness(signal, time_range):
    to_return = np.zeros((len(time_range),))
    for i in range(len(time_range)):
        to_return[i] = signal.get_value(i)
    return to_return


x = np.arange(0, 4 * np.pi, 0.1)  # start,stop,step
sig = np.cos(x * 5) + np.sin(x)

el = Elementary(sig)
r = robustness(el, x)

plt.plot(x, r)
plt.show()
