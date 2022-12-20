import pytest

import moreitertools as mit


def test_version():
    assert mit.__version__ == "0.1.0"


def test_windows_list(five_things):
    assert list(mit.windows(five_things, 3)) == [
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 4],
    ]


def test_windows_iter(five_things_iter):
    assert list(mit.windows(five_things_iter, 4)) == [
        ["a", "b", "c", "d"],
        ["b", "c", "d", "e"],
    ]


def test_windows_str(five_things_str):
    assert list(mit.windows(five_things_str, 2)) == [
        ["f", "g"],
        ["g", "h"],
        ["h", "i"],
        ["i", "j"],
    ]


def test_windows_size_1(five_things):
    assert list(mit.windows(five_things, 1)) == [
        [0],
        [1],
        [2],
        [3],
        [4],
    ]


def test_windows_size_5(five_things):
    assert list(mit.windows(five_things, 5)) == [
        [0, 1, 2, 3, 4],
    ]


def test_windows_size_6(five_things):
    assert list(mit.windows(five_things, 6)) == []


def test_windows_size_0(five_things):
    with pytest.raises(ValueError):
        list(mit.windows(five_things, 0))


def test_windows_empty():
    assert list(mit.windows([], 3)) == []
