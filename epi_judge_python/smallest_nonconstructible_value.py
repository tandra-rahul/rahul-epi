from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    # TODO - you fill in here.
    A.sort()
    max_val = 0
    for i in range(len(A)):
        if A[i] > max_val + 1:
            break
        else:
            max_val += A[i]

    return max_val+1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
