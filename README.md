# `moreitertools`

A collection of some more itertools that are useful from time to time.

## `windows`

Inspired by Rust’s `windows`.

```python
>>> from moreitertools import windows
>>> windows([1, 2, 3, 4, 5], 3)
[(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

## `chunks`

Inspired by Rust’s `chunks`.

```python
>>> from moreitertools import chunks
>>> chunks([1, 2, 3, 4, 5], 3)
[(1, 2, 3), (4, 5)]
>>> chunks([1, 2, 3, 4, 5], 2, include_orpahns=False)
[(1, 2), (3, 4)]
```

## `take`

A more common name for a subset of `itertools.islice`'s functionality.

```python
>>> from moreitertools import take
>>> take(3, [1, 2, 3, 4, 5])
[1, 2, 3]
```

## `drop`

Another more common name for a subset of `itertools.islice`'s functionality.

```python
>>> from moreitertools import drop
>>> drop(3, [1, 2, 3, 4, 5])
[4, 5]
```

## `split_at`

Split an iterable at a given index.

```python
>>> from moreitertools import split_at
>>> split_at(3, [1, 2, 3, 4, 5])
([1, 2, 3], [4, 5])
```

## `takeuntil`

Subtly different from `itertools.takewhile` in that it takes the element that passes the predicate.

```python
>>> from moreitertools import takeuntil
>>> takeuntil(lambda x: x == 3, [1, 2, 3, 4, 5])
[1, 2, 3]
```

## `dropuntil`

Subtly different from `itertools.dropwhile` in that it drops the element that passes the predicate.

```python
>>> from moreitertools import dropuntil
>>> dropuntil(lambda x: x == 3, [1, 2, 3, 4, 5])
[4, 5]
```

## `juxtapose`

Inspired by Clojure’s `juxt`.

```python
>>> from moreitertools import juxtapose
>>> f = juxtapose([lambda n: n + 2, lambda n: n * 3])
>>> f(5)
[7, 15]
```

## `minmax`

Return's both the minimum and maximum of an iterable or pair of values.

```python
>>> from moreitertools import minmax
>>> minmax([1, 2, 3, 4, 5])
(1, 5)
>>> minmax(9, 5)
(5, 9)
```

## `compose`

Inspired by Clojure’s `comp`. Applies functions right-to-left.

```python
>>> from moreitertools import compose
>>> f = compose(lambda n: n + 2, lambda n: n * 3)
>>> f(5)
17
```
