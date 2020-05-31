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
            x =A[l]
            result.append(x)
            while l < len(A) :
                if A[l] != x:
                    break
                l += 1
            while r < len(B):
                if B[r] != x:
                    break
                r += 1

    return result
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
