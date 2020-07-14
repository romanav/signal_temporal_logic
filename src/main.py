import numpy as np
from matplotlib import pyplot as plt

from src.robustness import feature_

# x = np.arange(0, 4 * np.pi, 0.1)  # start,stop,step
# signal = np.sin(x)
#
# plt.plot(range(122),  list(feature_(signal, (1, 5))), signal)
# plt.show()

from scipy import signal
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 500, endpoint=False)
sig = signal.square(2 * np.pi * 5 * t)
exp = list(feature_(sig, (10, 20)))
print(sig)
print(exp)


plt.plot(range(472), exp,  sig)
# plt.ylim(-2, 2)
plt.show()
#

