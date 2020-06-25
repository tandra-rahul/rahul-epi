from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.
    L, U = 0, len(A) -1
    while L < U:
        M = L + (U - L)//2
        if A[M] > A[U]:
            L = M +1
        else:
            U = M

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
