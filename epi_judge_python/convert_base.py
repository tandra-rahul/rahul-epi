from test_framework import generic_test
import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    num = 0
    is_negative = num_as_string[0] == '-'

    for i in range(len(num_as_string)-1):
        num += string.hexdigits.index(num_as_string[len(num_as_string) -1 -i].lower())*(b1**i)

    num += (0 if is_negative else string.hexdigits.index(num_as_string[0].lower())*(b1**(len(num_as_string)-1)))

    sout = []
    while True:
        d = string.hexdigits[num % b2].upper()
        sout.append(d)
        num //= b2
        if num == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(sout))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
