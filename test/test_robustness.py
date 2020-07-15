import src.robustness as rb

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]


def test_not():
    assert list(rb.not_(a)) == [-1, -2, -3, -4, -5]


def test_and():
    assert list(rb.and_(a, b)) == [1, 2, 3, 2, 1]


def test_or():
    assert list(rb.or_(a, b)) == [5, 4, 3, 4, 5]


def test_sat():
    assert list(rb.sat_(a)) == [1, 2, 3, 4, 5]


def test_feature():
    assert list(rb.feature_(range(0, 20), (1, 2))) == \
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


def test_feature_zero_window():
    assert list(rb.feature_(range(0, 20), (0, 1))) == \
           [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


def test_until():
    phi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ksi = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



    print(list(rb.until(phi, [0, 3], ksi)))
