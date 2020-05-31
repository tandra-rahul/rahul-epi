from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    curr = new = L

    while new:
        if new.data == curr.data:
            new = new.next
        else:
            curr.next = new
            curr = new
            new = new.next

        curr.next = new
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
