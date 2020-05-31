from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    if not tree:
        return True

    return symm_check(tree.left, tree.right)

def symm_check(r1, r2):
    if not r1 or not r2:
        return (not r1 and not r2)

    return (symm_check(r1.left, r2.right) and
            symm_check(r1.right, r2.left) and
            r1.data == r2.data)




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
