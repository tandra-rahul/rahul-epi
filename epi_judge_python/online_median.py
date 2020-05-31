from typing import Iterator, List
import heapq

from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    # TODO - you fill in here.
    min_heap = []  # Contain the larger half. len(min_heap) >= len(max_heap)
    max_heap = []  # Contain the smaller half.
    result = []

    for x in sequence:
        y = heapq.heappushpop(min_heap, x)
        heapq.heappush(max_heap, -y)
        if len(max_heap) > len(min_heap):
            e = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -e)

        result.append( (-max_heap[0] + min_heap[0])/2  if len(min_heap) == len(max_heap)
                        else min_heap[0] )
    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
