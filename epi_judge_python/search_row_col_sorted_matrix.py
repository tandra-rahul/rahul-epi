from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    # TODO - you fill in here.
    i, j = 0, len(A[0])-1
    while i <= len(A)-1 and j >= 0:
        if A[i][j] > x:
            j -= 1
        elif A[i][j] < x:
            i += 1
        else:
            return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
