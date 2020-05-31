from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    # TODO - you fill in here.
    citations.sort(reverse=True)
    ind = 0
    while ind < len(citations):
        if citations[ind] <  ind+1:
            break
        ind +=1

    return ind


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
