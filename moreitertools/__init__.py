__version__ = "0.1.0"

import collections
import itertools
from typing import Any, Callable, Iterable, ParamSpec, Tuple, TypeVar


def windows(iterable: Iterable, size: int) -> Iterable[Iterable]:
    if size < 1:
        raise ValueError("size must be at least 1")

    q: collections.deque = collections.deque(maxlen=size)

    for item in iterable:
        q.append(item)

        if len(q) == size:
            yield list(q)

            if len(q) < size:
                break

            q.popleft()


def chunks(iterable: Iterable, size: int, include_orphans=True) -> Iterable[Iterable]:
    if size < 1:
        raise ValueError("size must be at least 1")

    q: collections.deque = collections.deque(maxlen=size)

    for item in iterable:
        q.append(item)

        if len(q) == size:
            yield list(q)
            q.clear()

    if include_orphans and q:
        yield list(q)


def take(iterable: Iterable, n: int) -> Iterable:
    if n < 0:
        raise ValueError("n must be non-negative")

    return itertools.islice(iterable, n)


def drop(iterable: Iterable, n: int) -> Iterable:
    if n < 0:
        raise ValueError("n must be non-negative")

    return itertools.islice(iterable, n, None)


def split_at(iterable: Iterable, n: int) -> Tuple[Iterable, Iterable]:
    if n < 0:
        raise ValueError("n must be non-negative")

    it = iter(iterable)

    return (take(it, n), it)


def takeuntil(iterable: Iterable, predicate) -> Iterable:
    for item in iterable:
        if predicate(item):
            yield item
            break

        yield item


def dropuntil(iterable: Iterable, predicate) -> Iterable:
    it = iter(iterable)

    for item in it:
        if predicate(item):
            break

    yield from it


T = TypeVar("T")
P = ParamSpec("P")


def juxtapose(functions: Iterable[Callable[P, T]]) -> Callable[P, Iterable[T]]:
    for function in functions:
        if not callable(function):
            raise TypeError("functions must be callable")

    def _juxtapose(*args, **kwargs) -> Iterable[T]:
        return (function(*args, **kwargs) for function in functions)

    names = ", ".join(function.__name__ for function in functions)
    _juxtapose.__name__ = f"juxtapose({names})"
    _juxtapose.__doc__ = f"Apply each function in [{names}] to the same arguments"

    return _juxtapose


def minmax(*args, **kwargs):
    return min(*args, **kwargs), max(*args, **kwargs)


R = TypeVar("R")


def compose(a: Callable[[T], R], b: Callable[P, T]) -> Callable[P, R]:
    def _compose(*args, **kwargs):
        return a(b(*args, **kwargs))

    _compose.__name__ = f"compose({a.__name__}, {b.__name__})"
    _compose.__doc__ = f"Compose {a.__name__} and {b.__name__}"

    return _compose


def flatten(iterable: Iterable[Any]) -> Iterable[Any]:
    for item in iterable:
        if isinstance(item, collections.abc.Iterable):
            yield from flatten(item)
        else:
            yield item
