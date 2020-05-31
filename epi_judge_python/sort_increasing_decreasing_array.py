from typing import List
import heapq

from test_framework import generic_test


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    r = split_list(A)
    convert_increasing(r)
    result = merge_sorted_arrays(r)

    return result


def split_list(L):

    result = [[]]
    outer =0
    for ind, val in enumerate(L):
        if ind <= 1:
            result[outer].append(val)
            continue

        if (L[ind] - L[ind-1])*(L[ind-1] - L[ind-2]) >=0:
            result[outer].append(val)
        else:
            outer += 1
            result.append([])
            result[outer].append(val)

    return result

def convert_increasing(r):
    for ind, lis in enumerate(r):
        if len(lis) > 1:
            if lis[1] - lis[0] <= 0:
                lis = lis[::-1]
                r[ind] = lis
    return

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    result = []
    min_heap = []

    sorted_iters = [iter(x) for x in sorted_arrays]

    for j in range(len(sorted_arrays)):
        min_heap.append((sorted_arrays[j][0], j))
        next(sorted_iters[j])

    heapq.heapify(min_heap)

    while min_heap:
        val, ind = heapq.heappop(min_heap)
        result.append(val)
        next_element = next(sorted_iters[ind], None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, ind))


    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
