from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    #initial condition
    # if not tree:
    #     return True
    #
    # is_bst, m, n = is_bin_tree_bst(tree)
    #
    # return is_bst
    return check_range(tree)

def check_range(tree, low=float('-inf'), high=float('inf')):

    if not tree:
        return True
    elif tree.data < low or tree.data > high:
        return False

    return check_range(tree.left, low, tree.data) and check_range(tree.right, tree.data, high)


def is_bin_tree_bst(tree):

    if not tree.left and not tree.right:
        return True, tree.data, tree.data

    if tree.left and tree.right:
        is_left_bst, min_left, max_left  = is_bin_tree_bst(tree.left)
        is_right_bst, min_right, max_right = is_bin_tree_bst(tree.right)
        min_tree = min(min_left, min_right, tree.data)
        max_tree = max(max_left, max_right, tree.data)
        is_tree_bst = is_left_bst and is_right_bst and (tree.data >= max_left) and (tree.data <= min_right)
    elif tree.left:
        is_left_bst, min_val, max_val = is_bin_tree_bst(tree.left)
        min_tree = min(min_val, tree.data)
        max_tree = max(max_val, tree.data)
        is_tree_bst = is_left_bst and (tree.data >= max_val)
    else:
        is_right_bst, min_val, max_val = is_bin_tree_bst(tree.right)
        min_tree = min(min_val, tree.data)
        max_tree = max(max_val, tree.data)
        is_tree_bst = is_right_bst and (tree.data <= min_val)


    return is_tree_bst, min_tree, max_tree


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
