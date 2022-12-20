import pytest

import moreitertools as mit


def _render(iterable):
    return [list(i) for i in iterable]


def test_chunks(five_things):
    assert _render(mit.chunks(five_things, 3)) == [
        [0, 1, 2],
        [3, 4],
    ]


def test_chunks_iter(five_things_iter):
    assert _render(mit.chunks(five_things_iter, 2)) == [
        ["a", "b"],
        ["c", "d"],
        ["e"],
    ]


def test_chunks_str(five_things_str):
    assert _render(mit.chunks(five_things_str, 4)) == [
        ["f", "g", "h", "i"],
        ["j"],
    ]


def test_chunks_size_1(five_things):
    assert list(mit.chunks(five_things, 1)) == [
        [0],
        [1],
        [2],
        [3],
        [4],
    ]


def test_chunks_size_5(five_things):
    assert list(mit.chunks(five_things, 5)) == [
        [0, 1, 2, 3, 4],
    ]


def test_chunks_size_6(five_things):
    assert list(mit.chunks(five_things, 6)) == [
        [0, 1, 2, 3, 4],
    ]


def test_chunks_size_0(five_things):
    with pytest.raises(ValueError):
        list(mit.chunks(five_things, 0))


def test_chunks_empty():
    assert list(mit.chunks([], 3)) == []


def test_chunks_include_orphans(five_things):
    assert list(mit.chunks(five_things, 3, include_orphans=False)) == [
        [0, 1, 2],
    ]


def test_chunks_include_orpahns_6(five_things_iter):
    assert list(mit.chunks(five_things_iter, 6, include_orphans=False)) == []
