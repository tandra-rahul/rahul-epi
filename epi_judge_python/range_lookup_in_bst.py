import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    # TODO - you fill in here.
    # if not tree:
    #     return []
    #
    # if tree.data > interval.right:
    #     return range_lookup_in_bst(tree.left, interval)
    # elif tree.data < interval.left:
    #     return range_lookup_in_bst(tree.right, interval)
    #
    # return range_lookup_in_bst(tree.left, Interval(interval.left, tree.data)) + [tree.data] + range_lookup_in_bst(tree.right, Interval(tree.data, interval.right))
    def range_lookup_helper(tree, interval):

        if not tree:
            return

        if tree.data > interval.right:
            return range_lookup_helper(tree.left, interval)
        elif tree.data < interval.left:
            return range_lookup_helper(tree.right, interval)
        else:
            range_lookup_helper(tree.left, Interval(interval.left, tree.data))
            result.append(tree.data)
            range_lookup_helper(tree.right, Interval(tree.data, interval.right))

    result = []
    range_lookup_helper(tree, interval)
    return result




def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
