import pytest


@pytest.fixture
def five_things():
    return [0, 1, 2, 3, 4]


@pytest.fixture
def five_things_iter():
    return iter(["a", "b", "c", "d", "e"])


@pytest.fixture
def five_things_str():
    return "fghij"
