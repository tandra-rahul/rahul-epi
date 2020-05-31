from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.

    dummy = ListNode(0, L)

    first = dummy.next

    for i in range(k):
        first = first.next

    second = dummy

    while first:
        first = first.next
        second = second.next

    # Second points to "K+1 th from last"
    second.next = second.next.next

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
