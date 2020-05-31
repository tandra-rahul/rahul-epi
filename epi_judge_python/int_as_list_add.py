from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    carry = 0
    dummy_head = result = ListNode(0)

    while L1 or L2:

        result.next = ListNode(0)
        result = result.next

        if L1:
            carry += L1.data
            L1 = L1.next

        if L2:
            carry += L2.data
            L2 = L2.next

        result.data = carry %10
        carry = carry // 10

    if carry:
        result.next = ListNode(carry)

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
