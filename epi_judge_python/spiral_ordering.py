from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    n = len(square_matrix)
    if n <1:
        return []

    if n == 1:
        return [square_matrix[0][0]]

    outer_layer = ([square_matrix[0][j] for j in range(0,n)] +
                   [square_matrix[i][n-1] for i in range(1,n)] +
                   [square_matrix[n-1][j] for j in reversed(range(0,n-1))]+
                   [square_matrix[i][0] for i in reversed(range(1,n-1))])

    return outer_layer + matrix_in_spiral_order([[square_matrix[i][j] for j in range(1,n-1)] for i in range(1,n-1)])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
