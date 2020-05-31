from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    _, is_balanced = is_balanced_tree(tree)
    return is_balanced

def is_balanced_tree(tree):

    if is_leaf(tree):
        return 0, True

    print(tree.left)
    print(tree.right)

    if tree.left:
        hleft, is_left_balanced = is_balanced_tree(tree.left)
    else:
        hleft, is_left_balanced = 0, True

    if tree.right:
        hright, is_right_balanced = is_balanced_tree(tree.right)
    else:
        hright, is_right_balanced = 0, True

    print("Left tree", hleft, is_left_balanced)
    print("Right tree", hright, is_right_balanced)

    height = 1 + max(hleft, hright)
    hdiff = abs(hleft - hright)

    return height, is_left_balanced and is_right_balanced and hdiff <= 1

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
