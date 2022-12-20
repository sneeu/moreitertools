import moreitertools as mit


def test_compose():
    def add_1(x):
        return x + 1

    def mul_2(x):
        return x * 2

    c = mit.compose(add_1, mul_2)
    assert c(3) == 7
    assert c(5) == 11
    assert c.__name__ == "compose(add_1, mul_2)"
    assert c.__doc__ == "Compose add_1 and mul_2"

    c2 = mit.compose(mul_2, str)
    assert c2(3) == "33"
    assert c2(4) == "44"
