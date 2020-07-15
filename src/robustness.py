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


def feature_(ksi, interval: (int, int)):
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


def until(phi, interval: (int, int), ksi):
    start, stop = interval
    windows = {}
    ksi_list = list(ksi)
    for i in range(stop):
        _, min_values = supermaxmin(ksi_list, i + 1)
        windows[i + 1] = min_values

    z=0
    for t in range(len(ksi_list)-stop+1):
        for t_hat in range(t + start, t + stop):
            for t_hat_hat in range(t, t_hat+1):
                size = t_hat - t+1
                window_array = windows[size]
                min_value = window_array[t]
                z+=1

    print(z)



    #
    # for t_hat in range(t+start, t+stop):
    #     for t_hat_hat in range(t, t_hat+1):
    #         print(t_hat, t_hat_hat)
