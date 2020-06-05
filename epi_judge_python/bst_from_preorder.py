from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    #print(preorder_sequence)
    if not preorder_sequence:
        return None


    root = BstNode(preorder_sequence[0])
    ind = 0
    for val in preorder_sequence:
        #print(ind, val)
        if val > root.data:
            break
        ind += 1

    #print(ind)
    #print(preorder_sequence[1:ind])
    #print(preorder_sequence[ind:])
    root.left = rebuild_bst_from_preorder(preorder_sequence[1:ind])
    root.right = rebuild_bst_from_preorder(preorder_sequence[ind:])

    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
