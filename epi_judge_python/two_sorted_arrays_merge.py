from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    # TODO - you fill in here.
    write_idx = m + n - 1
    read_a_idx = m-1
    read_b_idx = n -1

    while read_a_idx >=0 and read_b_idx >= 0:
        if A[read_a_idx] >= B[read_b_idx]:
            A[write_idx] = A[read_a_idx]
            read_a_idx -= 1
        else:
            A[write_idx] = B[read_b_idx]
            read_b_idx -= 1
        write_idx -=1

    while read_b_idx >= 0:
        A[write_idx] = B[read_b_idx]
        write_idx -= 1
        read_b_idx -= 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
