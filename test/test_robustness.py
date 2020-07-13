import matplotlib.pyplot as plt
import numpy as np

from src.maxmin import supermaxmin


def robustness(signal, time_range):
    to_return = np.zeros((len(time_range),))
    for i in range(len(time_range)):
        to_return[i] = signal.get_value(i)
    return to_return


x = np.arange(0, 4 * np.pi, 0.1)  # start,stop,step
sig = np.cos(x * 5) + np.sin(x)


def and_(phi, ksi):
    for p, k in zip(phi, ksi):
        yield min(p, k)


def not_(phi):
    for i in phi:
        yield -1 * i


def or_(phi, ksi):
    return not_(and_(not_(phi), not_(ksi)))


a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

print(list(not_(a)))
print(list(and_(a, b)))
print(list(not_(and_(a, b))))
print(list(or_(a, b)))
