import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

def is_lin_intersect(s1, e1, s2, e2):
    # Check whether two line segments intersect or not
    return ((e2 - s1) >=0) and ((e1 - s2) >=0)

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # TODO - you fill in here.
    if not (is_lin_intersect(r1.x, r1.x + r1.width, r2.x, r2.x  + r2.width) and is_lin_intersect(r1.y, r1.y + r1.height, r2.y, r2.y + r2.height)):
        return Rect(0, 0, -1, -1)

    return Rect(max(r1.x, r2.x), max(r1.y, r2.y), min(r1.x + r1.width,  r2.x + r2.width) - max(r1.x, r2.x), min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y))


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
