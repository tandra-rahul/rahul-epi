from test_framework import generic_test
import math


def square_root(x: float) -> float:
    # TODO - you fill in here.
    L, U, = (1.0, x) if x >=1 else (x, 1.0)
    while not math.isclose(L, U):
        mid = (U+ L)/2
        if mid**2 > x:
            U = mid
        else:
            L = mid
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
