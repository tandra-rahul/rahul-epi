import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    # inprocess = [(tree, False)]
    # count = 0
    # #result = []
    #
    # while inprocess:
    #     node, left_tree_done = inprocess.pop()
    #     if node:
    #         if left_tree_done:
    #             count +=1
    #             #result.append(node.data)
    #             if count == k:
    #                 return node
    #         else:
    #             inprocess.append((node.right, False))
    #             inprocess.append((node,True))
    #             inprocess.append((node.left, False))
    while tree:
        comp = (tree.left.size if tree.left else 0)
        if k > comp +1:
            tree = tree.right
            k -= comp + 1
        elif k <= comp:
            tree = tree.left
        else:
            return tree

    return None


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
