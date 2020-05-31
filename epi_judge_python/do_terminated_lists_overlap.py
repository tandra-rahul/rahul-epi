import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    # TODO - you fill in here.
    # finding tail of first list

    n0,t0 = find_tail(l0)
    n1,t1 = find_tail(l1)

    if t0 is t1:
        # Lists intersect
        if n0 > n1:
            p0 = advance_ahead(l0, n0 -n1)
            p1 = l1
        elif n1 > n0:
            p0 = l0
            p1 = advance_ahead(l1, n1 - n0)
        else:
            p0 = l0
            p1 = l1

        while p0 is not p1:
            p0 = p0.next
            p1 = p1.next

        return p0

    return ListNode()

def find_tail(head):
    n = 0

    # finding tail of first list
    while head:
        n += 1
        head = head.next

    return n,head

def advance_ahead(head, n):

    for i in range(n):
        head = head.next

    return head


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
