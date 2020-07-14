import src.robustness as rb

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]


def test_not():
    assert list(rb.not_(a)) == [-1, -2, -3, -4, -5]


def test_and():
    assert list(rb.and_(a, b)) == [1, 2, 3, 2, 1]


def test_or():
    assert list(rb.or_(a, b)) == [5, 4, 3, 4, 5]


def test_feature():
    assert list(rb.feature_(range(0, 20), (1, 2))) == \
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# x = np.arange(0, 4 * np.pi, 0.1)  # start,stop,step
# signal = np.sin(x) + np.cos(5*x)
#
# print(len(signal))
# print(len(list(feature_(signal, (10, 20)))))
# plt.plot(range(98),  list(feature_(signal, (10, 20))), signal)
# x = np.arange(0, 4 * np.pi, 0.1)  # start,stop,step
# sig = np.cos(x * 5) + np.sin(x)


# plt.plot(x, list(not_(sin_y)))
# plt.show()
