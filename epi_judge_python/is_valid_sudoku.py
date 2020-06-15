from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    for i in range(9):
        x = [partial_assignment[i][j] for j in range(9)]
        if check_duplicates(x):
            return False

        y = [partial_assignment[j][i] for j in range(9)]
        if check_duplicates(y):
            return False

    for k1 in range(3):
        for k2 in range(3):
            z = [partial_assignment[3*k1 + i][ 3*k2 +j] for i in range(3) for j in range(3)]
            if check_duplicates(z):
                return False

    return True

def check_duplicates(A):
    d = {}
    for i in A:
        if i >0 and i in d:
            return True
        else:
            d[i] = 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
