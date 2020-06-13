from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    # Add one to LSB
    carry = 0
    A[-1] += 1
    for i in reversed(range(len(A))):
        val = A[i] + carry
        A[i] = val % 10
        carry = val // 10

    if carry:
        A[0] = 1
        A.append(0)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
