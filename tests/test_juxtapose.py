import pytest

import operator

import moreitertools as mit


def test_juxtapose():
    def add_2(n):
        return n + 2

    def mul_5(n):
        return n * 5

    j = mit.juxtapose([add_2, mul_5])

    assert list(j(11)) == [13, 55]
    assert j.__name__ == "juxtapose(add_2, mul_5)"
    assert j.__doc__ == "Apply each function in [add_2, mul_5] to the same arguments"


def test_juxtapose_with_multiple_args():
    j = mit.juxtapose([operator.add, operator.mul])

    assert list(j(7, 13)) == [20, 91]


def test_juxtapose_with_empty_iterable():
    assert list(mit.juxtapose([])(11)) == []


def test_juxtapose_with_non_callable():
    with pytest.raises(TypeError):
        mit.juxtapose([1, 2, 3])


def test_juxtapose_with_non_iterable():
    with pytest.raises(TypeError):
        mit.juxtapose(1)
