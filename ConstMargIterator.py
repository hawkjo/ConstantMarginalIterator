import numpy as np


class ConstantSumRowWithColMaxesIterator(object):
    """
    A class for iterating all non-negative integer valued rows with fixed, given sum subject to
    column max values.
    """
    def __init__(self, target_sum, col_maxes):
        self.target_sum = target_sum
        self.col_maxes = np.array(col_maxes)
        self.ncol = len(col_maxes)
        
    def __iter__(self):
        if self.target_sum == 0:
            yield np.zeros((self.ncol,), dtype=np.int)
        else:
            for row in self._iterate_rows(np.zeros((self.ncol,), dtype=np.int)):
                yield row
        
    def _ith_unit_vector(self, i):
        v = np.zeros((self.ncol,), dtype=np.int)
        v[i] = 1
        return v
        
    def _iterate_rows(self, prev_row, prev_idx=0):
        for i in xrange(prev_idx, self.ncol):
            if self.col_maxes[i] > prev_row[i]:
                new_row = prev_row + self._ith_unit_vector(i)
                if new_row.sum() == self.target_sum:
                    yield new_row
                else:
                    for new_row in self._iterate_rows(new_row, i):
                        yield new_row


class ConstantMarginalMatrixIterator(object):
    """
    A class for iterating all non-negative integer valued matrices with fixed, given marginals.
    """

    def __init__(self, row_mar, col_mar):
        self.row_mar = np.array(row_mar)
        self.col_mar = np.array(col_mar)
        self.nrow = len(row_mar)
        self.ncol = len(col_mar)
        assert self.row_mar.sum() == self.col_mar.sum(), 'Marginals must have equal sums.'
        
    def __iter__(self):
        if self.row_mar.sum() == 0:
            yield np.zeros((self.nrow, self.ncol), dtype=np.int)
        else:
            for rows in self._iterate_lists_of_rows(self.col_mar):
                M = np.array(rows)
                assert (M.sum(axis=1) == self.row_mar).all(), 'row_mar'
                assert (M.sum(axis=0) == self.col_mar).all(), 'col_mar'
                yield M
                
    def _iterate_lists_of_rows(self, remaining_col_mar, prev_row_idx=-1):
        row_idx = prev_row_idx + 1
        target_row_sum = self.row_mar[row_idx]
        if row_idx == self.nrow - 1:
            assert target_row_sum == sum(remaining_col_mar)
            for row in ConstantSumRowWithColMaxesIterator(target_row_sum, remaining_col_mar):
                yield [row]
        else:
            for row in ConstantSumRowWithColMaxesIterator(target_row_sum, remaining_col_mar):
                for remaining_rows in self._iterate_lists_of_rows(remaining_col_mar - row, 
                                                                 row_idx):
                    yield [row] + remaining_rows
