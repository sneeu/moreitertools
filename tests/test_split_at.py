import pytest

import moreitertools as mit


def _render(iterable):
    return [list(i) for i in iterable]


def test_split_at(five_things):
    assert _render(mit.split_at(five_things, 3)) == [[0, 1, 2], [3, 4]]


def test_split_at_iter(five_things_iter):
    assert _render(mit.split_at(five_things_iter, 2)) == [["a", "b"], ["c", "d", "e"]]


def test_split_at_str(five_things_str):
    assert _render(mit.split_at(five_things_str, 4)) == [["f", "g", "h", "i"], ["j"]]


def test_split_at_size_0(five_things):
    assert _render(mit.split_at(five_things, 0)) == [[], [0, 1, 2, 3, 4]]


def test_split_at_size_6(five_things):
    assert _render(mit.split_at(five_things, 6)) == [[0, 1, 2, 3, 4], []]


def test_split_at_negative_size(five_things):
    with pytest.raises(ValueError):
        _render(mit.split_at(five_things, -2))
