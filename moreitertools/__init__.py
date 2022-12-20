__version__ = "0.1.0"

import collections
import itertools
from typing import Iterable, Tuple


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
