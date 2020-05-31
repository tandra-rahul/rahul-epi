from typing import List
import heapq

from test_framework import generic_test


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
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
