import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    #TODO - you fill in here.
    val = [[0 for i in range(len(items) +1)] for j in range(capacity+1)]

    for cap in range(1, capacity+1):
        for i in range(1, len(items)+1):
            value_without = val[cap][i-1]
            if cap >= items[i-1].weight:
                value_with = val[cap - items[i-1].weight][i -1]  + items[i-1].value
            else:
                value_with = 0
            val[cap][i] = max(value_without, value_with)

    return val[-1][-1]



@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
