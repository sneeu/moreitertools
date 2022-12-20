import moreitertools as mit


def test_takeuntil(five_things):
    assert list(mit.takeuntil(five_things, lambda x: x == 2)) == [0, 1, 2]
    assert list(mit.takeuntil(five_things, lambda x: x == 5)) == [0, 1, 2, 3, 4]
    assert list(mit.takeuntil(five_things, lambda x: x == 10)) == [0, 1, 2, 3, 4]


def test_dropuntil(five_things):
    assert list(mit.dropuntil(five_things, lambda x: x == 2)) == [3, 4]
    assert list(mit.dropuntil(five_things, lambda x: x == 5)) == []
    assert list(mit.dropuntil(five_things, lambda x: x == 10)) == []
