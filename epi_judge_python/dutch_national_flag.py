import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # # TODO - you fill in here.
    # if len(A) == 1:
    #     return
    #
    # swap(A, 0, pivot_index)
    #
    # pend = 1
    # i = 1
    # for j in range(1, len(A)):
    #     if A[j] < A[0]:
    #         swap(A, i, j)
    #         i += 1
    #
    #     if A[j] == A[0]:
    #         swap(A, i, j)
    #         swap(A, pend, i)
    #         pend += 1
    #         i +=1
    #
    # for k in range(0, pend):
    #     swap(A, k, i-1-k)
    #
    # Two pass solution

    # # Pass 1:
    # smaller = 0
    # pivot = A[pivot_index]
    # for i in range(len(A)):
    #     if A[i] < pivot:
    #         A[smaller], A[i] = A[i], A[smaller]
    #         smaller += 1
    #
    # #Pass 2
    # larger = len(A) - 1
    # for i in reversed(range(len(A))):
    #     if A[i] > pivot:
    #         A[larger], A[i] = A[i], A[larger]
    #         larger -= 1

    # Single pass solution
    p = A[pivot_index]
    lesser, equal, larger = 0, 0, len(A)-1
    while equal <= larger:
        if A[equal] < p:
            A[lesser], A[equal] = A[equal], A[lesser]
            lesser += 1
            equal += 1
        elif A[equal] == p:
            equal += 1
        else:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1

    return



@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
