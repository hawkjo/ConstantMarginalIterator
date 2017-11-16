# Constant Marginal Matrix Iterator
A class for iterating all non-negative integer valued matrices with given marginals.

Also included is a class for iterating all non-negative integer valued rows with given sum
subject to column max values.


## Examples
### Constant Marginal Matrix Example

#### Example Usage:
```python
from ConstMargIterator import ConstantMarginalMatrixIterator

for M in ConstantMarginalMatrixIterator(row_mar=[0, 2, 0, 2, 0], 
                                        col_mar=[2, 0, 0, 1, 0, 1]):
    print M; print
```

#### Output:
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

#### Example Usage:
```python
from ConstMargIterator import ConstantSumRowWithColMaxesIterator

for row in ConstantSumRowWithColMaxesIterator(target_sum=3, 
                                              col_maxes=[2, 3, 0, 1]):
    print row; print
```

#### Output:
```
[2 1 0 0]

[2 0 0 1]

[1 2 0 0]

[1 1 0 1]

[0 3 0 0]

[0 2 0 1]
```

