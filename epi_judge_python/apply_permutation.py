from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.

    for i in range(len(perm)):
        while perm[i] != i:
            A[i], A[perm[i]] = A[perm[i]], A[i]
            temp = perm[perm[i]]
            perm[perm[i]] = perm[i]
            perm[i] = temp
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
