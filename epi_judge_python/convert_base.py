from test_framework import generic_test
import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    # num = 0
    # is_negative = num_as_string[0] == '-'
    #
    # for i in range(len(num_as_string)-1):
    #     num += string.hexdigits.index(num_as_string[len(num_as_string) -1 -i].lower())*(b1**i)
    #
    # num += (0 if is_negative else string.hexdigits.index(num_as_string[0].lower())*(b1**(len(num_as_string)-1)))
    #
    # sout = []
    # while True:
    #     d = string.hexdigits[num % b2].upper()
    #     sout.append(d)
    #     num //= b2
    #     if num == 0:
    #         break
    #
    # return ('-' if is_negative else '') + ''.join(reversed(sout))
    num = string_to_int(num_as_string, b1)
    return int_to_string(num, b2)

def int_to_string(x, b):

    result = []
    sign_char = ('-' if x <0 else '')
    x = abs(x)

    while True:
        #result.append(chr( ord('0')+ x%b))
        result.append(string.hexdigits[x%b].upper())
        x //= b
        if x ==0:
            break

    return sign_char + ''.join(reversed(result))


def string_to_int(s, b):

    result = 0
    sign = (-1 if s[0] == '-' else 1)
    if (s[0] == '-') or (s[0] == '+'):
        s = s[1:]

    for ind, val in enumerate(s):
        #d = ord(val) - 48
        d = string.hexdigits.index(val.lower())
        result = result*b + d

    return sign*result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
