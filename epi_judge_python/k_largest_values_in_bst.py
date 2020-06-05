from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO - you fill in here.
    result = []
    stack = [(tree, False)]

    while stack:
        node, process_done = stack.pop()
        if node:
            if not process_done:
                stack.append((node.left, False))
                stack.append((node, True))
                stack.append((node.right, False))
            else:
                if k > 0:
                    result.append(node.data)
                    k -= 1
                else:
                    return result

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
