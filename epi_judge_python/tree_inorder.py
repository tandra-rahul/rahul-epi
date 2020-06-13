from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    #Initial Condition

    if not tree:
        return []

    out = []
    l = [(tree, False)]

    while l:
        node, left_tree_done = l.pop()
        if left_tree_done:
            out.append(node.data)
        else:
            if node.right:
                l.append((node.right, False))
            l.append((node, True))
            if node.left:
                l.append((node.left, False))

    return out

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
