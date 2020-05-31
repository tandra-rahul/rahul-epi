from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
    slow = fast = L
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first, second = L, reverse_list(slow)
    while first and second:
        if first.data != second.data:
            return False

        first, second = first.next, second.next
    return True

def reverse_list(head):

    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
