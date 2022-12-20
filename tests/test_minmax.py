import moreitertools as mit


def test_minmax(five_things):
    assert mit.minmax(five_things) == (0, 4)
    assert mit.minmax(3, 9) == (3, 9)
    assert mit.minmax(10, 2) == (2, 10)
