from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # TODO - you fill in here.

    return sum_node_to_leaf(tree)

def sum_node_to_leaf(node, partial_sum = 0):

    if not node:
        return 0

    partial_sum = 2*partial_sum + node.data

    if not node.left and not node.right:
        return partial_sum

    return sum_node_to_leaf(node.left, partial_sum) + sum_node_to_leaf(node.right, partial_sum)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
