from typing import Iterator, List
import collections
from test_framework import generic_test

Buildings = collections.namedtuple('Building', ('id', 'height'))

def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    # TODO - you fill in here.
    result: List[Buildings] = []
    for ind, building_height in enumerate(sequence):
        while result and result[-1].height <= building_height:
            result.pop()
        result.append(Buildings(ind, building_height))

    return [c.id for c in reversed(result)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
