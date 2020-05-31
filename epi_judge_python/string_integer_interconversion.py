from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    is_negative = False
    if x < 0:
        is_negative, x = True, -x

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.

    result = 0
    for i in range(len(s)-1):
        d = ord(s[len(s) - i -1]) - 48
        result += (10**i)*d
        print(d,result)

    return (-1 if s[0]=='-' else 1)*result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
