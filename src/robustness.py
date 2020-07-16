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

    win_val_windows = get_minimum_in_expanding_windows(windows)

    ksi_list = list(ksi)

    for t in range(len(phi_list) - stop + 1):
        t_list = []
        for t_hat in range(t + start, t + stop + 1):
            t_list.append(min(ksi_list[t_hat], win_val_windows[t]))
        yield max(t_list)

    # for t in range(len(phi_list)-stop+1):
    #     for t_hat in range(t + start, t + stop):
    #         for t_hat_hat in range(t, t_hat+1):
    #             size = t_hat - t+1
    #             window_array = windows[size]
    #             min_value = window_array[t]

    #
    # print(z)

    #
    # for t_hat in range(t+start, t+stop):
    #     for t_hat_hat in range(t, t_hat+1):
    #         print(t_hat, t_hat_hat)


def get_minimum_in_expanding_windows(windows: dict):
    to_return = []

    min_length = min(_window_sizes(windows))

    for i in range(min_length):
        to_return.append(min(_get_index_values_of_windows(windows, i)))
    return to_return


def _get_index_values_of_windows(windows, index):
    for win_key in windows:
        yield windows[win_key][index]


def _window_sizes(windows):
    for win_key in windows:
        yield len(windows[win_key])
