import moreitertools as mit


def test_flatten():
    assert list(mit.flatten([[1, 2], [3, 4]])) == [1, 2, 3, 4]
    assert list(mit.flatten([[[[1]]]])) == [1]
    assert list(mit.flatten([1, [2, [3, [4, [5, []]]]]])) == [1, 2, 3, 4, 5]
