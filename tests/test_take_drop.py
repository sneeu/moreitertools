import pytest

import moreitertools as mit


def test_take(five_things):
    assert list(mit.take(five_things, 3)) == [0, 1, 2]


def test_take_iter(five_things_iter):
    assert list(mit.take(five_things_iter, 2)) == ["a", "b"]


def test_take_str(five_things_str):
    assert list(mit.take(five_things_str, 4)) == ["f", "g", "h", "i"]


def test_take_size_0(five_things):
    assert list(mit.take(five_things, 0)) == []


def test_take_size_6(five_things):
    assert list(mit.take(five_things, 6)) == [0, 1, 2, 3, 4]


def test_take_negative_size(five_things):
    with pytest.raises(ValueError):
        list(mit.take(five_things, -2))


def test_drop(five_things):
    assert list(mit.drop(five_things, 3)) == [3, 4]


def test_drop_iter(five_things_iter):
    assert list(mit.drop(five_things_iter, 2)) == ["c", "d", "e"]


def test_drop_str(five_things_str):
    assert list(mit.drop(five_things_str, 4)) == ["j"]


def test_drop_size_0(five_things):
    assert list(mit.drop(five_things, 0)) == [0, 1, 2, 3, 4]


def test_drop_size_6(five_things):
    assert list(mit.drop(five_things, 6)) == []


def test_drop_negative_size(five_things):
    with pytest.raises(ValueError):
        list(mit.drop(five_things, -2))
