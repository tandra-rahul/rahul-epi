from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.
    if len(perm) <= 1:
        return []

    i = len(perm)-2
    while i >=0:
        if perm[i] < perm[i+1]:
            break
        i -= 1

    if i < 0:
        return []

    k = len(perm) -1
    while perm[k] <= perm[i]:
        k -= 1

    perm[i], perm[k] = perm[k], perm[i]
    perm[i+1: ] = perm[:i:-1]


    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
