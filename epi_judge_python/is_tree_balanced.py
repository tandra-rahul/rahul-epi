from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.

    _, is_balanced = is_balanced_tree(tree)
    return is_balanced

def is_balanced_tree(tree):

    if not tree:
        return -1, True

    hleft, lbalanced = is_balanced_tree(tree.left)
    if not lbalanced:
        return 0, False

    hright, rbalanced = is_balanced_tree(tree.right)
    if not rbalanced:
        return 0, False

    return 1+max(hleft,hright), abs(hleft - hright) <= 1

def is_leaf(tree):
    if (tree.left == None) and (tree.right == None):
        return True
    else:
        return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
