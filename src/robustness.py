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
    phi_list = list(phi)
    for i in range(stop):
        _, min_values = supermaxmin(phi_list, i + 1)
        windows[i + 1] = min_values

    win_val_windows = []
    for i in range(len(windows[1])):
        min_val = windows[1][1]
        for win in windows:
            if len(windows[win]) <= i:
                continue
            current = windows[win][i]
            if current < min_val:
                min_val = current
        win_val_windows.append(min_val)

    for t in range(len(phi_list)-stop+1):
        for t_hat in range(t + start, t + stop):
            for t_hat_hat in range(t, t_hat+1):
                size = t_hat - t+1
                window_array = windows[size]
                min_value = window_array[t]

    #
    # print(z)



    #
    # for t_hat in range(t+start, t+stop):
    #     for t_hat_hat in range(t, t_hat+1):
    #         print(t_hat, t_hat_hat)
