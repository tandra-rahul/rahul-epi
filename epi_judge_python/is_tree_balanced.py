from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    if not tree:
        return True

    _, is_balanced = is_balanced_tree(tree)
    return is_balanced

def is_balanced_tree(tree):

    if is_leaf(tree):
        return 0, True

    if tree.left and tree.right:
        hleft, is_left_balanced = is_balanced_tree(tree.left)
        hright, is_right_balanced = is_balanced_tree(tree.right)
        height = 1 + max(hleft, hright)
        hdiff = abs(hleft - hright)
        return height,  is_left_balanced and is_right_balanced and hdiff <= 1

    node = tree.left or tree.right
    height, is_balanced = is_balanced_tree(node)
    return height+1, is_balanced and height == 0

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
