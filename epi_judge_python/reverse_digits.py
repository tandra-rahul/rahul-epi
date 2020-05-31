from test_framework import generic_test


def reverse(x: int) -> int:
    y = str(abs(x))
    result = ''
    for i in range(0, len(y)):
        result += y[len(y) -i -1]

    if x >=0:
        return int(result)
    else:
        return -1*int(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
