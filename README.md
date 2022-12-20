# `moreitertools`

A collection of some more itertools that are useful from time to time.

## `windows`

```python
>>> from moreitertools import windows
>>> windows([1, 2, 3, 4, 5], 3)
[(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

## `chunks`

```python
>>> from moreitertools import chunks
>>> chunks([1, 2, 3, 4, 5], 3)
[(1, 2, 3), (4, 5)]
>>> chunks([1, 2, 3, 4, 5], 2, include_orpahns=False)
[(1, 2), (3, 4)]
```

## `take`

```python
>>> from moreitertools import take
>>> take(3, [1, 2, 3, 4, 5])
[1, 2, 3]
```

## `drop`

```python
>>> from moreitertools import drop
>>> drop(3, [1, 2, 3, 4, 5])
[4, 5]
```

## `split_at`

```python
>>> from moreitertools import split_at
>>> split_at(3, [1, 2, 3, 4, 5])
([1, 2, 3], [4, 5])
```

## `takeuntil`

```python
>>> from moreitertools import takeuntil
>>> takeuntil(lambda x: x == 3, [1, 2, 3, 4, 5])
[1, 2, 3]
```

## `dropuntil`

```python
>>> from moreitertools import dropuntil
>>> dropuntil(lambda x: x == 3, [1, 2, 3, 4, 5])
[4, 5]
```
