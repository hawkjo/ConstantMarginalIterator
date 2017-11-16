# Constant Marginal Matrix Iterator
A class for iterating all non-negative integer valued matrices with fixed, given marginals.

Also included is a class for iterating all non-negative integer valued rows with fixed, given sum
subject to column max values.


## Examples
### Constant Marginal Matrix Example
Example Usage:
```python
for M in ConstantMarginalMatrixIterator(col_mar=[0, 2, 0, 2, 0], row_mar=[2, 0, 0, 1, 0, 1]):
    print M; print
```

Output:
```
[[0 0 0 0 0 0]
 [2 0 0 0 0 0]
 [0 0 0 0 0 0]
 [0 0 0 1 0 1]
 [0 0 0 0 0 0]]

[[0 0 0 0 0 0]
 [1 0 0 1 0 0]
 [0 0 0 0 0 0]
 [1 0 0 0 0 1]
 [0 0 0 0 0 0]]

[[0 0 0 0 0 0]
 [1 0 0 0 0 1]
 [0 0 0 0 0 0]
 [1 0 0 1 0 0]
 [0 0 0 0 0 0]]

[[0 0 0 0 0 0]
 [0 0 0 1 0 1]
 [0 0 0 0 0 0]
 [2 0 0 0 0 0]
 [0 0 0 0 0 0]]
```

### Row Iterator Example
Example Usage:
```python
for row in ConstantSumRowWithColMaxesIterator(target_sum=3, col_maxes=[2, 3, 0, 1]):
    print row; print
```

Output:
```
[2 1 0 0]

[2 0 0 1]

[1 2 0 0]

[1 1 0 1]

[0 3 0 0]

[0 2 0 1]
```
