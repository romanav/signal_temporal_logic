import numpy as np

from src.robustness import feature_, not_, sat_
import matplotlib.pyplot as plt

t = np.arange(0, 4 * np.pi, 0.1)
print(f'signal length: {len(t)}')
sig = np.sin(t)

# exp = list(not_(feature_(sig - 0.25, (1, 2))))
exp = list(sat_(sig-0.25))


plt.plot(range(len(exp)), exp, sig)
# plt.plot(range(472), exp,  sig)
# plt.ylim(-2, 2)
plt.show()
#
