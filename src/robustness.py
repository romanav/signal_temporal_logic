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
    """

    :param phi:
    :param interval: [a,b)
    :param ksi:
    :return:
    """
    start, stop = interval
    phi_list = list(phi)

    windows = _create_expanding_windows(phi_list, stop)
    win_val_windows = get_minimum_in_expanding_windows(windows)

    ksi_list = list(ksi)

    for t in range(len(phi_list) - stop + 1):
        t_list = []
        for t_hat in range(t + start, t + stop):
            t_list.append(min(ksi_list[t_hat], win_val_windows[t]))
        yield max(t_list)


def _create_expanding_windows(phi_list, max_window_size) -> dict:
    windows = {}
    for i in range(1, max_window_size):
        _, min_values = supermaxmin(phi_list, i)
        windows[i] = min_values
    return windows


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
