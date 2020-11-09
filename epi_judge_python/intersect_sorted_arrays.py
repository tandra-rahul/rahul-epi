from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.
    result = []
    l = r = 0

    while l < len(A) and r < len(B):

        if A[l] < B[r]:
            l +=1
        elif A[l] > B[r]:
            r +=1
        else:
            if l ==0 or A[l-1] != A[l]:
                result.append(A[l])
            l +=1
            r +=1

    return result
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
