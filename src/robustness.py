from src.maxmin import supermaxmin


def sat_(phi):
    for i in phi:
        yield i


def not_(phi):
    for i in phi:
        yield -1 * i


def and_(phi, ksi):
    for p, k in zip(phi, ksi):
        yield min(p, k)


def or_(phi, ksi):
    return not_(and_(not_(phi), not_(ksi)))


def feature_(ksi, interval: tuple):
    """

    :param ksi:
    :param interval: [x,y)
    :return:
    """
    start, end = interval
    length = end - start
    max_values, _ = supermaxmin(ksi, length)

    for i in range(start, len(max_values) - start):
        yield max_values[i]
