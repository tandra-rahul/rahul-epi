from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    # Add one to LSB
    N = A[-1] + 1
    carry = int(N/10)
    A[-1] = N % 10

    for i in range(len(A)-2,-1,-1):
        N = A[i] + carry
        carry = int(N/10)
        A[i] = N % 10

    if carry != 0:
        A.insert(0,carry)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
